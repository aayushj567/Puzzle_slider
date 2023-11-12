'''class Tile is for creating the  puzzle tiles/pieces.
Each tile of the puzzle is an instance of this class'''

import turtle
import math
from PositionService import*
from gameboard import*

global screen
screen = turtle.Screen()

class Tile:

    def __init__(self, name, number, size, image, x_pos, y_pos): #default constructor which will be provided name of puzzle like Mario, etc, its size, and its number of pieces
        
        self.name = name #name of puzzle like mario, luigi, etc...
        self.number = number #number of peices in the  puzzle 
        self.size = size #the size or width of the square tile
        self.image = image #the str containig the path of the image of tile 
        self.x_pos = x_pos #x coord of the turtle
        self.y_pos = y_pos #y coord of the turtle
        self.t1 = turtle.Turtle()

    def get_name(self):
        '''returns name of the puzzle'''
        return self.name
    
    def get_number(self):
        '''returns number of tiles in the puzzle'''
        return self.number

    def get_image(self):
        '''returns the location of  the image associated to that tile''' 
        return self.image

    def tile_size(self):
        '''returns the size of the tile'''
        return self.size

    def is_blank(self):
        '''checks if a tile is a blank tile (returns True) or not (returns False).'''
        file_name = self.get_name()
        image_name = f"Images/{file_name}/blank.gif"
        if self.image == image_name:
            return True
        else:
            return False

    def valid_square(self): #check if its a square or not. if not then False
        '''checks if  the puzzle number is a perfect square or not'''
        root = math.sqrt(self.number)
        if root**2 == self.number:
            return True
        else:
            raise False

    def make_turtle(self):
        '''makes a turtle and assigns image of a tile/piece to that turtle'''
        try:
            self.t1.up()
            self.t1.speed(0)
            self.t1.hideturtle() #useful to speed up the process
            self.t1.goto(self.x_pos, self.y_pos)
            screen.register_shape(self.image)

            self.t1.showturtle()
            self.t1.shape(self.image)
        except:
            return None

    def hide(self):
        self.t1.up()
        self.t1.speed(0)
        self.t1.hideturtle()
        self.t1.goto(-560, 500)
        
    def get_position(self):
        '''returns position of the turtle which has a tile attahed to it'''
        return self.t1.position()

    def is_tile(self, x, y):
        '''given position x,y it checks if (x,y) within the tile. returns True if (x,y) is in the tile'''
        xc, yc = self.get_position()
        width = self.tile_size() - 2
        if (abs(x - xc)<=(width/2)) and (abs(y-yc)<=(width/2)):
            return True

    def is_adjacent(self, other):
        '''given two instances of Tile class, checks if they are adjacent to each other'''

        xb, yb = self.get_position()
        xc, yc = other.get_position()
        
        x_diff = (xb - xc)**2
        y_diff = (yb - yc)**2

        dist = math.sqrt(x_diff + y_diff)#using the distance formula to see if tiles share an eddge with each other
        width = self.tile_size()
        if dist <= width:
            return True
        else:
            return False

    def swap_tiles(self, other): #swaps position of two instances of Tile class with each other

        if isinstance(other, Tile):

            placeholder = other.get_position()
            placeholder2 = self.get_position()

            other.t1.goto(placeholder2[0], placeholder2[1])
            self.t1.goto(placeholder[0], placeholder[1])




        
        
