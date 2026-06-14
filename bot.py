# Pulse - Daily Summary Bot
# Fetches weather from wttr.in and a quote from zenquotes
# Runs every day at 8 AM IST using GitHub Actions

import requests
from datetime import date

# Function 1 - gets the weather
def get_weather(city="Thiruvananthapuram"):
    url = f"https://wttr.in/{city}?format=3"
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        return response.text.strip()
    except Exception as e:
        return f"Weather unavailable ({e})"

# Function 2 - gets a random quote
def get_quote():
    url = "https://zenquotes.io/api/random"
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        data = response.json()
        quote = data[0]["q"]
        author = data[0]["a"]
        return f'"{quote}" - {author}'
    except Exception as e:
        return f"Quote unavailable ({e})"

# Function 3 - builds the full summary text
def build_summary():
    today = date.today().strftime("%A, %d %B %Y")
    weather = get_weather()
    quote = get_quote()

    summary = f"""
================================
  PULSE - Daily Summary
  {today}
================================

WEATHER
  {weather}

TODAY'S QUOTE
  {quote}

================================
"""
    return summary

# Function 4 - runs everything, saves the file
def run():
    summary = build_summary()
    print(summary)

    with open("daily_summary.txt", "w", encoding="utf-8") as f:
        f.write(summary)

    print("Pulse ran successfully.")

if __name__ == "__main__":
    run()
