from utils.gemini_client import generate_json


def review_itinerary(
    destination,
    duration_days,
    budget_data,
    itinerary_data
):
    """
    Agent 4: Reviewer
    Checks the itinerary for realism/budget issues and provides
    personalized travel tips. Can flag issues for revision.
    Returns a structured dict.
    """

    

    daily_plan_text = ""
    for day in itinerary_data.get("daily_plan", []):
        daily_plan_text += f"Day {day['day']} ({day['theme']}): Morning: {day['morning']} | Afternoon: {day['afternoon']} | Evening: {day['evening']}\n"

    total_cost = budget_data.get("total_estimated_cost", "unknown")

    prompt = f"""
You are a professional travel plan reviewer agent, part of a multi-agent
trip planning system. Your job is to critically review the itinerary
already created by another agent, check for realism issues (overpacked
days, illogical geography/sequencing, unrealistic pacing), verify it
roughly aligns with the stated budget, and provide final personalized
travel tips. You do NOT rewrite the itinerary yourself.

Destination: {destination}
Duration: {duration_days} days
Total estimated budget: {total_cost}

Itinerary to review:
{daily_plan_text}

Return ONLY valid JSON (no markdown, no commentary) in exactly this structure:

{{
  "needs_revision": true or false,
  "revision_notes": "if needs_revision is true, explain specifically what should change (e.g. 'Day 3 has too many activities packed in, spread across Day 3 and 4'). If false, leave as empty string.",
  "realism_check": "1-2 sentence assessment of whether the pacing/sequencing is realistic",
  "budget_alignment_check": "1-2 sentence assessment of whether the plan seems to fit within the stated budget",
  "personalized_travel_tips": ["tip 1", "tip 2", "tip 3", "tip 4"],
  "overall_verdict": "1 short sentence final verdict, e.g. 'A well-paced, realistic itinerary ready to go.'"
}}

Be genuinely critical, not just approving — if there's a real pacing or
logistics issue, flag it with needs_revision true.
"""

    try:
        result = generate_json(prompt)
        

        if result is None:
            return {"error": "Could not parse reviewer response."}

        return result

    except Exception as e:
        return {"error": f"Reviewer agent failed: {e}"}