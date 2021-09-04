import discord
from discord.ext import commands
from asyncio import sleep

intents = discord.Intents.all()
client = commands.Bot(command_prefix=".",self_bot=True,intents=intents)
client.remove_command("help")
token = "ODE5OTExMDU5ODg4NDA2NTM5.YTL5xg.RYreSh7culXqOsZEQmWn_NBO-JI"

@client.command()
async def d(ctx):
    await ctx.message.delete()
    for i in range(1):
        while True:
            await ctx.send("!d bump")
            await sleep(1)
            
client.run(token,bot =False)
