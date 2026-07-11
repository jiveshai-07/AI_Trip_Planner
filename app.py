import streamlit as st
from components.auth import check_login, logout
from components.ui import load_ui, footer
from components.navbar import navbar
from utils.trip_storage import get_user_trips

check_login()
load_ui()
navbar()

username = st.session_state.username
trips = get_user_trips(username)

trip_count = len(trips)
country_count = len({trip["inputs"]["destination"] for trip in trips})

# ============================================================
# HERO SECTION
# ============================================================

st.title("🧭 AI Trip Planner")

st.success(
    f"Welcome back, **{username}** 👋\n\n"
    "Plan smarter. Travel better.\n\n"
    "Multi-Agent AI powered travel planning with Deep Learning."
)

# ============================================================
# DASHBOARD
# ============================================================

st.header("📊 Dashboard")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Trips Saved", trip_count)

with col2:
    st.metric("Destinations Planned", country_count)

with col3:
    st.metric("AI Agents", "4")

st.divider()

# ============================================================
# QUICK ACCESS
# ============================================================

st.header("⚡ Quick Access")

col1, col2 = st.columns(2)

with col1:

    st.markdown("### 🧭 Plan a New Trip")
    st.caption("Generate a complete AI-powered itinerary.")

    if st.button(
        "Open Plan Trip",
        key="goto_plan",
        use_container_width=True
    ):
        st.switch_page("pages/_Plan_Trip.py")

    st.markdown("---")

    st.markdown("### 💬 Travel Assistant")
    st.caption("Ask follow-up questions about your itinerary.")

    if st.button(
        "Open Chat",
        key="goto_chat",
        use_container_width=True
    ):
        st.switch_page("pages/_Travel_Chat.py")

with col2:

    st.markdown("### 🕓 Trip History")
    st.caption("View, download and manage your saved trips.")

    if st.button(
        "Open History",
        key="goto_history",
        use_container_width=True
    ):
        st.switch_page("pages/_Trip_History.py")

    st.markdown("---")

    st.markdown("### ⚙️ Settings")
    st.caption("Customize your application preferences.")

    if st.button(
        "Open Settings",
        key="goto_settings",
        use_container_width=True
    ):
        st.switch_page("pages/_Settings.py")

st.divider()

# ============================================================
# TRAVEL TIP
# ============================================================

st.header("💡 Travel Tip")

st.info(
    "Travel during weekdays whenever possible. Flights and hotels are usually cheaper, "
    "popular attractions are less crowded, and you'll enjoy a more relaxed experience."
)

st.divider()
st.caption(
    "⚡ Powered by OpenRouter • Meta Llama 3.3 70B • Streamlit • CLIP • Multi-Agent AI"
)

st.markdown("<br>", unsafe_allow_html=True)
if st.button("🚪 Logout", use_container_width=True):
    logout()

footer()