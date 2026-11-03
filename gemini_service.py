"""
Gemini API Service for Travel Discovery AI.
Provides unified, robust integration with Google's Gemini Models.
Supports official Google Gen AI SDK (both google.genai and google.generativeai)
with resilient fallback to the official GenAI REST API, ensuring 100% reliability
across all Python versions, operating systems, and deployment platforms.
"""

import os
import json
import time
from typing import List, Dict, Any, Optional, Tuple
import requests

from config import DEFAULT_MODEL, GENERATION_CONFIG
from prompts import SYSTEM_INSTRUCTION

# Try importing the official SDKs
GENAI_SDK_AVAILABLE = False
GENAI_LEGACY_AVAILABLE = False

try:
    from google import genai
    from google.genai import types as genai_types
    GENAI_SDK_AVAILABLE = True
except (ImportError, Exception):
    GENAI_SDK_AVAILABLE = False

try:
    import google.generativeai as legacy_genai
    GENAI_LEGACY_AVAILABLE = True
except (ImportError, Exception):
    GENAI_LEGACY_AVAILABLE = False


def get_api_key_from_env_or_secrets() -> Optional[str]:
    """
    Safely retrieves the Gemini API key from:
    1. Environment variable GEMINI_API_KEY (primary for Railway/production)
    2. Streamlit secrets (local development fallback)
    """
    # 1. Primary: Check OS environment variable
    env_key = os.environ.get("GEMINI_API_KEY", "").strip()
    if env_key and not env_key.startswith("your_"):
        return env_key

    # 2. Fallback: Check Streamlit secrets (safe when secrets.toml doesn't exist)
    try:
        import streamlit as st
        if hasattr(st, "secrets"):
            try:
                if "GEMINI_API_KEY" in st.secrets:
                    key = st.secrets["GEMINI_API_KEY"]
                    if key and str(key).strip() and not str(key).strip().startswith("your_"):
                        return str(key).strip()
            except (FileNotFoundError, KeyError, Exception):
                pass
    except Exception:
        pass

    return None


