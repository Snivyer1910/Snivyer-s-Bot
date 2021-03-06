###
# Imports
###

from config import getarg

from discord.ext import commands
import discord

from util.embed import errorbox
from util.cooldownhandler import cooldownhandler

from random import choice

import translators

###
# Cache
###

prefix = getarg('prefix')
embed = discord.Embed(
    title="Snivyer's Maid",
    description=f'My prefix is `{prefix}` . Type `{prefix}help` for a list of my commands.'
)

###
# Cog
###

class pingdialog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        if self.bot.user.mentioned_in(message):
            await message.channel.send(embed=embed)


###
# Setup Cog
###

def setup(bot):
    bot.add_cog(pingdialog(bot))
