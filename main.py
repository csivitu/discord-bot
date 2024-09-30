import asyncio
import os
from discord.ext import commands

from discord.utils import setup_logging

from core import Bot
from dotenv import load_dotenv

load_dotenv(dotenv_path)


token = os.environ.get("TOKEN")

bot=bot = commands.Bot(command_prefix='!')

async def main() -> None:
    setup_logging()
    await bot.start(token=token, reconnect=True)
        
async def choose_emoji(ctx):

    message = await ctx.send("Choose an emoji:\n😂 - Laughing\n🤣 - Rolling on the floor laughing\n😭 - Crying")

    await message.add_reaction("😂")
    await message.add_reaction("🤣")
    await message.add_reaction("😭")

    def check(reaction, user):
        return user == ctx.author and str(reaction.emoji) in ["😂", "🤣", "😭"]

    reaction, user = await bot.wait_for("reaction_add", check=check)
    await ctx.send(f'You chose: {reaction.emoji}')


if __name__ == "__main__":
    asyncio.run(main())
