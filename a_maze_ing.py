from reading_config import reading_config
import sys 
 
def main():
    
    if len(sys.argv) != 2:
        print("Usage: python a_maze_ing.py <config_file>")
        sys.exit(1)
    try:
        config = reading_config(sys.argv[1])
        print(config)
    except:
        print("error")
        sys.exit(1)
if __name__ == "__main__":
    main()