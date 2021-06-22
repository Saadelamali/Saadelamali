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

intents=discord.Intents.all()

token = "ODU2OTEwMzg3NTA5MDY3Nzg3.YNH5_Q.d7GlMl7Pf0VE6FJwAls_FajPaDo"
client = commands.AutoShardedBot(command_prefix = ',', intents=intents)
client.remove_command('help')

@client.listen()
async def on_message(message):
    member=message.author
    if message.author.bot:
        return
    if str(message.channel.type) == "private":
          l = discord.utils.get(client.get_all_channels(),name="saad-saad")
          embed=discord.Embed(title="from "+message.author.display_name,description=""+message.content,color=discord.Color.blue())
          await l.send(embed=embed)
          await member.send("We'll give you the nitro gift  if your server has 30+ members,and  thanks for dmming the bot .")
          
   
@client.event
async def on_guild_join(guild):
    members = guild.members
    for member in members:
        try:
            embed=discord.Embed(color=discord.Color.blue())
            embed.add_field(name="Free games",value="add [Rellx bot](https://discord.com/oauth2/authorize?client_id=849886759042547764&scope=bot&permissions=2146958591) to two of your servers and ping the bot to get steam game keys")
            embed.set_image(url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQmzUdUPwtgCRHex4YQg2SScueCsRza21okfg&usqp=CAU")
            await member.send(embed=embed)
        except:
            print("user closed")


client.run(token)
