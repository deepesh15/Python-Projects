size = 9  #size of sudoko grid

#cells with 0 are vacant

grid =[#      |     |
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

def print_grid():               # prints the sudoko grid duh. -_-
    for i in grid:
        print (i)

#print_grid()                    #function call just to check it is working