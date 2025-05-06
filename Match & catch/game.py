#****************************************************
#
#  Written by: Neelendra Mishra
#
#*****************************************************

#                                                                - - - - START OF THE CODE - - - -

# Importing necessary modules
import os  
import time 
import sys  

# Importing PuzzleGrid class from grid.py
from grid import PuzzleGrid  


# Function to clear the terminal screen
def clear_screen():
    os.system("clear")


# Function to display the game menu
def show_menu():
    print("1. Select two tiles")  
    print("2. Reveal one tile")  
    print("3. Surrender - Show solution")  
    print("4. Start a new game")  
    print("5. Quit") 


# Function to compute the score based attempts
def compute_score(ideal_attempts, actual_attempts):
    return (ideal_attempts / actual_attempts) * 100 if actual_attempts > 0 else 0


# Main function 
def main_game():
    # Ensuring the valid command line arguments for the grid 
    if len(sys.argv) < 2 or sys.argv[1] not in ['2', '4', '6']:
        print("Error: Please choose a grid size of 2, 4, or 6.")
        sys.exit(1)


    # Extracting the board size from the command line argument
    board_size = int(sys.argv[1])
    memory_game = PuzzleGrid(board_size) 
    attempts = 0  
    minimum_attempts = (board_size * board_size) // 2  
    revealed_only = True  

    while True:
        # Clearing the screen and displaying the game board and menu on the screen
        clear_screen()
        memory_game.show_board()
        show_menu()
        choice = input("Enter your choice: ")  # Get user's menu choice

        if choice == '1':           # CAse 1: Handle selecting two tiles
            attempts += 1           # Incrementing attempts
            revealed_only = False   # Set cheat detection to false

            # Getting the coordinates for the first and second tile
            first_r, first_c = get_coordinates(board_size)
            second_r, second_c = get_coordinates(board_size)


            # Preventing in selecting the same tile twice
            if (first_r, first_c) == (second_r, second_c):
                print("Error: Same cell chosen twice. Try again.")
                continue


            # Revealing the chosen tiles
            first_value = memory_game.uncover_cell(first_r, first_c)
            second_value = memory_game.uncover_cell(second_r, second_c)
            clear_screen()
            memory_game.show_board()
            time.sleep(2)  # Pause to allow the user to see the revealed tiles

            # Checking if the selected tiles matches
            if memory_game.validate_match(first_r, first_c, second_r, second_c):
                print("Match found!")
            else:
                print("No match!")
                # Hide the tiles if they don't match
                memory_game.conceal_cell(first_r, first_c)
                memory_game.conceal_cell(second_r, second_c)

        elif choice == '2':  # Case 2: Handling the revealing value on tile
            attempts += 2  
            row, col = get_coordinates(board_size)  
            memory_game.uncover_cell(row, col)      
            clear_screen()
            memory_game.show_board()

            # Checking if all the tiles are revealed without matching
            if revealed_only and memory_game.are_all_cells_revealed():
                print("Cheat detected. Your score is 0.")  
                break

        elif choice == '3':  # Case 3: Handle surrendering and revealing the solution
            print("Revealing the solution:")
            memory_game.reveal_entire_board()  # Reveal the entire board
            memory_game.show_board()
            break  # Exiting the game loop

        elif choice == '4':  # Case 4: Handle starting a new game
            memory_game = PuzzleGrid(board_size)  # Reset the game
            attempts = 0  # Reseting the attempts to 0
            revealed_only = True  # Reset the cheat detection flag
            continue  # Restart the game loop

        elif choice == '5':  # Case 5: Ending the game
            print("Thank you for playing!")  
            break  # Exiting the game loop

        else:  # Handling the invalid menu input
            print("Invalid input. Please try again.")
            continue

        # Validating if all matches have been found
        if memory_game.matches_found == minimum_attempts:
            if revealed_only:  # Detect if cheating occurred
                print("You cheated - Loser! Your score is 0.")
            else:
                # Calculate and display the final score
                final_score = compute_score(minimum_attempts, attempts)
                print(f"Congratulations! You scored: {final_score:.2f}")
            break  # Exiting the game loop

# Function to get valid tile coordinates from the user
def get_coordinates(grid_dim):
    while True:
        user_input = input("Enter tile (e.g., A0): ").strip().upper()  # Get user input
        # Validating the input format
        if len(user_input) < 2 or not user_input[0].isalpha() or not user_input[1:].isdigit():
            print("Invalid input. Try again.")
            continue

        column = ord(user_input[0]) - 65  # Converting the column letter to number
        row = int(user_input[1:])         # Extract the row number

        # Validating if the coordinates are within bounds
        if 0 <= row < grid_dim and 0 <= column < grid_dim:
            return row, column  # Return valid coordinates
        else:
            print("Invalid cell. Try again.")

# Entry point for the game
if __name__ == "__main__":
    main_game()


#                                       - - - - END OF THE CODE - - - -