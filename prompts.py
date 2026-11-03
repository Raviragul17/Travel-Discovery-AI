"""
System prompts and structured templates for Travel Discovery AI.
Implements the travel consultant persona, specialized prompts, and bilingual instructions.
"""

SYSTEM_INSTRUCTION = """You are "Travel Discovery AI", an elite, world-class international travel consultant and cultural heritage specialist.
Your tagline is: "Discover Places. Explore Cultures. Experience the World."

CORE GUIDELINES:
1. Tone & Style: Warm, knowledgeable, inspiring, and professional. You speak with genuine passion for world destinations, ancient history, authentic cultures, and local traditions.
2. Structure & Readability:
   - Use crisp Markdown headings (###), bullet points, and bold text for landmarks and tips.
   - Avoid monolithic walls of text; keep paragraphs concise (2-4 sentences max per section).
   - Use tasteful travel emojis (🏛️, 🌿, 🍲, 🚆, 💡) to make reading pleasant.
3. Factual Integrity & Accuracy:
   - Provide accurate historical context, cultural etiquette, geographic facts, and best visiting seasons.
   - NEVER invent live ticket prices, exact real-time opening hours, availability, or fake addresses.
   - Explicitly clarify that costs and timings are AI-generated approximations and advise users to verify before departure.
4. Language Support:
   - Fluent in both English and Tamil (தமிழ்).
   - If the user writes in Tamil or selects Tamil language, respond warmly and eloquently in Tamil.
   - When introducing local terms or dishes, provide the local name alongside an explanation.
5. Conversational Continuity:
   - You remember previous turns in the ongoing conversation.
   - If the user asks a follow-up (e.g. "Which is the oldest?" after discussing temples in Tamil Nadu), resolve it seamlessly using the earlier context.
6. Proactive Engagement:
   - At the conclusion of helpful recommendations, offer 2-3 natural follow-up questions or next steps (e.g., local dining, day-trip additions, transit options).
"""

def build_destination_prompt(destination: str, duration: str = "", traveler_type: str = "Solo / Couple", language: str = "English") -> str:
    """Prompt template for general destination discovery."""
    lang_clause = "Respond entirely in Tamil." if "Tamil" in language else "Respond in English."
    return f"""Destination Discovery Request:
Destination: {destination}
Trip Length: {duration if duration else 'General exploration'}
Traveler Style: {traveler_type}

Please provide:
1. Overview & Cultural Essence (Why this place is special)
2. Top 4-5 Must-Visit Attractions & Sights (with brief highlights)
3. Best Time of Year & Seasonality
4. Recommended Experiences & Activities
5. Local Etiquette & Visiting Tips (transit, safety, customs)

{lang_clause}
Remember to keep prices/timings as estimates with a verification reminder.
"""

def build_ancient_places_prompt(region_or_country: str, era_or_type: str = "All Eras", language: str = "English") -> str:
    """Prompt template for ancient monuments, temples, forts, archaeological sites."""
    lang_clause = "Respond entirely in Tamil." if "Tamil" in language else "Respond in English."
    return f"""Ancient Places & Archaeological Explorer Request:
Region / Country: {region_or_country}
Historical Category: {era_or_type}

Please provide an in-depth yet accessible historical guide:
1. Historical Background & Civilizational Significance
2. 4-6 Ancient Wonders / Temples / Forts / UNESCO Heritage Sites (include estimated construction centuries/dynasties)
3. Architectural Marvels & Engineering Feats
4. Cultural & Mythological or Folkloric Context
5. Heritage Visiting Tips (dress codes, respectful behavior, best photography light)

{lang_clause}
Maintain historical rigor. Remind travelers to respect sacred and archaeological grounds.
"""

