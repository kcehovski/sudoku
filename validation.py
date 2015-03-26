SIZE = 9

def read_sudoku_from_file(filename):
    sudo = open(filename).readlines()
    sudoku = []
    for i in sudo: 
        i = i.strip().split()
        b = fix_list(i)
        sudoku.append(b)
    return sudoku
    
def copy_of_sudoku(ll):
    sudoku1 = []
    for x in ll:
        sudoku1.append(x)
    return sudoku1
    
def fix_list(l):
    a = []
    for x in l:
        if x == '-':
            a.append(-1)
        else:
            a.append(int(x))
    return a

def is_sequence_valid(l):
    for x in range(1, 10):
        if not (x in l):
            return False
    return True

def get_row(ll, i):
    return ll[i]
    
def get_column(ll, i):
    a = []
    for j in range(0, SIZE):
        a.append(ll[j][i])
#    print a
    return a    
    
def get_square(ll, x, y):
    a = []
    for i in range(x, x+3):
        for j in range(y, y+3):
            a.append(ll[i][j])
    #print a
    return a

def is_sudoku(ll):
    if not (len(ll) == SIZE):
        return False
        
    for x in ll:
        if not (len(x) == SIZE):
            return False
           
    return True
    
def is_valid(ll):
    if not (is_sudoku(ll)):
        return False
    
    for x in range(0, SIZE):
        if not is_sequence_valid(get_row(ll, x)):
            return False

    for y in range(0, SIZE):
        if not is_sequence_valid(get_column(ll, y)):
            return False
    
    for x in range(0, SIZE, 3):
        for y in range(0, SIZE, 3):
            if not (is_sequence_valid(get_square(ll, x, y))):
                return False
    
    return True