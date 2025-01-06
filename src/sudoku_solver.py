import math, time
from .sudoku_puzzle import SudokuPuzzle
from .sudoku_helper import SudokuHelper

class SudokuSolver(SudokuPuzzle):
    """SudokuSolver class."""

    def __init__(self, puzzle_grid: list[int] = []):

        puzzle_grid_size = math.sqrt(len(puzzle_grid))
        if not puzzle_grid_size.is_integer():
            raise ValueError(
                "Square root of the number of cells in the grid should be an integer. "
                f"The square root of {len(puzzle_grid)} is {puzzle_grid_size}."
            )
        
        self.size = int(puzzle_grid_size)
        self.grid = []
        puzzle_grid_counter = 0
        for row_index in range(self.size):
            self.grid.append([])
            for _ in range(self.size):
                if puzzle_grid[puzzle_grid_counter] == 0:
                    self.grid[row_index].append(dict(
                        value = "_",
                        fixed = False,
                        candidates = [],
                    ))
                else:
                    self.grid[row_index].append(dict(
                        value = puzzle_grid[puzzle_grid_counter],
                        fixed = True
                    ))
                puzzle_grid_counter += 1

        # generating candidates
        for row_index in range(self.size):
            for column_index in range(self.size):
                if not self.grid[row_index][column_index]["fixed"]:
                    self.grid[row_index][column_index]["candidates"] = self.generate_cell_candidates(row_index, column_index)

    def check_candidate(self, candidate_row_index, candidate_column_index, candidate, only_fixed = False):
        """Check if candidate is valid in current cell."""
        # checking row
        for i in range(self.size):
            if self.grid[candidate_row_index][i]["value"] == candidate:
                return False

        # checking column
        for j in range(self.size): # candidate_row_index excluded
            if self.grid[j][candidate_column_index]["value"] == candidate:
                return False

        #checking box
        sqrtSize = int(math.sqrt(self.size))
        candidate_box_row_index = int(candidate_row_index / sqrtSize)
        candidate_box_column_index = int(candidate_column_index / sqrtSize)
        for i in range(candidate_box_row_index * self.size, (candidate_box_row_index + 1) * sqrtSize):
            for j in range(candidate_box_column_index * self.size, (candidate_box_column_index + 1) * sqrtSize):
                if candidate_row_index != i and candidate_column_index != j: # don't compare to itself
                    if candidate == self.grid[i][j]["value"]:
                        return False
        return True # candidate is valid

    def solve(self, timer = False, sound = True):
        """Generates random sudoku grid."""
        print("Generating grid...")
        if timer:
            start_time = time.time()

        row_index = 0
        column_index = 0
        while (row_index < self.size):
            if self.grid[row_index][column_index]["fixed"] == False:
                while True: 
                    try:
                        candidate = self.grid[row_index][column_index]["candidates"][0]
                    except IndexError: # candidates list is empty
                        self.grid[row_index][column_index]["candidates"] = SudokuHelper.get_shuffled_range(1, self.size)
                        self.grid[row_index][column_index]["value"] = "_"
                        while True:
                            if column_index != 0:
                                column_index -= 1
                            else:
                                column_index = self.size - 1
                                row_index -= 1
                            if self.grid[row_index][column_index]["fixed"] == False:
                                break
                        break
                        
                    if self.check_candidate(row_index, column_index, candidate): # check candidate
                        self.grid[row_index][column_index]["candidates"].remove(candidate)
                        self.grid[row_index][column_index]["value"] = candidate
                        column_index += 1
                        if column_index == self.size:
                            column_index = 0
                            row_index += 1
                        break
                    else:
                        self.grid[row_index][column_index]["candidates"].remove(candidate)
            else:
                column_index += 1
                if column_index == self.size:
                    column_index = 0
                    row_index += 1

        print("Done!")
        if timer:
            print("Grid generated in %s sec" % (time.time() - start_time))

