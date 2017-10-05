import discord
import asyncio
import sys
import commands
import pickle
import os
#if len(sys.argv) != 2:
#    print('Usage: python3 main.py [token]')
try:
    with open(os.path.join(os.path.dirname(__file__), "token.pickle"), 'rb') as file:
        token = pickle.load(file)
    if len(token) == 59:
        print('Found saved token in stored.py, use command tokenreset to undo this.')#youll need to add the command
    else:
        raise
except:
    #code tokenreset with admin permissions
    token = input('What is your Discord bot token? (found on Discord developer page): ')
    with open(os.path.join(os.path.dirname(__file__), "token.pickle"), 'wb') as file:
        pickle.dump(token, file)
client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as' + '[' + client.user.id + ']' + client.user.name)
    print('--------')

@client.event
async def on_message(message):
    if message.content.startswith('!'):
        await handle_command(message)

async def handle_command(message):
    command = getattr(commands, message.content[1:], commands.ignore_command)
    await command(client, message)

client.run(token)
