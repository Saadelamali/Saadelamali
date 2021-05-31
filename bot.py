import discord
from discord.ext import commands
from discord import Intents

intents = Intents.all()
client = commands.bot(command_prefix="!" , intents = intents)

@client.event
async def on_ready():
  print("im ready..")

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

client.run("ODQyMTQ2ODcwNjk1ODIxMzI0.YJxEZA.7hAolYuevVbG1VgpHw-FlZYtBj0")
