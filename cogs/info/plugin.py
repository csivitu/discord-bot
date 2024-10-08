from discord import Embed, Member, Role
from discord.ext import commands
from cogs import Plugin
from core import Bot
from discord.ext.commands import Context
from datetime import datetime, timezone


class Info(Plugin):
    @commands.command(name="info", description="Info of a server member")
    async def info(self, ctx: Context, member: Member = None) -> None:
        if member is None:
            member = ctx.author
        roles: list[Role] = [role for role in member.roles]
        embed: Embed = Embed(
            colour=member.color,
            timestamp=datetime.now(timezone.utc),
            title=f"User Info - {member}",
        )
        embed.set_thumbnail(url=member.display_avatar)
        embed.add_field(name="ID:", value=member.id, inline=True)
        embed.add_field(name="Display Name:", value=member.display_name, inline=True)
        embed.add_field(
            name="Account Created:",
            value=f"<t:{int(member.created_at.timestamp())}:R>",
            inline=True,
        )
        embed.add_field(
            name="Server Joined:",
            value=f"<t:{int(member.joined_at.timestamp())}:R>",
            inline=True,
        )
        embed.add_field(
            name="Roles:", value=",".join([role.mention for role in roles]), inline=True
        )
        embed.add_field(
            name="Highest Role:", value=f"{member.top_role.mention}", inline=True
        )
        await ctx.send(embed=embed)

    @commands.command(name="count", help="Returns member count.")
    async def membercount(self, ctx: Context) -> None:
        human_users = sum(1 for member in ctx.guild.members if not member.bot)
        await ctx.send(f"Members: {human_users}")


async def setup(bot: Bot) -> None:
    await bot.add_cog(Info(bot))
