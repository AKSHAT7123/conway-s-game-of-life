import numpy as np
import time
import os

def print_grid(grid):
    """Print the grid to the console."""
    os.system('cls' if os.name == 'nt' else 'clear')  # Clear the screen for better visibility
    for row in grid:
        print("".join(["■" if cell else " " for cell in row]))
    print()

def get_next_generation(grid):
    """Calculate the next generation of the grid."""
    rows, cols = grid.shape
    next_grid = np.zeros((rows, cols), dtype=int)
    
    for row in range(rows):
        for col in range(cols):
            # Count live neighbors
            live_neighbors = sum([
                grid[(row - 1) % rows, (col - 1) % cols],  # Top-left
                grid[(row - 1) % rows, col],              # Top
                grid[(row - 1) % rows, (col + 1) % cols],  # Top-right
                grid[row, (col - 1) % cols],              # Left
                grid[row, (col + 1) % cols],              # Right
                grid[(row + 1) % rows, (col - 1) % cols],  # Bottom-left
                grid[(row + 1) % rows, col],              # Bottom
                grid[(row + 1) % rows, (col + 1) % cols]   # Bottom-right
            ])
            
            # Apply rules of the Game of Life
            if grid[row, col] == 1 and (live_neighbors == 2 or live_neighbors == 3):
                next_grid[row, col] = 1
            elif grid[row, col] == 0 and live_neighbors == 3:
                next_grid[row, col] = 1

    return next_grid

def main():
    rows, cols = 20, 40  # Grid size
    grid = np.random.choice([0, 1], size=(rows, cols))  # Random initial state

    while True:
        print_grid(grid)
        grid = get_next_generation(grid)
        time.sleep(0.5)  # Pause for a short time between generations

if __name__ == "__main__":
    main()
