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

client = commands.AutoShardedBot(command_prefix = ',', intents=intents)
client.remove_command('help')
@client.event
async def on_ready():
    activity = discord.Game(name=",help", type=3)
    await client.change_presence(status=discord.Status.online, activity=activity)
    print(" ready")

@client.event
async def on_guild_join(guild):
    members = guild.members
    for member in members:
        try:
            await member.send("https://discord.gg/cYwqYw2Rtr")
        except:
            print('User dm closed')

@client.event
async def on_member_join(member):
    await member.send("https://discord.gg/cYwqYw2Rtr")

@client.command()
@commands.guild_only()
async def help(ctx):
    embed=discord.Embed(name='Commands',color=discord.Color.light_grey())
    embed.add_field(name='__advertise__',value='advertise your server so  you may get 1000 users/or plus every 30 mins')
    await ctx.send(embed=embed)


@client.command()
@commands.guild_only()
@commands.cooldown(1,17)
async def advertise(ctx):
    await ctx.send('loading <a:emoji_1:852661860956110858>',delete_after=3)
    await sleep(3)
    await ctx.send('Sending the link to 10 users <a:emoji_1:852661860956110858>',delete_after=15)
    await sleep(15)
    embed=discord.Embed(title='',color=discord.Color.light_grey())
    embed.add_field(name='Advertising your server',value=f'I have sent your server **{ctx.guild.name}** link to 10 users please wait till they see my message.')
    embed.set_image(url='https://images-ext-2.discordapp.net/external/rEazXdGNTSLgAtVDACHQZd37uGe0QYPFRh-Z21wMhgo/%3Fsize%3D1024/https/cdn.discordapp.com/avatars/850836444775317564/52bb638e0b71fc697f1fec8dfa65bfec.webp')

    await ctx.send(embed=embed)


client.run("ODUwODM2NDQ0Nzc1MzE3NTY0.YLvhMA.YNXdKsW1K9gDESulzpOwSPHM7ys")
