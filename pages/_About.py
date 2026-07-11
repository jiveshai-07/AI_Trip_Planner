import streamlit as st
from components.auth import check_login
from components.ui import load_ui, footer
from components.navbar import navbar

check_login()
load_ui()
navbar()

st.title("ℹ️ About")

col1, col2 = st.columns([1, 3])

with col1:
    st.image("icons/profile.png", width=220)

with col2:
    st.markdown('<div class="card">', unsafe_allow_html=True)

    st.header("👨‍💻 Jivesh Mishra")

    st.write(
        "AI & Data Science Enthusiast passionate about building intelligent "
        "applications using Artificial Intelligence, Large Language Models, "
        "Deep Learning, Machine Learning, Computer Vision and Python."
    )

    st.write(
        "This project demonstrates a complete Multi-Agent AI system capable of "
        "researching destinations, planning budgets, generating detailed itineraries, "
        "reviewing travel plans, classifying travel styles using Deep Learning, "
        "generating PDF reports and maintaining personalized trip history."
    )

    st.markdown("</div>", unsafe_allow_html=True)

st.divider()

st.header("🚀 Project Overview")

st.markdown('<div class="card">', unsafe_allow_html=True)

st.subheader("✈️ AI Trip Planner")

st.write(
    "AI Trip Planner is a professional Multi-Agent AI application designed "
    "to simplify travel planning."
)

st.write(
    "Four specialized AI agents collaborate together to research destinations, "
    "plan budgets, generate itineraries and review the final travel plan."
)

st.write(
    "The application combines Large Language Models with Deep Learning to "
    "provide intelligent and personalized travel recommendations."
)

st.markdown("</div>", unsafe_allow_html=True)

st.header("✨ Key Features")

col1, col2 = st.columns(2)

with col1:

    st.markdown('<div class="card">', unsafe_allow_html=True)

    st.subheader("🤖 Artificial Intelligence")

    st.write("✅ Multi-Agent AI Workflow")
    st.write("✅ Research Agent")
    st.write("✅ Budget Planner")
    st.write("✅ Itinerary Writer")
    st.write("✅ Reviewer")
    st.write("✅ Self-Correcting Workflow")

    st.markdown("</div>", unsafe_allow_html=True)

    st.markdown('<div class="card">', unsafe_allow_html=True)

    st.subheader("📸 Deep Learning")

    st.write("✅ CLIP Image Classification")
    st.write("✅ Travel Style Detection")
    st.write("✅ Personalized Recommendations")

    st.markdown("</div>", unsafe_allow_html=True)

with col2:

    st.markdown('<div class="card">', unsafe_allow_html=True)

    st.subheader("💼 Productivity")

    st.write("✅ Trip History")
    st.write("✅ PDF Export")
    st.write("✅ Travel Chat Assistant")
    st.write("✅ Secure Login")
    st.write("✅ Google OAuth")

    st.markdown("</div>", unsafe_allow_html=True)

    st.markdown('<div class="card">', unsafe_allow_html=True)

    st.subheader("⚡ User Experience")

    st.write("✅ Professional Dashboard")
    st.write("✅ Responsive Layout")
    st.write("✅ Modern UI")
    st.write("✅ Easy Navigation")

    st.markdown("</div>", unsafe_allow_html=True)

st.header("🛠 Technology Stack")

st.markdown('<div class="card">', unsafe_allow_html=True)

st.write("**Backend:** Python, Streamlit")

st.write("**Artificial Intelligence:** Google Gemini API, Prompt Engineering")

st.write("**Deep Learning:** OpenAI CLIP, PyTorch, Transformers")

st.write("**Authentication:** Google OAuth, Secure Login")

st.write("**Database:** JSON Storage")

st.write("**PDF Generation:** ReportLab")

st.markdown("</div>", unsafe_allow_html=True)

st.header("🌐 Connect With Me")

col1, col2 = st.columns(2)

with col1:

    st.markdown('<div class="card">', unsafe_allow_html=True)

    st.subheader("GitHub")

    st.link_button(
        "Visit GitHub",
        "https://github.com/jiveshai-07",
        use_container_width=True,
    )

    st.markdown("</div>", unsafe_allow_html=True)

with col2:

    st.markdown('<div class="card">', unsafe_allow_html=True)

    st.subheader("LinkedIn")

    st.link_button(
        "Visit LinkedIn",
        "https://www.linkedin.com/in/jivesh-mishra",
        use_container_width=True,
    )

    st.markdown("</div>", unsafe_allow_html=True)

st.header("🎯 Project Highlights")

st.markdown('<div class="card">', unsafe_allow_html=True)

st.write("🏆 Multi-Agent AI System")
st.write("🧠 Deep Learning Integration")
st.write("📄 Automated PDF Generation")
st.write("📷 Image-based Travel Style Detection")
st.write("💬 AI Travel Assistant")
st.write("🕓 Trip History Management")
st.write("🔐 Secure Authentication")
st.write("🌍 Personalized Travel Planning")

st.markdown("</div>", unsafe_allow_html=True)

footer()