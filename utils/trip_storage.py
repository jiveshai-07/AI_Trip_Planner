import json
import os
from datetime import datetime

TRIPS_FILE = "data/trips.json"


def load_trips():
    if not os.path.exists(TRIPS_FILE):
        return {}
    with open(TRIPS_FILE, "r") as f:
        return json.load(f)


def save_trips(trips):
    os.makedirs("data", exist_ok=True)
    with open(TRIPS_FILE, "w") as f:
        json.dump(trips, f, indent=2)


def save_trip(username, trip_inputs, trip_result):
    trips = load_trips()

    if username not in trips:
        trips[username] = []

    trip_entry = {
        "saved_at": datetime.now().strftime("%Y-%m-%d %H:%M"),
        "inputs": trip_inputs,
        "result": trip_result
    }

    trips[username].append(trip_entry)
    save_trips(trips)


def get_user_trips(username):
    trips = load_trips()
    return trips.get(username, [])


def delete_trip(username, trip_index):
    trips = load_trips()
    if username in trips and 0 <= trip_index < len(trips[username]):
        trips[username].pop(trip_index)
        save_trips(trips)