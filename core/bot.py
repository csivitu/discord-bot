import os
from logging import getLogger
from typing import Union

from discord import Intents, Interaction, Message, AllowedMentions
from discord.ext import commands
from discord.ext.commands import DefaultHelpCommand

from utils import Context

__all__ = ("Bot",)

log = getLogger("Bot")


class Bot(commands.Bot):
    def __init__(self) -> None:
        super().__init__(
            command_prefix=commands.when_mentioned_or("."),
            intents=Intents.all(),
            case_insensitive=True,
            help_command=DefaultHelpCommand(),
            allowed_mentions=AllowedMentions(
                everyone=False, users=True, replied_user=True, roles=False
            ),
        )

    async def on_connect(self) -> None:
        log.info(f"Connected to discord as {self.user}(ID:{self.user.id})")

    async def on_disconnect(self) -> None:
        log.info("Bot disconnected")

    async def on_resumed(self) -> None:
        log.info("Bot resumed")

    async def on_ready(self) -> None:
        log.info("Bot ready")

    async def setup_hook(self) -> None:
        log.info("Running setup...")
        for file in os.listdir(os.path.join(os.getcwd(), 'cogs')):
            if not file.startswith("_"):
                try:
                    await self.load_extension(f"cogs.{file}.plugin")
                except Exception as e:
                    log.info(f"Couldn't load {file}\n{e}")

        try:
            await self.load_extension("jishaku")
            log.info("Loaded Jishaku")
        except Exception as e:
            log.info(f"Couldn't load Jishaku because of {e}")

        await self.tree.sync()

    async def get_context(
        self, origin: Union[Message, Interaction], *, cls=Context
    ) -> Context:
        return await super().get_context(origin, cls=cls)
