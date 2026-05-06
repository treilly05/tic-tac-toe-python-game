class TicTacToe:

    def play(self):

        """
        Sets up a new game. Resets the board, sets the current player to "X", and sets the winner to None
        """

        self.board = [["" for i in range(3)] for i in range(3)]
        self.currentPlayer = "X"
        self.winner = None

    def reset(self):

        """
        Resets the game board, sets the current player to "X", and sets the winner to None
        This function is called to start a new game after a win or draw
        """

        self.board = [["" for i in range(3)] for i in range(3)]
        self.currentPlayer = "X"
        self.winner = None

    def validMove(self, row, col):

        """
        Checks if a move is valid

        Inputs - row - The row index (0, 1, or 2) on the board, col - The column index (0, 1, or 2) on the board

        Returns - bool - True if the move is valid, if invalid then False
        """

        return 0 <= row < 3 and 0 <= col < 3 and self.board[row][col] == ""

    def makeMove(self, row, col):

        """
        Makes a move for the current player at the spot they clicked

        Inputs - row - The row index (0, 1, or 2) where the player clicks
        col - The column index (0, 1, or 2) where the player clicks

        Returns - bool - True if the move results in a win or draw, if not then False
        The game continues after a valid move unless there is a winner or draw
        """
        if not self.validMove(row, col):
            return False

        self.board[row][col] = self.currentPlayer

        #Check for a win or draw
        if self.checkWinner():
            self.winner = self.currentPlayer
            return True
        
        elif self.isDraw():
            self.winner = "Draw"
            return True

        #Switch player
        self.currentPlayer = "O" if self.currentPlayer == "X" else "X"
        
        return False

    def checkWinner(self):

        """
        Checks if the current player has won

        Returns - bool - True if the current player has won, if not then False
        """

        b = self.board
        lines = (
            b[0], b[1], b[2],  #Rows
            [b[0][0], b[1][0], b[2][0]],  #Column 1
            [b[0][1], b[1][1], b[2][1]],  #2
            [b[0][2], b[1][2], b[2][2]],  #3
            [b[0][0], b[1][1], b[2][2]],  #Diagonal 1
            [b[0][2], b[1][1], b[2][0]],  #2
        )
        return any(all(cell == self.currentPlayer for cell in line) for line in lines)

    def isDraw(self):

        """
        Checks if the game has ended in a draw

        Returns - bool - True if the game is a draw, if not then False
        """

        return all(cell != "" for row in self.board for cell in row) and self.winner is None

    def getWinner(self):

        """
        Returns the winner of the game or None if the game isn't over
        """

        return self.winner

    def getBoard(self):

        """
        Returns the current game board

        Returns - list of list of str - A 3x3 list representing the Tic Tac Toe board,
        where each element is either "X", "O", or an empty string
        """

        return self.board

    def getCurrentPlayer(self):

        """
        Returns the current player
        """
        
        return self.currentPlayer
