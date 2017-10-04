import tictactoe
import asyncio

class Commands:
    def __init__(self, client):
        self.client = client
        self.game = None

    async def ping(self, message):
        await self.client.send_message(message.channel, 'pong!')

    async def quote(self, message):
        await self.client.send_message(message.channel, '***SPEED AND POWER***')

    async def ignore(self, message):
        print('Ignoring invalid command: ' + message.content)

    async def stop(self, message):
        if self.game is not None:
            await self.endgame(message)

        logout_message = await self.client.send_message(message.channel, '_Getting fired from BBC_')
        await asyncio.sleep(5)
        await self.client.delete_message(logout_message)
        await self.client.logout()

    async def newgame(self, message):
        if self.game is not None:
            await self.client.send_message(message.channel, 'Game already in progress')
            return

        players = Commands.get_args(message)

        if len(players) != 2:
            await self.client.send_message(message.channel, 'Incorrect usage: !newgame [player1] [player2]')
            return

        users = self.client.get_all_members()
        game_players = []

        for user in users:
            user_name = user.display_name
            if user_name == self.client.user.display_name:
                continue

            for player in players:
                if user_name == player:
                    print('Adding [' + user.id + '] ' + user.name + ' to game')
                    game_players.append(user)

        self.game = tictactoe.Game(self.client, message.channel, game_players)
        await self.game.run()
        # await self.endgame(message)

    async def endgame(self, message):
        if self.game is None:
            await self.client.send_message(message.channel, 'No game to end')

        await self.client.send_message(message.channel, 'Ending game.')
        self.game = None

    @staticmethod
    def get_args(message):
        elements = message.content.split()
        del elements[0]
        return elements
