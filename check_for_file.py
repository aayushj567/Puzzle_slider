
import os
def check_file_or_not():
    print(os.getcwd())
    x = os.getcwd()
    y = os.listdir(x)
    z= []
    for each in y:
        if each.endswith(".puz"):
            z.append(each[0:-4])
    print(z)

def check_image_file():
    path = f"Images/marios_not_here/16.gif"
    print(os.path.isfile(path))
    
check_file_or_not()
check_image_file()