def build_hidden_gems_prompt(destination: str, vibe: str = "Peaceful Nature", language: str = "English") -> str:
    """Prompt template for lesser-known, off-the-beaten-path destinations."""
    lang_clause = "Respond entirely in Tamil." if "Tamil" in language else "Respond in English."
    return f"""Hidden Gems & Off-the-Beaten-Path Discovery Request:
Destination / Region: {destination}
Desired Vibe: {vibe} (e.g. peaceful village, secluded nature, tranquil mountains, artisan culture)

Please provide:
1. Introduction to the Region's Lesser-Known Side
2. 4-5 Underrated / Secret Destinations & Spots
3. What makes each spot authentic, quiet, and special
4. How to reach these locations respectfully without disrupting local communities
5. What unique cultural interaction or nature experience to seek out

{lang_clause}
Emphasize sustainable, responsible travel.
"""

def build_trip_planner_prompt(
    destination: str,
    days: int,
    budget_level: str,
    interests: list,
    traveler_party: str = "Couple",
    language: str = "English"
) -> str:
    """Prompt template for structured 1-7 day itineraries."""
    interests_str = ", ".join(interests) if interests else "Culture, Nature, Food"
    lang_clause = "Respond entirely in Tamil." if "Tamil" in language else "Respond in English."
    return f"""Smart Day-by-Day Trip Itinerary Request:
Destination: {destination}
Duration: {days} Days (Detailed Day-by-Day Breakdown)
Budget Tier: {budget_level} (e.g. Backpacker / Moderate / Premium)
Interests: {interests_str}
Travelers: {traveler_party}

Format requirements:
- For EACH day (Day 1 through Day {days}), organize chronologically:
  * 🌅 Morning (attraction, walk, breakfast idea)
  * ☀️ Afternoon (cultural site, scenic stop, authentic lunch)
  * 🌙 Evening (sunset point, local market, dinner & nightlife/ambiance)
- Include Transit & Navigation Tips between stops (metro, walking, local taxis)
- Highlight 1-2 Local Culinary Recommendations per day
- Conclude with a helpful summary of packing tips and pacing advice.

{lang_clause}
Keep pacing realistic (avoid overwhelming itineraries).
"""

def build_food_explorer_prompt(destination: str, diet_pref: str = "All (Omnivore)", language: str = "English") -> str:
    """Prompt template for authentic local culinary exploration."""
    lang_clause = "Respond entirely in Tamil." if "Tamil" in language else "Respond in English."
    return f"""Culinary & Food Explorer Request:
Destination / Region: {destination}
Dietary Preference: {diet_pref} (e.g. Vegetarian, Non-Vegetarian, Vegan, Halal, Street Food)

Please provide:
1. Regional Culinary Identity & Signature Flavors (key spices, ingredients, history)
2. 5 Iconic Dishes Everyone Must Try (names, what they are, how they are eaten)
3. Must-Try Street Food & Iconic Local Snacks
4. Traditional Dining Etiquette & Ordering Customs
5. Famous Food Neighborhoods or Historic Markets to Explore

{lang_clause}
Make the culinary descriptions mouth-watering and culturally grounded.
"""

def build_budget_planner_prompt(
    destination: str,
    days: int,
    traveler_count: int,
    currency: str = "USD",
    travel_style: str = "Mid-Range / Comfort",
    language: str = "English"
) -> str:
    """Prompt template for comprehensive budget estimation."""
    lang_clause = "Respond entirely in Tamil." if "Tamil" in language else "Respond in English."
    return f"""Budget Travel Planner Request:
Destination: {destination}
Trip Duration: {days} Days
Number of Travelers: {traveler_count}
Preferred Currency: {currency}
Travel Style: {travel_style} (Backpacker / Budget, Mid-range / Comfort, Luxury / Splurge)

Please provide an itemized expense breakdown in {currency}:
1. Accommodation Estimates (Daily & Total range)
2. Food & Dining Estimates (Street food to casual sit-down)
3. Local Transportation (Public transit, metros, taxis, intercity trains)
4. Sightseeing, Heritage Entry Tickets & Activities
5. Contingency / Miscellaneous Buffer (10-15%)
6. Grand Total Estimated Budget (formatted with a low-to-high realistic range)
7. Money-Saving Insider Tips for this destination

{lang_clause}
IMPORTANT: Add a clear disclaimer that all figures are estimated ranges based on historical travel data and subject to seasonal fluctuations, currency rates, and personal spending habits.
"""
