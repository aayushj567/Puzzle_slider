'''Aayush Jaiswal
CS5002 Final Project
Slider puzzle - helper file'''

import turtle
global screen
screen = turtle.Screen()

class Gameboard:
    '''a class for the game area, menu area and leaderboard area'''
    def __init__(self):
        '''making the three rectangles for the puzzle'''
        
        self.make_rectangle(-560, 290, 450, 450, color = "black") #the play area where the puzzle is
        
        self.make_rectangle(-40, 290, 210, 450, color = "blue") #area for leaderboard
        self.default_header()#the turtle which will write the word 'LEADERS' in the leaderboard area
                
        self.make_rectangle(-560, -200, 730, 90, color = "black") #area for menu buttons

        buttons = ["loadbutton", "resetbutton", "quitbutton"] #making the 3 buttons
        i = 0
        for each in buttons:
            each = f"Resources/{each}.gif"
            x = -200 + i
            self.make_button(each, x,-250)
            i = i+100

    def make_rectangle(self, x, y, length, width, color = "black"): #x,y is the start position
        '''function - make_rectangle: makes a rectangle using turtle
            inputs - x,y: floats are the strting position
                    length,width - the length,width of the retcangle also floats
                    color = color of turtle pen. is black by default'''
        self.t1 = turtle.Turtle()
        self.t1.speed(0)

        length = length + 5
        width = width + 5
        self.t1.up()
        self.t1.goto(x,y)
        self.t1.down()

        self.t1.pensize(5)
        self.t1.pencolor(color)
        
        self.t1.forward(length)
        self.t1.right(90)
        self.t1.forward(width)
        self.t1.right(90)
        self.t1.forward(length)
        self.t1.right(90)
        self.t1.forward(width)
        self.t1.right(90)
        self.t1.up()
        self.t1.hideturtle()

    def make_button(self, image, x, y):
        '''function - make_button: makes the three buttons which are at the bottom'''
        self.t1 = turtle.Turtle()
        self.t1.speed(0)
        self.t1.up()
        self.t1.hideturtle() #useful to speed up the process
        self.t1.goto(x, y)
        screen.register_shape(image)#image is the str input of the image file path 

        self.t1.showturtle()
        self.t1.shape(image)
        self.t1.down()

    def default_header(self):
        '''function - default_header: makes turtle write the word 'LEADERs' at the top'''
        header = turtle.Turtle()
        header.up()
        header.speed(0)
        header.hideturtle()
        header.goto(-20,230)
        header.color("blue")
        header.write(f"LEADERS", False, align = "left", font = ("Arial", 15))

