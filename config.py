"""
Configuration settings for Travel Discovery AI.
Keeps models, branding, destinations, and UI parameters centralized and configurable.
"""

# Branding & Metadata
APP_NAME = "TRAVEL DISCOVERY AI"
TAGLINE = "Discover Places. Explore Cultures. Experience the World."
HERO_TITLE = "Discover the World, One Journey at a Time."
HERO_SUBTITLE = "Explore extraordinary destinations, uncover ancient wonders and plan your next unforgettable adventure with AI."

# Gemini Model Settings
DEFAULT_MODEL = "gemini-3.5-flash-lite"
SUPPORTED_MODELS = [
    "gemini-3.5-flash-lite",
    "gemini-3.8-flash",
    "gemini-2.5-flash",
    "gemini-1.5-flash",
]

GENERATION_CONFIG = {
    "temperature": 0.7,
    "top_p": 0.95,
    "top_k": 40,
    "max_output_tokens": 2048,
}

# Navigation Pages
PAGES = {
    "HOME": "🏠 Home",
    "DISCOVER": "🌍 Discover Destinations",
    "ANCIENT": "🏛️ Ancient Places",
    "HIDDEN_GEMS": "💎 Hidden Gems",
    "TRIP_PLANNER": "📅 Smart Trip Planner",
    "FOOD_EXPLORER": "🍲 Food Explorer",
    "CHAT": "💬 Travel Chat",
    "SETTINGS": "⚙️ Settings",
}

# Suggested Questions for Homepage and Chat
SUGGESTED_QUESTIONS = [
    "Discover ancient places in India.",
    "Find hidden gems in Japan.",
    "Plan a 3-day trip to Kerala.",
    "Explore famous foods in Italy.",
    "Suggest peaceful mountain destinations.",
    "Plan a budget-friendly trip.",
]

# Follow-up Quick Prompts
FOLLOW_UP_SUGGESTIONS = [
    "What is the best time of year to visit?",
    "Can you provide a realistic budget breakdown?",
    "What are the top 3 authentic local dishes to try?",
    "Are there any lesser-known hidden spots nearby?",
    "What are important cultural etiquette tips here?",
]

# Curated Destination Showcase for Landing Page
POPULAR_DESTINATIONS = [
    {
        "title": "Kyoto, Japan",
        "tag": "Ancient Culture & Zen",
        "desc": "Thousands of classical Buddhist temples, gardens, imperial palaces, and traditional wooden machiya houses.",
        "image": "https://images.unsplash.com/photo-1493976040374-85c8e12f0c0e?auto=format&fit=crop&w=800&q=80",
        "prompt": "Tell me about Kyoto, Japan: must-see temples, hidden Zen gardens, cultural etiquette, and top local matcha treats."
    },
    {
        "title": "Rome, Italy",
        "tag": "Living History & Food",
        "desc": "The Eternal City blends nearly three millennia of globally influential art, architecture, and world-class cuisine.",
        "image": "https://images.unsplash.com/photo-1552832230-c0197dd311b5?auto=format&fit=crop&w=800&q=80",
        "prompt": "Explore Rome, Italy: iconic ancient monuments like the Colosseum, secret piazzas, and authentic Roman pasta dishes."
    },
    {
        "title": "Rajasthan, India",
        "tag": "Royal Heritage & Forts",
        "desc": "Land of Maharajas featuring colossal hill forts, ornate desert palaces, vibrant bazaars, and rich folklore.",
        "image": "https://images.unsplash.com/photo-1599661046289-e31897846e41?auto=format&fit=crop&w=800&q=80",
        "prompt": "Discover Rajasthan, India: magnificent forts in Jaipur, Jodhpur, and Udaipur, royal history, and traditional Rajasthani thali."
    },
    {
        "title": "Machu Picchu, Peru",
        "tag": "Archaeological Wonder",
        "desc": "Mist-shrouded 15th-century Incan citadel perched high in the Andes mountains above the Urubamba River valley.",
        "image": "https://images.unsplash.com/photo-1526392060635-9d6019884377?auto=format&fit=crop&w=800&q=80",
        "prompt": "Guide me through visiting Machu Picchu: historical significance, Incan engineering, hiking routes, and acclimatization tips."
    },
    {
        "title": "Santorini, Greece",
        "tag": "Aegean Coast & Architecture",
        "desc": "Iconic whitewashed cubic houses and blue-domed chapels clinging to soaring volcanic cliffs above turquoise waters.",
        "image": "https://images.unsplash.com/photo-1570077188670-e3a8d69ac5ff?auto=format&fit=crop&w=800&q=80",
        "prompt": "Tell me the best of Santorini: quieter villages beyond Oia, volcanic beaches, Aegean seafood, and panoramic sunset spots."
    },
    {
        "title": "Kerala, India",
        "tag": "Tropical Backwaters & Nature",
        "desc": "God's Own Country: tranquil palm-fringed backwaters, spice plantations, misty Munnar hills, and Ayurvedic wellness.",
        "image": "https://images.unsplash.com/photo-1602216056096-3b40cc0c9944?auto=format&fit=crop&w=800&q=80",
        "prompt": "Plan a serene getaway to Kerala, India: backwater houseboats in Alleppey, spice gardens, Kathakali, and coastal delicacies."
    }
]

# Feature cards on homepage
FEATURE_CARDS = [
    {
        "icon": "🌍",
        "title": "Destination Discovery",
        "desc": "Uncover top sights, cultural context, best seasons, and tailored advice for cities and countries across all 7 continents."
    },
    {
        "icon": "🏛️",
        "title": "Ancient Places & UNESCO",
        "desc": "Deep dives into ancient temples, medieval fortresses, archaeological excavations, and civilizational wonders."
    },
    {
        "icon": "💎",
        "title": "Untouched Hidden Gems",
        "desc": "Escape tourist traps with hand-curated secret viewpoints, quaint heritage villages, and serene nature sanctuaries."
    },
    {
        "icon": "📅",
        "title": "Day-by-Day Itineraries",
        "desc": "Custom 1-to-7 day schedules organized by morning, afternoon, and evening with transit and pacing logic."
    },
    {
        "icon": "🍲",
        "title": "Authentic Cuisine Explorer",
        "desc": "Savor authentic regional flavors, legendary street foods, market stalls, and cultural dining customs."
    },
    {
        "icon": "💰",
        "title": "Smart Budget Planning",
        "desc": "Clear itemized estimates for stays, dining, transport, and tickets across backpacker, moderate, and luxury styles."
    }
]

# Supported Languages
LANGUAGES = {
    "English": "English",
    "Tamil (தமிழ்)": "Tamil"
}

# Verification & Disclaimer Notice
LEGAL_DISCLAIMER = (
    "Travel Discovery AI provides inspirational guides and estimated budgets. "
    "Ticket prices, opening hours, visa rules, and safety advisories fluctuate. "
    "Always confirm real-time specifics with official consulates, operators, and heritage boards before travel."
)
