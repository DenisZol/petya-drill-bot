# Petya Drill Bot

This is a simple Telegram bot built with [python-telegram-bot](https://github.com/python-telegram-bot/python-telegram-bot).

## Features

- `/инструкция` &mdash; sends drilling instructions from Petya.
- `/complain` — acknowledges your complaint with a short reply.

## Usage

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Set your bot token in the `TELEGRAM_TOKEN` environment variable.
3. Run the bot:
   ```bash
   python bot.py
   ```
4. Send `/инструкция` or `/complain` in chat to interact with the bot.
