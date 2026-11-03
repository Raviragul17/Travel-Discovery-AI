# 🌍 TRAVEL DISCOVERY AI

> **Discover Places. Explore Cultures. Experience the World.**

A premium, modern AI-powered travel discovery assistant built with **Python**, **Streamlit**, and the **Google Gemini API**. TRAVEL DISCOVERY AI helps travelers explore worldwide destinations, uncover ancient historical wonders, discover peaceful hidden gems, generate realistic day-by-day itineraries, savor authentic regional cuisines, and estimate realistic travel budgets.

---

## ✨ Features

- **🏠 Interactive Landing Page**: Hero showcase, large natural-language travel search input, bucket-list destination cards, and quick question suggestions.
- **🌍 Destination Discovery**: Deep dives into cities, states, and nations worldwide covering highlights, culture, seasonality, and local customs.
- **🏛️ Ancient Places & Archaeological Explorer**: Detailed historical context, architectural marvels, and preservation etiquette for ancient temples, imperial forts, and UNESCO Heritage sites.
- **💎 Untouched Hidden Gems**: Uncover off-the-beaten-path villages, peaceful mountain viewpoints, and authentic artisan culture away from tourist crowds.
- **📅 Smart 1–7 Day Trip Planner**: Structured day-by-day schedules with chronological Morning 🌅, Afternoon ☀️, and Evening 🌙 activities, transit tips, and local dining suggestions.
- **🍲 Food Explorer**: Authentic regional delicacies, street food hotspots, traditional cuisines, and dining customs.
- **💰 Smart Budget Planner**: Itemized approximations for accommodation, dining, local transit, and sightseeing tickets with clear disclaimers.
- **💬 Travel Chat with Session Memory**: Full multi-turn conversational AI that remembers previous questions (e.g. asking *"Suggest ancient places in Tamil Nadu"* followed by *"Which is the oldest?"*).
- **🌐 Bilingual Support**: Seamless conversational fluency in both **English** and **Tamil (தமிழ்)**.
- **🎨 Premium UI Design**: Warm white and coastal sand aesthetic, deep navy typography, teal accents, rounded cards, and an optional **Midnight Ocean Dark Mode**.

---

## 🏗️ Technology Stack

- **Frontend & App Framework**: [Streamlit](https://streamlit.io/)
- **AI Intelligence**: [Google Gemini API](https://ai.google.dev/) (Default: `gemini-3.5-flash-lite` / `gemini-3.8-flash`)
- **SDK & Client**: Official Google Gen AI SDK + Resilient HTTP Failover
- **Styling**: Custom CSS with responsive modern startup typography and cards
- **State Management**: Streamlit Session State for conversation history

---

## 📁 Project File Structure

```text
Travel-Discovery-AI/
├── app.py                     # Main Streamlit application and page controllers
├── gemini_service.py          # Unified Gemini service with SDK & REST failover
├── prompts.py                 # Structured system instructions and feature templates
├── ui_components.py           # Custom CSS styling, hero banner, cards, and footer
├── config.py                  # App configuration, models, curated destinations
├── requirements.txt           # Python dependencies
├── README.md                  # Complete documentation and setup guide
├── .gitignore                 # Excludes secrets and temporary cache
└── .streamlit/
    ├── config.toml            # UI theme parameters (colors, fonts)
    ├── secrets.toml.example   # Example template for API key
    └── secrets.toml           # Local API key configuration (git-ignored)
```

---

## 🚀 Quick Start Guide

### 1. Prerequisites
- Python 3.8 or higher installed on your computer.
- A free Google Gemini API key from [Google AI Studio](https://aistudio.google.com/app/apikey).

### 2. Clone or Navigate to the Directory
```bash
cd Travel-Discovery-AI
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure Your Gemini API Key
Create or edit `.streamlit/secrets.toml`:
```toml
GEMINI_API_KEY = "your_actual_gemini_api_key_here"
```
*(Alternatively, you can paste your API key directly inside the in-app **Settings** tab, or export it as an environment variable: `export GEMINI_API_KEY="your_key"`)*

### 5. Launch the Application
```bash
streamlit run app.py
```
The application will launch automatically in your default browser at `http://localhost:8501`.

---

## ☁️ Deployment to Streamlit Community Cloud

Deploying your Travel Discovery AI chatbot online for free is simple:

1. Push your repository to **GitHub**:
   ```bash
   git init
   git add .
   git commit -m "Initial commit: Travel Discovery AI"
   git remote add origin https://github.com/<your-username>/Travel-Discovery-AI.git
   git branch -M main
   git push -u origin main
   ```
2. Go to [share.streamlit.io](https://share.streamlit.io/) and sign in with GitHub.
3. Click **"New app"**, select your repository, branch (`main`), and set the main file path to `app.py`.
4. Under **Advanced Settings** ➔ **Secrets**, paste:
   ```toml
   GEMINI_API_KEY = "your_actual_gemini_api_key_here"
   ```
5. Click **"Deploy!"** Your chatbot will be live with a public URL!

---

## 🛡️ Traveler Advisory & Disclaimer

Travel Discovery AI provides inspirational guides and estimated budgets based on historical travel knowledge. Ticket prices, opening hours, local visa regulations, and safety advisories fluctuate frequently. Always verify current entry requirements and details with official travel authorities, national parks, consulates, and operators prior to departure.

---

## 📄 License
MIT License. Created with passion for travel and culture.
