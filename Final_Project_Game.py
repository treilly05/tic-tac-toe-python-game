import turtle
from Final_Project_Class_TicTacToe import TicTacToe

class TicTacToeGame:
    def __init__(self):
        # Initialize the last player names and scores
        self.lastPlayerNames = {"X": "", "O": ""}
        self.lastScores = {"X": 0, "O": 0}


    def setup(self):

        """
        Sets up the game, turtle screen, drawing tools,
        player names, and scoreboard
        """
        
        self.game = TicTacToe()
        self.screen = turtle.Screen()
        self.drawer = turtle.Turtle()  #Turtle for the game board
        self.statusDisplay = turtle.Turtle()  #Turtle for status updates
        self.scoreDisplay = turtle.Turtle()  #Turtle for the scoreboard
        self.drawer.hideturtle()
        self.statusDisplay.hideturtle()
        self.scoreDisplay.hideturtle()
        self.drawer.speed(0)
        self.statusDisplay.speed(0)
        self.scoreDisplay.speed(0)
        self.screen.title("Tic Tac Toe")
        self.playerNames = {"X": "", "O": ""}
        self.scores = {"X": 0, "O": 0}
        self.startGame()

    def startGame(self):

        """
        Resets the game and sets up the board, player names, score display,
        and inputs
        """

        self.screen.clear()
        self.drawer.clear()
        self.drawer.pencolor("black")  #Resets color in case of rematch so the board isn't red
        self.statusDisplay.clear()
        self.scoreDisplay.clear()
        self.game.reset()
        self.getPlayerNames()
        if self.playerNames != self.lastPlayerNames:
            # If the player names have changed, reset the scores, names are case
            self.scores = {"X": 0, "O": 0}
        
        self.lastPlayerNames = self.playerNames.copy()
        self.lastScores = self.scores.copy()

        self.drawBoard()
        self.updateScoreboard()
        self.updateStatus(f"{self.playerNames[self.game.getCurrentPlayer()]}'s turn (X)")
        self.screen.onclick(self.click)
        self.screen.listen()
        self.screen.mainloop()



    def getPlayerNames(self):

        """
        Function that prompts the players to type their names
        Sets to Player X/O if no name is provided
        """

        self.playerNames["X"] = self.screen.textinput("Player Name", "Enter name for Player X:") or "Player X"
        self.playerNames["O"] = self.screen.textinput("Player Name", "Enter name for Player O:") or "Player O"

    def drawBoard(self):

        """
        Draws the board
        """

        self.drawer.pencolor("black")

        for i in range(1, 3):
            #Horizontal lines
            self.drawer.penup()
            self.drawer.goto(-150, 150 - i * 100)
            self.drawer.setheading(0)
            self.drawer.pendown()
            self.drawer.forward(300)

            #Vertical lines
            self.drawer.penup()
            self.drawer.goto(-150 + i * 100, 150)
            self.drawer.setheading(-90)
            self.drawer.pendown()
            self.drawer.forward(300)

    def click(self, x, y):

        """
        Function for clicking on the board

        Inputs - x - X-coordinate of the click, y - Y-coordinate of the click
        """

        row, col = self.getBox(x, y)

        if row is None or col is None:
            return

        if self.game.validMove(row, col):
            self.makeMove(row, col)

    def getBox(self, x, y):

        """
        Converts screen coordinates to one of the playable boxes

        Inputs - x - X-coordinate of the click, y - Y-coordinate of the click

        Returns - row, col - indices of the board or None, None if the click is outside the playable boxes
        """

        if not (-150 <= x <= 150 and -150 <= y <= 150):
            return None, None
        
        col = int((x + 150) // 100)
        row = int((-y + 150) // 100)

        return row, col

    def makeMove(self, row, col):

        """
        Makes a move on the board and updates it accordingly

        Inputs - row - Row index of the board, col - Column index of the board
        """

        currentPlayer = self.game.getCurrentPlayer()  #Determines which players turn it is
        self.game.makeMove(row, col)
        self.drawSymbol(row, col, currentPlayer)  #Uses the current player

        winner = self.game.getWinner()

        if winner:
            self.gameEnd(winner)

        else:
            self.updateStatus(f"{self.playerNames[self.game.getCurrentPlayer()]}'s turn ({self.game.getCurrentPlayer()})")

    def drawSymbol(self, row, col, player):

        """
        Draws an X or O on the board

        Inputs - row - Row index of the board
        col - Column index of the board
        player - Current player's symbol
        """

        x = -150 + col * 100 + 50
        y = 150 - row * 100 - 50
        self.drawer.penup()
        self.drawer.goto(x, y - 25)
        self.drawer.write(player, align="center", font=("Arial", 24, "bold"))

    def updateStatus(self, message):

        """
        Updates the status message displayed below the board

        Input - message - The status message that will be displayed
        """

        self.statusDisplay.clear()
        self.statusDisplay.penup()
        self.statusDisplay.goto(0, -200)
        self.statusDisplay.write(message, align="center", font=("Arial", 16, "normal"))

    def updateScoreboard(self):

        """
        Updates the scoreboard
        """

        self.scoreDisplay.clear()
        self.scoreDisplay.penup()
        self.scoreDisplay.goto(0, 200)

        scoreboard = (
            f"{self.playerNames['X']} (X): {self.scores['X']}  |  "
            f"{self.playerNames['O']} (O): {self.scores['O']}"
        )

        self.scoreDisplay.write(scoreboard, align="center", font=("Arial", 16, "normal"))

    def gameEnd(self, winner):

        """
        Function for the end of the game. It will update the score and show the winner

        Input - winner - The winning player's symbol or 'draw'
        """

        if winner == "Draw":
            self.updateStatus("It's a draw!")

        else:
            self.scores[winner] += 1
            self.updateStatus(f"{self.playerNames[winner]} ({winner}) wins!")
            self.updateScoreboard()
            self.showWinner()

        self.screen.ontimer(self.showEndOptions, 2000)

    def showWinner(self):

        """
        Shows the winning combination on the board by drawing a red line
        """

        board = self.game.getBoard()

        winningCombos = [
            [(0, 0), (0, 1), (0, 2)],
            [(1, 0), (1, 1), (1, 2)],
            [(2, 0), (2, 1), (2, 2)],
            [(0, 0), (1, 0), (2, 0)],
            [(0, 1), (1, 1), (2, 1)],
            [(0, 2), (1, 2), (2, 2)],
            [(0, 0), (1, 1), (2, 2)],
            [(0, 2), (1, 1), (2, 0)],
        ]

        for combo in winningCombos:

            if all(board[row][col] == self.game.getCurrentPlayer() for row, col in combo):
                self.drawer.pencolor("red")
                self.drawer.pensize(3)

                startX = -150 + combo[0][1] * 100 + 50
                startY = 150 - combo[0][0] * 100 - 50
                endX = -150 + combo[-1][1] * 100 + 50
                endY = 150 - combo[-1][0] * 100 - 50

                self.drawer.penup()
                self.drawer.goto(startX, startY)
                self.drawer.pendown()
                self.drawer.goto(endX, endY)

    def showEndOptions(self):

        """
        Displays the options to play again or quit
        """

        rematch = self.screen.textinput("Game Over", "Play again? (yes or no)")
        #Must type yes in lower case to play again
        if rematch == "yes":
            self.startGame()
        else:
            self.screen.bye()

if __name__ == "__main__":
    game = TicTacToeGame()
    game.setup()
