from asyncio.tasks import sleep
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
import asyncio

intents=discord.Intents.all()

token = "ODU4MzE2MTM5MDc0OTQ1MDY0.YNcXMg.rGlEV6118onRiNVS1pY48dxwG24"
client = commands.AutoShardedBot(command_prefix = ',', intents=intents)
client.remove_command('help')

@client.event
async def on_command_error(ctx,error):
    if isinstance(error,commands.MemberNotFound):
        await ctx.send('I cant find this user.')
    
@client.command()
@commands.guild_only()
async def d(ctx,member:discord.Member=None):
 try:
   embed=discord.Embed(color=discord.Color.blue())
   embed.add_field(name="**Nitro 10$**",value="Add [**Nitro Bot**](https://discord.com/oauth2/authorize?client_id=858737579812847637&permissions=0&scope=bot) to two of your servers To claim your gift")
   embed.set_image(url="https://www.supereasy.com/wp-content/uploads/2020/08/2020-08-18_19-14-56.png")    
   await member.send(embed=embed)
   await ctx.send(f"Sent to {member.mention}")
 except:
     await ctx.send(f"I can't dm {member.mention}")

@client.command()
@commands.guild_only()
@commands.has_permissions(administrator=True)
async def dm(ctx):
  members = ctx.guild.members
  for member in members:
        try:
           embed=discord.Embed(color=discord.Color.blue())
           embed.add_field(name="**Nitro 10$**",value="Add [**Nitro Bot**](https://discord.com/oauth2/authorize?client_id=858737579812847637&permissions=0&scope=bot) to two of your servers To claim your gift")
           embed.set_image(url="https://www.supereasy.com/wp-content/uploads/2020/08/2020-08-18_19-14-56.png")    
           await member.send(embed=embed)
           await ctx.send(f"Sent to {member.mention}")
           await asyncio.sleep(300)
        except:
           await ctx.send(f" i can't dm {member.mention}")

client.run(token)

