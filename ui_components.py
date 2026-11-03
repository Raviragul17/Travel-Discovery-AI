"""
UI Components and Styling for Travel Discovery AI.
Provides premium, luxury-travel styling, custom HTML cards, chat bubbles, and layout components.
Supports light (Warm White & Sand) and dark (Midnight Ocean) themes.
"""

import streamlit as st
from config import APP_NAME, TAGLINE, HERO_TITLE, HERO_SUBTITLE, LEGAL_DISCLAIMER


def get_custom_css(dark_mode: bool = False) -> str:
    """Returns responsive CSS adhering to startup-grade travel UI standards."""
    if dark_mode:
        # Midnight Ocean Theme
        bg_main = "#0B132B"
        bg_card = "#1C2541"
        bg_card_alt = "#243256"
        text_primary = "#F8FAFC"
        text_secondary = "#94A3B8"
        accent_teal = "#14B8A6"
        accent_blue = "#38BDF8"
        border_color = "rgba(255, 255, 255, 0.1)"
        card_shadow = "0 10px 25px -5px rgba(0, 0, 0, 0.4), 0 8px 10px -6px rgba(0, 0, 0, 0.4)"
        badge_bg = "rgba(20, 184, 166, 0.15)"
        chat_user_bg = "#0369A1"
        chat_user_text = "#FFFFFF"
        chat_ai_bg = "#1C2541"
        chat_ai_border = "rgba(255, 255, 255, 0.12)"
    else:
        # Warm White & Coastal Sand Theme
        bg_main = "#FAF8F5"
        bg_card = "#FFFFFF"
        bg_card_alt = "#F5EFE6"
        text_primary = "#0F1E36"
        text_secondary = "#475569"
        accent_teal = "#0D9488"
        accent_blue = "#0284C7"
        border_color = "rgba(15, 30, 54, 0.08)"
        card_shadow = "0 4px 20px -2px rgba(15, 30, 54, 0.06), 0 2px 6px -1px rgba(15, 30, 54, 0.04)"
        badge_bg = "#E6F4F1"
        chat_user_bg = "#0284C7"
        chat_user_text = "#FFFFFF"
        chat_ai_bg = "#FFFFFF"
        chat_ai_border = "rgba(15, 30, 54, 0.09)"

    return f"""
    <style>
    /* Google Fonts */
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&family=Playfair+Display:ital,wght@0,600;0,700;1,600&display=swap');

    html, body, [class*="css"] {{
        font-family: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
        color: {text_primary};
    }}

    .stApp {{
        background-color: {bg_main};
        color: {text_primary};
    }}

    /* Top padding cleanup */
    .block-container {{
        padding-top: 2rem !important;
        padding-bottom: 3.5rem !important;
        max-width: 1200px;
    }}

    /* Sidebar Styling */
    section[data-testid="stSidebar"] {{
        background-color: {bg_card} !important;
        border-right: 1px solid {border_color} !important;
    }}
    
    section[data-testid="stSidebar"] .block-container {{
        padding-top: 2rem !important;
    }}

    /* Brand Header in Sidebar */
    .brand-sidebar-box {{
        padding: 16px 12px;
        margin-bottom: 20px;
        border-bottom: 1px solid {border_color};
        text-align: center;
    }}
    .brand-logo-icon {{
        font-size: 32px;
        display: inline-block;
        margin-bottom: 6px;
    }}
    .brand-sidebar-title {{
        font-size: 1.15rem;
        font-weight: 800;
        letter-spacing: 0.08em;
        color: {accent_teal};
        margin: 0;
        text-transform: uppercase;
    }}
    .brand-sidebar-tagline {{
        font-size: 0.75rem;
        color: {text_secondary};
        margin-top: 4px;
        font-weight: 500;
    }}

    /* Hero Section */
    .hero-container {{
        text-align: center;
        padding: 42px 20px 32px 20px;
        background: linear-gradient(180deg, {bg_card_alt} 0%, {bg_main} 100%);
        border-radius: 24px;
        margin-bottom: 32px;
        border: 1px solid {border_color};
    }}
    .hero-badge {{
        display: inline-flex;
        align-items: center;
        gap: 6px;
        background-color: {badge_bg};
        color: {accent_teal};
        padding: 6px 16px;
        border-radius: 30px;
        font-size: 0.82rem;
        font-weight: 700;
        letter-spacing: 0.05em;
        text-transform: uppercase;
        margin-bottom: 18px;
    }}
    .hero-title {{
        font-family: 'Playfair Display', Georgia, serif;
        font-size: 2.85rem;
        font-weight: 700;
        line-height: 1.2;
        color: {text_primary};
        margin-bottom: 16px;
        letter-spacing: -0.02em;
    }}
    .hero-subtitle {{
        font-size: 1.12rem;
        line-height: 1.6;
        color: {text_secondary};
        max-width: 760px;
        margin: 0 auto 24px auto;
        font-weight: 400;
    }}

    /* Destination Cards */
    .dest-card {{
        background: {bg_card};
        border-radius: 18px;
        overflow: hidden;
        border: 1px solid {border_color};
        box-shadow: {card_shadow};
        transition: transform 0.25s ease, box-shadow 0.25s ease;
        height: 100%;
        display: flex;
        flex-direction: column;
    }}
    .dest-card:hover {{
        transform: translateY(-5px);
        box-shadow: 0 16px 30px -4px rgba(15, 30, 54, 0.12);
    }}
    .dest-image-wrap {{
        position: relative;
        width: 100%;
        height: 190px;
        overflow: hidden;
    }}
    .dest-image {{
        width: 100%;
        height: 100%;
        object-fit: cover;
        transition: transform 0.4s ease;
    }}
    .dest-card:hover .dest-image {{
        transform: scale(1.05);
    }}
    .dest-tag-badge {{
        position: absolute;
        top: 12px;
        left: 12px;
        background: rgba(15, 30, 54, 0.75);
        backdrop-filter: blur(8px);
        color: #FFFFFF;
        font-size: 0.72rem;
        font-weight: 600;
        padding: 4px 10px;
        border-radius: 20px;
        letter-spacing: 0.03em;
    }}
    .dest-content {{
        padding: 18px;
        display: flex;
        flex-direction: column;
        flex-grow: 1;
    }}
    .dest-title {{
        font-size: 1.25rem;
        font-weight: 700;
        color: {text_primary};
        margin-bottom: 8px;
    }}
    .dest-desc {{
        font-size: 0.875rem;
        color: {text_secondary};
        line-height: 1.5;
        margin-bottom: 16px;
        flex-grow: 1;
    }}

    /* Feature Cards */
    .feature-card {{
        background: {bg_card};
        border: 1px solid {border_color};
        border-radius: 16px;
        padding: 22px 18px;
        box-shadow: {card_shadow};
        height: 100%;
        transition: border-color 0.2s ease, transform 0.2s ease;
    }}
    .feature-card:hover {{
        border-color: {accent_teal};
        transform: translateY(-3px);
    }}
    .feature-icon {{
        font-size: 2rem;
        margin-bottom: 12px;
        display: inline-block;
    }}
    .feature-title {{
        font-size: 1.1rem;
        font-weight: 700;
        color: {text_primary};
        margin-bottom: 6px;
    }}
    .feature-desc {{
        font-size: 0.85rem;
        color: {text_secondary};
        line-height: 1.5;
    }}

    /* Chat Bubbles */
    .chat-bubble-user {{
        background-color: {chat_user_bg};
        color: {chat_user_text};
        padding: 14px 18px;
        border-radius: 18px 18px 4px 18px;
        max-width: 82%;
        margin-left: auto;
        margin-bottom: 14px;
        font-size: 0.95rem;
        line-height: 1.5;
        box-shadow: 0 4px 12px rgba(2, 132, 199, 0.2);
    }}
    .chat-bubble-ai {{
        background-color: {chat_ai_bg};
        color: {text_primary};
        border: 1px solid {chat_ai_border};
        padding: 20px 22px;
        border-radius: 18px 18px 18px 4px;
        max-width: 90%;
        margin-right: auto;
        margin-bottom: 20px;
        font-size: 0.95rem;
        line-height: 1.6;
        box-shadow: {card_shadow};
    }}
    .chat-header-ai {{
        display: flex;
        align-items: center;
        gap: 8px;
        margin-bottom: 10px;
        font-size: 0.82rem;
        font-weight: 700;
        color: {accent_teal};
        text-transform: uppercase;
        letter-spacing: 0.05em;
    }}

    /* Buttons & Form controls */
    .stButton>button {{
        border-radius: 10px !important;
        font-weight: 600 !important;
        transition: all 0.2s ease !important;
        border: 1px solid {border_color} !important;
    }}
    .stButton>button:hover {{
        border-color: {accent_teal} !important;
        color: {accent_teal} !important;
        transform: translateY(-1px);
    }}

    /* Primary Accent Button */
    button[kind="primary"] {{
        background-color: {accent_teal} !important;
        border: none !important;
        color: #FFFFFF !important;
    }}
    button[kind="primary"]:hover {{
        background-color: #0f766e !important;
        color: #FFFFFF !important;
    }}

    /* Footer disclaimer */
    .travel-disclaimer {{
        text-align: center;
        font-size: 0.78rem;
        color: {text_secondary};
        padding: 24px 16px 8px 16px;
        border-top: 1px solid {border_color};
        margin-top: 40px;
        line-height: 1.5;
    }}

    /* Responsive Mobile */
    @media (max-width: 768px) {{
        .hero-title {{
            font-size: 2rem !important;
        }}
        .hero-subtitle {{
            font-size: 0.95rem !important;
        }}
        .chat-bubble-user {{
            max-width: 92% !important;
        }}
        .chat-bubble-ai {{
            max-width: 98% !important;
            padding: 15px !important;
        }}
    }}
    </style>
    """


