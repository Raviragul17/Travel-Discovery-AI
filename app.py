"""
TRAVEL DISCOVERY AI - Main Streamlit Application
Tagline: Discover Places. Explore Cultures. Experience the World.
"""

import time
import streamlit as st

import config
import prompts
from gemini_service import GeminiTravelService, get_api_key_from_env_or_secrets
import ui_components

# ---------------------------------------------------------
# Page Configuration
# ---------------------------------------------------------
st.set_page_config(
    page_title=f"{config.APP_NAME} - Explore the World",
    page_icon="🌍",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ---------------------------------------------------------
# Session State Initialization
# ---------------------------------------------------------
if "current_page" not in st.session_state:
    st.session_state.current_page = config.PAGES["HOME"]

if "chat_messages" not in st.session_state:
    st.session_state.chat_messages = []

if "dark_mode" not in st.session_state:
    st.session_state.dark_mode = False

if "language" not in st.session_state:
    st.session_state.language = "English"

if "selected_model" not in st.session_state:
    st.session_state.selected_model = config.DEFAULT_MODEL

if "api_key_override" not in st.session_state:
    # Check environment variable first, then Streamlit secrets
    st.session_state.api_key_override = get_api_key_from_env_or_secrets() or ""

if "pending_query" not in st.session_state:
    st.session_state.pending_query = None

if "last_copied" not in st.session_state:
    st.session_state.last_copied = None

# Initialize Gemini Service
gemini_service = GeminiTravelService(
    api_key=st.session_state.api_key_override,
    model_name=st.session_state.selected_model
)

# ---------------------------------------------------------
# Inject Custom Theme CSS
# ---------------------------------------------------------
st.markdown(ui_components.get_custom_css(dark_mode=st.session_state.dark_mode), unsafe_allow_html=True)


# ---------------------------------------------------------
# Helper Functions
# ---------------------------------------------------------
def switch_page(page_name: str, query: str = None):
    """Navigates to a specific page and optionally enqueues a prompt."""
    st.session_state.current_page = page_name
    if query:
        st.session_state.pending_query = query
    st.rerun()


def reset_chat():
    """Resets conversation history."""
    st.session_state.chat_messages = []
    st.session_state.pending_query = None
    st.rerun()


def send_chat_message(user_text: str):
    """Processes user message, updates chat history, and calls Gemini."""
    if not user_text or not user_text.strip():
        return

    # Add user message to state
    st.session_state.chat_messages.append({
        "role": "user",
        "content": user_text.strip()
    })

    # Call Gemini
    with st.spinner("✈️ Travel Discovery AI is searching ancient archives and travel wisdom..."):
        try:
            # Pass past messages as context
            history = st.session_state.chat_messages[:-1]
            response_text = gemini_service.generate_chat_response(
                user_message=user_text,
                conversation_history=history
            )
            st.session_state.chat_messages.append({
                "role": "assistant",
                "content": response_text
            })
        except Exception as e:
            error_feedback = gemini_service._format_error_message(e)
            st.session_state.chat_messages.append({
                "role": "assistant",
                "content": error_feedback
            })


# ---------------------------------------------------------
# Sidebar Navigation
# ---------------------------------------------------------
ui_components.render_brand_sidebar()

nav_options = list(config.PAGES.values())
try:
    current_index = nav_options.index(st.session_state.current_page)
except ValueError:
    current_index = 0

selected_page = st.sidebar.radio(
    "Navigation",
    nav_options,
    index=current_index,
    label_visibility="collapsed"
)

if selected_page != st.session_state.current_page:
    st.session_state.current_page = selected_page
    st.rerun()

st.sidebar.markdown("<div style='height: 12px;'></div>", unsafe_allow_html=True)

# Quick Chat Session Controls in Sidebar
col_sb1, col_sb2 = st.sidebar.columns(2)
with col_sb1:
    if st.button("🔄 New Chat", use_container_width=True, help="Clear history and start fresh"):
        reset_chat()
with col_sb2:
    if st.button("🗑️ Clear", use_container_width=True, help="Wipe conversation messages"):
        st.session_state.chat_messages = []
        st.rerun()

# Sidebar Status Card
ui_components.render_sidebar_status(
    model_name=st.session_state.selected_model,
    language=st.session_state.language,
    message_count=len(st.session_state.chat_messages)
)


# ---------------------------------------------------------
# Page 1: 🏠 Home
# ---------------------------------------------------------
if st.session_state.current_page == config.PAGES["HOME"]:
    ui_components.render_hero_section()

    # Search Box Container
    st.markdown(
        """
        <div style="background: #FFFFFF; border: 1px solid #E2E8F0; border-radius: 20px; padding: 22px 24px; margin-bottom: 24px; box-shadow: 0 4px 14px -2px rgba(15, 23, 42, 0.05);">
            <div style="display: flex; align-items: center; gap: 8px; margin-bottom: 12px;">
                <span style="font-size: 1.25rem;">🔍</span>
                <strong style="font-size: 1.05rem; color: #0F172A;">Where would you like to travel today?</strong>
            </div>
        """,
        unsafe_allow_html=True
    )
    col_search, col_btn = st.columns([5, 1.4])
    with col_search:
        home_query = st.text_input(
            "Search or ask any travel question:",
            placeholder="e.g. Plan a 4-day heritage tour of Kyoto or tell me ancient temples in Egypt...",
            label_visibility="collapsed"
        )
    with col_btn:
        start_btn = st.button("Explore with AI ✈️", type="primary", use_container_width=True)
    st.markdown("</div>", unsafe_allow_html=True)

    if start_btn and home_query:
        switch_page(config.PAGES["CHAT"], query=home_query)

    # Suggested Questions
    st.markdown("#### 💡 Popular Inspiration & Quick Questions")
    cols_sug = st.columns(3)
    for i, question in enumerate(config.SUGGESTED_QUESTIONS):
        with cols_sug[i % 3]:
            if st.button(f"👉 {question}", key=f"sug_{i}", use_container_width=True):
                switch_page(config.PAGES["CHAT"], query=question)

    st.markdown("<br><hr style='border: none; border-top: 1px solid #E2E8F0; margin: 24px 0;'><br>", unsafe_allow_html=True)

    # Destination Showcase Section
    st.markdown("### 🌟 Extraordinary Destinations Showcase")
    st.markdown(
        "<p style='color: #475569; margin-top: -6px; margin-bottom: 20px;'>"
        "Hand-curated bucket-list destinations combining rich heritage, culinary wonders, and breathtaking landscapes."
        "</p>",
        unsafe_allow_html=True
    )
    
    dest_cols = st.columns(3)
    for idx, dest in enumerate(config.POPULAR_DESTINATIONS):
        with dest_cols[idx % 3]:
            ui_components.render_destination_card(dest)
            if st.button(f"Discover {dest['title']} ➔", key=f"dest_btn_{idx}", use_container_width=True):
                switch_page(config.PAGES["CHAT"], query=dest["prompt"])
            st.markdown("<div style='height: 18px;'></div>", unsafe_allow_html=True)

    st.markdown("<br><hr style='border: none; border-top: 1px solid #E2E8F0; margin: 24px 0;'><br>", unsafe_allow_html=True)

    # Core Features Grid
    st.markdown("### 🧭 Intelligent Travel Features")
    st.markdown(
        "<p style='color: #475569; margin-top: -6px; margin-bottom: 20px;'>"
        "Purpose-built discovery modules powered by Google Gemini AI."
        "</p>",
        unsafe_allow_html=True
    )
    feat_cols = st.columns(3)
    for idx, feat in enumerate(config.FEATURE_CARDS):
        with feat_cols[idx % 3]:
            ui_components.render_feature_card(feat)
            st.markdown("<div style='height: 18px;'></div>", unsafe_allow_html=True)

    ui_components.render_footer()


# ---------------------------------------------------------
# Page 2: 🌍 Discover Destinations
# ---------------------------------------------------------
elif st.session_state.current_page == config.PAGES["DISCOVER"]:
    ui_components.render_page_header(
        icon="🌍",
        title="Destination Discovery",
        subtitle="Get a comprehensive travel briefing for any city, region, or country worldwide.",
        badge="Global Sights & Tips"
    )

    col1, col2, col3 = st.columns([2.5, 1.5, 1.5])
    with col1:
        dest_input = st.text_input("Destination Name:", placeholder="e.g. Barcelona, Spain or Kyoto, Japan or Cairo")
    with col2:
        duration_input = st.selectbox("Trip Length:", ["Weekend Getaway (2-3 Days)", "Full Week (7 Days)", "Extended Trip (10-14 Days)", "Custom"])
    with col3:
        traveler_style = st.selectbox("Traveler Style:", ["Solo Explorer", "Couple / Romantic", "Family Vacation", "Adventure & Hiking", "Luxury Leisure"])

    # Quick inspiration buttons
    st.markdown("<div style='font-size: 0.85rem; color: #64748B; margin-top: 6px; margin-bottom: 6px;'>Popular Hotspots:</div>", unsafe_allow_html=True)
    c_q1, c_q2, c_q3, c_q4, c_q5 = st.columns(5)
    if c_q1.button("🇯🇵 Tokyo", use_container_width=True):
        dest_input = "Tokyo, Japan"
    if c_q2.button("🇫🇷 Paris", use_container_width=True):
        dest_input = "Paris, France"
    if c_q3.button("🇮🇳 Kerala", use_container_width=True):
        dest_input = "Kerala, India"
    if c_q4.button("🇮🇹 Florence", use_container_width=True):
        dest_input = "Florence, Italy"
    if c_q5.button("🇪🇬 Cairo", use_container_width=True):
        dest_input = "Cairo, Egypt"

    if st.button("Generate Destination Guide 🌍", type="primary", use_container_width=True):
        if not dest_input:
            st.warning("Please provide a destination name to explore.")
        else:
            prompt_str = prompts.build_destination_prompt(
                destination=dest_input,
                duration=duration_input,
                traveler_type=traveler_style,
                language=st.session_state.language
            )
            with st.spinner(f"Curating comprehensive guide for {dest_input}..."):
                try:
                    guide_resp = gemini_service.generate_chat_response(prompt_str, [])
                    st.markdown("---")
                    st.markdown(guide_resp)
                    if st.button("💬 Continue Discussion in Travel Chat", type="secondary"):
                        switch_page(config.PAGES["CHAT"], query=f"Tell me more about experiences and transit in {dest_input}")
                except Exception as e:
                    st.markdown(gemini_service._format_error_message(e))

    ui_components.render_footer()


# ---------------------------------------------------------
# Page 3: 🏛️ Ancient Places
# ---------------------------------------------------------
elif st.session_state.current_page == config.PAGES["ANCIENT"]:
    ui_components.render_page_header(
        icon="🏛️",
        title="Ancient Places & Archaeological Explorer",
        subtitle="Uncover timeless wonders, ancient temples, imperial forts, and UNESCO World Heritage locations.",
        badge="Civilizations & Heritage"
    )

    col1, col2 = st.columns([2.5, 1.5])
    with col1:
        region_input = st.text_input("Region, State, or Country:", placeholder="e.g. Tamil Nadu, India or Greece or Egypt or Jordan")
    with col2:
        era_input = st.selectbox("Category / Period:", ["All Historical Wonders", "Ancient Temples & Sanctuaries", "Imperial Fortresses & Palaces", "Archaeological Excavations", "UNESCO World Heritage Sites"])

    st.markdown("<div style='font-size: 0.85rem; color: #64748B; margin-top: 6px; margin-bottom: 6px;'>Popular Ancient Regions:</div>", unsafe_allow_html=True)
    c1, c2, c3, c4 = st.columns(4)
    if c1.button("🏛️ Tamil Nadu Temples", use_container_width=True):
        region_input = "Tamil Nadu, India"
    if c2.button("🏺 Athens & Delphi", use_container_width=True):
        region_input = "Greece"
    if c3.button("👑 Pyramids & Luxor", use_container_width=True):
        region_input = "Egypt"
    if c4.button("🗿 Angkor Wat & Siem Reap", use_container_width=True):
        region_input = "Cambodia"

    if st.button("Uncover Ancient Wonders 🏛️", type="primary", use_container_width=True):
        if not region_input:
            st.warning("Please enter a region or country to explore ancient history.")
        else:
            ancient_prompt = prompts.build_ancient_places_prompt(
                region_or_country=region_input,
                era_or_type=era_input,
                language=st.session_state.language
            )
            with st.spinner(f"Deciphering historical annals for {region_input}..."):
                try:
                    ancient_resp = gemini_service.generate_chat_response(ancient_prompt, [])
                    st.markdown("---")
                    st.markdown(ancient_resp)
                    if st.button("💬 Ask Follow-up in Travel Chat", key="btn_anc_chat"):
                        switch_page(config.PAGES["CHAT"], query=f"Which is the oldest among these ancient places in {region_input} and what was its original architectural purpose?")
                except Exception as e:
                    st.markdown(gemini_service._format_error_message(e))

    ui_components.render_footer()


# ---------------------------------------------------------
# Page 4: 💎 Hidden Gems
# ---------------------------------------------------------
elif st.session_state.current_page == config.PAGES["HIDDEN_GEMS"]:
    ui_components.render_page_header(
        icon="💎",
        title="Hidden Gems & Off-the-Beaten-Path Explorer",
        subtitle="Venture beyond crowded tourist spots to discover tranquil villages, secret trails, and authentic cultural sanctuaries.",
        badge="Secret Spots & Nature"
    )

    col1, col2 = st.columns([2.5, 1.5])
    with col1:
        gem_dest = st.text_input("Destination / Country:", placeholder="e.g. Japan, Italy, Himachal Pradesh, Scotland, Portugal")
    with col2:
        gem_vibe = st.selectbox("Desired Vibe:", [
            "Peaceful Mountain Sanctuaries",
            "Untouched Coastal Coves & Beaches",
            "Traditional Heritage Villages",
            "Artisan & Folk Culture Enclaves",
            "Serene Spiritual Retreats"
        ])

    if st.button("Find Secret Places 💎", type="primary", use_container_width=True):
        if not gem_dest:
            st.warning("Please specify a country or destination.")
        else:
            gem_prompt = prompts.build_hidden_gems_prompt(
                destination=gem_dest,
                vibe=gem_vibe,
                language=st.session_state.language
            )
            with st.spinner(f"Scouting secluded gems across {gem_dest}..."):
                try:
                    gems_resp = gemini_service.generate_chat_response(gem_prompt, [])
                    st.markdown("---")
                    st.markdown(gems_resp)
                    if st.button("💬 Plan an Itinerary for these Hidden Gems", key="btn_gem_chat"):
                        switch_page(config.PAGES["CHAT"], query=f"Plan a slow-travel 4-day itinerary visiting these hidden gems in {gem_dest}")
                except Exception as e:
                    st.markdown(gemini_service._format_error_message(e))

    ui_components.render_footer()


# ---------------------------------------------------------
# Page 5: 📅 Smart Trip Planner
# ---------------------------------------------------------
elif st.session_state.current_page == config.PAGES["TRIP_PLANNER"]:
    ui_components.render_page_header(
        icon="📅",
        title="Smart Day-by-Day Trip Planner",
        subtitle="Create a customized, realistic itinerary (1 to 7 days) with morning, afternoon, and evening suggestions.",
        badge="Custom Schedules"
    )

    col1, col2 = st.columns([2, 1])
    with col1:
        trip_dest = st.text_input("Where are you traveling to?", placeholder="e.g. Kerala, India or London, UK or Iceland")
    with col2:
        trip_days = st.slider("Duration (Days):", min_value=1, max_value=7, value=3)

    col3, col4 = st.columns(2)
    with col3:
        trip_budget = st.selectbox("Budget Tier:", ["Backpacker / Budget-Friendly", "Mid-Range / Comfort", "Luxury / Indulgence"])
    with col4:
        traveler_party = st.selectbox("Traveler Party:", ["Solo", "Couple", "Family with Kids", "Friends Group"])

    trip_interests = st.multiselect(
        "Select Your Key Travel Interests:",
        ["Historical Monuments & Temples", "Local Food & Street Markets", "Nature & Scenery", "Beaches & Water Sports", "Art & Architecture", "Relaxation & Spa", "Shopping & Bazaars"],
        default=["Historical Monuments & Temples", "Local Food & Street Markets", "Nature & Scenery"]
    )

    if st.button("Build My Smart Itinerary 📅", type="primary", use_container_width=True):
        if not trip_dest:
            st.warning("Please enter your destination.")
        else:
            itinerary_prompt = prompts.build_trip_planner_prompt(
                destination=trip_dest,
                days=trip_days,
                budget_level=trip_budget,
                interests=trip_interests,
                traveler_party=traveler_party,
                language=st.session_state.language
            )
            with st.spinner(f"Crafting realistic {trip_days}-day itinerary for {trip_dest}..."):
                try:
                    itinerary_resp = gemini_service.generate_chat_response(itinerary_prompt, [])
                    st.markdown("---")
                    st.markdown(itinerary_resp)
                    if st.button("💬 Refine or Adjust Itinerary in Chat", key="btn_itin_chat"):
                        switch_page(config.PAGES["CHAT"], query=f"How can I adjust this {trip_days}-day itinerary for {trip_dest} to make it more relaxed with less travel time?")
                except Exception as e:
                    st.markdown(gemini_service._format_error_message(e))

    ui_components.render_footer()


# ---------------------------------------------------------
# Page 6: 🍲 Food Explorer
# ---------------------------------------------------------
elif st.session_state.current_page == config.PAGES["FOOD_EXPLORER"]:
    ui_components.render_page_header(
        icon="🍲",
        title="Authentic Food & Culinary Explorer",
        subtitle="Delve into authentic regional cuisines, legendary street foods, market stalls, and culinary customs.",
        badge="Flavors & Dining"
    )

    col1, col2 = st.columns([2.5, 1.5])
    with col1:
        food_dest = st.text_input("Destination / Region for Culinary Discovery:", placeholder="e.g. Italy or Tamil Nadu or Mexico or Thailand or Turkey")
    with col2:
        diet_pref = st.selectbox("Dietary Preference:", [
            "All (Omnivore & Traditional)",
            "Pure Vegetarian",
            "Vegan / Plant-Based",
            "Halal",
            "Street Food & Night Markets Only"
        ])

    st.markdown("<div style='font-size: 0.85rem; color: #64748B; margin-top: 6px; margin-bottom: 6px;'>Popular Foodie Hotspots:</div>", unsafe_allow_html=True)
    f1, f2, f3, f4 = st.columns(4)
    if f1.button("🇮🇹 Italian Regional Pasta", use_container_width=True):
        food_dest = "Italy"
    if f2.button("🇮🇳 Tamil Nadu Filter Coffee & Meals", use_container_width=True):
        food_dest = "Tamil Nadu, India"
    if f3.button("🇹🇭 Bangkok Night Markets", use_container_width=True):
        food_dest = "Bangkok, Thailand"
    if f4.button("🇲🇽 Oaxaca Street Tacos", use_container_width=True):
        food_dest = "Oaxaca, Mexico"

    if st.button("Explore Culinary Wonders 🍲", type="primary", use_container_width=True):
        if not food_dest:
            st.warning("Please enter a destination to explore its cuisine.")
        else:
            food_prompt = prompts.build_food_explorer_prompt(
                destination=food_dest,
                diet_pref=diet_pref,
                language=st.session_state.language
            )
            with st.spinner(f"Gathering culinary recipes and secret market foods of {food_dest}..."):
                try:
                    food_resp = gemini_service.generate_chat_response(food_prompt, [])
                    st.markdown("---")
                    st.markdown(food_resp)
                    if st.button("💬 Discuss Food Experiences in Travel Chat", key="btn_food_chat"):
                        switch_page(config.PAGES["CHAT"], query=f"What are the best neighborhoods or street markets in {food_dest} to try these foods?")
                except Exception as e:
                    st.markdown(gemini_service._format_error_message(e))

    ui_components.render_footer()


# ---------------------------------------------------------
# Page 7: 💬 Travel Chat
# ---------------------------------------------------------
elif st.session_state.current_page == config.PAGES["CHAT"]:
    # Chat Header
    c_title, c_lang, c_actions = st.columns([4.5, 1.8, 2.2])
    with c_title:
        st.markdown(
            """
            <div style="display: flex; align-items: center; gap: 10px;">
                <h2 style="margin: 0; font-size: 1.8rem; font-weight: 800; color: #0F172A;">💬 Travel Discovery AI Chat</h2>
                <span style="background: #E6F4F1; color: #0D9488; font-size: 0.72rem; font-weight: 700; padding: 4px 10px; border-radius: 20px; text-transform: uppercase;">
                    ● Active Consultant
                </span>
            </div>
            <p style="color: #64748B; margin: 4px 0 0 0; font-size: 0.9rem;">Multi-turn conversational memory active. Ask follow-up questions anytime.</p>
            """,
            unsafe_allow_html=True
        )
    with c_lang:
        lang_choice = st.selectbox(
            "Language",
            list(config.LANGUAGES.keys()),
            index=0 if st.session_state.language == "English" else 1,
            label_visibility="collapsed"
        )
        if lang_choice != st.session_state.language:
            st.session_state.language = lang_choice
            st.rerun()
    with c_actions:
        b1, b2 = st.columns(2)
        with b1:
            if st.button("🔄 New Chat", use_container_width=True):
                reset_chat()
        with b2:
            if st.button("🗑️ Clear", use_container_width=True):
                st.session_state.chat_messages = []
                st.rerun()

    st.markdown("<hr style='border: none; border-top: 1px solid #E2E8F0; margin: 18px 0;'>", unsafe_allow_html=True)

    # If pending query transferred from another page, trigger it
    if st.session_state.pending_query:
        query_to_run = st.session_state.pending_query
        st.session_state.pending_query = None
        send_chat_message(query_to_run)
        st.rerun()

    # Empty State: Welcome Message
    if not st.session_state.chat_messages:
        st.markdown(
            """
            <div style="background: #FFFFFF; border: 1px dashed #CBD5E1; border-radius: 20px; padding: 32px 24px; text-align: center; margin-bottom: 28px; box-shadow: 0 4px 14px -2px rgba(15, 23, 42, 0.04);">
                <div style="font-size: 38px; margin-bottom: 10px;">👋</div>
                <h3 style="margin-top: 0; color: #0F172A; font-weight: 800;">Welcome to Travel Discovery AI!</h3>
                <p style="color: #475569; max-width: 650px; margin: 0 auto 16px auto; font-size: 0.98rem; line-height: 1.6;">
                    I am your knowledgeable international travel consultant and heritage specialist.
                    Ask me anything about ancient ruins, hidden gems, day-by-day itineraries, authentic cuisine, or budget estimates.
                </p>
                <div style="display: inline-flex; align-items: center; gap: 6px; background: #E6F4F1; color: #0D9488; font-size: 0.82rem; font-weight: 600; padding: 6px 14px; border-radius: 20px;">
                    ✨ Conversational memory enabled: You can ask natural follow-up questions anytime!
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

        st.markdown("##### 💡 Try asking:")
        q_cols = st.columns(3)
        for i, q in enumerate(config.SUGGESTED_QUESTIONS):
            with q_cols[i % 3]:
                if st.button(f"✨ {q}", key=f"chat_sug_{i}", use_container_width=True):
                    send_chat_message(q)
                    st.rerun()

    # Render Chat History
    for idx, msg in enumerate(st.session_state.chat_messages):
        if msg["role"] == "user":
            st.markdown(
                f"""
                <div class="chat-bubble-user">
                    <strong>You</strong><br>
                    {msg["content"]}
                </div>
                """,
                unsafe_allow_html=True
            )
        else:
            st.markdown(
                f"""
                <div class="chat-bubble-ai">
                    <div class="chat-header-ai">
                        <div class="chat-avatar-ai">🌍</div>
                        <div class="chat-title-ai">Travel Discovery AI</div>
                    </div>
                </div>
                """,
                unsafe_allow_html=True
            )
            # Render Markdown content cleanly
            st.markdown(msg["content"])

            # Copy / action row for assistant response
            col_cp, col_space = st.columns([1.8, 6])
            with col_cp:
                with st.expander("📋 View / Copy Text"):
                    st.code(msg["content"], language="markdown")

    # Follow-up quick prompts if chat has messages
    if st.session_state.chat_messages:
        st.markdown("<br><div style='font-size: 0.85rem; font-weight: 700; color: #475569; margin-bottom: 8px;'>Suggested Follow-ups:</div>", unsafe_allow_html=True)
        f_cols = st.columns(len(config.FOLLOW_UP_SUGGESTIONS))
        for idx, f_prompt in enumerate(config.FOLLOW_UP_SUGGESTIONS):
            with f_cols[idx]:
                if st.button(f_prompt, key=f"follow_{idx}", use_container_width=True):
                    send_chat_message(f_prompt)
                    st.rerun()

    # Bottom Chat Input
    user_input = st.chat_input("Ask any travel question or continue the conversation...")
    if user_input:
        send_chat_message(user_input)
        st.rerun()

    ui_components.render_footer()


# ---------------------------------------------------------
# Page 8: ⚙️ Settings
# ---------------------------------------------------------
elif st.session_state.current_page == config.PAGES["SETTINGS"]:
    ui_components.render_page_header(
        icon="⚙️",
        title="Application Settings & Preferences",
        subtitle="Configure your Google Gemini API key, model selection, interface theme, and language preferences.",
        badge="Control Panel"
    )

    # 1. API Configuration Section
    st.markdown("### 🔑 Google Gemini API Key")
    current_key = st.session_state.api_key_override

    # Mask key for display security
    key_input = st.text_input(
        "Enter or update your Gemini API Key:",
        value=current_key,
        type="password",
        help="Reads from GEMINI_API_KEY environment variable or .streamlit/secrets.toml."
    )

    c_save, c_test = st.columns([1, 1.5])
    with c_save:
        if st.button("Save API Key", type="primary", use_container_width=True):
            st.session_state.api_key_override = key_input.strip()
            gemini_service.set_api_key(key_input.strip())
            st.success("API Key updated in current session!")

    with c_test:
        if st.button("🧪 Test API Connection", use_container_width=True):
            gemini_service.set_api_key(key_input.strip())
            with st.spinner("Testing connection to Gemini..."):
                success, msg = gemini_service.test_connection()
                if success:
                    st.success(f"✅ {msg}")
                else:
                    st.error(msg)

    st.markdown(
        """
        <div style="font-size: 0.82rem; color: #64748B; margin-top: 8px;">
            🔒 <strong>Security:</strong> API keys are held securely in memory, environment variables, or Streamlit secrets and are never exposed.
            Need a key? Get one free at <a href="https://aistudio.google.com/app/apikey" target="_blank" style="color: #0D9488;">Google AI Studio</a>.
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown("<hr style='border: none; border-top: 1px solid #E2E8F0; margin: 24px 0;'>", unsafe_allow_html=True)

    # 2. Model Settings Section
    st.markdown("### 🤖 Gemini Model Selection")
    col_m1, col_m2 = st.columns(2)
    with col_m1:
        model_choice = st.selectbox(
            "Selected Gemini Model:",
            config.SUPPORTED_MODELS,
            index=config.SUPPORTED_MODELS.index(st.session_state.selected_model) if st.session_state.selected_model in config.SUPPORTED_MODELS else 0
        )
        if model_choice != st.session_state.selected_model:
            st.session_state.selected_model = model_choice
            gemini_service.set_model(model_choice)
            st.info(f"Model updated to `{model_choice}`.")

    with col_m2:
        st.markdown(
            f"""
            <div style="padding: 14px; background: #E6F4F1; border-radius: 12px; font-size: 0.85rem; border: 1px solid rgba(13,148,136,0.15); color: #0F766E;">
                <strong>Recommended:</strong> <code>gemini-3.5-flash-lite</code> is fast, highly capable, and fully free within standard Gemini API limits.
            </div>
            """,
            unsafe_allow_html=True
        )

    st.markdown("<hr style='border: none; border-top: 1px solid #E2E8F0; margin: 24px 0;'>", unsafe_allow_html=True)

    # 3. UI Theme & Preferences
    st.markdown("### 🎨 UI Appearance & Language")
    col_t1, col_t2 = st.columns(2)
    with col_t1:
        theme_toggle = st.radio(
            "Interface Color Theme:",
            ["Clean White & Light Slate (Default)", "Midnight Ocean (Dark Mode)"],
            index=1 if st.session_state.dark_mode else 0
        )
        is_dark = "Dark" in theme_toggle
        if is_dark != st.session_state.dark_mode:
            st.session_state.dark_mode = is_dark
            st.rerun()

    with col_t2:
        lang_pref = st.radio(
            "Default Language:",
            list(config.LANGUAGES.keys()),
            index=0 if st.session_state.language == "English" else 1
        )
        if lang_pref != st.session_state.language:
            st.session_state.language = lang_pref
            st.rerun()

    ui_components.render_footer()
