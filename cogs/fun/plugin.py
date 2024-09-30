from discord.ext import commands
from cogs import Plugin
from core import Bot
from random import choice
from discord.ext.commands import Context


class Fun(Plugin):

    @commands.command(name="emoji", description="sends a random emoji")
    async def _(self, ctx: Context) -> None:
        emojis: list[str] = ["sob", "grinning", "skull", "eagle", "goat", "sunglasses"]
        emoji: str = choice(emojis)
        await ctx.reply(f":{emoji}:")


async def setup(bot: Bot) -> None:
    await bot.add_cog(Fun(bot))
