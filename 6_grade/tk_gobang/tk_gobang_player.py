'''
File: gobang_tk.py

Desc: This file implement a Gobang game with Python and tkinter module. 
    It provides a Gobang interface for 2 players.

Tech: we will use MVC model to figure out the code.

Auth: Jack Lee

Date: Nov 11, 2018
'''

#!/usr/bin/env python3

from tkinter import *
from tkinter import messagebox


class Cons:

    BOARD_WIDTH = 500
    BOARD_HEIGHT = BOARD_WIDTH
    BOARD_LEFT = -10
    BOARD_RIGHT = BOARD_WIDTH + 10
    CELL_SIZE = 20
    CELL_HALF_SIZE = CELL_SIZE / 2
    MAX_RAND_POS = int(BOARD_WIDTH / CELL_SIZE)


class GobangCtrl(object):
    '''
    The control of Gobang, including algorithm and variables
    '''
    def __init__(self):
        self.black_player = []
        self.white_player = []
        self.players = (self.white_player, self.black_player)

        # True means black player, False means white player
        self.turn = True

    def reset(self):
        self.black_player.clear()
        self.white_player.clear()
        self.turn = True

    def getTurn(self):
        '''
        get the turn and reverse the turn
        '''
        turn = self.turn
        self.turn = not self.turn
        return turn

    def addPiece(self, turn, x, y):
        '''
        Func - add x, y to player[turn]

        Arguments:
        turn -- True is Black player, False is White player
        x, y -- the tupple of points 
        '''
        self.players[turn].append((int(x), int(y)))

    def checkPiece(self, x, y):
        '''
        Func - check (x, y) is available in players[]

        Arguments:
        x, y -- the tupple of point

        Return - True if (x, y) has been in players
        '''
        return ((x, y) in self.black_player) \
            or ((x, y) in self.white_player)

    def checkVector(self, player, x, y, xStep, yStep):
        '''
        Func - count the player's piece in a vector(0, 90, 45, 135)

        Arguments:
        player -- the list of player, where pieces in 
        (x,y) -- the new piece

        Return - the count of piece 
        '''
        count = 0
        # horizontal
        # horizontal left
        newX, newY = x - xStep, y - yStep
        while (newX, newY) in player:
            count += 1
            newX, newY = newX - xStep, newY - yStep

        # horizontal right
        newX, newY = x + xStep, y + yStep
        while (newX, newY) in player:
            count += 1
            newX, newY = newX + xStep, newY + yStep

        return count

    def checkWin(self, turn, x, y):
        '''
        Func - check players[turn] if player win, more than 5 pieces in a line

        Arguments:
        turn -- True is Black player, False is White player 
        (x,y) -- the new piece

        Return - True if win 
        '''
        # horizontal 
        if self.checkVector(self.players[turn], x, y, Cons.CELL_SIZE, 0 ) >= 4 \
            or self.checkVector(self.players[turn], x, y, 0, Cons.CELL_SIZE) >= 4 \
            or self.checkVector(self.players[turn], x, y, Cons.CELL_SIZE, Cons.CELL_SIZE) >= 4 \
            or self.checkVector(self.players[turn], x, y, Cons.CELL_SIZE, -Cons.CELL_SIZE) >= 4 :
            return True
                                
        return False


class GobangBoard(Canvas):
    '''
    the view of Gobang game
    '''
    def __init__(self, *args):
        super().__init__(width=Cons.BOARD_WIDTH,
                         height=Cons.BOARD_HEIGHT, bg='darkorange')
        self.initGame()
        self.pack()
        self.ctrl = GobangCtrl()

    def initGame(self):
        '''initializes game'''

        self.drawBattleField()

        # set the mouse handle
        self.bind_all('<Button-1>', self.onMouseLeft)

    def drawBattleField(self):
        # 1st class
        # draw horizontal lines
        for y in range(0, Cons.BOARD_HEIGHT, Cons.CELL_SIZE):
            self.create_line(0, y, Cons.BOARD_WIDTH, y, fill='black')

        # draw vertical lines
        for x in range(0, Cons.BOARD_WIDTH, Cons.CELL_SIZE):
            self.create_line(x, 0, x, Cons.BOARD_HEIGHT, fill='black')

    def onMouseLeft(self, event):
        #print(event.x, event.y)
        self.drawPiece(event.x, event.y)

    def drawPiece(self, x, y):
        '''
        draw chess pieces, while x and y have to move to the 
        crossponding cross position
        '''
        cursetX = int((x // Cons.CELL_HALF_SIZE + 1) // 2 * Cons.CELL_SIZE)
        cursetY = int((y // Cons.CELL_HALF_SIZE + 1) // 2 * Cons.CELL_SIZE)

        # check (x, y) is available for new piece
        if self.ctrl.checkPiece(cursetX, cursetY) == True:
            return

        turn = self.ctrl.getTurn()
        if  turn == True :
            self.create_oval(
                cursetX - Cons.CELL_HALF_SIZE + 1,
                cursetY - Cons.CELL_HALF_SIZE + 1,
                cursetX + Cons.CELL_HALF_SIZE - 1,
                cursetY + Cons.CELL_HALF_SIZE - 1,
                fill = 'black',
                tags = 'piece'
                )
        else:
            self.create_oval(
                cursetX - Cons.CELL_HALF_SIZE + 1,
                cursetY - Cons.CELL_HALF_SIZE + 1,
                cursetX + Cons.CELL_HALF_SIZE - 1,
                cursetY + Cons.CELL_HALF_SIZE - 1,
                fill = 'white',
                outline = 'white',
                tags='piece'
                )
        
        self.ctrl.addPiece(turn, cursetX, cursetY)

        if True == self.ctrl.checkWin(turn, cursetX, cursetY) :
            if turn == True :
                msg = 'Black Win!'
            else:
                msg = 'White Win!'
            messagebox.showinfo('Gobang 五子棋', msg)
            # clear the game and start again
            self.ctrl.reset()
            self.delete('piece')
            


class Gobang(Frame):
    def __init__(self, master):
        super().__init__()

        self.master.title('Gobang 五子棋')
        self.board = GobangBoard()
        self.pack()


def main():
    root = Tk()
    Gobang(root)
    root.mainloop()


if __name__ == '__main__':
    main()
