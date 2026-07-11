from agents.researcher import research_destination
from agents.budget_planner import plan_budget
from agents.itinerary_writer import write_itinerary
from agents.reviewer import review_itinerary


def plan_trip(
    destination,
    trip_style,
    duration_days,
    num_travelers,
    budget_level,
    travel_style_hint=None,
    progress_callback=None,
    max_revisions=1
):
    """
    Runs all four AI agents sequentially with a reviewer-driven
    self-correction loop.
    """

    log = []

    def notify(step):
        log.append(step)

        if progress_callback:
            progress_callback(step)

    # ==================================================
    # STEP 1 - RESEARCHER
    # ==================================================

    notify("🔍 Researcher Agent")

    research_result = research_destination(
        destination,
        trip_style,
        duration_days,
        num_travelers,
        travel_style_hint
    )

    if "error" in research_result:
        return {
            "error": research_result["error"],
            "step_failed": "researcher",
            "log": log
        }

    # ==================================================
    # STEP 2 - BUDGET
    # ==================================================

    notify("💰 Budget Agent")

    attractions = research_result.get(
        "top_attractions",
        []
    )

    budget_result = plan_budget(
        destination,
        duration_days,
        num_travelers,
        budget_level,
        attractions
    )

    if "error" in budget_result:
        return {
            "error": budget_result["error"],
            "step_failed": "budget",
            "log": log
        }

    # ==================================================
    # STEP 3 - ITINERARY
    # ==================================================

    notify("📅 Itinerary Agent")

    itinerary_result = write_itinerary(
        destination,
        duration_days,
        num_travelers,
        trip_style,
        research_result,
        budget_result
    )

    if "error" in itinerary_result:
        return {
            "error": itinerary_result["error"],
            "step_failed": "itinerary",
            "log": log
        }

    # ==================================================
    # STEP 4 - REVIEWER
    # ==================================================

    revision_count = 0

    while revision_count <= max_revisions:

        notify("🧐 Reviewer Agent")

        review_result = review_itinerary(
            destination,
            duration_days,
            budget_result,
            itinerary_result
        )

        if "error" in review_result:

            return {
                "error": review_result["error"],
                "step_failed": "reviewer",
                "log": log
            }

        if (
            not review_result.get("needs_revision")
            or revision_count >= max_revisions
        ):
            break

        notify("🔁 Revising")

        itinerary_result = write_itinerary(
            destination,
            duration_days,
            num_travelers,
            trip_style,
            research_result,
            budget_result,
            revision_notes=review_result.get(
                "revision_notes"
            )
        )

        if "error" in itinerary_result:

            return {
                "error": itinerary_result["error"],
                "step_failed": "itinerary_revision",
                "log": log
            }

        revision_count += 1

    # ==================================================
    # COMPLETE
    # ==================================================

    notify("✅ Complete")

    return {
        "research": research_result,
        "budget": budget_result,
        "itinerary": itinerary_result,
        "review": review_result,
        "revision_count": revision_count,
        "log": log
    }