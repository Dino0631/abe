# -*- coding: utf-8 -*-

"""
The MIT License (MIT)

Copyright (c) 2017 SML

Permission is hereby granted, free of charge, to any person obtaining a
copy of this software and associated documentation files (the "Software"),
to deal in the Software without restriction, including without limitation
the rights to use, copy, modify, merge, publish, distribute, sublicense,
and/or sell copies of the Software, and to permit persons to whom the
Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS
OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
DEALINGS IN THE SOFTWARE.
"""
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


class Test:
    """
    Test cog
    """

    def __init__(self, bot):
        """Constructor."""
        self.bot = bot


    @commands.command(pass_context=True, no_pm=True)
    @checks.admin_or_permissions()
    async def lekic(self, ctx, member: discord.Member=None, *roles: str):
        """Change roles of a user.
        Example: !changerole SML +Delta "-Foxtrot Lead" "+Delta Lead"
        Multi-word roles must be surrounded by quotes.
        Operators are used as prefix:
        + for role addition
        - for role removal
        """
        server = ctx.message.server
        author = ctx.message.author
        if member is None:
            await self.bot.say("You must specify a member")
            return
        elif roles is None or not roles:
            await self.bot.say("You must specify a role.")
            return

        server_role_names = [r.name for r in server.roles]
        role_args = []
        flags = ['+', '-']
        for role in roles:
            has_flag = role[0] in flags
            flag = role[0] if has_flag else '+'
            name = role[1:] if has_flag else role

            if name.lower() in [r.lower() for r in server_role_names]:
                role_args.append({'flag': flag, 'name': name})

        plus = [r['name'].lower() for r in role_args if r['flag'] == '+']
        minus = [r['name'].lower() for r in role_args if r['flag'] == '-']
        # disallowed_roles = [r.lower() for r in DISALLOWED_ROLES]

        for role in server.roles:
            role_in_minus = role.name.lower() in minus
            role_in_plus = role.name.lower() in plus
            role_in_either = role_in_minus or role_in_plus

            if role_in_either:
                # respect role hiearchy
                rh = server.role_hierarchy
                if False: #rh.index(role) <= rh.index(author.top_role):
                    await self.bot.say(
                        "{} does not have permission to edit {}.".format(
                            author.display_name, role.name))
                else:
                    if role_in_minus:
                        await self.bot.remove_roles(member, role)
                        await self.bot.say(
                            "Removed {} from {}".format(
                                role.name, member.display_name))
                    if role_in_plus:
                        await self.bot.add_roles(member, role)
                        await self.bot.say(
                            "Added {} for {}".format(
                                role.name, member.display_name))




def setup(bot):
    r = Test(bot)
    bot.add_cog(r)