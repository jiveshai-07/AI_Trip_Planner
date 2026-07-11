import streamlit as st
from PIL import Image


@st.cache_resource
def load_model():
    """
    Loads a CLIP model once and caches it across the session.
    """
    from transformers import CLIPProcessor, CLIPModel

    model = CLIPModel.from_pretrained("openai/clip-vit-base-patch32")
    processor = CLIPProcessor.from_pretrained("openai/clip-vit-base-patch32")

    return model, processor


TRAVEL_STYLES = [
    "a beach and tropical coastal destination",
    "snowy mountains and alpine scenery",
    "a historic old city with traditional architecture",
    "a modern city skyline with skyscrapers",
    "a dense green forest or jungle nature scene",
    "a desert landscape",
    "a countryside with rolling hills and villages",
    "an island getaway with clear water",
]

STYLE_LABELS = {
    "a beach and tropical coastal destination": "Beach & Coastal",
    "snowy mountains and alpine scenery": "Mountains & Alpine",
    "a historic old city with traditional architecture": "Historic & Cultural",
    "a modern city skyline with skyscrapers": "Urban & Modern City",
    "a dense green forest or jungle nature scene": "Nature & Forest",
    "a desert landscape": "Desert",
    "a countryside with rolling hills and villages": "Countryside & Rural",
    "an island getaway with clear water": "Island & Tropical Water",
}


def detect_travel_style(image_file):
    """
    Takes an uploaded image file, runs it through CLIP zero-shot
    classification against a fixed set of travel style prompts.
    Returns (style_label, confidence_score) for the top match.
    """

    try:
        model, processor = load_model()

        image = Image.open(image_file).convert("RGB")

        inputs = processor(
            text=TRAVEL_STYLES,
            images=image,
            return_tensors="pt",
            padding=True
        )

        outputs = model(**inputs)
        logits_per_image = outputs.logits_per_image
        probs = logits_per_image.softmax(dim=1)[0]

        top_idx = probs.argmax().item()
        top_style = TRAVEL_STYLES[top_idx]
        confidence = probs[top_idx].item()

        return STYLE_LABELS[top_style], round(confidence * 100, 1)

    except Exception as e:
        return None, f"Error: {e}"