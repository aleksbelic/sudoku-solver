import random, csv

class SudokuHelper:
    """SudokuHelper class. Used for additional Sudoku methods."""

    @staticmethod
    def get_shuffled_range(min: int, max: int) -> list[int]:
        """
        Returns a shuffled list of unique integers between min and max (inclusive).

        Args:
            min (int): The minimum value in the range.
            max (int): The maximum value in the range.
        
        Returns:
            list[int]: A list of unique integers in the specified range.
    
        Raises:
            ValueError: If min is greater than max.
        """

        if min > max:
            raise ValueError("Min value should not be greater than max value.")
    
        return random.sample(range(min, max + 1), max - min + 1)

    @staticmethod

    def store(sudoku_puzzle) -> None:

        """Stores generated grid to appropriate CSV file. No duplicates will be added."""
        csv_file_name = str(sudoku_puzzle.size) + "x" + str(sudoku_puzzle.size) + ".csv"
        csv_file_path = "sudoku-puzzles/" + csv_file_name
        try:
            with open(csv_file_path, "r", newline="") as csv_file:
                csv_file_reader = csv.reader(csv_file)
                grid_list = [grid for grid in csv_file_reader]
                if not (sudoku_puzzle.grid_values_to_list() in grid_list):
                    grid_list.append(sudoku_puzzle.grid_values_to_list())
                    
            with open(csv_file_path, "w", newline="") as csv_file:
                csv_file_writer = csv.writer(csv_file)
                for grid in grid_list:
                    csv_file_writer.writerow(grid)
        except FileNotFoundError:
            exit("ERROR: Sudoku puzzle could not be stored, file \"" + csv_file_path + "\" was not found.")

    @staticmethod
    def remove_duplicates_from_storage(csv_file_name: str) -> None:
        """Removes all duplicates from storage file."""

        duplicate_counter = 0
        csv_file_path = "sudoku-puzzles/" + csv_file_name
        try:
            with open(csv_file_path, "r", newline="") as csv_file:
                csv_file_reader = csv.reader(csv_file)
                grid_list = [grid for grid in csv_file_reader]
                grid_list_unique = []
                for i in range(0, len(grid_list)):
                    if not grid_list[i] in grid_list_unique:
                        grid_list_unique.append(grid_list[i])
                    else:
                        duplicate_counter += 1
                    
            with open(csv_file_path, "w", newline="") as csv_file:
                csv_file_writer = csv.writer(csv_file)
                for grid in grid_list_unique:
                    csv_file_writer.writerow(grid)

            if duplicate_counter > 0:
                print(str(duplicate_counter) + (" duplicate" if duplicate_counter == 1 else " duplicates") + " removed.")
            else:
                print("No duplicates found.")

        except FileNotFoundError:
            exit("ERROR: Sudoku puzzle could not be stored, file \"" + csv_file_path + "\" was not found.")
