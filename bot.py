import requests
from datetime import date

# FUNCTION 1: Weather
def get_weather(city="Thiruvananthapuram"):
    """Get weather data for a given city and return text summary."""
    url = f"https://wttr.in/{city}?format=3"
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        return response.text.strip()  # remove trailing whitespace/headlines
    except Exception as e:
        return f"Weather unavailable ({e})"

# FUNCTION 2: Quote
def get_quote():
    """Get random motivational quote from ZenQuotes."""
    url = "https://zenquotes.io/api/random"
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        data = response.json()[0]  # convert JSON text to Python list
        return f"{data['q']} — {data['a']}"
    except Exception as e:
        return f"Quote unavailable ({e})"

# FUNCTION 3: Build the summary
def build_summary():
    """Assemble the full daily summary from all data sources."""
    today = date.today().strftime("%A, %d %B %Y")  # e.g. "Monday, 09 June 2026"
    weather = get_weather()
    quote = get_quote()

    summary = f"""
PULSE - Daily Summary
=====================
{today}
=====================
WEATHER
{weather}

TODAY'S QUOTE
{quote}
=====================
"""
    return summary

# FUNCTION 4: Run everything
def run():
    """Main entry point. Called by GitHub Actions."""
    summary = build_summary()

    # Print to the GitHub Actions Log (visible in the Actions tab)
    print(summary)

    # Save to a file (uploaded as a downloadable artifact by the workflow)
    with open("daily_summary.txt", "w", encoding="utf-8") as f:
        f.write(summary)

    print("Pulse run successfully.")

# Entry point guard
if __name__ == "__main__":
    run()
