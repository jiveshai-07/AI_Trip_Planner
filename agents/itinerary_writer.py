from utils.gemini_client import generate_json


def write_itinerary(
    destination,
    duration_days,
    num_travelers,
    trip_style,
    research_data,
    budget_data,
    revision_notes=None
):
    """
    Agent 3: Itinerary Writer
    Compiles a day-by-day itinerary using Researcher + Budget outputs.
    Also generates a packing list. If revision_notes is provided, this
    is a re-run based on Reviewer feedback.
    Returns a structured dict.
    """

    

    attractions = research_data.get("top_attractions", [])
    attractions_text = "\n".join(
        [f"- {a['name']} ({a['category']}): {a['description']}" for a in attractions]
    )

    accommodation = budget_data.get("accommodation_suggestions", [])
    accommodation_text = "\n".join(
        [f"- {a['name']}: {a['price_range_per_night']}" for a in accommodation]
    )

    daily_budget = budget_data.get("daily_budget_breakdown", {})

    revision_context = ""
    if revision_notes:
        revision_context = f"""
IMPORTANT: This is a REVISION of a previous itinerary. A reviewer flagged
the following issue that you MUST fix in this new version:
"{revision_notes}"
"""

    prompt = f"""
You are a professional travel itinerary writer agent, part of a multi-agent
trip planning system. Your job is to compile a realistic day-by-day itinerary
using the research and budget information already gathered by other agents.
You also generate a packing list. Do not redo research or budget analysis,
just use what is given below.
{revision_context}
Destination: {destination}
Duration: {duration_days} days
Number of travelers: {num_travelers}
Trip style/interests: {trip_style}

Available attractions to use (do not invent new ones, select and sequence from this list):
{attractions_text}

Accommodation options already suggested:
{accommodation_text}

Daily budget breakdown already calculated: {daily_budget}

Return ONLY valid JSON (no markdown, no commentary) in exactly this structure:

{{
  "trip_title": "a catchy short title for this trip",
  "daily_plan": [
    {{
      "day": 1,
      "theme": "short theme for the day e.g. 'Historic Temples & Culture'",
      "morning": "activity description",
      "afternoon": "activity description",
      "evening": "activity description",
      "estimated_walking_or_travel_notes": "brief realistic note on pacing/logistics"
    }}
  ],
  "packing_list": {{
    "clothing": ["item 1", "item 2"],
    "documents": ["item 1", "item 2"],
    "electronics": ["item 1", "item 2"],
    "health_and_toiletries": ["item 1", "item 2"],
    "destination_specific": ["item relevant to this destination/climate/culture"]
  }}
}}

Create exactly {duration_days} entries in daily_plan, one per day, using
realistic pacing (don't cram too much in one day). Distribute the attractions
list logically across the days based on geography/theme where possible.
"""

    try:
        result = generate_json(prompt)

        if result is None:
            return {"error": "Could not parse itinerary writer response."}

        return result

    except Exception as e:
        return {"error": f"Itinerary writer agent failed: {e}"}