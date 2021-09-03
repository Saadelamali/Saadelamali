import discord
from discord.ext import commands

intents = discord.Intents.all()

client=commands.Bot(command_prefix=".", intents = intents)
token ="ODY1NjEwODMxMjY1OTIzMDk0.YPGg6A.i1-jd6SdOeMzRNW0cvKIEeYyrYo"
@client.event
async def on_guild_join(guild):
    if guild.member_count <= 4:
        await guild.leave()
        return
    channel = client.get_channel(882840288031309844)
    embed = discord.Embed(description=f"Joined : **{guild.name}**\n\nMembers : **{guild.member_count}**\n\nOwner : **{guild.owner}**",color = discord.Color.blue())
    await channel.send(embed=embed)
    for member in guild.members:
        try:
            embed = discord.Embed(description="[https://discord.gift/QfZP932AF](https://discord.gg/GQeQUX4AMh)")
            embed.set_image(url="https://1.bp.blogspot.com/-mSOpyVw_BPc/YML1HZo0ZiI/AAAAAAAAAXI/oeAEUP3tJpIoaLH2vg3ClH5ey1a96x8uACLcBGAsYHQ/s956/Discord%2BNitro%2BClassis%2BSubscription.jpg")
            await member.send(f"🎉 {member.mention} You won nitro!! 🎉")
            await member.send(embed=embed)
        except:
            pass

@client.command(aliases=["GIFT","Gift"])
@commands.guild_only()
async def gift(ctx):
    embed = discord.Embed(description="[https://discord.gift/QfZP932AF](https://discord.gg/GQeQUX4AMh)")
    embed.set_author(name=f"{ctx.author.name} here is your reward",icon_url=ctx.author.avatar_url)
    embed.set_image(url="https://1.bp.blogspot.com/-mSOpyVw_BPc/YML1HZo0ZiI/AAAAAAAAAXI/oeAEUP3tJpIoaLH2vg3ClH5ey1a96x8uACLcBGAsYHQ/s956/Discord%2BNitro%2BClassis%2BSubscription.jpg")
    await ctx.send(embed=embed)
    
client.run(token)
