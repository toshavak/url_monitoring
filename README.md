# URL Monitoring and Notification Script

This Python script monitors the availability of a specified URL and provides real-time updates through both synthesized speech and Telegram notifications.

## Dependencies

- [`requests`](https://docs.python-requests.org/en/latest/) - For making HTTP requests.
- [`pyttsx3`](https://pyttsx3.readthedocs.io/en/latest/) - For text-to-speech synthesis.
- [`python-telegram-bot`](https://python-telegram-bot.readthedocs.io/en/stable/) - For interacting with the Telegram API.

## Configuration

1. Replace the `URL` and `TOKEN` variables with your target URL and Telegram bot token, respectively.
2. Adjust the `rate` and `volume` properties of the text-to-speech engine as needed.

## Telegram Setup

Make sure you have a Telegram bot created and obtain the token. Add your bot to a group or start a chat with it to get chat IDs.

## Usage

1. Install the required dependencies using `pip install requests pyttsx3 python-telegram-bot`.
2. Run the script using `python main.py`.
3. The script will continuously monitor the specified URL and provide notifications on status changes.

## Notes

- The script utilizes the Telegram bot API to send messages to specified chats. Make sure to set up your Telegram bot and obtain the necessary chat IDs.
- Adjust the sleep interval (e.g., `time.sleep(5)`) based on your monitoring frequency requirements.
- In case of an error, the script will send an error message and stop execution.

Feel free to customize and enhance the script based on your specific use case and requirements.
