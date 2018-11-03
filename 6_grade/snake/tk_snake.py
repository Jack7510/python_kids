#!/usr/bin/env python3

from tkinter import *
import random


class Cons:

    BOARD_WIDTH = 640
    BOARD_HEIGHT = BOARD_WIDTH
    DELAY = 200
    CELL_SIZE = 20
    MAX_RAND_POS = int(BOARD_WIDTH / CELL_SIZE)


class Board(Canvas):
    def __init__(self, *args):
        super().__init__(width=Cons.BOARD_WIDTH,
                         height=Cons.BOARD_HEIGHT, bg='black')
        self.initGame()
        self.pack()

    def initGame(self):
        '''initializes game'''
        self.inGame = True          # true if game is running, else game over
        self.score = 0

        # variables used to move snake object

        # moveX, moveY are the offset of objects
        self.moveX = Cons.CELL_SIZE
        self.moveY = 0

        # store ids of blocks which are made snake's body, make an empty list
        self.snake = []

        # apple's ID
        self.apple = -1

        self.drawGrid()
        self.createScore()
        self.createSnake()
        self.createApple()

        # set the keyboard handle
        self.bind_all('<Key>', self.onKeyPressed)

        # start the timer
        self.after(Cons.DELAY, self.onTimer)

    def drawGrid(self):
        # 1st class
        # draw horizontal lines
        for y in range(0, Cons.BOARD_HEIGHT, Cons.CELL_SIZE):
            self.create_line(0, y, Cons.BOARD_WIDTH, y, fill='darkgray')

        # draw vertical lines
        for x in range(0, Cons.BOARD_WIDTH, Cons.CELL_SIZE):
            self.create_line(x, 0, x, Cons.BOARD_HEIGHT, fill='darkgray')

    def createApple(self):
        '''places the apple object on Canvas'''
        # 3rd topic
        apple = self.find_withtag('apple')
        if len(apple) > 0:
            self.delete(apple[0])

        appleX = Cons.CELL_SIZE * random.randint(5, Cons.MAX_RAND_POS - 5)
        appleY = Cons.CELL_SIZE * random.randint(5, Cons.MAX_RAND_POS - 5)
        self.apple = self.create_rectangle(appleX, appleY,
                                           appleX + Cons.CELL_SIZE, appleY + Cons.CELL_SIZE, fill='red', tags='apple')

    def checkAppleCollision(self):
        # check if the snake hit the apple
        # 4th topic
        apple_coords = self.coords(self.apple)
        snake_head_coords = self.coords(self.snake[0])
        if apple_coords == snake_head_coords:
            self.score += 1
            self.createApple()

            # append snake body
            id = self.create_rectangle(apple_coords[0], apple_coords[1],
                                       apple_coords[2], apple_coords[3], fill='green', tags='snake')
            self.snake.insert(0, id)
            # move head
            self.move(self.snake[0], self.moveX, self.moveY)

    def createScore(self):
        '''create score objects on Canvas'''
        # create score
        self.create_text(30, 10, text='Score: {0}'.format(self.score),
                         tag='score', fill='white')

    def drawScore(self):
        '''draws score'''
        score = self.find_withtag('score')
        self.itemconfig(score, text='Score: {0}'.format(self.score))

    def createSnake(self):
        # create snake (id, x, y)
        # 2nd class
        #startX = random.randint(5, Cons.MAX_RAND_POS - 6)
        #startY = random.randint(5, Cons.MAX_RAND_POS - 6)
        startX = startY = int(Cons.MAX_RAND_POS / 2)
        items = ((startX, startY), (startX - 1, startY), (startX - 2, startY))

        for x, y in items:
            id = self.create_rectangle(Cons.CELL_SIZE * x, Cons.CELL_SIZE * y,
                                       (x + 1) * Cons.CELL_SIZE, (y + 1) * Cons.CELL_SIZE, fill='green', tags='snake')
            self.snake.append(id)

    def moveSnake(self):
        # move snake body
        # 2nd class
        for i in range(len(self.snake) - 1, 0, -1):
            c1 = self.coords(self.snake[i])
            c2 = self.coords(self.snake[i-1])
            #print(c1, c2, c2[0] - c1[0], c2[1] - c1[1])
            self.move(self.snake[i], c2[0] - c1[0], c2[1] - c1[1])

        # move head
        self.move(self.snake[0], self.moveX, self.moveY)

    def checkSnakeSelfCollisions(self):
        # check if the snake head hit its own body or hit the boarder of the board
        # 5th topic
        head = self.coords(self.snake[0])
        print(head)

        for item in self.snake[1:]:
            body = self.coords(item)
            print(body)
            if body == head:
                self.inGame = False
                print('hit')

        if head[0] < 0 or head[0] > (Cons.BOARD_WIDTH - Cons.CELL_SIZE) \
                or head[1] < 0 or head[1] > (Cons.BOARD_WIDTH - Cons.CELL_SIZE):
            self.inGame = False

    def onKeyPressed(self, e):
        # controls direction variables with cursor keys
        key = e.keysym

        if key == 'Left' and self.moveX <= 0:
            self.moveX = -Cons.CELL_SIZE
            self.moveY = 0

        if key == 'Right' and self.moveX >= 0:
            self.moveX = Cons.CELL_SIZE
            self.moveY = 0

        if key == 'Up' and self.moveY <= 0:
            self.moveX = 0
            self.moveY = -Cons.CELL_SIZE

        if key == 'Down' and self.moveY >= 0:
            self.moveX = 0
            self.moveY = Cons.CELL_SIZE

    def onTimer(self):
        # create a game cycle each timer event
        self.drawScore()
        self.checkSnakeSelfCollisions()

        if self.inGame:
            # check collision apple
            self.checkAppleCollision()
            self.moveSnake()
            self.after(Cons.DELAY, self.onTimer)
        else:
            self.gameOver()

    def gameOver(self):
        self.inGame = False
        self.delete(ALL)
        self.create_text(self.winfo_width() / 2, self.winfo_height()/2,
                         text="Game Over with score {0}".format(self.score), fill="white")


class App(Frame):
    def __init__(self, master):
        super().__init__()

        self.master.title('Snake')
        self.board = Board()
        self.pack()


def main():
    root = Tk()
    App(root)
    root.mainloop()


if __name__ == '__main__':
    main()
