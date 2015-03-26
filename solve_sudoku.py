from __future__ import division
from pprint import pprint
import sys
import random
import itertools
from sudoku import validation

SIZE = 9
    
def putting_numbers_in_sudoku(sudoku):
    a = []
    for x in sudoku:
        b = []
        for y in x:
            if not (y == -1):
                b.append(y) 
            else:
                b.append(random.randint(0, SIZE))
        a.append(b)
    return a
                
def solving_sudoku_random(sudoku):
    a = putting_numbers_in_sudoku(sudoku)
    while not (validation.is_valid(a)):
        a = putting_numbers_in_sudoku(sudoku)
    return a
    
def insert(ll, v):
    c = 0
    a = []
    for x in ll:
        b = []
        for y in x:
            if not (y == -1):
                b.append(y) 
            else:
                b.append(v[c])
                c += 1
        a.append(b)
    return a

def count_empty(sudoku):
    n = 0
    for x in sudoku:
        for y in x:
            if y == -1:
                n += 1
    return n
    
def generate_values(n):
    choices = itertools.product(range(1, 10), repeat = n)
    return choices
    
def solving_sudoku_permutation(sudoku, values, number_of_empty_places):
    y = 0
    u = 9**number_of_empty_places
    for x in values:
        y += 1
        if y % 10000 == 0:
            print "%.2f %%" %((y/u) *100)
        a = insert(sudoku, x)
        if validation.is_valid(a):
            return a
    return None

def main(): 
    if len(sys.argv)!=3 or sys.argv[2] not in ['random', 'permutation']:
        print "Usage: python solve_sudoku.py [input_file] [permutation|random]"
        sys.exit(1)
    
    
    script, filename, solving = sys.argv
    
    sudoku = validation.read_sudoku_from_file(filename)
    number_of_empty_places = count_empty(sudoku)
    values = generate_values(number_of_empty_places)
    way_of_solving = solving

    pprint(sudoku)

    if way_of_solving == "random":
        pprint(solving_sudoku_random(sudoku))
    else:
        pprint(solving_sudoku_permutation(sudoku, values, number_of_empty_places))
    
if __name__ == '__main__':
    main()
    