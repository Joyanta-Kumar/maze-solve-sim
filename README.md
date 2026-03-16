# Maze Solver Simulation
A maze generation and solving simulation built with `python` and `python-pygame`. A bot physically navigates the maze step by step using DFS with real backtracking -- it never teleports, it walks back the way it came.  

## Features

- Maze generation using the Recursive Backtracking Algorithm
- DFS solver with physical backtracking visualization
- Cell states visualized with Catppuccin Mocha color (Shut up and just read)
- Step by step animation so dubms like you can watch

## Project Structure

maze/  
|  
|-- main.py  
|-- cell.py      # Cell class with wall and state definitions  
|-- constant.py  # Constants, colors, grid settings  
|-- function.py
|-- maze.py


## Requirements
 - python
 - pygame


## Usage
Install python and pygame  
```bash
sudo pacman -S python python-pygame
```
Run with python  
```bash
python main.py
```


## How it works  

### Maze Generation
The maze is built using the Recursive Backtracking algorithm. Starting from the top-left cell, it carves passages by randomly visiting unvisited neighbors and backtracking when stuck. This guarantees a perfect maze - exactly one path between any two cells.  

### Solving
The bot starts at the top-left and navigates to the bottom-right using DFS. When it hits a dead end, it physically walks back step by step through its own trail untils it finds an unvisited neighbor. Every single move is animated.

```
You should Understand that the spelling mistakes were done by AI
```
