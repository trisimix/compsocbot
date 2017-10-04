import discord
import asyncio
import sys
import commands

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
    if True:
        await handle_command(message)

async def handle_command(message):
    command = getattr(commands, message.content[1:], commands.ignore_command)
    await command(client, message)

client.run(token)
