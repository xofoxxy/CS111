def load_grid(filename):
    letter_grid = []
    with open(filename, "r") as text_file:
        for line in text_file:
            line = line.strip()
            letter_grid.append([])
            for letter in line:
                letter_grid[-1].append(letter)
    return letter_grid


def exists(grid, word):
    def exists_helper(grid, word_list, x, y, visited):
        if len(word_list) == 0:
            return True
        if x > 0:
            if not visited[y][x - 1] and grid[y][x - 1] == word_list[0]:
                visited[y][x - 1] = True
                if exists_helper(grid, word_list[1:], x - 1, y, visited):
                    return True
                else:
                    visited[y][x - 1] = False
        if x < len(grid[0]) - 1:
            if not visited[y][x + 1] and grid[y][x + 1] == word_list[0]:
                visited[y][x + 1] = True
                if exists_helper(grid, word_list[1:], x + 1, y, visited):
                    return True
                else:
                    visited[y][x + 1] = False
        if y > 0:
            if not visited[y-1][x] and grid[y-1][x] == word_list[0]:
                visited[y-1][x] = True
                if exists_helper(grid, word_list[1:], x, y-1, visited):
                    return True
                else:
                    visited[y-1][x] = False
        if y < len(grid) - 1:
            if not visited[y+1][x] and grid[y+1][x] == word_list[0]:
                visited[y+1][x] = True
                if exists_helper(grid, word_list[1:], x, y+1, visited):
                    return True
                else:
                    visited[y+1][x] = False
        return False
    visited = [[False for x in range(len(grid[0]))] for y in range(len(grid))]
    word_list = []
    for letter in word:
        word_list.append(letter)
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if grid[y][x] == word_list[0]:
                visited[y][x] = True
                word_list.pop(0)
                return exists_helper(grid, word_list, x, y, visited)
    return False


if __name__ == "__main__":
    grid = load_grid("test_files/grid1.txt")
    print(exists(grid, "CAT"))