from src import *

sudoku_puzzle = [0,0,0,2,6,0,7,0,1,6,8,0,0,7,0,0,9,0,1,9,0,0,0,4,5,0,0,8,2,0,1,0,0,0,4,0,0,0,4,6,0,2,9,0,0,0,5,0,0,0,3,0,2,8,0,0,9,3,0,0,0,7,4,0,4,0,0,5,0,0,3,6,7,0,3,0,1,8,0,0,0,]
#sudoku_puzzle = [0,0,5,0,1,0,0,0,0,0,2,0,4,0,0,0,0,1,0,9,0,5,0,0,0,8,0,5,0,8,0,0,0,3,0,0,0,7,2,0,4,0,1,6,0,0,0,6,0,0,0,7,0,2,0,5,0,0,0,1,0,2,0,7,0,0,0,0,8,0,3,0,0,0,0,0,3,0,6,0,0,]
sudoku_solver = SudokuSolver(sudoku_puzzle)
sudoku_solver.solve() # timer = False, sound = True
sudoku_solver.check_grid()
sudoku_solver.print_grid()

#sudoku_example = SudokuGenerator() # size = 9
#sudoku_example.generate() # timer = False, sound = True
#sudoku_example.check_grid()
#sudoku_example.print_grid()
#Helper.store(sudoku_example) # storing grid to file ./storage/9x9.csv
