import streamlit as st
from components.auth import check_login
from components.ui import load_ui, footer
from components.navbar import navbar
from utils.gemini_client import get_model

check_login()
load_ui()
navbar()

st.title("💬 Travel Chat")

st.write(
    "Ask follow-up questions about your generated itinerary."
)

if "last_trip_result" not in st.session_state:

    st.info(
        "Generate a trip first from the Plan Trip page."
    )

    footer()
    st.stop()

trip = st.session_state.last_trip_result
inputs = st.session_state.last_trip_inputs

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

for message in st.session_state.chat_history:

    with st.chat_message(message["role"]):

        st.markdown(message["content"])

user_input = st.chat_input(
    "Ask about your trip..."
)

if user_input:

    st.session_state.chat_history.append(
        {
            "role": "user",
            "content": user_input
        }
    )

    with st.chat_message("user"):

        st.markdown(user_input)

    trip_context = f"""
Destination: {inputs['destination']}
Duration: {inputs['duration_days']} days
Trip Title: {trip['itinerary'].get('trip_title','')}
Daily Plan: {trip['itinerary'].get('daily_plan',[])}
Budget: {trip['budget'].get('total_estimated_cost','')}
Safety Tips: {trip['research'].get('local_safety_tips',[])}
"""

    prompt = f"""
You are a helpful travel assistant.

Use the following trip information to answer the user's follow-up question.

{trip_context}

User Question:
{user_input}
"""

    with st.chat_message("assistant"):

        with st.spinner("Thinking..."):

            try:

                client = get_model()

                response = client.chat.completions.create(

                    model="meta-llama/llama-3.3-70b-instruct",

                    messages=[
                        {
                            "role": "user",
                            "content": prompt
                        }
                    ]
                )

                reply = response.choices[0].message.content

            except Exception as e:

                reply = f"Error: {e}"

            st.markdown(reply)

    st.session_state.chat_history.append(
        {
            "role": "assistant",
            "content": reply
        }
    )

if st.session_state.chat_history:

    if st.button(
        "🗑️ Clear Chat",
        use_container_width=True
    ):

        st.session_state.chat_history = []

        st.rerun()

footer()