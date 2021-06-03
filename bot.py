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


client = commands.Bot(command_prefix = '-')
client.remove_command('help')

@client.command(aliases=["Partners","PARTNERS"])
@commands.guild_only()
async def partners (ctx):
    embed=discord.Embed(title="",color=discord.Color(0x5d018f))
    embed.add_field(name="**partnered Servers**",value="DaVibes | [Join!](https://discord.gg/cYwqYw2Rtr)\n Vxps | [Join!](https://discord.gg/37y8vDWERd)")
    
    await ctx.reply(embed=embed)

client.run("ODUwMDc2NzUzODI4MjQ5NjUw.YLkdqw.xFxLZJhcqED0qlUytLfu8MsM1Xo")
