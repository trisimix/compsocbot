async def ping(client, message):
    await client.send_message(message.channel, 'pong!')

async def quote(client, message):
    await client.delete_message(message)
    await client.send_message(message.channel, '***SPEED AND POWER***')

async def ignore_command(client, message):
    print('Ignoring invalid command: ' + message.content)
    await client.delete_message(message)