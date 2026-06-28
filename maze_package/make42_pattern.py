from sys import stderr
from .dict_validate import ConfigError, MazeConfig


def make_42_pattern(maze_config: MazeConfig) -> list[list[bool]]:
    """
    This function is to make 42 pattern
    first make a list of lists (row,colom)
                                ^^  ^^^^
                                y  , x

    made by mabu-are

    Returns:
        list[list[bool]]: same shape as need_open
        True where '42' cells should be closed
        or dont need to open
    """
    need_open = [
            [False] * maze_config.width for _ in range(maze_config.height)
                 ]
    if maze_config.width < 10 or maze_config.height < 7:
        print(
                "Warning: maze too small for '42' pattern, omitting",
                file=stderr
                )
        return need_open

    elif maze_config.width > 29 and maze_config.height > 29:
        block_size = 3
    else:
        block_size = 1

    def draw_block(start_col: int, start_row: int) -> None:
        """
        This function is to draw a thick block instead of a single cell
        it takes the starting point (start_col, start_row)
                                       ^^^^^^^^^ , ^^^^^^^^^
                                           x     ,     y

        modifies need_open directly by making a block size of True

        made by mabu-are
        """
        for row_offset in range(block_size):
            for col_offset in range(block_size):
                current_row = start_row + row_offset
                current_col = start_col + col_offset

                if not all(
                    (
                        (current_col, current_row) != maze_config.entry,
                        (current_col, current_row) != maze_config.exit,
                    )
                ):
                    raise ConfigError(
                        "Invalid configuration: '42' pattern overlaps"
                        " with entry or exit."
                    )

                need_open[current_row][current_col] = True

    pattern_offsets = [
        # 4
        (-3, -2), (-3, -1), (-3, 0),
        (-2, 0), (-1, 0),
        (0, -2), (0, -1), (0, 0), (0, 1), (0, 2),

        # 2
        (2, -2), (3, -2), (4, -2),
        (4, -1),
        (4, 0), (3, 0), (2, 0),
        (2, 1),
        (2, 2), (3, 2), (4, 2)
    ]

    min_x = min(pt[0] for pt in pattern_offsets)
    max_x = max(pt[0] for pt in pattern_offsets)
    min_y = min(pt[1] for pt in pattern_offsets)
    max_y = max(pt[1] for pt in pattern_offsets)

    pattern_width_blocks = max_x - min_x + 1
    pattern_height_blocks = max_y - min_y + 1

    maze_center_x = maze_config.width // 2
    maze_center_y = maze_config.height // 2

    start_draw_x = maze_center_x - ((pattern_width_blocks * block_size) // 2)
    start_draw_y = maze_center_y - ((pattern_height_blocks * block_size) // 2)

    for x_offset, y_offset in pattern_offsets:
        normalized_x = x_offset - min_x
        normalized_y = y_offset - min_y

        target_x = start_draw_x + (normalized_x * block_size)
        target_y = start_draw_y + (normalized_y * block_size)
        draw_block(target_x, target_y)

    return need_open
