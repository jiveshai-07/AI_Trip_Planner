from utils.gemini_client import generate_json


def research_destination(
    destination,
    trip_style,
    duration_days,
    num_travelers,
    travel_style_hint=None
):
    """
    Agent 1: Researcher
    Finds attractions, safety tips, and visa info for a destination.
    Returns a structured dict.
    """

    

    style_context = ""
    if travel_style_hint:
        style_context = f"\nThe traveler's visual preference style detected from an inspiration photo is: {travel_style_hint}. Factor this into your attraction recommendations."

    prompt = f"""
You are a professional travel researcher agent, part of a multi-agent trip
planning system. Your ONLY job is research — do not create a day-by-day
itinerary or discuss budget, that is handled by other agents.

Destination: {destination}
Trip style/interests: {trip_style}
Duration: {duration_days} days
Number of travelers: {num_travelers}
{style_context}

Return ONLY valid JSON (no markdown, no commentary) in exactly this structure:

{{
  "destination_overview": "2-3 sentence overview of the destination",
  "top_attractions": [
    {{"name": "attraction name", "description": "1 sentence why it's worth visiting", "category": "e.g. historic, nature, food, adventure"}}
  ],
  "local_safety_tips": ["tip 1", "tip 2", "tip 3"],
  "visa_information": "brief visa/entry requirement guidance for typical travelers (note: general guidance, not legal advice)",
  "best_time_to_visit": "short answer",
  "local_customs": ["custom or etiquette tip 1", "tip 2"]
}}

Include 6-10 top_attractions. Be specific and realistic, not generic.
"""

    try:
        result = generate_json(prompt)
        

        if result is None:
            return {"error": "Could not parse researcher response."}

        return result

    except Exception as e:
        return {"error": f"Researcher agent failed: {e}"}