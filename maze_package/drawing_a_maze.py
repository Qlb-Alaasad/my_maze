# type: ignore
from .dict_validate import MazeConfig
from .make42_pattern import make_42_pattern


class Colors:
    purple: str = '\033[45m'
    red: str = '\033[41m'
    cyan: str = '\033[46m'  # لون سبيشال جديد مخصص للـ 42 باتيرن تبعك
    original: str = '\033[0m'


def drawing_a_maze(maze: list[list[any]], maze_config: MazeConfig,
                   color: str = '\033[47m') -> None:

    """
    هذه دالة الرسم المدمجة: تجمع طريقة عبد بالبلوكات الملونة
    مع منطق الـ 42 باتيرن الخاص بمابو.
    """
    pattern_42 = make_42_pattern(maze_config)
    x = f"{color}██{Colors.original}"
    for _ in range(maze_config.width * 2 + 1):
        print(x, end="")
    print()
    for i in range(maze_config.height):
        print(x, end="")
        for j in range(maze_config.width):
            if (j, i) == maze_config.entry:
                print(f"{Colors.purple}  {Colors.original}", end="")
            elif (j, i) == maze_config.exit:
                print(f"{Colors.red}  {Colors.original}", end="")
            elif pattern_42[i][j]:
                print(f"{Colors.cyan}  {Colors.original}", end="")
            else:
                print("  ", end="")
            if maze[i][j].east:
                print(x, end="")
            else:
                print("  ", end="")
        print()
        print(x, end="")
        for j in range(maze_config.width):
            if maze[i][j].south:
                print(x, end="")
            else:
                print("  ", end="")
            print(x, end="")
        print()
