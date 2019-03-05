import winsound             #library for sing soud reated functions
import turtle               #python's inbuilt library for graphics
import time                 #for delay

############################################################################################  
# TO DO BLOCK
# . something more creative maybe draw the solved one on screen using turtle
# . maybe use open cv for scanning the grid and solvving it
############################################################################################  
#easy to copy paste for the next grid


 
initial_grid = [0,0,0,0,0,0,0,0,0]
                


############################################################################################ 

size = 9  #size of sudoko grid

#cells with 0 are vacant

grid =[ #     |     |
        [1,0,0,0,0,7,0,9,0],
        #     |     |
        [0,3,0,0,2,0,0,0,8],
        #     |     |
        [0,0,9,6,0,0,5,0,0],
        #     |     |
        [0,0,5,3,0,0,9,0,0],
        #     |     |
        [0,1,0,0,8,0,0,0,2],
        #     |     |
        [6,0,0,0,0,4,0,0,0],
        #     |     |
        [3,0,0,0,0,0,0,1,0],
        #     |     |
        [0,4,0,0,0,0,0,0,7],
        #     |     |
        [0,0,7,0,0,0,3,0,0],
        #     |     |
        ]

n = len(grid)
m = len(grid[0])


############################################################################################  
def print_grid():                       # prints the sudoko grid duh. |-_-|
    for i in grid:
        print (i)

#print_grid()                           #function call just to check it is working
############################################################################################  

############################################################################################  
#this function checks whether the grid is empty or not
#if the grid is empty it retrn a list
#the list contains r,c and flag =1
#r is row variable, c is the colun variable and flag just tells us that it is empty

def check_unassigned(r,c):
    flag =0
    for i in range(0,size):
        for j in range(0,size):
            if grid[i][j] == 0:
                r=i
                c=j
                flag =1
                a = [r,c,flag]          #list which is returned containg all the
                return a                #necessary values
    a=[-1,-1,flag]                      # if grid was not empty then r =-1,c=-1 and flag =0
    return a

############################################################################################  

############################################################################################  
#this function checks whether we can put a number isn  the cell or not

def is_safe(n,row,col):
    #checking the row
    for i in range(0,size):
        #checking whether the same values exist in row or not
        if grid[row][i] == n:
            return False
        
    #checking the row
    for i in range(0,size):
        #checking whether the same value exist in column or not
        if grid[i][col] == n:
            return False
    
    #checking the 3x3 grid
    r_s = (row//3)*3                    #denotes the row start of the sub-grid
    c_s = (col//3)*3                    #denotes the col start of the sub-grid
    for i in range(r_s,r_s+3):
        for j in range(c_s,c_s+3):
            if grid[i][j] == n:
                return False
    return True

############################################################################################  

############################################################################################
#this is the graphics part of the script


win = turtle.Screen()
win.title("Sudoku solver by dy")
win.bgcolor("white")
win.setup(width=600, height=600)
#win.tracer(0)


############################################################################################

############################################################################################

def draw_grid():        #function to draw grid on screen

    draw =turtle.Turtle()
    draw.color('white')
    draw.hideturtle()
    draw.goto(-150,-150) 
    dist = 300
    draw.speed(1000)
    draw.color('black')
    
    
    for _ in range(4):
        draw.forward(dist)
        draw.left(90)           #90 is angle here not distance
    

    a=33.33
    for _ in range(4):
        draw.forward(a)
        draw.left(90)
        draw.forward(dist)
        draw.right(90)
        draw.forward(a)
        draw.right(90)
        draw.forward(dist)
        draw.left(90)
        
    draw.forward(a)
    draw.left(90)
    for _ in range(4):
        draw.forward(a)
        draw.left(90)
        draw.forward(dist)
        draw.right(90)
        draw.forward(a)
        draw.right(90)
        draw.forward(dist)
        draw.left(90)

draw_grid()

############################################################################################

def print_numbers():
    text = turtle.Turtle()
    text.color('white')
    text.goto(0,250)
    text.hideturtle()
    text.color('black')
    text.write("SUDOKU - SOLVER",align='center',font=('COURIER',24,'normal'))
    text.color('white')
    #text.setposition(0,150)
    x= " "
    '''
    for i in grid:
        text.color('black')
        text.write(grid[8-i],align='center',font=('COURIER',15,'normal'))
        text._newLine()
        text.color('white')
        text.goto(0,i*15)
    '''
    b=120
    text.color('black')
    text.up()                   #disables line that is drawn by turtle
    for i in grid:
        text.setposition(180,b)
        b-=35
        c=1
        for j in reversed(i):
            c+=6
            text.write(str(j)+x*c,align='center',font=('COURIER',14,'normal'))
            #pos = text.position()
          

print(print_numbers())

############################################################################################ 
#this is the heart and soul of  sudoko_Solver
#this solves the gird using back_tracking
'''

def solve_sudoku():
    row = 0
    col = 0
    #first we check whether is there any empty cell or not
    #if there is no unassigned cell then sudokuis solved
    a = check_unassigned(row,col)
    if a[2]==0:
        return True
    row = a[0]
    col = a[1]
    #returns true ie; the grid is already solved
    for i in range(1,10):
        #can we assign i to the cell or not ?
        if is_safe(i,row,col):
            grid[row][col]=i
            #backtracking
            if solve_sudoku():
                return True
            #if we can't solve the grid with this solution
            #make that cell 0 again and try again
            grid[row][col]=0
    return False

if solve_sudoku():
    print_grid()
    winsound.PlaySound("finished.wav",winsound.SND_FILENAME)            
else:
    print("Hmmm... Sorry couldn't find the solution :( ")

'''
############################################################################################
win.exitonclick()