import requests


def convert_currency(amount, to_currency):
    """
    Converts USD amount into the destination currency.
    Uses exchangerate.host free API.
    """

    try:
        url = (
            f"https://api.exchangerate.host/convert"
            f"?from=USD&to={to_currency}&amount={amount}"
        )

        response = requests.get(url, timeout=10)
        data = response.json()

        if data.get("success"):
            return round(data["result"], 2)

    except Exception:
        pass

    return None