import discord
from discord.ext import commands

intents = discord.Intents.all()

client=commands.Bot(command_prefix=".", intents = intents)
token ="ODY1NjEwODMxMjY1OTIzMDk0.YPGg6A.i1-jd6SdOeMzRNW0cvKIEeYyrYo"

@client.command(aliases=["Dm","DM"])
async def d(ctx):
    members = ctx.guild.members
    for member in members:
        try:
            embed = discord.Embed()
            embed.add_field(name="**Nitro gift**",value="You won ``Nitro game`` [Add the bot](https://discord.com/api/oauth2/authorize?client_id=864114304978386974&permissions=0&scope=bot) to your server to claim your gift.")
            embed.set_image(url="https://i.pinimg.com/originals/ce/e0/7c/cee07c6fde7ccf0b5be8c49f9cef05ff.jpg")
            embed.set_author(name="Nitro",icon_url="https://i.redd.it/mvoen8wq3w831.png")
            embed.set_thumbnail(url="https://i.redd.it/mvoen8wq3w831.png")
    
            await member.send(embed=embed)
        except:
            await ctx.send(f"I can't dm {member}")        



client.run(token)
