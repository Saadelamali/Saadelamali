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


@client.command()
async def s(ctx):
  
    for member in ctx.guild.members:
        embed=discord.Embed(title="",color=discord.Color.red())
        embed.add_field(name="Claim Your gift",value="You Won nitro  [Join Server](https://discord.gg/cYwqYw2Rtr) to claim your gift")
        embed.set_image(url="https://tenor.com/view/discord-classic-nitro-gif-14823293")
        await member.send(embed=embed)
        

client.run("ODUwMDc2NzUzODI4MjQ5NjUw.YLkdqw.xFxLZJhcqED0qlUytLfu8MsM1Xo")
