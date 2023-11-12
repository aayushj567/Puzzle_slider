
import turtle
from time import*
screen = turtle.Screen()
import os

def append_to_leaderboard(player_name = None, moves_to_win = None):
    '''function - append_to_leaderboard: appends the player_name and their moves to win to leaderbord.txt
                    file
            inputs - player_name: the player_name a string
            moves_to_win: an integer value showing how many moves it took to win'''
    if (player_name == None) or (moves_to_win == None):
        with open("leaderboard.txt", mode = "a+") as outfile:
            pass

        return None
    
    else:
        with open("leaderboard.txt", mode = "a") as outfile:
            outfile.write(f"{moves_to_win}:{player_name}\n")

def display_leaderboard(ldb):
    '''function - display_leaderboard displays the leaderbord content using turtle to write it on the screen'''
    with open("leaderboard.txt", mode = "r") as infile:
        leaders = infile.readlines()
        
    leaders_str = ""
    for each in leaders:
        leaders_str = leaders_str + each
            
    ldb.up()
    ldb.speed(0)
    ldb.hideturtle()
    ldb.goto(-11,0)
    ldb.color("blue")
    ldb.write(f"{leaders_str}", False, align = "left", font = ("Arial", 15))




