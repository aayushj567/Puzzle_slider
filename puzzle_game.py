from Tile import *
from puz_info import*
import math
import random
from gameboard import*
from thumbnail import*
from turtle import*
from Message import*
from leaderboard import*
import time
import os

p_moves = turtle.Turtle()
p_moves.hideturtle()

tmb = turtle.Turtle()
tmb.hideturtle()

global screen
screen = turtle.Screen()

global player_name
global moves_limit

screen.setup(1000, 700)

def play_message(image):
    '''functiton - play_message: used to display messages from the Resources folder
        inputs - image: the name of image_file which is a string'''
    
    m1 = Message(f"Resources/{image}.gif")
    m1.display_message()
    screen.ontimer(screen.update(), 2600)#show the message for 2 seconds before hiding it
    m1.hide()

def puzzle_options():
    x = os.getcwd()
    y = os.listdir(x)
    names_of_puzzles = []
    for each in y:
        if each.endswith(".puz"):
            names_of_puzzles.append(each[0:-4])

    if len(names_of_puzzles) >= 10:
        play_message("file_warning")
        names_of_puzzles = names_of_puzzles[0:10]

    names_of_puzzles = "\n".join(names_of_puzzles)
    return names_of_puzzles
    

def puzzle_choice(): #if they click on the cancel option do nothing
    '''function - puzzle_choice asks for a name input for puzzle. Returns that file name or Fasle if cancelled'''
    names_of_puzzles = puzzle_options()
    file_to_use = screen.textinput("Load Puzzle", f"Enter name of puzzle you wish to load. \
Choices are:\n{names_of_puzzles}")
    file_name = file_to_use
    if not(file_name == None):
        return file_name
    else:
        print("You pressed cancel")
        return False #pressing cancel should close the pop up window and do nothing

def player_moves():
    '''function - player_moves asks for an integer number of moves to play the puzzle and returns it if between 5 and 200'''
    moves_limit = screen.numinput("Hi", "How many moves? (between 5 - 200)", default = 50, minval = 5, maxval = 200)
    check = (5 <= moves_limit <= 200)
    while not(check == True):
        moves_limit = screen.numinput("5001 Puzzle Slide Moves", "Enter number of moves (chances) you want? (5 - 200)", default = 50, minval = 5, maxval = 200)
        check = (5 <= moves_limit <= 200)

    return moves_limit

def update_player_moves(number):
    '''function - update_player_moves: makes a turtle that displays the player moves on screen
        input - number: a string'''
    p_moves.speed(0)
    p_moves.clear()
    p_moves.up()
    p_moves.hideturtle()
    p_moves.goto(-460, -270)
    p_moves.write(f"Player moves:\n{number}", False, align = "center", font = ("Arial", 20))

def check_bad_image(image_list_to_check):
    for each in image_list_to_check:
        if os.path.isfile(each) == False:
            with open("errors.txt", mode = "a+") as new_file:
                now = time.ctime()
                new_file.write(f"{now}:Error: {each} NOT FOUND. LOCATION: puzzle_game.check_bad_image()\n")
                return False

