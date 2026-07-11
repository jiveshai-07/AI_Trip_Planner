import urllib.parse
import streamlit as st
from streamlit_folium import st_folium

from components.auth import check_login
from components.ui import load_ui, footer
from components.navbar import navbar

from utils.orchestrator import plan_trip
from utils.image_classifier import detect_travel_style
from utils.trip_storage import save_trip
from utils.pdf_generator import generate_trip_pdf
from utils.map_generator import generate_destination_map
from utils.weather import get_weather
from utils.currency_converter import convert_currency

check_login()
load_ui()
navbar()

st.title("🧭 Plan a Trip")

st.write(
    "Fill in your trip details and let four AI agents collaborate to create your personalized travel itinerary."
)

# ==================================================
# USER INPUTS
# ==================================================

destination = st.text_input(
    "Destination",
    placeholder="e.g. Kyoto, Japan"
)

trip_style = st.text_input(
    "Trip Style / Interests",
    placeholder="Adventure, Culture, Nature, Food..."
)

st.markdown("### 📸 Travel Style Detection (Optional)")

st.caption(
    "Upload an inspiration photo and AI will detect your preferred travel style."
)

inspiration_photo = st.file_uploader(
    "Upload Image",
    type=["jpg", "jpeg", "png"]
)

travel_style_hint = None

st.markdown("---")

col1, col2, col3 = st.columns(3)

with col1:
    duration_days = st.number_input(
        "Duration (Days)",
        min_value=1,
        max_value=30,
        value=5
    )

with col2:
    num_travelers = st.number_input(
        "Travelers",
        min_value=1,
        max_value=20,
        value=2
    )

with col3:
    budget_level = st.selectbox(
        "Budget",
        [
            "Budget",
            "Mid-range",
            "Luxury"
        ]
    )

generate_clicked = st.button(
    "🚀 Generate Trip Plan",
    use_container_width=True
)

# ==================================================
# IMAGE ANALYSIS
# ==================================================

if generate_clicked and inspiration_photo:

    col_img, col_result = st.columns([1, 2])

    with col_img:
        st.image(inspiration_photo, width=220)

    with col_result:

        with st.spinner("Analyzing travel style..."):

            style_label, confidence = detect_travel_style(
                inspiration_photo
            )

        if style_label:

            travel_style_hint = style_label

            st.success(
                f"Detected Travel Style: **{style_label}** ({confidence}% confidence)"
            )

        else:

            st.warning(confidence)

# ==================================================
# GENERATE TRIP
# ==================================================

if generate_clicked:

    if destination.strip() == "":
        st.warning("Please enter a destination.")
        st.stop()

    progress_text = st.empty()

    progress = st.progress(0, text="🚀 Starting AI agents...")

    agent_progress = {
        "research": 25,
        "budget": 50,
        "itinerary": 75,
        "review": 90,
        "revis": 95,
        "complete": 100,
    }

    def show_progress(step):

        step_lower = step.lower()

        percent = 10

        if "research" in step_lower:
            percent = agent_progress["research"]

        elif "budget" in step_lower:
            percent = agent_progress["budget"]

        elif "itinerary" in step_lower:
            percent = agent_progress["itinerary"]

        elif "review" in step_lower:
            percent = agent_progress["review"]

        elif "revis" in step_lower:
            percent = agent_progress["revis"]

        elif "complete" in step_lower:
            percent = agent_progress["complete"]

        progress.progress(
            percent,
            text=f"🤖 AI Agents Working... {percent}%"
        )

        progress_text.info(step)

    with st.spinner("Generating your trip..."):

        result = plan_trip(
            destination=destination,
            trip_style=trip_style,
            duration_days=duration_days,
            num_travelers=num_travelers,
            budget_level=budget_level,
            travel_style_hint=travel_style_hint,
            progress_callback=show_progress,
        )

    progress.progress(
        100,
        text="✅ Trip Completed (100%)"
    )

    progress_text.empty()

    if "error" in result:

        st.error(
            f"Error during {result.get('step_failed','unknown')} step.\n\n{result['error']}"
        )

        st.stop()

    st.session_state.last_trip_result = result

    st.session_state.last_trip_inputs = {
        "destination": destination,
        "trip_style": trip_style,
        "duration_days": duration_days,
        "num_travelers": num_travelers,
        "budget_level": budget_level,
    }

