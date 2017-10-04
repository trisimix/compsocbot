import discord
import sys
import commands as cmd

if len(sys.argv) != 2:
    print('Usage: python3 main.py [token]')

token = sys.argv[1]

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
    command = getattr(commands, message.content.split()[0][1:], commands.ignore_command)
    await client.delete_message(message)
    await command(message)

client.run(token)
