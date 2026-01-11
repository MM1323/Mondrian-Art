# Mondrian-Art

A Python program that generates pseudo-random art in the style of Piet Mondrian using recursion and turtle graphics.

## Project Overview

This project creates Mondrian-inspired abstract paintings by recursively subdividing rectangular regions and filling them with random colors. The algorithm randomly splits rectangles either vertically or horizontally, with randomized split points, then recursively applies the same process to each subdivision until the desired recursion depth is reached.

## Features

-   **Recursive Algorithm**: Uses recursion to generate intricate nested rectangle patterns
-   **Random Color Generation**: Assigns random colors (red, skyblue, yellow, and white) to rectangles
-   **Randomized Splits**: Each rectangle is randomly split either vertically or horizontally with varying ratios (1/3-2/3 or 2/3-1/3)
-   **Adjustable Complexity**: Recursion depth is randomized between 3-7 levels for varied artwork
-   **Turtle Graphics**: Uses Python's built-in turtle module for visualization

## Requirements

-   Python 3.x
-   turtle module (included with Python)

## Usage

Run the program from the command line:

```bash
python hw10_mondrian.py
```

The program will:

1. Create a turtle graphics window
2. Generate a random Mondrian-style artwork
3. Display the completed artwork
4. Close when you click the window

Each run produces a unique artwork due to the randomized nature of the recursion.

## How It Works

1. **Main Canvas**: Starts with a 1024x768 pixel canvas
2. **Recursive Subdivision**:
    - Draws a rectangle with a random color
    - Randomly chooses vertical or horizontal split
    - Randomly selects split ratio (1:2 or 2:1)
    - Recursively applies the process to each subdivided region
3. **Base Case**: Stops when recursion depth reaches 0

## Technical Details

-   **Canvas Size**: 1024 x 768 pixels
-   **Pen Size**: 5 pixels for visible borders
-   **Color Palette**: Red, Sky Blue, Yellow, and White
-   **Recursion Levels**: 3-7 (randomly selected per run)
