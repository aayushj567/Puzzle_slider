'''Aayush Jaiswal
CS 5001 Final Project'''

import turtle
global screen
screen = turtle.Screen()

class Message:
    '''a class for making messages using turtle'''
    def __init__(self, image):
        '''initializes a turtle which will display the message based on the image file provided'''
        self.image = image
        self.msgturtle = turtle.Turtle()

    def display_message(self):
        '''displays the message onm the screen'''
        self.msgturtle.up()
        self.msgturtle.hideturtle()
        screen.register_shape(self.image)
        self.msgturtle.showturtle()
        self.msgturtle.shape(self.image)

    def hide(self):
        '''when error is done showing it will be asked to hide itself'''
        self.msgturtle.speed(0)
        self.msgturtle.hideturtle()
        self.msgturtle.goto(-700,800)
        
