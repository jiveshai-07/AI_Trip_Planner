import streamlit as st

PAGES = {
    "Dashboard": "app.py",
    "Plan Trip": "pages/_Plan_Trip.py",
    "History": "pages/_Trip_History.py",
    "Chat": "pages/_Travel_Chat.py",
    "About": "pages/_About.py",
    "Settings": "pages/_Settings.py",
}


def navbar():

    st.markdown("<br>", unsafe_allow_html=True)

    c1, c2, c3, c4, c5, c6 = st.columns([1.2, 1.3, 1.2, 1.2, 1, 1.1])

    with c1:
        if st.button("🏠 Dashboard", use_container_width=True):
            st.switch_page(PAGES["Dashboard"])

    with c2:
        if st.button("🧭 Plan Trip", use_container_width=True):
            st.switch_page(PAGES["Plan Trip"])

    with c3:
        if st.button("🕓 History", use_container_width=True):
            st.switch_page(PAGES["History"])

    with c4:
        if st.button("💬 Chat", use_container_width=True):
            st.switch_page(PAGES["Chat"])

    with c5:
        if st.button("ℹ️ About", use_container_width=True):
            st.switch_page(PAGES["About"])

    with c6:
        if st.button("⚙️ Settings", use_container_width=True):
            st.switch_page(PAGES["Settings"])

    st.markdown("<br>", unsafe_allow_html=True)