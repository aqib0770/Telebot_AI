# TELEBOT_AI
### Description
This script creates a telegram bot that uses Gemini AI to provide intelligent and informative responses to user queries. This bot is built using the aiogram library and integrates with the Gemini AI API.

### Pre-requisites
1. Python 3.9 or higher
2. A Telegram bot token (You can get this from the BotFather on Telegram)
3. A Gemini AI API key (You can get this from the Gemini AI website)

### Installation
1. Clone this repository
2. Install the required dependencies using the following command:
```bash
pip install -r requirements.txt
```
3. Create a .env file in the root directory of the project and add the following environment variables:
```bash
TELEGRAM_BOT_TOKEN=<YOUR_TELEGRAM_BOT_TOKEN>
GEMINI_AI_API_KEY=<YOUR_GEMINI_AI_API_KEY>
```
4. Run the script using the following command:
```bash
python telebot.py
```

### Usage
1. Start the bot by sending the /start command to the bot on Telegram
2. Send a message to the bot to get an intelligent response from the Gemini AI
