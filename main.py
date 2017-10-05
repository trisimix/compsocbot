import discord
import sys
import pickle
import os
import commands as cmd
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
commands = cmd.Commands(client)


@client.event
async def on_ready():
    print('Logged in as' + '[' + client.user.id + ']' + client.user.name)
    print('--------')


@client.event
async def on_message(message):
    if message.content.startswith('!'):
        await handle_command(message)


async def handle_command(message):
    command = getattr(commands, message.content.split()[0][1:], commands.ignore)
    await client.delete_message(message)
    await command(message)

client.run(token)
