"""
UI Components and Styling for Travel Discovery AI.
Provides premium, luxury travel startup styling, custom HTML cards,
modern hero section with background travel imagery, responsive layouts,
smooth subtle animations, and elevated chat interface.
Supports light (Clean White & Slate) and dark (Midnight Ocean) themes.
"""

import streamlit as st
from config import APP_NAME, TAGLINE, HERO_TITLE, HERO_SUBTITLE, LEGAL_DISCLAIMER


def get_custom_css(dark_mode: bool = False) -> str:
    """Returns responsive modern CSS adhering to luxury travel startup design systems."""
    if dark_mode:
        # Midnight Ocean Theme
        bg_main = "#0B132B"
        bg_card = "#1C2541"
        bg_card_alt = "#243256"
        bg_subtle = "#162038"
        text_primary = "#F8FAFC"
        text_secondary = "#94A3B8"
        text_muted = "#64748B"
        accent_teal = "#14B8A6"
        accent_blue = "#38BDF8"
        border_color = "rgba(255, 255, 255, 0.12)"
        border_subtle = "rgba(255, 255, 255, 0.06)"
        card_shadow = "0 10px 25px -5px rgba(0, 0, 0, 0.5), 0 8px 10px -6px rgba(0, 0, 0, 0.5)"
        card_shadow_hover = "0 20px 35px -5px rgba(0, 0, 0, 0.65)"
        badge_bg = "rgba(20, 184, 166, 0.18)"
        badge_text = "#5EEAD4"
        chat_user_bg = "linear-gradient(135deg, #0284C7 0%, #0369A1 100%)"
        chat_user_text = "#FFFFFF"
        chat_ai_bg = "#1C2541"
        chat_ai_border = "rgba(255, 255, 255, 0.12)"
        input_bg = "#151F36"
    else:
        # Clean White & Light Background with Dark Readable Text
        bg_main = "#F8FAFC"
        bg_card = "#FFFFFF"
        bg_card_alt = "#F1F5F9"
        bg_subtle = "#F8FAFC"
        text_primary = "#0F172A"      # Slate 900: Crisp & readable
        text_secondary = "#334155"    # Slate 700: High contrast
        text_muted = "#64748B"        # Slate 500: Clear secondary
        accent_teal = "#0D9488"       # Deep Aegean Teal
        accent_blue = "#0284C7"       # Ocean Blue
        border_color = "#E2E8F0"      # Slate 200: Elegant subtle border
        border_subtle = "#F1F5F9"     # Slate 100
        card_shadow = "0 4px 14px -2px rgba(15, 23, 42, 0.05), 0 2px 6px -1px rgba(15, 23, 42, 0.03)"
        card_shadow_hover = "0 18px 30px -4px rgba(15, 23, 42, 0.1), 0 6px 12px -2px rgba(15, 23, 42, 0.06)"
        badge_bg = "#E6F4F1"
        badge_text = "#0F766E"
        chat_user_bg = "linear-gradient(135deg, #0284C7 0%, #0369A1 100%)"
        chat_user_text = "#FFFFFF"
        chat_ai_bg = "#FFFFFF"
        chat_ai_border = "#E2E8F0"
        input_bg = "#FFFFFF"

    return f"""
    <style>
    /* -------------------------------------------------------------
       1. Typography & Global Resets
       ------------------------------------------------------------- */
    @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@400;500;600;700;800&family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&display=swap');

    html, body, [class*="css"], [class*="st-"] {{
        font-family: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
        color: {text_primary};
    }}

    h1, h2, h3, h4, .brand-title, .hero-title, .page-header-title {{
        font-family: 'Outfit', 'Plus Jakarta Sans', sans-serif !important;
        font-weight: 700 !important;
        color: {text_primary} !important;
        letter-spacing: -0.02em !important;
    }}

    .stApp {{
        background-color: {bg_main} !important;
        color: {text_primary} !important;
    }}

    /* Main Container Padding */
    .block-container {{
        padding-top: 1.6rem !important;
        padding-bottom: 3.5rem !important;
        max-width: 1240px;
    }}

    /* -------------------------------------------------------------
       2. Keyframe Animations
       ------------------------------------------------------------- */
    @keyframes fadeInUp {{
        from {{
            opacity: 0;
            transform: translateY(14px);
        }}
        to {{
            opacity: 1;
            transform: translateY(0);
        }}
    }}

    @keyframes pulseGlow {{
        0%, 100% {{
            box-shadow: 0 0 0 0 rgba(13, 148, 136, 0.4);
        }}
        50% {{
            box-shadow: 0 0 0 8px rgba(13, 148, 136, 0);
        }}
    }}

    .animate-fade-in {{
        animation: fadeInUp 0.5s cubic-bezier(0.16, 1, 0.3, 1) forwards;
    }}

    /* -------------------------------------------------------------
       3. Modern Navigation Sidebar
       ------------------------------------------------------------- */
    section[data-testid="stSidebar"] {{
        background-color: {bg_card} !important;
        border-right: 1px solid {border_color} !important;
        box-shadow: 2px 0 12px rgba(15, 23, 42, 0.03);
    }}

    section[data-testid="stSidebar"] .block-container {{
        padding-top: 1.5rem !important;
        padding-left: 1.2rem !important;
        padding-right: 1.2rem !important;
    }}

    .brand-sidebar-box {{
        padding: 16px 14px;
        margin-bottom: 18px;
        background: linear-gradient(145deg, {bg_card_alt} 0%, {bg_card} 100%);
        border: 1px solid {border_color};
        border-radius: 16px;
        text-align: center;
        box-shadow: {card_shadow};
        transition: transform 0.25s ease;
    }}
    .brand-sidebar-box:hover {{
        transform: translateY(-2px);
    }}
    .brand-logo-wrap {{
        display: inline-flex;
        align-items: center;
        justify-content: center;
        width: 52px;
        height: 52px;
        background: linear-gradient(135deg, {accent_teal} 0%, {accent_blue} 100%);
        border-radius: 14px;
        margin-bottom: 8px;
        box-shadow: 0 6px 16px rgba(13, 148, 136, 0.25);
    }}
    .brand-logo-icon {{
        font-size: 28px;
        line-height: 1;
    }}
    .brand-sidebar-title {{
        font-family: 'Outfit', sans-serif;
        font-size: 1.08rem;
        font-weight: 800;
        letter-spacing: 0.06em;
        color: {accent_teal};
        margin: 0;
        text-transform: uppercase;
    }}
    .brand-sidebar-tagline {{
        font-size: 0.74rem;
        color: {text_muted};
        margin-top: 4px;
        font-weight: 500;
        line-height: 1.3;
    }}

    /* Sidebar Status Card */
    .sidebar-status-pill {{
        background: {bg_card_alt};
        border: 1px solid {border_color};
        border-radius: 14px;
        padding: 12px 14px;
        margin-top: 14px;
        font-size: 0.8rem;
        line-height: 1.6;
    }}
    .sidebar-status-indicator {{
        display: inline-block;
        width: 8px;
        height: 8px;
        background-color: #10B981;
        border-radius: 50%;
        margin-right: 6px;
        animation: pulseGlow 2s infinite;
    }}

    /* Radio Navigation in Sidebar */
    div[data-testid="stRadio"] > div {{
        gap: 6px;
    }}
    div[data-testid="stRadio"] label {{
        background: {bg_card} !important;
        border: 1px solid {border_color} !important;
        border-radius: 10px !important;
        padding: 9px 14px !important;
        margin-bottom: 4px !important;
        transition: all 0.2s cubic-bezier(0.16, 1, 0.3, 1) !important;
        cursor: pointer !important;
        font-weight: 500 !important;
    }}
    div[data-testid="stRadio"] label:hover {{
        background: {bg_card_alt} !important;
        border-color: {accent_teal} !important;
        transform: translateX(3px);
    }}
    div[data-testid="stRadio"] label[data-checked="true"] {{
        background: linear-gradient(135deg, rgba(13, 148, 136, 0.1) 0%, rgba(2, 132, 199, 0.08) 100%) !important;
        border-color: {accent_teal} !important;
        font-weight: 700 !important;
        color: {accent_teal} !important;
    }}

    /* -------------------------------------------------------------
       4. Hero Section with Travel Background Image
       ------------------------------------------------------------- */
    .hero-banner-wrap {{
        position: relative;
        border-radius: 26px;
        overflow: hidden;
        margin-bottom: 32px;
        box-shadow: 0 16px 36px -8px rgba(15, 23, 42, 0.2);
        border: 1px solid {border_color};
        /* Stunning high-res panoramic travel background */
        background-image: url('https://images.unsplash.com/photo-1469854523086-cc02fe5d8800?auto=format&fit=crop&w=1920&q=85');
        background-size: cover;
        background-position: center center;
        background-repeat: no-repeat;
    }}
    .hero-overlay {{
        position: relative;
        padding: 56px 32px 48px 32px;
        background: linear-gradient(180deg, rgba(15, 23, 42, 0.72) 0%, rgba(15, 23, 42, 0.88) 100%);
        backdrop-filter: blur(2px);
        text-align: center;
        color: #FFFFFF;
    }}
    .hero-pill-badge {{
        display: inline-flex;
        align-items: center;
        gap: 8px;
        background: rgba(255, 255, 255, 0.14);
        backdrop-filter: blur(10px);
        border: 1px solid rgba(255, 255, 255, 0.25);
        color: #FFFFFF;
        padding: 7px 18px;
        border-radius: 30px;
        font-size: 0.82rem;
        font-weight: 700;
        letter-spacing: 0.06em;
        text-transform: uppercase;
        margin-bottom: 20px;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15);
    }}
    .hero-title {{
        font-family: 'Outfit', sans-serif !important;
        font-size: 3.1rem !important;
        font-weight: 800 !important;
        line-height: 1.18 !important;
        color: #FFFFFF !important;
        max-width: 860px;
        margin: 0 auto 18px auto;
        letter-spacing: -0.03em !important;
        text-shadow: 0 2px 14px rgba(0, 0, 0, 0.4);
    }}
    .hero-title-gradient {{
        background: linear-gradient(135deg, #38BDF8 0%, #2DD4BF 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        display: inline-block;
    }}
    .hero-subtitle {{
        font-size: 1.15rem;
        line-height: 1.65;
        color: rgba(241, 245, 249, 0.94);
        max-width: 720px;
        margin: 0 auto 28px auto;
        font-weight: 400;
        text-shadow: 0 1px 4px rgba(0, 0, 0, 0.3);
    }}
    .hero-stats-row {{
        display: flex;
        align-items: center;
        justify-content: center;
        gap: 20px;
        flex-wrap: wrap;
        margin-top: 10px;
    }}
    .hero-stat-item {{
        background: rgba(255, 255, 255, 0.1);
        backdrop-filter: blur(8px);
        border: 1px solid rgba(255, 255, 255, 0.18);
        border-radius: 12px;
        padding: 8px 16px;
        font-size: 0.82rem;
        font-weight: 600;
        color: #F8FAFC;
        display: inline-flex;
        align-items: center;
        gap: 6px;
    }}

    /* -------------------------------------------------------------
       5. Modern Page Header for Feature Pages
       ------------------------------------------------------------- */
    .page-header-container {{
        background: {bg_card};
        border: 1px solid {border_color};
        border-radius: 20px;
        padding: 28px 28px 24px 28px;
        margin-bottom: 28px;
        box-shadow: {card_shadow};
        position: relative;
        overflow: hidden;
    }}
    .page-header-container::before {{
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        height: 4px;
        background: linear-gradient(90deg, {accent_teal} 0%, {accent_blue} 100%);
    }}
    .page-header-top {{
        display: flex;
        align-items: center;
        gap: 12px;
        margin-bottom: 8px;
    }}
    .page-header-icon-box {{
        width: 44px;
        height: 44px;
        border-radius: 12px;
        background: {badge_bg};
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 24px;
    }}
    .page-header-title {{
        font-size: 1.85rem !important;
        font-weight: 800 !important;
        color: {text_primary} !important;
        margin: 0 !important;
    }}
    .page-header-subtitle {{
        font-size: 0.98rem;
        color: {text_secondary};
        margin: 0;
        line-height: 1.55;
    }}

    /* -------------------------------------------------------------
       6. Destination Cards (Responsive Grid)
       ------------------------------------------------------------- */
    .dest-card {{
        background: {bg_card};
        border-radius: 20px;
        overflow: hidden;
        border: 1px solid {border_color};
        box-shadow: {card_shadow};
        transition: transform 0.3s cubic-bezier(0.16, 1, 0.3, 1), box-shadow 0.3s cubic-bezier(0.16, 1, 0.3, 1), border-color 0.3s ease;
        height: 100%;
        display: flex;
        flex-direction: column;
    }}
    .dest-card:hover {{
        transform: translateY(-6px);
        box-shadow: {card_shadow_hover};
        border-color: rgba(13, 148, 136, 0.35);
    }}
    .dest-image-wrap {{
        position: relative;
        width: 100%;
        height: 205px;
        overflow: hidden;
        background-color: {bg_card_alt};
    }}
    .dest-image {{
        width: 100%;
        height: 100%;
        object-fit: cover;
        transition: transform 0.6s cubic-bezier(0.16, 1, 0.3, 1);
    }}
    .dest-card:hover .dest-image {{
        transform: scale(1.08);
    }}
    .dest-tag-badge {{
        position: absolute;
        top: 14px;
        left: 14px;
        background: rgba(15, 23, 42, 0.72);
        backdrop-filter: blur(8px);
        color: #FFFFFF;
        font-size: 0.74rem;
        font-weight: 600;
        padding: 5px 12px;
        border-radius: 20px;
        letter-spacing: 0.04em;
        box-shadow: 0 4px 10px rgba(0, 0, 0, 0.15);
        border: 1px solid rgba(255, 255, 255, 0.15);
    }}
    .dest-content {{
        padding: 20px;
        display: flex;
        flex-direction: column;
        flex-grow: 1;
    }}
    .dest-title {{
        font-family: 'Outfit', sans-serif;
        font-size: 1.25rem;
        font-weight: 700;
        color: {text_primary};
        margin-bottom: 8px;
        line-height: 1.3;
    }}
    .dest-desc {{
        font-size: 0.88rem;
        color: {text_secondary};
        line-height: 1.55;
        margin-bottom: 16px;
        flex-grow: 1;
    }}

    /* -------------------------------------------------------------
       7. Feature Cards
       ------------------------------------------------------------- */
    .feature-card {{
        background: {bg_card};
        border: 1px solid {border_color};
        border-radius: 18px;
        padding: 24px 20px;
        box-shadow: {card_shadow};
        height: 100%;
        transition: all 0.25s cubic-bezier(0.16, 1, 0.3, 1);
    }}
    .feature-card:hover {{
        border-color: {accent_teal};
        transform: translateY(-4px);
        box-shadow: {card_shadow_hover};
    }}
    .feature-icon-wrap {{
        width: 48px;
        height: 48px;
        border-radius: 14px;
        background: linear-gradient(135deg, rgba(13, 148, 136, 0.12) 0%, rgba(2, 132, 199, 0.12) 100%);
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 24px;
        margin-bottom: 16px;
    }}
    .feature-title {{
        font-family: 'Outfit', sans-serif;
        font-size: 1.12rem;
        font-weight: 700;
        color: {text_primary};
        margin-bottom: 8px;
    }}
    .feature-desc {{
        font-size: 0.88rem;
        color: {text_secondary};
        line-height: 1.55;
    }}

    /* -------------------------------------------------------------
       8. Chat Interface & Bubbles
       ------------------------------------------------------------- */
    .chat-bubble-user {{
        background: {chat_user_bg};
        color: {chat_user_text} !important;
        padding: 16px 20px;
        border-radius: 20px 20px 4px 20px;
        max-width: 82%;
        margin-left: auto;
        margin-bottom: 16px;
        font-size: 0.96rem;
        line-height: 1.55;
        box-shadow: 0 4px 14px rgba(2, 132, 199, 0.22);
        animation: fadeInUp 0.3s ease;
    }}
    .chat-bubble-user strong {{
        color: #FFFFFF !important;
        font-weight: 700;
    }}

    .chat-bubble-ai {{
        background-color: {chat_ai_bg};
        color: {text_primary};
        border: 1px solid {chat_ai_border};
        padding: 22px 24px;
        border-radius: 20px 20px 20px 4px;
        max-width: 92%;
        margin-right: auto;
        margin-bottom: 22px;
        font-size: 0.96rem;
        line-height: 1.65;
        box-shadow: {card_shadow};
        animation: fadeInUp 0.35s ease;
    }}
    .chat-header-ai {{
        display: flex;
        align-items: center;
        gap: 10px;
        margin-bottom: 12px;
        padding-bottom: 10px;
        border-bottom: 1px solid {border_color};
    }}
    .chat-avatar-ai {{
        width: 32px;
        height: 32px;
        border-radius: 10px;
        background: linear-gradient(135deg, {accent_teal} 0%, {accent_blue} 100%);
        color: #FFFFFF;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 16px;
        box-shadow: 0 2px 8px rgba(13, 148, 136, 0.25);
    }}
    .chat-title-ai {{
        font-size: 0.88rem;
        font-weight: 700;
        color: {accent_teal};
        text-transform: uppercase;
        letter-spacing: 0.05em;
    }}

    /* Markdown inside AI response */
    .chat-bubble-ai h1, .chat-bubble-ai h2, .chat-bubble-ai h3 {{
        color: {text_primary} !important;
        margin-top: 14px;
        margin-bottom: 8px;
    }}
    .chat-bubble-ai ul, .chat-bubble-ai ol {{
        padding-left: 20px;
        margin-bottom: 10px;
    }}
    .chat-bubble-ai li {{
        margin-bottom: 4px;
        color: {text_secondary};
    }}

    /* -------------------------------------------------------------
       9. Form Inputs & Interactive Controls
       ------------------------------------------------------------- */
    .stTextInput input, .stSelectbox [data-baseweb="select"], .stTextArea textarea {{
        border-radius: 12px !important;
        border: 1px solid {border_color} !important;
        background-color: {input_bg} !important;
        color: {text_primary} !important;
        padding: 10px 14px !important;
        font-size: 0.95rem !important;
        box-shadow: 0 1px 3px rgba(0, 0, 0, 0.03) !important;
        transition: all 0.2s ease !important;
    }}
    .stTextInput input:focus, .stSelectbox [data-baseweb="select"]:focus-within {{
        border-color: {accent_teal} !important;
        box-shadow: 0 0 0 3px rgba(13, 148, 136, 0.16) !important;
    }}

    /* Button Enhancements */
    .stButton > button {{
        border-radius: 12px !important;
        font-weight: 600 !important;
        font-size: 0.92rem !important;
        padding: 8px 18px !important;
        transition: all 0.22s cubic-bezier(0.16, 1, 0.3, 1) !important;
        border: 1px solid {border_color} !important;
        background-color: {bg_card} !important;
        color: {text_primary} !important;
    }}
    .stButton > button:hover {{
        border-color: {accent_teal} !important;
        color: {accent_teal} !important;
        transform: translateY(-2px);
        box-shadow: 0 6px 16px rgba(15, 23, 42, 0.08) !important;
    }}
    .stButton > button:active {{
        transform: translateY(0) !important;
    }}

    /* Primary Buttons */
    button[kind="primary"], .stButton > button[kind="primary"] {{
        background: linear-gradient(135deg, {accent_teal} 0%, #0F766E 100%) !important;
        border: none !important;
        color: #FFFFFF !important;
        box-shadow: 0 4px 14px rgba(13, 148, 136, 0.25) !important;
    }}
    button[kind="primary"]:hover, .stButton > button[kind="primary"]:hover {{
        background: linear-gradient(135deg, #0F766E 0%, #115E59 100%) !important;
        color: #FFFFFF !important;
        box-shadow: 0 8px 20px rgba(13, 148, 136, 0.35) !important;
        transform: translateY(-2px);
    }}

    /* Chat input box at bottom */
    div[data-testid="stChatInput"] {{
        border-radius: 18px !important;
        box-shadow: 0 8px 24px rgba(15, 23, 42, 0.08) !important;
        border: 1px solid {border_color} !important;
        background-color: {bg_card} !important;
    }}

    /* -------------------------------------------------------------
       10. Footer & Legal Disclaimer
       ------------------------------------------------------------- */
    .travel-disclaimer {{
        text-align: center;
        font-size: 0.8rem;
        color: {text_muted};
        padding: 28px 16px 12px 16px;
        border-top: 1px solid {border_color};
        margin-top: 48px;
        line-height: 1.6;
    }}

    /* -------------------------------------------------------------
       11. Responsive Mobile Design
       ------------------------------------------------------------- */
    @media (max-width: 768px) {{
        .block-container {{
            padding-top: 1rem !important;
            padding-left: 0.8rem !important;
            padding-right: 0.8rem !important;
        }}
        .hero-overlay {{
            padding: 36px 18px 32px 18px !important;
        }}
        .hero-title {{
            font-size: 2.1rem !important;
        }}
        .hero-subtitle {{
            font-size: 0.98rem !important;
            margin-bottom: 20px !important;
        }}
        .hero-stats-row {{
            gap: 10px !important;
        }}
        .hero-stat-item {{
            font-size: 0.75rem !important;
            padding: 6px 12px !important;
        }}
        .page-header-container {{
            padding: 20px 16px !important;
        }}
        .page-header-title {{
            font-size: 1.45rem !important;
        }}
        .dest-image-wrap {{
            height: 175px !important;
        }}
        .chat-bubble-user {{
            max-width: 90% !important;
            padding: 12px 16px !important;
        }}
        .chat-bubble-ai {{
            max-width: 96% !important;
            padding: 16px 16px !important;
        }}
    }}
    </style>
    """


