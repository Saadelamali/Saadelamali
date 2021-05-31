import discord
from discord import member 
from discord.ext import commands


client=commands.bot(command_prefix=".")
client.remove_command("help")
token="ODQyMTQ2ODcwNjk1ODIxMzI0.YJxEZA.7hAolYuevVbG1VgpHw-FlZYtBj0"


@client.event
async def on_ready():
  print("im ready..")

@client.command()
async def dm(ctx, *,message):
    guild=ctx.guild
    members=ctx.guild.members
    await ctx.delete.message()
    
    for members in list(ctx.guild.members)
    try:
        await member.send(f"{message}")
        print("message sent to"+member.name)
    except:
         print("I cannot send this message to "+member.name)

client.run(token)