# ==================================================
# DISPLAY RESULTS
# ==================================================

if "last_trip_result" in st.session_state:

    result = st.session_state.last_trip_result
    inputs = st.session_state.last_trip_inputs

    research = result["research"]
    budget = result["budget"]
    itinerary = result["itinerary"]
    review = result["review"]
    # ==================================================
    # SUCCESS MESSAGE
    # ==================================================

    if result["revision_count"] > 0:

        st.success(
            f"✅ Reviewer improved the itinerary {result['revision_count']} time(s)."
        )

    else:

        st.success(
            "✅ Trip passed AI review on the first attempt."
        )

    # ==================================================
    # OVERVIEW
    # ==================================================

    st.markdown(
        f"# 🗺️ {itinerary.get('trip_title', inputs['destination'])}"
    )

    st.write(
        research.get(
            "destination_overview",
            ""
        )
    )

    st.markdown("---")

    # ==================================================
    # DAY BY DAY ITINERARY
    # ==================================================

    st.markdown("## 📅 Day-by-Day Itinerary")

    for day in itinerary.get("daily_plan", []):

        with st.expander(
            f"📍 Day {day['day']} — {day['theme']}"
        ):

            st.write(
                f"🌅 **Morning:** {day['morning']}"
            )

            st.write(
                f"☀️ **Afternoon:** {day['afternoon']}"
            )

            st.write(
                f"🌙 **Evening:** {day['evening']}"
            )

            notes = day.get(
                "estimated_walking_or_travel_notes",
                ""
            )

            if notes:
                st.caption(notes)

    st.markdown("---")

    # ==================================================
    # BUDGET SUMMARY
    # ==================================================

    st.markdown("## 💰 Budget Summary")

    currency_note = budget.get(
        "currency_note",
        ""
    )

    if currency_note:
        st.caption(currency_note)

    for hotel in budget.get(
        "accommodation_suggestions",
        []
    ):

        st.markdown(
            f"""
### 🏨 {hotel['name']}

**Price:** {hotel['price_range_per_night']}

{hotel['why']}
"""
        )

    st.success(
        f"Estimated Total Cost: **{budget.get('total_estimated_cost','')}**"
    )

    st.markdown("---")

    # ==================================================
    # WEATHER
    # ==================================================

    st.markdown("## 🌤️ Current Weather")

    weather = get_weather(
        inputs["destination"]
    )

    if weather:

        c1, c2, c3, c4 = st.columns(4)

        with c1:
            st.metric(
                "🌡 Temperature",
                f"{weather['temperature']}°C"
            )

        with c2:
            st.metric(
                "☁️ Condition",
                weather["condition"]
            )

        with c3:
            st.metric(
                "💧 Humidity",
                f"{weather['humidity']}%"
            )

        with c4:
            st.metric(
                "🌬 Wind",
                f"{weather['wind']} m/s"
            )

        st.info(weather["description"])

    else:

        st.info(
            "Weather information unavailable."
        )

    st.markdown("---")

    # ==================================================
    # CURRENCY CONVERTER
    # ==================================================

    st.markdown("## 💱 Estimated Cost in Local Currency")

    currency_codes = {

        "Japan": "JPY",
        "France": "EUR",
        "Germany": "EUR",
        "Italy": "EUR",
        "Spain": "EUR",
        "United Kingdom": "GBP",
        "United States": "USD",
        "India": "INR",
        "Thailand": "THB",
        "Singapore": "SGD",
        "Australia": "AUD",
        "Canada": "CAD",

    }

    country = inputs["destination"].split(",")[-1].strip()

    currency = currency_codes.get(country)

    if currency:

        total_cost = budget.get(
            "total_estimated_cost",
            ""
        )

        numbers = "".join(
            c for c in total_cost
            if c.isdigit()
        )

        if numbers:

            converted = convert_currency(
                float(numbers),
                currency
            )

            if converted:

                st.success(
                    f"Approximate Cost: **{converted} {currency}**"
                )

    st.markdown("---")
    # ==================================================
    # FLIGHT SEARCH
    # ==================================================

    st.markdown("## ✈️ Book Your Flights")

    destination_encoded = urllib.parse.quote(
        inputs["destination"]
    )

    google_flights = (
        f"https://www.google.com/travel/flights?q={destination_encoded}"
    )

    # Use homepage because destination URLs frequently break
    skyscanner = (
        "https://www.skyscanner.com/flights"
    )

    col1, col2 = st.columns(2)

    with col1:

        st.link_button(
            "🔍 Search on Google Flights",
            google_flights,
            use_container_width=True
        )

    with col2:

        st.link_button(
            "🌍 Search on Skyscanner",
            skyscanner,
            use_container_width=True
        )

    st.markdown("---")

    # ==================================================
    # PACKING LIST
    # ==================================================

    st.markdown("## 🎒 Packing Checklist")

    packing = itinerary.get(
        "packing_list",
        {}
    )

    if packing:

        for category, items in packing.items():

            st.markdown(
                f"### {category.replace('_',' ').title()}"
            )

            for item in items:

                st.checkbox(
                    item,
                    key=f"{category}_{item}",
                    value=False
                )

    st.markdown("---")

    # ==================================================
    # SAFETY TIPS
    # ==================================================

    st.markdown("## 🛡️ Safety Tips")

    for tip in research.get(
        "local_safety_tips",
        []
    ):

        st.write(f"• {tip}")

    st.markdown("---")

    # ==================================================
    # VISA INFORMATION
    # ==================================================

    st.markdown("## 📄 Visa Information")

    st.info(

        research.get(

            "visa_information",

            "Visa information unavailable."

        )

    )

    st.markdown("---")

    # ==================================================
    # PERSONALIZED AI TIPS
    # ==================================================

    st.markdown("## 💡 Personalized Travel Tips")

    for tip in review.get(

        "personalized_travel_tips",

        []

    ):

        st.write(f"• {tip}")

    st.success(

        review.get(

            "overall_verdict",

            ""

        )

    )

    st.markdown("---")
    # ==================================================
    # INTERACTIVE MAP
    # ==================================================

    st.markdown("## 🗺️ Explore the Destination")

    trip_map = generate_destination_map(
        inputs["destination"],
        research.get("top_attractions", [])
    )

    if trip_map:

        st_folium(
            trip_map,
            width=None,
            height=500,
            use_container_width=True
        )

    else:

        st.info(
            "Map unavailable for this destination."
        )

    st.markdown("---")

    # ==================================================
    # SAVE + DOWNLOAD
    # ==================================================

    col_save, col_pdf = st.columns(2)

    with col_save:

        if st.button(
            "💾 Save This Trip",
            use_container_width=True
        ):

            try:

                save_trip(
                    st.session_state.username,
                    inputs,
                    result
                )

                st.success(
                    "✅ Trip saved successfully!"
                )

            except Exception as e:

                st.error(
                    f"Unable to save trip:\n\n{e}"
                )

    with col_pdf:

        pdf_bytes = generate_trip_pdf(
            inputs["destination"],
            result
        )

        st.download_button(
            label="📄 Download PDF Itinerary",
            data=pdf_bytes,
            file_name=f"{inputs['destination'].replace(' ','_')}_itinerary.pdf",
            mime="application/pdf",
            use_container_width=True
        )

footer()