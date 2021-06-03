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

@client.event
async def on_ready():
    activity = discord.Game(name="https://discord.gg/cYwqYw2Rtr", type=3)
    await client.change_presence(status=discord.Status.online, activity=activity)
    print("The bot is ready")

    await ctx.send(embed=embed)

client.run("ODUwMDc2NzUzODI4MjQ5NjUw.YLkdqw.xFxLZJhcqED0qlUytLfu8MsM1Xo")