class GeminiTravelService:
    """Service to handle all conversational and structured requests with Gemini."""

    def __init__(self, api_key: Optional[str] = None, model_name: str = DEFAULT_MODEL):
        self.api_key = api_key or get_api_key_from_env_or_secrets() or ""
        self.model_name = model_name
        self.system_instruction = SYSTEM_INSTRUCTION
        self._init_sdk()

    def set_api_key(self, api_key: str):
        """Update active API key."""
        self.api_key = api_key.strip()
        self._init_sdk()

    def set_model(self, model_name: str):
        """Update active model name."""
        self.model_name = model_name

    def _init_sdk(self):
        """Initialize whichever official SDK is available."""
        if not self.api_key:
            return

        if GENAI_LEGACY_AVAILABLE:
            try:
                legacy_genai.configure(api_key=self.api_key)
            except Exception:
                pass

    def test_connection(self) -> Tuple[bool, str]:
        """
        Tests the API key with a minimal query to verify validity and quota.
        Returns (success: bool, message: str).
        """
        if not self.api_key:
            return False, "No Gemini API key provided. Please configure it in settings or .streamlit/secrets.toml."

        try:
            response_text = self._call_rest_api(
                prompt="Reply with exactly 'OK' to test connectivity.",
                history=[]
            )
            if response_text:
                return True, "Successfully connected to Gemini API!"
            return False, "Empty response received from Gemini."
        except Exception as e:
            return False, self._format_error_message(e)

    def generate_chat_response(
        self,
        user_message: str,
        conversation_history: List[Dict[str, str]]
    ) -> str:
        """
        Sends a multi-turn conversation to Gemini and returns the assistant's reply.
        conversation_history is a list of {'role': 'user'|'assistant', 'content': str}.
        """
        if not self.api_key:
            raise ValueError(
                "Gemini API Key is missing. Please add your key in the Settings page "
                "or create a .streamlit/secrets.toml file with GEMINI_API_KEY."
            )

        # Attempt 1: Modern official SDK google-genai (Python 3.10+)
        if GENAI_SDK_AVAILABLE:
            try:
                return self._call_official_genai_sdk(user_message, conversation_history)
            except Exception as e:
                error_msg = str(e).lower()
                if "api_key" in error_msg or "unauthenticated" in error_msg or "quota" in error_msg:
                    raise e
                # Fall back to REST if SDK had transient issue

        # Attempt 2: Direct Official Google GenAI REST API (Fastest, ultra-resilient, handles system instruction)
        try:
            return self._call_rest_api(user_message, conversation_history)
        except Exception as e:
            error_msg = str(e).lower()
            if "api_key" in error_msg or "unauthenticated" in error_msg or "quota" in error_msg:
                raise e
            
            # Attempt 3: Legacy SDK fallback if REST had issue
            if GENAI_LEGACY_AVAILABLE:
                try:
                    return self._call_legacy_sdk(user_message, conversation_history)
                except Exception:
                    pass
            raise e

    def _call_official_genai_sdk(
        self,
        user_message: str,
        conversation_history: List[Dict[str, str]]
    ) -> str:
        """Call via modern google-genai SDK."""
        client = genai.Client(api_key=self.api_key)
        # Format history
        contents = []
        for msg in conversation_history:
            role = "user" if msg["role"] == "user" else "model"
            contents.append(genai_types.Content(
                role=role,
                parts=[genai_types.Part.from_text(text=msg["content"])]
            ))
        contents.append(genai_types.Content(
            role="user",
            parts=[genai_types.Part.from_text(text=user_message)]
        ))

        config = genai_types.GenerateContentConfig(
            system_instruction=self.system_instruction,
            temperature=GENERATION_CONFIG["temperature"],
            top_p=GENERATION_CONFIG["top_p"],
            max_output_tokens=GENERATION_CONFIG["max_output_tokens"],
        )

        response = client.models.generate_content(
            model=self.model_name,
            contents=contents,
            config=config
        )
        return response.text or ""

    def _call_legacy_sdk(
        self,
        user_message: str,
        conversation_history: List[Dict[str, str]]
    ) -> str:
        """Call via google-generativeai SDK."""
        legacy_genai.configure(api_key=self.api_key)
        model = legacy_genai.GenerativeModel(
            model_name=self.model_name,
            generation_config=GENERATION_CONFIG,
            system_instruction=self.system_instruction
        )
        
        # Build chat history
        chat_history = []
        for msg in conversation_history:
            role = "user" if msg["role"] == "user" else "model"
            chat_history.append({"role": role, "parts": [msg["content"]]})

        chat = model.start_chat(history=chat_history)
        response = chat.send_message(user_message)
        return response.text or ""

    def _call_rest_api(
        self,
        prompt: str,
        history: List[Dict[str, str]]
    ) -> str:
        """
        Direct REST call to Google Gemini endpoint.
        Used as resilient fallback or standalone engine with automatic model failover.
        """
        # Format contents for Gemini v1beta API
        contents = []
        for msg in history:
            role = "user" if msg["role"] == "user" else "model"
            contents.append({
                "role": role,
                "parts": [{"text": msg["content"]}]
            })
        contents.append({
            "role": "user",
            "parts": [{"text": prompt}]
        })

        payload: Dict[str, Any] = {
            "contents": contents,
            "system_instruction": {
                "parts": [{"text": self.system_instruction}]
            },
            "generationConfig": {
                "temperature": GENERATION_CONFIG["temperature"],
                "topP": GENERATION_CONFIG["top_p"],
                "topK": GENERATION_CONFIG["top_k"],
                "maxOutputTokens": GENERATION_CONFIG["max_output_tokens"],
            }
        }

        headers = {"Content-Type": "application/json"}
        
        # Candidate model failover order
        models_to_try = [self.model_name]
        for fallback in ["gemini-3.5-flash-lite", "gemini-3.8-flash"]:
            if fallback not in models_to_try:
                models_to_try.append(fallback)

        last_error = None
        for candidate_model in models_to_try:
            url = f"https://generativelanguage.googleapis.com/v1beta/models/{candidate_model}:generateContent?key={self.api_key}"
            for attempt in range(2):
                try:
                    response = requests.post(url, headers=headers, json=payload, timeout=35)
                    
                    if response.status_code == 200:
                        data = response.json()
                        candidates = data.get("candidates", [])
                        if candidates:
                            parts = candidates[0].get("content", {}).get("parts", [])
                            if parts:
                                return parts[0].get("text", "")
                        return "No content received from travel AI."

                    # If quota/auth error, don't retry other models
                    if response.status_code == 400:
                        err_data = response.json().get("error", {})
                        err_msg = err_data.get("message", "Bad request.")
                        if "not found" in err_msg.lower() or "not supported" in err_msg.lower():
                            break  # Move to next candidate model
                        raise ValueError(f"Invalid API Request or Key: {err_msg}")
                    elif response.status_code == 403:
                        raise PermissionError("API Key is forbidden or unauthorized for Gemini services.")
                    elif response.status_code == 429:
                        time.sleep(2)
                        continue
                    elif response.status_code == 503:
                        # High demand spike, brief backoff
                        time.sleep(2)
                        continue
                    elif response.status_code == 404:
                        break  # Move to next candidate model
                    else:
                        last_error = f"Gemini API returned HTTP {response.status_code}: {response.text}"
                except (requests.ConnectionError, requests.Timeout) as conn_err:
                    last_error = f"Connection timeout: {str(conn_err)}"
                    time.sleep(1)

        if last_error:
            raise RuntimeError(last_error)
        raise RuntimeError("Unable to generate response from Gemini API.")

    @staticmethod
    def _format_error_message(e: Exception) -> str:
        """Format an exception into a polite, actionable user message."""
        raw_msg = str(e)
        low_msg = raw_msg.lower()

        if "api_key" in low_msg or "unauthorized" in low_msg or "400" in low_msg or "403" in low_msg:
            return (
                "⚠️ **Invalid or Expired API Key**: Please verify your Gemini API key in the "
                "Settings tab or `.streamlit/secrets.toml`. You can generate a free key at "
                "[Google AI Studio](https://aistudio.google.com/app/apikey)."
            )
        elif "quota" in low_msg or "429" in low_msg or "resource_exhausted" in low_msg:
            return (
                "⏳ **Rate Limit or Quota Reached**: Google Gemini is temporarily limiting requests. "
                "Please wait 30–60 seconds before submitting another travel query."
            )
        elif "connection" in low_msg or "timeout" in low_msg or "dns" in low_msg:
            return (
                "🌐 **Network Connection Issue**: Unable to reach Google Gemini servers. "
                "Please check your internet connection."
            )
        elif "not found" in low_msg or "404" in low_msg:
            return (
                f"🔍 **Model Not Found**: The selected model was not found in your API tier. "
                f"Please switch to `{DEFAULT_MODEL}` in Settings."
            )
        else:
            return f"❌ **Travel Assistant Error**: {raw_msg}"
