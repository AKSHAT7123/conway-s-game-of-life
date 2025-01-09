# Game of Life

This project is an implementation of Conway's Game of Life in Python. The Game of Life is a cellular automaton devised by the British mathematician John Horton Conway in 1970. It is a zero-player game, meaning that its evolution is determined by its initial state, requiring no further input.

## Files

- `first.py`: Main implementation of the Game of Life.
- `diffrent_ways_to_import_library.py`: Examples of different ways to import libraries in Python.
- `module2_or_library.py`: Examples of using various Python libraries and modules.
- `practice1.py`: Practice problems and examples.

## How to Run

1. Ensure you have Python installed on your system.
2. Install the required libraries using pip:
    ```sh
    pip install numpy
    ```
3. Run the `first.py` script:
    ```sh
    python first.py
    ```

## How It Works

The [first.py](http://_vscodecontentref_/0) script initializes a random grid of cells, where each cell can be either alive (1) or dead (0). The grid evolves over time according to the following rules:

1. Any live cell with fewer than two live neighbors dies, as if by underpopulation.
2. Any live cell with two or three live neighbors lives on to the next generation.
3. Any live cell with more than three live neighbors dies, as if by overpopulation.
4. Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.

The script continuously updates the grid and prints it to the console, creating an animation of the Game of Life.

## Functions

- [print_grid(grid)](http://_vscodecontentref_/1): Clears the console and prints the current state of the grid.
- [get_next_generation(grid)](http://_vscodecontentref_/2): Calculates the next generation of the grid based on the current state.
- [main()](http://_vscodecontentref_/3): Initializes the grid and runs the main loop to update and print the grid.

## Example Output
