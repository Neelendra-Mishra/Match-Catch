#****************************************************
#
#  Written by: Neelendra Mishra
#
#*****************************************************

#                                                                - - - - START OF THE CODE - - - -


# Importing the random module for shuffling values
import random

# Creating a Class representing the PuzzleGrid for the memory game
class PuzzleGrid:

    # Creating the Constructor to initialize the grid with the given dimension
    def __init__(self, dimension):
        self.dimension = dimension      # Size of the grid (dimension x dimension)
        self.solution_board = []        # Storing the actual solution values
        self.hidden_board = []          # Storing the current hidden state of the board
        self.matches_found = 0          # Tracking the number of matches found by the player
        self.initialize_board()         # Calling the method to set up the board


    # Creating a method to initialize the solution and hidding the boards
    def initialize_board(self):
        total_pairs = (self.dimension * self.dimension) // 2  # Total pairs of tiles on the board

        # Creating a list of values, each appearing twice for pairing
        values = [n for n in range(total_pairs) for _ in range(2)]
        random.shuffle(values)  # Using a random to Randomize the order of the values

        # Creating the solution board as a 2D grid
        self.solution_board = [values[i:i + self.dimension] for i in range(0, len(values), self.dimension)]

        # Creating the hidden board filled with 'X' to conceal the solution
        self.hidden_board = [['X' for _ in range(self.dimension)] for _ in range(self.dimension)]

    # Method to display the current state of the hidden board
    def show_board(self):
        print("-------------------------")
        print("|       Memory Game     |")
        print("-------------------------")

        # Displaying the column headers (A, B, C, etc.)
        print("    " + " ".join(f"[{chr(65 + i)}]" for i in range(self.dimension)))

        # Displaying each row with row headers and current board state
        for r in range(self.dimension):
            row_content = " ".join(f" {self.hidden_board[r][c]} " for c in range(self.dimension))
            print(f"[{r}] {row_content}\n")

    # Creating a method to uncover a tile at the specified coordinates
    def uncover_cell(self, row, col):
        self.hidden_board[row][col] = str(self.solution_board[row][col])  # Reveal the value
        return self.solution_board[row][col]                              # Return the revealed value


    # Creating a method to hide a tile at the specified coordinates
    def conceal_cell(self, row, col):
        self.hidden_board[row][col] = 'X'  # Hide the value with 'X'

    # Creating a method to validate if two uncovered tiles form a matching pair
    def validate_match(self, r1, c1, r2, c2):
        if self.solution_board[r1][c1] == self.solution_board[r2][c2]:  # Check if values match
            self.matches_found += 1                                     # Incrementing match count
            return True                                                 # Returning True if it's a match
        return False                                                    # Returning False if it's not a match

    # Creating a method to reveal the entire board 
    def reveal_entire_board(self):
        for r in range(self.dimension):
            for c in range(self.dimension):
                self.hidden_board[r][c] = str(self.solution_board[r][c])  # Reveal all values

    # Creating a method to check if all tiles have been revealed
    def are_all_cells_revealed(self):
        return all('X' not in row for row in self.hidden_board)  # Return True if no 'X' remains


#                                       - - - - END OF THE CODE - - - -