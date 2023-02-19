from tkinter import *


class Move:

    def __init__(self, master=None):

        self.master = master
        master.geometry("1200x1200")
        master.title("Kuboble")
        master.config(background="black")
        Label(self.master, text="Use arrow keys for GREEN Object", font=('Helvetica 25 bold')).pack(padx=100)
        Label(self.master, text="Use W,A,S,D keys for RED Object", font=('Helvetica 25 bold')).pack(padx=100)

        # width and height of canvas
        self.WIDTH = 600
        self.HEIGHT = 600

        # moves counter
        self.counter = 0

        # canvas object to create shape
        self.canvas = Canvas(master, width=self.WIDTH, height=self.HEIGHT)
        self.canvas.config(background="black")

        # creating rectangle
        self.greenObj = self.canvas.create_rectangle(0, 0, 200, 200, fill="green")
        self.redObj = self.canvas.create_rectangle(200, 0, 400, 200, fill="red")
        self.greenWin = self.canvas.create_rectangle(200, 400, 400, 600, outline="green", width=5)
        self.redWin = self.canvas.create_rectangle(0, 400, 200, 600, outline="red", width=5)
        self.canvas.pack(padx=50, pady=50)

    # for motion in negative x direction
    def left(self, event):
        sideGreenObj = self.canvas.coords(self.greenObj)
        sideRedObj = self.canvas.coords(self.redObj)

        if str(event.keysym) == "Left":
            # for green collision
            if (sideGreenObj[0] == sideRedObj[2]) & (sideGreenObj[1] - sideRedObj[1] == 0):
                self.canvas.move(self.greenObj, 0, 0)

            # for one gap left move
            elif (sideGreenObj[0] - sideRedObj[2] == 200) & (sideGreenObj[1] - sideRedObj[1] == 0):
                self.canvas.move(self.greenObj, -200, 0)
                self.counter += 1

            else:
                # for normal move
                self.canvas.move(self.greenObj, 0 - sideGreenObj[0], 0)
                if (0 - sideGreenObj[0]) != 0:
                    self.counter += 1


        elif str(event.keysym) == "a":
            # for red collision
            if (sideRedObj[0] == sideGreenObj[2]) & (sideRedObj[1] - sideGreenObj[1] == 0):
                self.canvas.move(self.redObj, 0, 0)

            # for one gap left move
            elif (sideRedObj[0] - sideGreenObj[2] == 200) & (sideRedObj[1] - sideGreenObj[1] == 0):
                self.canvas.move(self.redObj, -200, 0)
                self.counter += 1

            else:
                # for normal move
                self.canvas.move(self.redObj, 0 - sideRedObj[0], 0)
                if (0 - sideRedObj[0]) != 0:
                    self.counter += 1

        self.ifWin(sideGreenObj, sideRedObj)

    # for motion in positive x direction
    def right(self, event):
        sideGreenObj = self.canvas.coords(self.greenObj)
        sideRedObj = self.canvas.coords(self.redObj)

        if str(event.keysym) == "Right":
            # for green collision
            if (sideGreenObj[2] == sideRedObj[0]) & (sideGreenObj[1] - sideRedObj[1] == 0):
                self.canvas.move(self.greenObj, 0, 0)
            # for one gap right move
            elif (sideGreenObj[2] - sideRedObj[0] == -200) & (sideGreenObj[1] - sideRedObj[1] == 0):
                self.canvas.move(self.greenObj, 200, 0)
                self.counter += 1
            else:
                # for normal move
                self.canvas.move(self.greenObj, 600 - sideGreenObj[2], 0)
                if (600 - sideGreenObj[2]) != 0:
                    self.counter += 1


        elif str(event.keysym) == "d":
            # for red collision
            if (sideRedObj[2] == sideGreenObj[0]) & (sideRedObj[1] - sideGreenObj[1] == 0):
                self.canvas.move(self.greenObj, 0, 0)
            # for one gap right move
            elif (sideRedObj[2] - sideGreenObj[0] == -200) & (sideRedObj[1] - sideGreenObj[1] == 0):
                self.canvas.move(self.redObj, 200, 0)
                self.counter += 1
            else:
                # for normal move
                self.canvas.move(self.redObj, 600 - sideRedObj[2], 0)
                if (600 - sideRedObj[2]) != 0:
                    self.counter += 1

        self.ifWin(sideGreenObj, sideRedObj)

    # for motion in positive y direction
    def up(self, event):
        sideGreenObj = self.canvas.coords(self.greenObj)
        sideRedObj = self.canvas.coords(self.redObj)

        if str(event.keysym) == "Up":
            # for green collision
            if (sideGreenObj[1] == sideRedObj[3]) & (sideGreenObj[2] - sideRedObj[2] == 0):
                self.canvas.move(self.greenObj, 0, 0)
            # for one gap up move
            elif (sideGreenObj[1] - sideRedObj[3] == 200) & (sideGreenObj[2] - sideRedObj[2] == 0):
                self.canvas.move(self.greenObj, 0, -200)
                self.counter += 1
            else:
                # for normal move
                self.canvas.move(self.greenObj, 0, 0 - sideGreenObj[1])
                if (0 - sideGreenObj[1]) != 0:
                    self.counter += 1

        elif str(event.keysym) == "w":
            # for red collision
            if (sideRedObj[1] == sideGreenObj[3]) & (sideRedObj[2] - sideGreenObj[2] == 0):
                self.canvas.move(self.redObj, 0, 0)
            # for one gap up move
            elif (sideRedObj[1] - sideGreenObj[3] == 200) & (sideRedObj[2] - sideGreenObj[2] == 0):
                self.canvas.move(self.redObj, 0, -200)
                self.counter += 1
            else:
                # for normal move
                self.canvas.move(self.redObj, 0, 0 - sideRedObj[1])
                if (0 - sideGreenObj[0]) != 0:
                    self.counter += 1

        self.ifWin(sideGreenObj, sideRedObj)

    # for motion in negative y direction
    def down(self, event):
        sideGreenObj = self.canvas.coords(self.greenObj)
        sideRedObj = self.canvas.coords(self.redObj)

        if str(event.keysym) == "Down":
            # for green collision
            if (sideGreenObj[3] == sideRedObj[1]) & (sideGreenObj[2] - sideRedObj[2] == 0):
                self.canvas.move(self.greenObj, 0, 0)
            # for one gap down move
            elif (sideGreenObj[3] - sideRedObj[1] == -200) & (sideGreenObj[2] - sideRedObj[2] == 0):
                self.canvas.move(self.greenObj, 0, 200)
                self.counter += 1
            else:
                # for normal move
                self.canvas.move(self.greenObj, 0, 600 - sideGreenObj[3])
                if (600 - sideGreenObj[3]) != 0:
                    self.counter += 1

        elif str(event.keysym) == "s":
            # for red collision
            if (sideRedObj[3] == sideGreenObj[1]) & (sideRedObj[2] - sideGreenObj[2] == 0):
                self.canvas.move(self.redObj, 0, 0)
            # for one gap down move
            elif (sideRedObj[3] - sideGreenObj[1] == -200) & (sideRedObj[2] - sideGreenObj[2] == 0):
                self.canvas.move(self.redObj, 0, 200)
                self.counter += 1
            else:
                # for normal move
                self.canvas.move(self.redObj, 0, 600 - sideRedObj[3])
                if (600 - sideRedObj[3]) != 0:
                    self.counter += 1

        self.ifWin(sideGreenObj, sideRedObj)

    # for checking if wins after any move
    def ifWin(self, firstObject, secondObject):
        print(firstObject)
        print(secondObject)
        if (self.canvas.coords(self.greenWin) == firstObject) & (self.canvas.coords(self.redWin) == secondObject):
            Label(self.master, text="Congratulations", font=('Helvetica 35 bold')).pack(pady=20)
            Label(self.master, text="Total Moves = " + str(self.counter), font=('Helvetica 20 bold')).pack()
