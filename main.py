import asyncio
import os
import logging
from discord.ext import commands  # Assuming you're using discord.ext.commands for Bot
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get the Discord bot token from environment variables
token = os.environ.get("TOKEN")

# Set up logging for the bot
logging.basicConfig(level=logging.INFO)

# Define the bot class
class Bot(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix="!")  # You can set the command prefix as per your need

async def main() -> None:
    async with Bot() as bot:
        # Start the bot and reconnect if disconnected
        await bot.start(token=token, reconnect=True)

if __name__ == "__main__":
    if token is None:
        print("Error: TOKEN environment variable not set.")
    else:
        try:
            asyncio.run(main())
        except KeyboardInterrupt:
            print("Bot stopped.")
        except Exception as e:
            print(f"An error occurred: {e}")
