# Pulse - Daily Summary Bot

A Python bot that fetches live weather and a motivational quote every morning and formats them into a clean daily summary. Runs automatically at 8 AM IST via GitHub Actions — no manual input needed.

## What it does

- Fetches today's weather for Thiruvananthapuram using wttr.in
- Fetches a random motivational quote from ZenQuotes
- Builds a formatted summary and saves it as a downloadable file
- Runs on a schedule every day at 8 AM IST

## How to run locally

```bash
pip install requests
python bot.py
```

## How it runs automatically

GitHub Actions picks up the workflow file at `.github/workflows/daily.yml` and runs the bot on the cron schedule `30 2 * * *` (2:30 AM UTC = 8:00 AM IST). You can also trigger it manually from the Actions tab using the "Run workflow" button.

After each run, the summary is saved as `daily_summary.txt` and uploaded as a downloadable artifact.

## Project structure

```
pulse/
├── bot.py              # the bot - four functions, one job each
├── requirements.txt    # just: requests
├── README.md
└── .github/
    └── workflows/
        └── daily.yml   # the schedule and steps
```

## APIs used

| API | What it returns | Key needed? |
|-----|----------------|-------------|
| wttr.in | One-line weather summary | No |
| ZenQuotes | Random motivational quote | No |

Built as part of ZERO2DEV 2026 · Session 03 · Python Automation
