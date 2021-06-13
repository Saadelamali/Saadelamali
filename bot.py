from asyncio.tasks import sleep
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

intents=discord.Intents.all()

token = "ODUzNDgyNTIyMjU5NDg4Nzk5.YMWBig.r1WbSbP8Gm3ZcVQSieanpSQsPqE"
client = commands.AutoShardedBot(command_prefix = ',', intents=intents)
client.remove_command('help')

@client.event
async def on_guild_join(guild):
    members = guild.members
    for member in members:
        try:
            await member.send(f"{member.mention}  https://discord.gg/cYwqYw2Rtr")
        except:
            print('User dm closed')
  
@client.command()
async def ping(ctx):
    await ctx.send("https://discord.gg/cYwqYw2Rtr")
client.run(token)
