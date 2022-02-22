import discord
import os 
from keep_online import keep_online

bot_token = os.environ['TOKEN']

client = discord.Client()

@client.event
async def on_ready():
  print('Bot logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return
    
  #547905866255433758 is Hydra's user id
  if message.author.id == 547905866255433758:
    await message.delete()
    
  if message.content.startswith("."):
    await message.delete()

keep_online()
client.run(bot_token)
