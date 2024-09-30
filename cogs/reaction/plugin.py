from discord import Embed, User, Message
from cogs import Plugin
from core import Bot
from discord.ext import commands
from discord.ext.commands import Context
from asyncio import TimeoutError


class Reaction(Plugin):
    @commands.command(name="react", description="React to the message")
    async def _(self, ctx: Context) -> None:
        m: Message = await ctx.send(
            embed=Embed(title="Forkthis", description="React to the message with 👍")
        )

        def check(reaction: Reaction, user) -> bool:
            return reaction.message == m and str(reaction.emoji) == "👍" and user == ctx.author

        await m.add_reaction("👍")
        try:
            reaction, user = await self.bot.wait_for(
                "reaction_add", timeout=60.0, check=check
            )
        except TimeoutError:
            await m.edit(content="You took too long", suppress=True)
        else:
            if str(reaction.emoji) == "👍":
                await m.edit(content="You Reacted to the message", suppress=True)
            else:
                await m.edit(content="Wrong Reaction", suppress=True)


async def setup(bot: Bot) -> None:
    await bot.add_cog(Reaction(bot))