def puzzle(puzzle_name, reset = False):
    '''function - puzzle: gathers info about the tiles and stores them in a list
        inputs: puzzle_name: a string which is the puzzle file we have to load
               reset: true or false if the puzzle needs to be reset. Is false by default'''
    if puzzle_name == False:
        return None
    
    else: 
        while to_use(puzzle_name) == None: #if a valid puzzle name was not given keep asking the player
            play_message("file_error")
            with open("errors.txt", mode = "a+") as new_file:
                now = time.ctime()
                new_file.write(f"{now}:Error: File {puzzle_name} does not exist. LOCATION: puzzle_game.puzzle()\n")

            puzzle_name = puzzle_choice()
        
        info = to_use(puzzle_name) #making use of the function to_use from the file puz_info
        name = info[0] #the name of the puzzle file
        number = int(info[1])#total number of tiles

        valid_number_of_tiles = [4,9,16]

        if not(number in valid_number_of_tiles): #if invalid number of tiles provided
            with open("errors.txt", mode = "a+") as new_file:
                now = time.ctime()
                new_file.write(f"{now}:Error: Invalid number of tiles. LOCATION: puzzle_game.puzzle()\n")
                return "bad number"
            
        tile_width = info[2] + 2 #so that pieces arnt too close
        global thumbnail
        thumbnail = info[3] #the thumbnail to be displayed above the leaderboard
        global image_original
        image_original = info[4] #list of all images
        if check_bad_image(image_original) == False:
            return "bad image"
        image = image_original[:]#original images copy

        if reset == False:
            random.shuffle(image)#if player didnt ask to reset shuffle the images in random order

        root = math.sqrt(number)
        
        x_pos = -500
        y_pos = 200

        global tile #tile instance from Tile class
        global lst_original #lst for storing Tile instances
        
        global lst #going to be copy of lst_original
        lst_original = []
        
        for index in range(number):
            
            if (index % root == 0) and not(index == 0):#changing the y_position and resetting x_position 
                y_pos = y_pos - tile_width
                x_pos = - 500
                tile = Tile(name, number, tile_width, image[index], x_pos, y_pos)
                lst_original.append(tile)

            else: #shifting x_position of tiles
                if index == 0:
                    x_pos = x_pos
                else:
                    x_pos = x_pos + tile_width
                 
                tile = Tile(name, number, tile_width, image[index], x_pos, y_pos)
                lst_original.append(tile)

        lst = lst_original[:]


def display_puzzle():#display the puzzle
    '''function - display_puzzle: shows the Tile instances stored in global variable lst and makes the thumbnail
        if lst is empty it displays nothing on the screen'''
    global valid_moves #the number of valid swaps of the puzzle tile that occurs
    valid_moves = 0
    update_player_moves(valid_moves)#runs the function to show player moves on the screen
    try:
        global thumbnail
        make_thumbnail(tmb, thumbnail)#function makes  the thumbnail

    except:
        with open("errors.txt", mode = "a+") as new_file:
            now = time.ctime()
            new_file.write(f"{now}:Error: Could not load thumbnail image. LOCATION: puzzle_game.display_puzzle()\n")
        return None
    else:
        try:
            global lst
            for each in lst:
                each.make_turtle()
        except:
            return None

'''-------------------------------------load, reset, and quit button functionality-----------------------------------------------'''
def load_puzzle():
    '''function - load_puzzle: if fplayer clicks on load button, this function runs which will ask for a puzzle name
        and then display on screen
        Returns None if the player doesn't provide a valid puzzle file name or if they click on cancel'''
##    global loaded_new
    
    puzzle_name = puzzle_choice()#asking which puzzle to load
    current_puzzle = lst[0].get_name()#gettin current puzzle name

    if puzzle_name ==  False: #if they click on the cancel option do nothing
        return None
    
    else:
        if to_use(puzzle_name) == None: #if valid puzzle name was not given show error message
            play_message("file_error")
            return None

        else:
            for each in lst:
                each.hide()
            hide_thumbnail(tmb)

            lst.clear()
            puzzle(puzzle_name, False)
            display_puzzle()

def quit_game():
    play_message("quitmsg")
    turtle.bye()

def reset_puzzle():

    puzzle_name = lst[0].get_name() #get name of current puzzle

    for each in lst:
        each.hide()
        
    lst.clear()
    puzzle(puzzle_name, True)
    display_puzzle()


'''-------------------------------------swapping tiles with blank tile functionality-------------------------------------------'''
def clicked_tile(copy, x, y): #returns the tile which was clicked.
    '''function - clicked_tile: takes a list of tiles and the clicked_position as inputs
        and returns that tile corresponding to the position from the list
        inputs: copy - the list tiles
                x,y - the x,y position of the click. both are float
        returns - each: the tile which was clicked'''
    for each in copy:
        if each.is_tile(x,y) == True:
            return each

def blank_tile(copy):#returns the blank tile from the global lst
    for each in copy:
        if each.is_blank() == True:
            return each

def update_tile_list(tile1, tile2):
    '''function - update_tile_list: swaps indexes of two tiles, which have are provided as imputs, in the global lst'''
    placeholder1 = lst.index(tile1)
    placeholder2 = lst.index(tile2)
    
    lst[placeholder1] = tile2
    lst[placeholder2] = tile1
    
