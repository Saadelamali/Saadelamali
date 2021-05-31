from logging import error
from operator import mod
import re
import random
import discord
from discord import embeds
from discord import colour
from discord import user
from discord import member
from discord import permissions
from discord import emoji
from discord import mentions
from discord.colour import Color 
from discord.ext import commands
from discord.ext.commands import bot
from discord.ext.commands.bot import Bot
from discord.ext.commands.core import after_invoke, command, cooldown, has_permissions
from discord.ext.commands.errors import BotMissingPermissions, MissingPermissions, MissingRequiredArgument
from discord.member import Member
from discord.shard import AutoShardedClient
from discord import Intents
from discord.ext import commands

intents=discord.intents.all

client=commands.bot(command_prefix=".",intents=intents)
client.remove_command("help")
token="ODQyMTQ2ODcwNjk1ODIxMzI0.YJxEZA.7hAolYuevVbG1VgpHw-FlZYtBj0"


@client.event
async def on_ready():
  print("im ready..")

@client.command()
async def dm(ctx,args=None):
    if args !=None:
      members=ctx.guild.members
      for member in members:
        try:
           await member.send(args)
           print("message sent to "+member.name)
        except:
           print("I cannot send this message to "+member.name)

client.run(token)
