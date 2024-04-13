import telegram
import time

# Telegram bot token
TOKEN = '6257502067:AAFK6WJWE7zB_921Ql4s5bCGik'
# List of channel IDs where the bot is admin
CHANNEL_IDS = [-10017335464]  # Add more channel IDs as needed
# Sticker file ID
STICKER_FILE_ID = 'CAACAgUAAxkBAAJF9mXrZNS-psRoYjoytEk85XdshxJ5AAI9DwAC0rOpVh9Vv7t5-XjhNAQ'

# Initialize bot
bot = telegram.Bot(token=TOKEN)

# Dictionary to store the last message ID for each channel ID
last_message_ids = {channel_id: None for channel_id in CHANNEL_IDS}

# Function to send a sticker and delete the previous one for each channel ID
def send_sticker_and_delete_previous(sticker_file_id, chat_ids):
    global last_message_ids
    try:
        for chat_id in chat_ids:
            # Send a new sticker
            sent_sticker = bot.send_sticker(chat_id=chat_id, sticker=sticker_file_id)

            # Delete the previous message if available
            if last_message_ids[chat_id]:
                bot.delete_message(chat_id=chat_id, message_id=last_message_ids[chat_id])

            # Update the last message ID for this channel
            last_message_ids[chat_id] = sent_sticker.message_id

    except telegram.error.TimedOut as e:
        print(f"Timed out while trying to communicate with Telegram API: {e}")

# Main function
def main():
    while True:
        # Send a sticker to all channel IDs
        send_sticker_and_delete_previous(STICKER_FILE_ID, CHANNEL_IDS)
        # Wait for 2 seconds (reduce wait time for stickers)
        time.sleep(2)

if __name__ == '__main__':
    main()
