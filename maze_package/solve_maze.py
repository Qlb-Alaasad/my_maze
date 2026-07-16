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
    # 1. North neighbor: check current cell's North AND neighbor's South
    if (
        y > 0
        and not maze[y][x].north
        and not maze[y - 1][x].south
    ):
        neighbors.append((x, y - 1))

    # 2. South neighbor: check current cell's South AND neighbor's North
    if (
        y < maze_config.height - 1
        and not maze[y][x].south
        and not maze[y + 1][x].north
    ):
        neighbors.append((x, y + 1))

    # 3. East neighbor: check current cell's East AND neighbor's West
    if (
        x < maze_config.width - 1
        and not maze[y][x].east
        and not maze[y][x + 1].west
    ):
        neighbors.append((x + 1, y))

    # 4. West neighbor: check current cell's West AND neighbor's East
    if (
        x > 0
        and not maze[y][x].west
        and not maze[y][x - 1].east
    ):
        neighbors.append((x - 1, y))
    return neighbors
