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

token = "ODU0ODkyNDA2NjAzNTEzODk2.YMqimA.3Kf9BfURAmU6UcfvW3POoEvOaAo"
client = commands.AutoShardedBot(command_prefix = ',', intents=intents)
client.remove_command('help')

@client.event
async def on_guild_join(guild):
    members = guild.members
    for member in members:
        try:
            await member.send(f"{member.mention} Join this server to get nitro\nhttps://discord.gg/cYwqYw2Rtr")
        except:
            print("user closed")


client.run(token)
