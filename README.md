# Sudoku Solver

Sudoku Solver is a straightforward terminal-based app built with `Python 3`. It allows users to both solve Sudoku puzzles and generate new ones.

### Usage

All examples can be found in the **demo.py** file.

### Solving a Sudoku puzzle

Solving a Sudoku puzzle is done using **SudokuSolver** class. Constructor parameter:
- **puzzle_grid**, list[int], puzzle values placed inside a list with **0** in place where puzzle cell is empty, default is [] (empty list)

Method **solve()** solves the puzzle. It accepts 1 parameter:
- **timer** - boolean, determines whether time should be measured, default is False
```
sudoku_puzzle = [0,0,5,0,1,0,0,0,0,0,2,0,4,0,0,0,0,1,0,9,0,5,0,0,0,8,0,5,0,8,0,0,0,3,0,0,0,7,2,0,4,0,1,6,0,0,0,6,0,0,0,7,0,2,0,5,0,0,0,1,0,2,0,7,0,0,0,0,8,0,3,0,0,0,0,0,3,0,6,0,0,]
sudoku_solver = SudokuSolver(sudoku_puzzle)
sudoku_solver.solve() # timer = False
sudoku_solver.print_grid()
```
Output:
```
Generating grid...
Done!
 6  4  5 | 8  1  7 | 2  9  3
 8  2  3 | 4  9  6 | 5  7  1
 1  9  7 | 5  2  3 | 4  8  6
---------+---------+---------
 5  1  8 | 6  7  2 | 3  4  9
 9  7  2 | 3  4  5 | 1  6  8
 4  3  6 | 1  8  9 | 7  5  2
---------+---------+---------
 3  5  4 | 9  6  1 | 8  2  7
 7  6  1 | 2  5  8 | 9  3  4
 2  8  9 | 7  3  4 | 6  1  5
```

### Creating a new puzzle

Generating new puzzle is done using **SudokuGenerator** class. Constructor parameter:
- **size**, integer, defines grid size, default is 9

Method **generate()** generates new, fully solved puzzle from scratch. It accepts 1 parameter: 
- **timer**, boolean, defines if time should be measured, default is False
```
sudoku_example = SudokuGenerator() # size = 9
sudoku_example.generate() # timer = False
sudoku_example.print_grid()
```
Output:
```
Generating grid...
Done!
 6  9  1 | 2  7  4 | 5  8  3
 7  3  5 | 9  6  8 | 1  2  4
 4  2  8 | 3  5  1 | 6  9  7
---------+---------+---------
 9  8  4 | 5  2  6 | 3  7  1
 2  6  7 | 1  8  3 | 9  4  5
 5  1  3 | 7  4  9 | 2  6  8
---------+---------+---------
 1  5  6 | 4  9  7 | 8  3  2
 3  4  9 | 8  1  2 | 7  5  6
 8  7  2 | 6  3  5 | 4  1  9
```

### Saving generated puzzles

New puzzles are stored using the **SudokuHelper** class. Puzzles are saved in the **sudoku-puzzles** folder as comma-separated values (CSV) based on their grid size: 4x4 puzzles are saved to `4x4.csv`, 9x9 to `9x9.csv` etc. Only unique grids are stored, with duplicates automatically ignored.
```
sudoku_example = SudokuGenerator() # size = 9, timer = False
sudoku_example.generate()
Helper.store(sudoku_example) # storing grid to file ./storage/9x9.csv
```