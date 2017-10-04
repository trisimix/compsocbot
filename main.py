import discord
import asyncio
import sys

if len(sys.argv) != 2:
    print('Usage: python3 main.py [token]')

token = sys.argv[1]

client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as' + '[' + client.user.id + ']' + client.user.name)
    print('--------')

@client.event
async def on_message(message):
    if message.content.startswith('!ping'):
        await client.send_message(message.channel, 'Pong!')

client.run(token)