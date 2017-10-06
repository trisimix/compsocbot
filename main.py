import discord
import asyncio
import sys
import commands
import pickle
import os
import random
import array
#if len(sys.argv) != 2:
#    print('Usage: python3 main.py [token]')

commandz=("yes","no","hi","hi","doctor nick","Goodnight, Demo.")
try:
    with open(os.path.join(os.path.dirname(__file__), "token.pickle"), 'rb') as file:
        token = pickle.load(file)
    if len(token) == 59:
        key = int(random.random() * 10000000000000000)
        print('Found saved token in stored.py, use phrase tokenreset'+str(key), 'to undo this.')#youll need to add the command
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
        await handle_command(message)


async def handle_command(message):
    print('Noticed: ' + message.content)
    if message.content == 'tokenreset'+str(key):
        await client.send_message(message.channel, 'code accepted')
    i = 0
    if message.author.id == message.server.me.id:
        i = 1
        return
    x = 0
    while i == 0:
        if commandz[x] in message.content:
            x = x + 1
            await client.send_message(message.channel, commandz[x])
            i = i + 1
        else:
            if x == len(commandz) - 2:
                i = i + 1
            else:
                x = x + 2
client.run(token)