def swap_them(x,y):
    '''function - swap_them: swaps the positions of the turtle displaying puzzle tiles.
        inputs - x,y : floats which is the position of the mouse click
        returns None. However if swap was successful updates player moves and the global lst'''
    try:
        copy = lst[:]
        width = copy[0].tile_size()
        
        blank = blank_tile(copy)
        clicked = clicked_tile(copy, x, y)

        if clicked.is_blank() == True:#clicked on the blank tile should do nothing
            return None  
        else:
            if blank.is_adjacent(clicked) == True:#if a tile adjacent to blank tile is clicked on
##                print("Swapping with blank tile")
                blank.swap_tiles(clicked)#swaps the turtle positions of the blank with the clicked
                global valid_moves
                valid_moves = valid_moves + 1
                update_player_moves(valid_moves)#updates valid_moves
                update_tile_list(blank, clicked)#updates lst

            else:
                return None
    except:
        return None

'''----------------------------checking for loss, win, and what to do if clicked on one of the buttons--------------------------'''
def check_win():
    '''function - check_win: checks for a winning arrangement of tiles after every valid_move. If player wins, game exits'''
    image_scrambled = []  
    for each in lst: #getting the scrambled order of the images which may have been rnadomly shuffled
        image_scrambled.append(each.get_image())

    if image_scrambled == image_original: #the original list has not been shuffled and has the images stored in order of puzzle solution 
        global player_name
        global valid_moves
        append_to_leaderboard(player_name, valid_moves)#append name of player and their moves to leaderboard
        play_message("winner")#displays winning message
        turtle.bye()#exits   

def out_of_moves():
    '''function - out_of_moves: checks if player has used up all their moves. If they have show lose message,credits and exit game'''
    global valid_moves
    global moves_limit
    if valid_moves == moves_limit:
        play_message("Lose")
        play_message("credits")
        turtle.bye()

def click_action(x,y):
    '''function click_action: determines which action to carry out based on where the player clicks
        inputs - x,y: mouse clicked position both floats'''
    if (-560 < x < -110) and (-160 < y < 290): #if inside the puzzle
        swap_them(x,y)
        check_win()
        out_of_moves()

    elif (-240 < x < -160) and (-290 < y < -210):
        load_puzzle()#load a new puzzle if clicked on load button

    elif (-140 < x < -60) and (-290 < y < -210):
        reset_puzzle()#reset the current puzzle if reset button clicked

    elif (-39 < x < 38) and (-290 < y < -210):
        quit_game()#if quit button clicked        


def play_puzzle():
    '''function - play_puzzle - simulates the puzzle game'''
    global player_name
    player_name = screen.textinput("CS 5001 Puzzle Slide", "Your name")#ask for player name
    global moves_limit
    moves_limit = player_moves()#ask for how number of moves from player    
  
    puzzle_name = puzzle_choice()#ask for puzzle name
    
    if puzzle_name == False:#if player clicks on cancel button at the start
        turtle.bye() #close the turtle window
        return None #proceed no further as the turtle window had been closed
    
    if puzzle(puzzle_name, False) == "bad number" or puzzle(puzzle_name, False) == "bad image":
        print("number or image bad")
##        pass
        return None#load the puzzle without resetting it. Meaning tiles would be scrambled randomly.
    border_1 = Gameboard()#show the gameboard, leaderboard and menu areas and the buttons
    display_puzzle()#display the puzzle on the screen
    
    ldb = turtle.Turtle()#leaderboard turtle
    ldb.hideturtle()
    try:
        display_leaderboard(ldb)#display the leaderboard
    except:
        play_message("leaderboard_error")
        append_to_leaderboard(None, None)
        
        with open("errors.txt", mode = "a+") as new_file:
            now = time.ctime()
            new_file.write(f"{now}:Error: Could not open leaderboard.txt. LOCATION: leaderboard.display_leaderboard()\n")
            
    screen.onclick(click_action)            

def main():
    play_message("splash_screen")#displays the splash screen at the beginning
    play_puzzle()
    
if __name__=="__main__":
    main()