def render_brand_sidebar():
    """Renders elegant branding at the top of the sidebar."""
    st.sidebar.markdown(
        f"""
        <div class="brand-sidebar-box">
            <span class="brand-logo-icon">🌍</span>
            <div class="brand-sidebar-title">{APP_NAME}</div>
            <div class="brand-sidebar-tagline">{TAGLINE}</div>
        </div>
        """,
        unsafe_allow_html=True
    )


def render_hero_section():
    """Renders the startup-style hero section on the homepage."""
    st.markdown(
        f"""
        <div class="hero-container">
            <div class="hero-badge">✨ Next-Generation Travel Intelligence</div>
            <h1 class="hero-title">{HERO_TITLE}</h1>
            <p class="hero-subtitle">{HERO_SUBTITLE}</p>
        </div>
        """,
        unsafe_allow_html=True
    )


def render_destination_card(dest: dict) -> None:
    """Renders a single destination card with imagery, badge and description."""
    st.markdown(
        f"""
        <div class="dest-card">
            <div class="dest-image-wrap">
                <img src="{dest['image']}" alt="{dest['title']}" class="dest-image" loading="lazy" />
                <span class="dest-tag-badge">{dest['tag']}</span>
            </div>
            <div class="dest-content">
                <div class="dest-title">{dest['title']}</div>
                <div class="dest-desc">{dest['desc']}</div>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )


def render_feature_card(feat: dict) -> None:
    """Renders a single feature card."""
    st.markdown(
        f"""
        <div class="feature-card">
            <div class="feature-icon">{feat['icon']}</div>
            <div class="feature-title">{feat['title']}</div>
            <div class="feature-desc">{feat['desc']}</div>
        </div>
        """,
        unsafe_allow_html=True
    )


def render_footer():
    """Renders verification disclaimer and copyright note."""
    st.markdown(
        f"""
        <div class="travel-disclaimer">
            <strong>🛡️ Traveler Advisory:</strong> {LEGAL_DISCLAIMER}
            <br>
            <span style="opacity: 0.8; margin-top: 6px; display: inline-block;">
                © 2026 {APP_NAME}. Powered by Google Gemini AI.
            </span>
        </div>
        """,
        unsafe_allow_html=True
    )
