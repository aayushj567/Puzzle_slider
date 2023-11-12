'''Extracting info from puz files'''

from pathlib import Path

def puzzle_info(file):#tries opening the file and and turns each line to a list
    #returns nothing if unsuccessful/file not found
    try:
        file = file + ".puz"
        file = Path(file)
        with open(file, mode = "r") as infile:
            info = infile.readlines()

        for i in range(len(info)):

            info[i] = info[i].strip("\n")

        return info

    except:
        return None

def info(line): # separates each line into a nested list. each element inside
    #the nested list is 2 elements. THe first is the number 1,2,3... and the second
    #the info for the puzzle we care abt like the nmae, size, image path, etc.
    #we only use the information from the second element and thats whats returned
    info = line.split(":")
    info = info[1].strip()
    return info

def name(lst):#the name of the puzzle like 'mario', 'luigi', etc...
    name = info(lst[0])
    return name

def number(lst):#the number of pieces in the puzzle
    num_of_tiles = info(lst[1])
    return float(num_of_tiles)

def size_info(lst):# returns the width of the square image which acts as a tile
    img_size = info(lst[2])
    return float(img_size)

def thumbnail(lst): #returns file path for the thumbnail
    thumbnail = info(lst[3])
    return thumbnail

def images_info(lst): #returns where the image path for each tile as a list
    images = lst[4:]
    my_images = []
    for each in images:
        x = info(each)
        my_images.append(x)
        
    return my_images

def to_use(file_name):#returns everything above in a tuple
    lst = puzzle_info(file_name)
    if lst == None:
        return None        
    x = (name(lst), number(lst), size_info(lst), thumbnail(lst), images_info(lst))
    return x
     

