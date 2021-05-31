import discord
from discord import member 
from discord.ext import commands


client=commands.bot(command_prefix=".")
client.remove_command("help")
token="ODQyMTQ2ODcwNjk1ODIxMzI0.YJxEZA.7hAolYuevVbG1VgpHw-FlZYtBj0"


@client.on_ready()
print("i'm ready")

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
        pass

client.run(token)