def render_brand_sidebar():
    """Renders elegant branding at the top of the sidebar with glowing logo icon."""
    st.sidebar.markdown(
        f"""
        <div class="brand-sidebar-box">
            <div class="brand-logo-wrap">
                <span class="brand-logo-icon">🌍</span>
            </div>
            <div class="brand-sidebar-title">{APP_NAME}</div>
            <div class="brand-sidebar-tagline">{TAGLINE}</div>
        </div>
        """,
        unsafe_allow_html=True
    )


def render_sidebar_status(model_name: str, language: str, message_count: int):
    """Renders a polished status card in the sidebar."""
    st.sidebar.markdown(
        f"""
        <div class="sidebar-status-pill">
            <div style="display: flex; align-items: center; margin-bottom: 4px;">
                <span class="sidebar-status-indicator"></span>
                <strong style="color: #10B981;">AI Engine Online</strong>
            </div>
            <div><strong>Model:</strong> <code>{model_name}</code></div>
            <div><strong>Language:</strong> {language}</div>
            <div><strong>Chat Messages:</strong> {message_count}</div>
        </div>
        """,
        unsafe_allow_html=True
    )


def render_hero_section():
    """Renders the startup-style hero banner with travel background photography and metrics."""
    st.markdown(
        f"""
        <div class="hero-banner-wrap animate-fade-in">
            <div class="hero-overlay">
                <div class="hero-pill-badge">✨ Next-Generation AI Travel Intelligence</div>
                <h1 class="hero-title">
                    Discover the World, <span class="hero-title-gradient">One Journey at a Time</span>
                </h1>
                <p class="hero-subtitle">{HERO_SUBTITLE}</p>
                <div class="hero-stats-row">
                    <div class="hero-stat-item">🌍 195+ Countries</div>
                    <div class="hero-stat-item">🏛️ 10,000+ Ancient Wonders</div>
                    <div class="hero-stat-item">📅 Instant 1–7 Day Plans</div>
                    <div class="hero-stat-item">🌐 English & தமிழ்</div>
                </div>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )


def render_page_header(icon: str, title: str, subtitle: str, badge: str = ""):
    """Renders an attractive, consistent header card for individual feature pages."""
    badge_html = f'<span style="background: #E6F4F1; color: #0D9488; font-size: 0.72rem; font-weight: 700; padding: 4px 10px; border-radius: 20px; text-transform: uppercase;">{badge}</span>' if badge else ""
    st.markdown(
        f"""
        <div class="page-header-container animate-fade-in">
            <div class="page-header-top">
                <div class="page-header-icon-box">{icon}</div>
                <div>
                    <div style="display: flex; align-items: center; gap: 10px;">
                        <h2 class="page-header-title">{title}</h2>
                        {badge_html}
                    </div>
                </div>
            </div>
            <p class="page-header-subtitle">{subtitle}</p>
        </div>
        """,
        unsafe_allow_html=True
    )


def render_destination_card(dest: dict) -> None:
    """Renders a single destination card with high-impact imagery, badge, and description."""
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
    """Renders a single feature card with refined icon box and typography."""
    st.markdown(
        f"""
        <div class="feature-card">
            <div class="feature-icon-wrap">{feat['icon']}</div>
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
            <span style="opacity: 0.85; margin-top: 8px; display: inline-block;">
                © 2026 {APP_NAME}. Powered by Google Gemini AI. Built with precision for world explorers.
            </span>
        </div>
        """,
        unsafe_allow_html=True
    )
