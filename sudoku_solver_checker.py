from sqlalchemy import true


board = [ [ 7, 9, 2, 1, 5, 4, 3, 8, 6 ],
            [ 6, 4, 3, 8, 2, 7, 1, 5, 9 ],
            [ 8, 5, 1, 3, 9, 6, 7, 2, 4 ],
            [ 2, 6, 5, 9, 7, 3, 8, 4, 1 ],
            [ 4, 8, 9, 5, 6, 1, 2, 7, 3 ],
            [ 3, 1, 7, 4, 8, 2, 9, 6, 5 ],
            [ 1, 3, 6, 7, 4, 8, 5, 9, 2 ],
            [ 9, 7, 4, 2, 1, 5, 6, 3, 8 ],
            [ 5, 2, 8, 6, 3, 9, 4, 1, 7 ] ]
def constraint_sudoku(board):
    valid = False
    for i in board :
        for j in i:
            check = j
            if(check<=9):
                valid = True

def square_checker(board):
    valid = True
    head_row=0
    for times in range(0,3):
        
        
        count = 0
        
        head_column =0 
        for time in range(0,3):
            
            row = head_row
            square = set()
            for rowi in range(row,row+3):  
                column = head_column           
                for columni in range(column,column+3): 
                    square.add(board[rowi][columni])
                    #print(board[rowi][columni])
                    #count+=1
            if(len(square)!=9):
                valid = False
            head_column+=3
        head_row+=3
    if(valid == True):
        print("It is a valid sudoku")
    else:
        print("It is not a valid sudoku")
    #print(count)
def row_check(board):
    square = set()
    for i in board:
        for j in i:
            square.add(j)
        if(len(board)!=9):
            return False
    return True
def column_check(board):

square_checker(board)