import streamlit as st
from components.auth import check_login
from components.ui import load_ui, footer
from components.navbar import navbar
from utils.trip_storage import get_user_trips, delete_trip
from utils.pdf_generator import generate_trip_pdf

check_login()
load_ui()
navbar()

st.title("🕓 Trip History")

trips = get_user_trips(st.session_state.username)

if not trips:
    st.info("You haven't saved any trips yet. Generate and save a trip on the Plan Trip page.")
else:
    for i, trip in enumerate(reversed(trips)):
        actual_index = len(trips) - 1 - i
        result = trip["result"]
        inputs = trip["inputs"]

        with st.expander(f"🗺️ {result['itinerary'].get('trip_title', inputs['destination'])} — saved {trip['saved_at']}"):
            st.write(f"**Destination:** {inputs['destination']}")
            st.write(f"**Duration:** {inputs['duration_days']} days")
            st.write(f"**Total Cost:** {result['budget'].get('total_estimated_cost', '')}")

            for day in result["itinerary"].get("daily_plan", []):
                st.write(f"**Day {day['day']}:** {day['theme']}")

            col1, col2 = st.columns(2)

            with col1:
                pdf_bytes = generate_trip_pdf(inputs['destination'], result)
                st.download_button(
                    "📥 Download PDF",
                    pdf_bytes,
                    file_name=f"{inputs['destination'].replace(' ', '_')}_itinerary.pdf",
                    mime="application/pdf",
                    key=f"pdf_{actual_index}",
                    use_container_width=True
                )

            with col2:
                if st.button("🗑️ Delete", key=f"del_{actual_index}", use_container_width=True):
                    delete_trip(st.session_state.username, actual_index)
                    st.rerun()

footer()