import streamlit as st
import json
from openai import OpenAI


def get_model():

    api_key = st.secrets.get("OPENROUTER_API_KEY")

    if not api_key:
        st.error("OpenRouter API key not found.")
        st.stop()

    client = OpenAI(
        api_key=api_key,
        base_url="https://openrouter.ai/api/v1"
    )

    return client
def generate_json(prompt):

    client = get_model()

    response = client.chat.completions.create(

        model="meta-llama/llama-3.3-70b-instruct",

        temperature=0.2,

        response_format={
            "type": "json_object"
        },

        messages=[
            {
                "role": "system",
                "content":
                "You are an AI assistant that ALWAYS returns ONLY valid JSON. Never add markdown, explanations or text outside the JSON."
            },
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    text = response.choices[0].message.content

    return parse_json_response(text)
import re


def parse_json_response(text):

    try:
        return json.loads(text)

    except:

        pass

    match = re.search(r"\{.*\}", text, re.DOTALL)

    if match:

        try:
            return json.loads(match.group())

        except:

            pass

    return None