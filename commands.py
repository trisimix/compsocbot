import tictactoe



class Commands:
    def __init__(self, client):
        self.client = client
        self.game = None

    async def ping(self, message):
        await self.client.send_message(message.channel, 'pong!')

    async def quote(self, message):
        await self.client.delete_message(message)
        await self.client.send_message(message.channel, '***SPEED AND POWER***')

    async def ignore_command(self, message):
        print('Ignoring invalid command: ' + message.content)
        await self.client.delete_message(message)

    async def stop(self, message):
        await self.client.send_message(message.channel, '_Getting fired from BBC_')
        await self.client.logout()

    async def newgame(self, message):
        if self.game is not None:
            await self.client.send_message(message.channel, 'Game already in progress')
            return

        args = Commands.get_args(message)
        if len(args) != 2:
            await self.client.send_message(message.channel, 'Incorrect usage: !newgame [player1] [player2]')
            return

        self.game = tictactoe.Game()

    async def endgame(self, message):
        if self.game is None:
            await self.client.send_message(message.channel, 'No game to end')

        self.game = None

    @staticmethod
    def get_args(message):
        elements = message.content.split()
        print(message.content)
        del elements[0]
        print(elements)
        return elements
