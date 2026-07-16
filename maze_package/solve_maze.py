from .dict_validate import MazeConfig
from .create_maze import Cell


def solve_maze(
        maze: list[list[Cell]], maze_config: MazeConfig
        ) -> list[tuple[int, int]]:
    """
    Solves the maze using Depth-First Search (DFS)
    Returns a list of (x, y) coordinates
    representing the path from entry to exit

    Made by mabu-are
    """
    start: tuple[int, int] = maze_config.entry
    end: tuple[int, int] = maze_config.exit

    stack: list[tuple[int, int]] = [start]
    visited: set[tuple[int, int]] = {start}

    parent_map: dict[tuple[int, int], tuple[int, int]] = {}

    while stack:
        current = stack.pop()

        # if we reached our target node (end)
        if current == end:
            break

        curr_x, curr_y = current
        for neighbor in get_neighbors(curr_x, curr_y, maze, maze_config):
            if neighbor not in visited:
                visited.add(neighbor)
                parent_map[neighbor] = current
                stack.append(neighbor)

    if end not in visited:
        return []

    # the last path that we sure its correct
    path: list[tuple[int, int]] = []
    curr_node: tuple[int, int] = end

    while curr_node != start:
        path.append(curr_node)
        curr_node = parent_map[curr_node]

    path.append(start)
    path.reverse()

    return path


def get_neighbors(
        x: int, y: int, maze: list[list[Cell]], maze_config: MazeConfig
        ) -> list[tuple[int, int]]:
    """
    Acts as the graph edge lookup

    Returns adjacent cells (neighbors) that are connected to (x, y)
    by an open path (no wall between them)

    Made by mabu-are
    """
    neighbors: list[tuple[int, int]] = []

    # 1. North neighbor: check if we can go up
    if y > 0 and not maze[y][x].north:
        neighbors.append((x, y - 1))

    # 2. South neighbor: check if we can go down
    if y < maze_config.height - 1 and not maze[y][x].south:
        neighbors.append((x, y + 1))

    # 3. East neighbor: check if we can go right
    if x < maze_config.width - 1 and not maze[y][x].east:
        neighbors.append((x + 1, y))

    # 4. West neighbor: check if we can go left
    if x > 0 and not maze[y][x].west:
        neighbors.append((x - 1, y))

    return neighbors
