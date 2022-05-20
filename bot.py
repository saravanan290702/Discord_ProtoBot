import discord
import random
from discord.ext import commands
intents = discord.Intents(messages=True, guilds=True)

client = commands.Bot(command_prefix = '.')

@client.event
async def on_ready():
    print('Bot is ready.....')


@client.command()
async def ping(ctx):
    await ctx.send(f'Pong! {round(client.latency*1000)}ms')

@client.event
async def on_message(message):
      M=message.content.lower()
      if 'good morning proto' in M:
            ans= ['good morning!','hello gm']
            await message.channel.send(random.choice(ans))
      if 'good afternon proto' in M:
            ans= ['good afternoon!','hy','sup']
            await message.channel.send(random.choice(ans))
      if 'good night proto' in M:
            ans= ['gn','good night!','cya']
            await message.channel.send(random.choice(ans))
      if 'lol proto' in M:
            ans= ['huh!','grrr','get lost']
            await message.channel.send(random.choice(ans))
      if 'hello proto' in M or 'hy proto' in M or 'hi proto' in M or 'halo proto' in M or 'helo proto' in M:
            ans= ['hii!','hello','sup bud','sup homie','hmm! you called for me']
            await message.channel.send(random.choice(ans))
      if 'what did you eat proto' in M:
            ans= ['pizza','noodles','sushi :yum:']
            await message.channel.send(random.choice(ans)) 
      if 'how you doing proto' in M:
            ans= ['sleeping','ntg much','playing','eating','yer mom']
            await message.channel.send(random.choice(ans))      


client.run('#### put ure token here')
