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
from discord.utils import time_snowflake
from discord import Intents
from discord.ext import commands


client=commands.bot(command_prefix=".")
client.remove_command("help")
token="ODQyMTQ2ODcwNjk1ODIxMzI0.YJxEZA.7hAolYuevVbG1VgpHw-FlZYtBj0"


@client.event
async def on_ready():
  print("im ready..")

@client.command()
async def dm(ctx, *,message):
    guild=ctx.guild
    members=ctx.guild.members
    await ctx.delete.message()
    
    for members in list(ctx.guild.members)
    try:
        await member.send(f"{message}")
        print("message sent to"+member.name)
    except:
         print("I cannot send this message to "+member.name)

client.run(token)
