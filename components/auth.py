import streamlit as st
from utils.auth_helpers import register_user, verify_user, username_exists


def check_login():

    if "logged_in" not in st.session_state:
        st.session_state.logged_in = False
        st.session_state.username = None

    if st.session_state.logged_in:
        return

    # ==================================================
    # PAGE STYLING
    # ==================================================

    st.markdown("""
    <style>
    [data-testid="stSidebarNav"], [data-testid="stSidebar"] {
        display:none;
    }

    .stApp {
        background:#F8FAFC;
    }

    .auth-title {
        text-align:center;
        font-size:42px;
        font-weight:800;
        color:#0F766E;
        margin-top:40px;
        margin-bottom:6px;
    }

    .auth-subtitle {
        text-align:center;
        font-size:16px;
        color:#64748B;
        margin-bottom:30px;
    }

    div[data-testid="stForm"] {
        background:white;
        padding:30px;
        border-radius:18px;
        box-shadow:0 10px 30px rgba(0,0,0,.08);
        border:1px solid #E2E8F0;
    }
    </style>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="auth-title">✈️ AI Trip Planner</div>
    <div class="auth-subtitle">
        Plan smarter trips with AI agents working for you
    </div>
    """, unsafe_allow_html=True)

    col1, col2, col3 = st.columns([1, 1.3, 1])

    with col2:

        # ==================================================
        # LOGIN / SIGNUP
        # ==================================================

        tab1, tab2 = st.tabs(["🔐 Login", "📝 Sign Up"])

        # ---------------- LOGIN ----------------

        with tab1:

            with st.form("login_form"):

                login_username = st.text_input("Username")

                login_password = st.text_input(
                    "Password",
                    type="password"
                )

                login_submitted = st.form_submit_button(
                    "Login",
                    use_container_width=True
                )

                if login_submitted:

                    if verify_user(
                        login_username,
                        login_password
                    ):

                        st.session_state.logged_in = True
                        st.session_state.username = login_username
                        st.rerun()

                    else:

                        st.error("Invalid username or password.")

        # ---------------- SIGN UP ----------------

        with tab2:

            with st.form("signup_form"):

                signup_username = st.text_input(
                    "Choose a Username"
                )

                signup_email = st.text_input(
                    "Email (optional)"
                )

                signup_password = st.text_input(
                    "Choose a Password",
                    type="password"
                )

                signup_confirm = st.text_input(
                    "Confirm Password",
                    type="password"
                )

                signup_submitted = st.form_submit_button(
                    "Create Account",
                    use_container_width=True
                )

                if signup_submitted:

                    if not signup_username or not signup_password:

                        st.error(
                            "Username and password are required."
                        )

                    elif signup_password != signup_confirm:

                        st.error(
                            "Passwords do not match."
                        )

                    elif username_exists(signup_username):

                        st.error(
                            "Username already taken."
                        )

                    else:

                        success, message = register_user(
                            signup_username,
                            signup_password,
                            signup_email
                        )

                        if success:

                            st.success(
                                message + " Please log in."
                            )

                        else:

                            st.error(message)

    st.stop()


def logout():

    st.session_state.logged_in = False
    st.session_state.username = None
    st.rerun()