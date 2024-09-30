import asyncio
import os

from discord.utils import setup_logging

from core import Bot
from dotenv import load_dotenv

load_dotenv()


token = os.environ.get("TOKEN")


async def main() -> None:
    setup_logging()
    async with Bot() as bot:
        await bot.start(token=token, reconnect=True)


if __name__ == "__main__":
    asyncio.run(main())
