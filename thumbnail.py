'''making and clearing the thumbnail'''

import turtle
global screen
screen = turtle.Screen()

def make_thumbnail(tmb, thumbnail):
    '''fucntion - make_thumnail: creates a thumbnail near the top right of the leaderboard using turtle'''
    tmb.up()
    tmb.speed(0)
    tmb.hideturtle() #useful to speed up the process
    tmb.goto(170, 250)
    screen.register_shape(thumbnail)

    tmb.showturtle()
    tmb.shape(thumbnail)

def hide_thumbnail(tmb):
    '''hides the thumbnail. sends it to shadow realm'''
    tmb.speed(0)
    tmb.hideturtle()  
    tmb.goto(-760, 800)
