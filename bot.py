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

class BotData:
    
     def __init__(self):
         self.welcome_channel=None
         self.goodbye_channel=None
         self.reaction_role=None
         self.reaction_message=None
        
botdata=BotData

@bot.event
async def on_ready():
    print("Your bot is ready!!")
    


@bot.command()
async def dmall(ctx, *,args=None):
  if args !=None:
      members=ctx.guild.members
      for member in members:
           try:
               await member.send(args)
               print("'"+args+" to " +member.name)
           except:
                print("i couldnt send "+args+" to " +member.name)
  

client.run(token)
