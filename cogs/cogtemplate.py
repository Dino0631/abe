
import itertools
import discord
from discord.ext import commands
from discord.ext.commands import Context
import cogs
from cogs.utils.chat_formatting import pagify
from cogs.utils import checks
from random import choice
import aiohttp
from __main__ import send_cmd_help
from cogs.economy import SetParser


class COGNAME:
    """Display RACF specifc info.

    Note: RACF specific plugin for Red
    """

    def __init__(self, bot):
        """Constructor."""
        self.bot = bot

        

def setup(bot):
    r = COGNAME(bot)
    bot.add_cog(r)
