import datetime

import discord
from discord.ext import commands

from core import checks
from core.models import PermissionLevel
from core.decorators import trigger_typing


class Uptime(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @checks.has_permissions(PermissionLevel.REGULAR)
    @trigger_typing
    async def uptime(self, ctx):
        """Shows uptime for the bot."""

        desc = "This is a plugin command to view how long your bot has been "
        desc += "online since the last time it restarted."

        embed = discord.Embed(
            description=desc,
            color=self.bot.main_color,
            timestamp=datetime.datetime.utcnow(),
        )

        embed.set_author(
            name="Modmail - Uptime",
            icon_url=self.bot.user.avatar_url,
        )

        embed.set_thumbnail(url=self.bot.user.avatar_url)

        embed.add_field(name="Uptime", value=self.bot.uptime)

        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Uptime(bot))
