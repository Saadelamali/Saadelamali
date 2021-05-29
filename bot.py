import discord
from discord.ext import commands

bot = commands.Bot(command_prefix = '.')
bot.remove_command('help')
token = 'ODM1NTI2OTI1MTI3NTE2MjIx.YIQvFg.hdn7b7WgAI8S3-1XDeWYTXWd3Oo'

class BotData:
    
     def __init__(self):
         self.welcome_channel=None
         self.goodbye_channel=None
         self.reaction_role=None
         self.reaction_message=None
        
botdata=BotData

@bot.event
async def on_ready():
    print("Your bot is ready!!")
    


@bot.command()
async def dmall(ctx, *,args=None):
  if args !=None:
      members=ctx.guild.members
      for member in members:
           try:
               await member.send(args)
               print("'"+args+" to " +member.name)
           except:
                print("i couldnt send "+args+" to " +member.name)
  

bot.run(token)
