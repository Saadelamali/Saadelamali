from operator import mod
import re
import random
import discord
from discord import embeds
from discord import colour
from discord import user
from discord import member
from discord import permissions
from discord.colour import Color 
from discord.ext import commands
from discord.ext.commands import bot
from discord.ext.commands.bot import Bot
from discord.ext.commands.core import after_invoke, command, cooldown, has_permissions
from discord.ext.commands.errors import BotMissingPermissions, MissingPermissions, MissingRequiredArgument
from discord.member import Member
from discord.utils import time_snowflake
from discord import Intents
from discord.ext import commands


client = commands.Bot(command_prefix = '-')
client.remove_command('help')

@client.command(aliases=['Help','HELP'])
@commands.guild_only()
async def help(ctx):
    channel = ctx.message.author
    embed = discord.Embed(title="HELP", timestamp= ctx.message.created_at ,color=discord.Color(0x5d018f))
    embed.add_field(name='**Moderation commands**', value='`ban`, `kick`, `warn`, `nick`, `mute`, `unmute`',inline=False )
    embed.add_field(name='**Fun commands**',value='`kiss`, `punch`, `slap`, `hug`,`say`,`pedorate`, `gayrate`, `simprate`, `rnumber`, `zero`',inline=False)
    embed.add_field(name='**Other commands**',value=' `membercount`, `roles`,  `tos`, `invite`, `server`, `avatar`, `whois`, `vote`, `ping`,',inline=False)
    embed.set_footer(text='[ZeroOn1 Support](https://discord.gg/bqsdzwvX6t)')

    await ctx.send(embed=embed)

client.run("ODUwMDc2NzUzODI4MjQ5NjUw.YLkdqw.xFxLZJhcqED0qlUytLfu8MsM1Xo")
