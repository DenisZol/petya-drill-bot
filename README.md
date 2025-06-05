# Petya Drill Bot

This is a simple Telegram bot built with [python-telegram-bot](https://github.com/python-telegram-bot/python-telegram-bot).

## Features

- `/instr` &mdash; sends drilling instructions from Petya.
- `/complain` &mdash; accepts your complaint, which Petya will promptly ignore.

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
4. Send the `/instr` command to receive instructions from Petya.
5. Send the `/complain` command if you want to file a complaint.
