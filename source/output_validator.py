#!/usr/bin/env python3
"""
A-Maze-ing Output Validator

This script validates the coherence of maze output files by checking that
neighboring cells sharing a wall have consistent wall encoding on both sides.

The validator checks the hexadecimal wall encoding where each digit represents:
- Bit 0 (LSB): North wall
- Bit 1: East wall  
- Bit 2: South wall
- Bit 3: West wall

Usage:
    python3 output_validator.py <output_file>

Author: 42 School
Version: 1.0
"""

import sys
import os
from typing import List, Tuple


def load_maze_from_file(filename: str) -> List[List[int]]:
    """
    Load maze data from the output file.
    
    Args:
        filename: Path to the maze output file
        
    Returns:
        2D list representing the maze grid with hexadecimal values converted to integers
        
    Raises:
        FileNotFoundError: If the specified file doesn't exist
        ValueError: If the file contains invalid hexadecimal characters
    """
    if not os.path.exists(filename):
        raise FileNotFoundError(f"File '{filename}' not found")
    
    maze_grid = []
    
    try:
        with open(filename, 'r') as file:
            for line_num, line in enumerate(file, 1):
                stripped_line = line.strip()
                
                if stripped_line == '':
                    break
                    
                row = []
                for char in stripped_line:
                    if char in ' \t\n\r':
                        continue
                    row.append(int(char, 16))
                
                if row:
                    maze_grid.append(row)
                    
    except ValueError as e:
        raise ValueError(f"Invalid hexadecimal character in line {line_num}: {e}")
    
    return maze_grid


def validate_wall_coherence(maze_grid: List[List[int]]) -> List[Tuple[int, int]]:
    """
    Validate that neighboring cells have coherent wall encoding.
    
    Args:
        maze_grid: 2D list representing the maze
        
    Returns:
        List of (x, y) coordinates where wall encoding is inconsistent
    """
    if not maze_grid or not maze_grid[0]:
        return []
    
    errors = []
    rows = len(maze_grid)
    
    for row in range(rows):
        cols = len(maze_grid[row])  # Get actual column count for this row
        
        for col in range(cols):
            cell_value = maze_grid[row][col]
            
            wall_checks = []
            
            if row > 0 and col < len(maze_grid[row-1]):
                wall_checks.append((cell_value & 1, (maze_grid[row-1][col] >> 2) & 1, "North"))
            
            if col < cols-1:
                wall_checks.append(((cell_value >> 1) & 1, (maze_grid[row][col+1] >> 3) & 1, "East"))
            
            if row < rows-1 and col < len(maze_grid[row+1]):
                wall_checks.append(((cell_value >> 2) & 1, maze_grid[row+1][col] & 1, "South"))
            
            if col > 0:
                wall_checks.append(((cell_value >> 3) & 1, (maze_grid[row][col-1] >> 1) & 1, "West"))
            
            for current_wall, neighbor_wall, direction in wall_checks:
                if current_wall != neighbor_wall:
                    errors.append((col, row))
                    break
    
    return errors


def main():
    """Main function to run the maze validator."""
    if len(sys.argv) != 2:
        print(f"Usage: python3 {sys.argv[0]} <output_file>")
        print("\nThis validator checks that neighboring cells sharing a wall")
        print("have consistent wall encoding on both sides.")
        sys.exit(1)
    
    filename = sys.argv[1]
    
    try:
        maze_grid = load_maze_from_file(filename)
        
        if not maze_grid:
            print("Error: Empty maze file or no valid maze data found")
            sys.exit(1)
        
        print(f"Loaded maze: {len(maze_grid)} rows × {len(maze_grid[0])} columns")
        
        errors = validate_wall_coherence(maze_grid)
        
        if errors:
            print(f"\nValidation FAILED: Found {len(errors)} cell(s) with inconsistent wall encoding:")
            for x, y in errors:
                print(f"  - Wrong encoding at position ({x}, {y})")
            sys.exit(1)
        else:
            print("\nValidation PASSED: All neighboring walls are coherent")
            
    except FileNotFoundError as e:
        print(f"Error: {e}")
        sys.exit(1)
    except ValueError as e:
        print(f"Error: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"Unexpected error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
