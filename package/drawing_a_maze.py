

def drawing_a_maze(maze, maze_config):

    for i in range(maze_config.height):
        print("+",end="")
        for j in range(maze_config.width):
            if maze[i][j].north == True:
                print("---",end="")
            else:
                print("   ", end="")
            print("+",end="")
        print()
        print("|", end="")
        for j in range(maze_config.width):
            if (j, i) == maze_config.entry:
                print(" E ", end="")
            elif (j, i) == maze_config.exit:
                print(" X ", end="")
            else:
                print("   ", end="")
            if maze[i][j].east == True:
                print("|",end="")
            else:
                print(" ",end="")
        print()
            
    print("+", end="")
    for i in range(maze_config.width):
        if maze[maze_config.height-1][i].south:
            print("---", end="")
        else:
            print("   ", end="")
        print("+", end="")
    print()
    
