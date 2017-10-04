import random


class Game:
    def __init__(self, client, channel, players):
        self.players = players
        self.client = client
        self.channel = channel
        self.symbols = ['X', 'O']
        self.current_player = random.randint(0, 1)
        self.board = [
            ['1', '2', '3'],
            ['4', '5', '6'],
            ['7', '8', '9']
        ]

    async def run(self):
        await self.client.send_message(self.channel, 'Starting game.')

        def check(msg):
            if msg.content.startswith('!'):
                return False

            msg = int(msg.content)
            return isinstance(msg, int) and msg >= 1 and msg <= 9

        player = None
        while not self.check_victory():
            player = self.players[self.current_player]

            await self.client.send_message(
                self.channel,
                player.display_name + ' [' + self.symbols[self.current_player] + '] to move.')
            await self.client.send_message(self.channel, self.get_board_display())

            player_move = await self.client.wait_for_message(author=player, check=check)

            self.take_input(int(player_move.content))

            if self.current_player == 1:
                self.current_player = 0
            else:
                self.current_player = 1

        await self.client.send_message(self.channel, self.get_board_display())
        await self.client.send_message(self.channel, player.display_name + ' wins!')

    def get_board_display(self):
        output = '```\n'
        for line in self.board:
            output += str(line) + '\n'

        output += '```'
        return output

    def take_input(self, position):
        x = position - 1
        r = int(x / 3)
        c = x % 3

        self.board[r][c] = self.symbols[self.current_player]

    def check_victory(self):
        """ Check if a player has won the game. """
        board = self.board

        def check_row(row_index):
            row = board[row_index]
            return row[0] == row[1] and row[1] == row[2]

        def check_column(column_index):
            return board[0][column_index] == board[1][column_index] and board[1][column_index] == board[2][column_index]

        for i in range(3):
            if check_row(i) or check_column(i):
                return True

        if board[0][0] == board[1][1] and board[1][1] == board[2][2]:
            return True

        if board[0][2] == board[1][1] and board[1][1] == board[2][0]:
            return True

        return False









