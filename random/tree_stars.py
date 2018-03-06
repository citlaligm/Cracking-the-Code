def print_tree_left(number_rows):
    '''
    print a tree made with asterisks of this from:
    *
    **        
    ***
    ****
    *****    
    '''
    for row in range (number_rows+1):
        blank_spaces = " "*(number_rows-row)
        stars = "*"*row
        print(stars+blank_spaces)
        
        
        
def print_tree_right(number_rows):
    '''
    print a tree made with asterisks of this from:
            *
           **        
          ***
         ****
        *****    
    '''
    for row in range (number_rows+1):
        blank_spaces = " "*(number_rows-row)
        stars = "*"*row
        print(blank_spaces+stars)
        
        
def print_tree_inverted(number_rows):
    '''
    print a tree made with asterisks of this from:
        *****
        ****
        ***
        **
        *
    '''
    for row in range(number_rows,0,-1):
        
        blank_spaces = " "*(number_rows-row)
        stars = "*"*row
        print(stars+blank_spaces)
        
        
def print_tree_center_spaces(base_number):
    '''
    print a tree made with asterisks of this from:
            *
           * *        
          * * *
         * * * *
        * * * * *
    '''
    
    left = base_number
    row = 1
    
    while row <= base_number:
        print(left*" ",row*"* ")
        left -= 1
        row += 1
        
    
    
def print_tree_center(number_rows):
    '''
    print a tree made with asterisks of this from:  
            *
           ***
          *****
         *******
        *********
    '''
    for row in range(number_rows):
        blank_spaces = ' '*(number_rows-row-1)
        stars = "*"*(2*row+1)

        print (blank_spaces + stars)

            