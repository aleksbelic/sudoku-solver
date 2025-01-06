import math
from .sudoku_helper import SudokuHelper

class SudokuPuzzle:
    """SudokuPuzzle class."""
    
    def __init__(self, size):
        self.size = size
        self.grid = []

    def grid_values_to_list(self):
        """Generates list with grid values."""
        values_list = []
        for row_index in range(self.size):
            for column_index in range(self.size):
                values_list.append(str(self.grid[row_index][column_index]["value"]))
        return values_list

    def generate_cell_candidates(self, cell_row_index, cell_column_index):
        """Generates candidate list for specific cell."""
        candidates_to_validate = SudokuHelper.get_rand_unique_int_list(1, self.size)
        valid_candidates = []
        for candidate in candidates_to_validate:
            if self.check_candidate(cell_row_index, cell_column_index, candidate):
                valid_candidates.append(candidate)
        return valid_candidates

    def check_grid(self):
        """Checks sudoku grid cell by cell."""
        for row_index in range(self.size):
            for column_index in range(self.size):
                if not self.check_candidate(row_index, column_index, self.grid[row_index][column_index]["value"]):
                    return False
        return True

    def check_candidate(self, candidate_row_index, candidate_column_index, candidate):
        """Check if candidate is valid in current cell."""
        # checking row
        if self.__class__.__name__ == "SudokuGenerator":
            for i in range(candidate_column_index): # candidate_column_index excluded
                if self.grid[candidate_row_index][i]["value"] == candidate:
                    return False
        elif self.__class__.__name__ == "SudokuSolver":
            for i in range(self.size):
                if self.grid[candidate_row_index][i]["value"] == candidate:
                    return False

        # checking column
        if self.__class__.__name__ == "SudokuGenerator":
            for j in range(candidate_row_index): # candidate_row_index excluded
                if self.grid[j][candidate_column_index]["value"] == candidate:
                    return False
        elif self.__class__.__name__ == "SudokuSolver":
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

    def print_grid(self):
        """Prints sudoku grid."""
        sizeSqrt = int(math.sqrt(self.size))
        for row_index in range(self.size):
            # printing horizontal dashes
            if row_index != 0 and row_index % sizeSqrt == 0:
                dashes = ""
                for box_counter in range(sizeSqrt):
                    if box_counter != 0:
                        dashes += "+"
                    for _ in range(sizeSqrt):
                        dashes += "---"
                print(dashes)
            # printing row
            row = ""
            for cell_index, cell in enumerate(self.grid[row_index]):
                if cell_index != 0 and cell_index % sizeSqrt == 0:
                    row += "|"
                row += " " + str(cell["value"]) + " "
            print(row)
