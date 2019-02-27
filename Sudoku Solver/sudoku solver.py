############################################################################################  
# TO DO BLOCK
# 1. add a soundfile when the script finishes solving the  grid
# 2. something more creative maybe draw the solved one on screen
# 3. maybe use open cv for scanning the grid and solvving it
############################################################################################  



size = 9  #size of sudoko grid

#cells with 0 are vacant

grid =[ #      |     |
        [1,2,3,4,5,6,7,8,9],
        [1,2,3,4,5,6,7,8,9],
        [1,2,3,4,5,6,7,8,9],
        #      |     |
        [1,2,3,4,5,6,7,8,9],
        [1,2,3,4,5,6,7,8,9],
        [1,2,3,4,5,6,7,8,9],
        #      |     |
        [1,2,3,4,5,6,7,8,9],
        [1,2,3,4,5,6,7,8,9],
        [1,2,3,4,5,6,7,8,9],
        #      |     |
        ]


############################################################################################  
def print_grid():                       # prints the sudoko grid duh. -_-
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