from .dict_validate import MazeConfig
from .make42_pattern import make_42_pattern
from .create_maze import Cell


class Colors:
    purple: str = '\033[45m'   # Entry Point (خلفية بنفسجية)
    red: str = '\033[41m'      # Exit Point (خلفية حمراء)
    cyan: str = '\033[46m'     # 42 Pattern (خلفية سماوية)
    green: str = '\033[42m'    # Solution Path الافتراضي (خلفية خضراء)
    magenta: str = '\033[43m'  # Solution Path البديل (خلفية صفراء/برتقالية في حال كانت الحيطان خضراء)
    original: str = '\033[0m'


def drawing_a_maze(
    maze: list[list[Cell]],
    maze_config: MazeConfig,
    pattern_42: list[list[bool]],
    color: str = '\033[47m',
    show_path: bool = False,
    solution_path: list[tuple[int, int]] = None
) -> None:
    """
    دالة الرسم المدمجة المحدثة:
    ترسم المتاهة، وتضمن ديناميكياً عدم تطابق لون مسار الحل مع لون الجدران.
    """
    if solution_path is None:
        solution_path = []

    # تحديد لون المسار ديناميكياً لتفادي التطابق مع لون الجدران الممرر (color)
    # إذا كان لون الجدار يحتوي على الكود '92' (الأخضر)، نغير لون الحل إلى الأصفر/البرتقالي
    if '92' in color:
        path_color = Colors.magenta
    else:
        path_color = Colors.green

    # تحويل مسار الحل إلى set لسرعة البحث
    path_set = set(solution_path) if show_path else set()

    pattern_42 = make_42_pattern(maze_config)
    x = f"{color}██{Colors.original}"
    
    # 1. رسم الجدار العلوي للمتاهة
    for _ in range(maze_config.width * 2 + 1):
        print(x, end="")
    print()

    # 2. رسم صفوف المتاهة
    for i in range(maze_config.height):
        # الجدار الأيسر
        print(x, end="")
        
        for j in range(maze_config.width):
            # طباعة ما بداخل الخلية
            if (j, i) == maze_config.entry:
                print(f"{Colors.purple}  {Colors.original}", end="")
            elif (j, i) == maze_config.exit:
                print(f"{Colors.red}  {Colors.original}", end="")
            elif (j, i) in path_set:
                print(f"{path_color}  {Colors.original}", end="")
            elif pattern_42[i][j]:
                print(f"{Colors.cyan}  {Colors.original}", end="")
            else:
                print("  ", end="")

            # رسم الجدار الشرقي (East Wall)
            if maze[i][j].east:
                print(x, end="")
            else:
                # تلوين الممر الشرقي إذا كان كلاً من الخليتين المتجاورتين في الحل
                if show_path and (j, i) in path_set and (j + 1, i) in path_set:
                    print(f"{path_color}  {Colors.original}", end="")
                else:
                    print("  ", end="")
        print()

        # الجدار الجنوبي (South Wall)
        print(x, end="")
        for j in range(maze_config.width):
            if maze[i][j].south:
                print(x, end="")
            else:
                # تلوين الممر الجنوبي إذا كان كلاً من الخليتين المتجاورتين في الحل
                if show_path and (j, i) in path_set and (j, i + 1) in path_set:
                    print(f"{path_color}  {Colors.original}", end="")
                else:
                    print("  ", end="")
            print(x, end="")
        print()
