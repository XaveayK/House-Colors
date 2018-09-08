'''--------------------------------------------------------
#                      Xavier Kidston
#                  
--------------------------------------------------------'''



#These import the necessary set of functions to run my program
from graphics import *
import random, time



#These establish universal constants
WIN_W, WIN_H = 500, 400
COLOURS = ('red', 'blue','orange', 'pink','purple', 'green','brown','black', 'yellow', 'white')
HOME_SPECS = (70, WIN_H-50, WIN_W-150, 150, 100)



'''
Function: To create a house and all of its components
Parameters: win - the window to draw in
            specs - the spacing
Returns: House - the big box
         door - the houses door
         leftwindow - the rectangle left window
         rightwindow - the rectangle right window
         roof - the triangle roof
'''
def create_house(win, specs):
    
    #This creates all of the components of the house
    house=Rectangle(Point(specs[0], specs[1] -specs[3]), Point(specs[0]+specs[2], specs[1]))
    house.draw(win)
    leftwindow= Rectangle(Point(specs[0]+10,specs[1]-(2*specs[3]//3)), Point(specs[0]+10+ specs[2]//3,specs[1]-specs[3]//3))
    leftwindow.draw(win)
    rightwindow= Rectangle(Point(specs[0]+2*specs[2]//3-10,specs[1]-(2*specs[3]//3)), Point(specs[0]+specs[2]-10,specs[1]-specs[3]//3))
    rightwindow.draw(win)
    door=Rectangle(Point(specs[0]+specs[2]//2-20, specs[1] -specs[3]//3), Point(specs[0] + specs[2]//2+20, specs[1]))
    door.draw(win)
    roof=Polygon(Point( specs[0]+ specs[2]//2, specs[1]-specs[3]-specs[4]), Point(specs[0]-25, specs[1]-specs[3]), Point(specs[0]+specs[2]+25, specs[1] -specs[3]))
    roof.draw(win)
    
    return [house, door, leftwindow, rightwindow, roof]



'''
Function: Creates a list of colors for the house to change too
Parameters: myhouse
Returns: None
'''
def house_colours(myhouse):
    mycolor=["red","brown", "white", "yellow","green"]
    i=0
    
    #for each object in the house this sets the color
    for myobject in myhouse:
        myobject.setFill(mycolor[i])
        i+=1
    return



'''
Function: Checks if a click is in the triangle
Parameters: pt, A, B, C
Returns: A trigonometric check
'''
def in_Triangle(pt, A, B, C):
    Ax, Bx, Cx, Dx = A.getX(), B.getX(), C.getX(), pt.getX()
    Ay, By, Cy, Dy = A.getY(), B.getY(), C.getY(), pt.getY()
    det = (Cy-Ay)*(Bx-Ax) - (Ay-By)*(Ax-Cx)
    u = ((Cy-Ay)*(Dx-Ax) + (Ax-Cx)*(Dy-Ay))/det
    v = ((Ay-By)*(Dx-Ax) + (Bx-Ax)*(Dy-Ay))/det
    #print('u, v = ' + str((u, v)))                         # Dev check

    return u > 0 and v > 0 and (u + v < 1)
   
   
   
'''    
Function: Creates a text object
Parameters: win - the window
            x - the x coord
            y - the y coord
            text - the text you want displayed
Returns: info - the text with placement 
'''
def info_create(win, x, y, text):
    
    info= Text(Point(x,y), "")
    info.setText(text)
    info.draw(win)
    
    return info



'''
Function: Makes something a button
Parameters: win - The window
            Ulx - The upper left X coord
            Uly - The upper left Y coord
            width - The width of the button
            height - the height of the button
            text - the text you want on the button
            colour - the color you want to button to be
Returns: rect - the rectangle 
         label - the label of the button
'''
def make_button(win, Ulx, Uly, width, height, text, colour):
    
    #Creates a rectangle
    rect= Rectangle( Point( Ulx, Uly), Point(Ulx+width, Uly+height))
    rect.setFill(colour)
    rect.draw(win)
    
    #Creates a text label on the rectangle
    label= Text(Point(Ulx + width//2, Uly + height//2), text)
    label.setSize(16)
    label.draw(win)
    
    return [rect, label]



'''
Function: Checks if it's in the rectangle
Parameters: Point - The point that is clicked
            Button - The button 
Returns: A comparison checking if clicks within points
'''
def in_rectangle(point, button):
    top_left=button.getP1()
    bottom_right= button.getP2()
    
    return(top_left.getX() <= point.getX() <= bottom_right.getX() and \
            top_left.getY() <= point.getY() <= bottom_right.getY())



'''
Function: Combines all the other functions to make the house clickable
Parameters: None
Returns: None
'''
def main():
    
    #these make the window, house, resetbutton, quit button, color the house, and name it
    win= GraphWin("Fun_House", 500, 400)
    my_house=create_house(win, HOME_SPECS)
    house_colours(my_house)
    reset_button= make_button(win, 445, 5, 50, 25, "Reset", "red")
    quit_button= make_button(win, 445, 45, 50, 25, "Quit", "yellow")
    info=info_create(win, 250, 50, "Xavier's house")
    
    #this runs a while loop to check if the mouse has been clicked, and if it hasn't
    while True:
        try:
            point = win.getMouse()
        except GraphicsError:
            return
        newcolor=COLOURS[random.randint(0,9)]
        
        #this checks if the mouse click is in the quit button and closes if it is
        if in_rectangle(point, quit_button[0]):
            info.setText("quitting the program")
            time.sleep(2)
            win.close()
            break
        
        #This checks if the mouse click is in the reset button, and resets the house if it is
        elif in_rectangle(point, reset_button[0]):
            house_colours(my_house)
            
        #This checks if the click was in the triangle
        elif in_Triangle(point, my_house[4].getPoints()[0], my_house[4].getPoints()[1],my_house[4].getPoints()[2]):
            my_house[4].setFill(newcolor)
            info.setText("Roof selected and changed to "+ newcolor)
            
        #This checks if the door was clicked
        elif in_rectangle(point, my_house[1]):
            my_house[1].setFill(newcolor)
            info.setText("Door selected and changed to "+ newcolor)
            
        #This checks if the left window was clicked
        elif in_rectangle(point, my_house[2]):
            my_house[2].setFill(newcolor) 
            info.setText("Left Window selected and changed to "+ newcolor)
            
        #this checks if the right window was clicked
        elif in_rectangle(point, my_house[3]):
            my_house[3].setFill(newcolor)
            info.setText("Right Window selected and changed to "+ newcolor)
            
        #This checks if the base of the house (base rectangle) was clicked and changes the color to that
        elif in_rectangle(point, my_house[0]):
            my_house[0].setFill(newcolor)
            info.setText("House selected and changed to "+ newcolor)
            
        #if none of the objects were clicked, it tells you where you clicked
        else:
            x=point.getX()
            y=point.getY()
            string= "Point (" + str(x) + ", " + str(y) + ")"
            info.setText("You clicked "+string)
            print(my_house[4].getPoints())
            
    time.sleep(1 / 20)
    
    return