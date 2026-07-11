import folium
from geopy.geocoders import Nominatim


def generate_destination_map(destination, attractions):
    geolocator = Nominatim(user_agent="ai_trip_planner")

    try:
        location = geolocator.geocode(destination)

        if not location:
            return None

        m = folium.Map(
            location=[location.latitude, location.longitude],
            zoom_start=12
        )

        folium.Marker(
            [location.latitude, location.longitude],
            popup=destination,
            tooltip="Destination",
            icon=folium.Icon(color="red", icon="info-sign")
        ).add_to(m)

        popup_text = "<b>Top Attractions</b><br><br>"

        for place in attractions:
            popup_text += f"• {place['name']}<br>"

        folium.Marker(
            [location.latitude, location.longitude],
            popup=folium.Popup(popup_text, max_width=300),
            icon=folium.Icon(color="blue")
        ).add_to(m)

        return m

    except Exception:
        return None