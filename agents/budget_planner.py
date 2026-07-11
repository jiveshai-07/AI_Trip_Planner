from utils.gemini_client import generate_json


def plan_budget(
    destination,
    duration_days,
    num_travelers,
    budget_level,
    attractions_list=None
):
    """
    Agent 2: Budget Planner
    Estimates costs and suggests accommodation based on trip details.
    Returns a structured dict.
    """

    

    attractions_context = ""
    if attractions_list:
        names = ", ".join([a.get("name", "") for a in attractions_list])
        attractions_context = f"\nThe traveler plans to visit these attractions: {names}. Factor entry fees/costs where relevant."

    prompt = f"""
You are a professional travel budget planner agent, part of a multi-agent
trip planning system. Your ONLY job is cost estimation and accommodation
suggestions — do not create a day-by-day itinerary, that is handled by
another agent.

Destination: {destination}
Duration: {duration_days} days
Number of travelers: {num_travelers}
Budget level: {budget_level} (e.g. budget, mid-range, luxury)
{attractions_context}
Provide all cost estimates in Indian Rupees (INR, ₹), since the traveler is based in India — even if the destination uses a different local currency, convert everything to INR.

Return ONLY valid JSON (no markdown, no commentary) in exactly this structure:

{{
  "currency_note": "All estimates are in Indian Rupees (INR)",
  "accommodation_suggestions": [
    {{"name": "type or example of accommodation", "price_range_per_night": "e.g. $80-120", "why": "1 sentence reason it fits"}}
  ],
  "daily_budget_breakdown": {{
    "accommodation": "estimated per night cost",
    "food": "estimated per day cost",
    "local_transport": "estimated per day cost",
    "activities_attractions": "estimated per day cost"
  }},
  "total_estimated_cost": "total cost estimate for the full trip for all travelers combined",
  "money_saving_tips": ["tip 1", "tip 2", "tip 3"]
}}

Provide 3 accommodation_suggestions ranging appropriately within the
budget_level given. Be realistic and specific to the destination, not generic.
"""

    try:
        result = generate_json(prompt)
        

        if result is None:
            return {"error": "Could not parse budget planner response."}

        return result

    except Exception as e:
        return {"error": f"Budget planner agent failed: {e}"}