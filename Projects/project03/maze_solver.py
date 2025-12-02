from Grid import Grid

def load_maze(filename):
    # Read maze layout from file
    lines = []
    with open(filename, 'r') as f:
        lines = f.readlines()
    # Create new grid with dimensions from file
    new_maze = Grid(len(lines[0]), len(lines))
    # Parse characters and set corresponding cells in the grid
    for y in range(0, len(lines)):
        for x in range(0, len(lines[y])):
            if lines[y][x] == "#":
                new_maze.set(x, y, "#")  # Wall
            elif lines[y][x] == "S":
                new_maze.set(x, y, "S")  # Start position
            elif lines[y][x] == "E":
                new_maze.set(x, y, "E")  # End position
            else:
                new_maze.set(x, y, " ")  # Empty space
    return new_maze

def solve_maze(maze_filename, maze=None):
    # Load maze from file if not provided
    if maze is None:
        maze = load_maze(maze_filename)

    def find_start(maze):
        # Locate the starting position 'S' in the maze
        for x in range(maze.width):
            for y in range(maze.height):
                if maze.get(x, y) == "S":
                    return x, y
        return False
    start = find_start(maze)

    def recursive_search(maze, x, y):
        maze_r = maze.copy()
        # Check if we've reached the exit
        if maze_r.get(x, y) == "E":
            print(f"Success! The path is as follows:{str(maze_r)}")
            return True
        # Define possible movement directions (right, left, up, down)
        movement_priorities = [[1, 0],
                               [-1, 0],
                               [0, -1],
                               [0, 1]]
        for dx, dy in movement_priorities:
            # Mark the current path with dots except start and end positions
            if maze_r.get(x, y) not in ["S", "E"]:
                maze_r.set(x, y, ".")
            next_x = x + dx
            next_y = y + dy
            # Check if next position is valid and not visited
            if maze_r.in_bounds(next_x, next_y) and maze_r.get(next_x, next_y) not in ["#", "."]:
                if recursive_search(maze_r, next_x, next_y):
                    return True
                # Backtrack by unmarking current position
                maze_r.set(x, y, " ")
        return False
    
    if recursive_search(maze, start[0], start[1]):
        return True
    else:
        print("Error: No solution found.")

def generate_maze(width, height, output_file):
    # Ensure dimensions are integers
    width = int(width)
    height = int(height)
    import random
    # Ensure odd dimensions for proper maze generation
    if width%2 == 0:
        width += 1
    if height%2 == 0:
        height += 1
    new_maze = Grid(width, height)

    def replace(maze, value_in, value_out):
        # Utility function to replace all occurrences of one value with another
        for x in range(maze.width):
            for y in range(maze.height):
                if maze.get(x, y) == value_in:
                    maze.set(x, y, value_out)
    # Initialize maze with walls
    replace(new_maze, value_in=None, value_out="#")

    def recursive_maze_carver(maze, x, y):
        # Carve passages through the maze using recursive backtracking
        maze.set(x, y, " ")
        # Define possible movement directions (by 2 cells to maintain walls)
        movement_priorities = [(2, 0),
                               (-2, 0),
                               (0, 2),
                               (0, -2)]
        import random
        # Randomize direction order
        random.shuffle(movement_priorities)
        for dx, dy in movement_priorities:
            new_x = x + dx
            new_y = y + dy
            # Check bounds
            if not (1 <= new_x < width-1 and 1 <= new_y < height-1):
                continue
            # Calculate intermediate cell (wall to be removed)
            intermediate_x = int((x + new_x)//2)
            intermediate_y = int((y + new_y)//2)
            if maze.get(new_x, new_y) == "#":
                # Carve through walls
                maze.set(intermediate_x, intermediate_y, " ")
                maze.set(new_x, new_y, " ")
                recursive_maze_carver(maze, new_x, new_y)
    
    recursive_maze_carver(new_maze, 1, 1)
    # Set start and end positions
    new_maze.set(1, 1, "S")
    new_maze.set(width - 2, height - 2, "E")
    # Save maze to file
    with open(output_file, 'w') as f:
        f.write(str(new_maze))
    return None

if __name__ == "__main__":
    import sys
    # Define available commands and their parameter types
    command_dict = {
        "-s" : [solve_maze, str],
        "-g" : [generate_maze, str, str, str],
    }
    usage_help_string = "Usage: python maze_solver.py [-s filename.txt] [-g width height output_filename.txt]"
    # Default debug arguments
    debug_args = ("-g", 10, 10, "test_files/newMaze.txt")
    args = sys.argv[1:]
    if len(args) == 0:
        args = debug_args
    if args[0] not in command_dict:
        print(usage_help_string)
    try:
        # Validate maze dimensions for generation
        if args[0] == "-g":
            width = int(args[1])
            height = int(args[2])
            if width < 3 or height < 5:
                print("Error! Minimum maze size is 3x5!")
                raise IndexError
        command_args = args[1:]
        command_dict[args[0]][0](*command_args)
    except Exception as e:
        print("Error: " + str(e))
        print(usage_help_string)