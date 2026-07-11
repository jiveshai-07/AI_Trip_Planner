import requests

API_KEY = "ac9517cffd0be368900e60de00b1186c"


def get_weather(destination):
    try:
        url = (
            "https://api.openweathermap.org/data/2.5/weather"
            f"?q={destination}&appid={API_KEY}&units=metric"
        )

        response = requests.get(url, timeout=10)
        data = response.json()

        if response.status_code != 200:
            return None

        return {
            "temperature": data["main"]["temp"],
            "condition": data["weather"][0]["main"],
            "description": data["weather"][0]["description"].title(),
            "humidity": data["main"]["humidity"],
            "wind": data["wind"]["speed"],
        }

    except Exception:
        return None