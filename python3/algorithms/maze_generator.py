import random

def create_maze1():
    maze = []
    maze.append(["#","#", "#", "#", "#", "S","#"])
    maze.append(["#"," ", " ", " ", "#", " ","#"])
    maze.append(["#"," ", "#", " ", "#", " ","#"])
    maze.append(["#"," ", "#", " ", " ", " ","#"])
    maze.append(["#"," ", "#", "#", "#", " ","#"])
    maze.append(["#"," ", " ", " ", "#", " ","#"])
    maze.append(["#","#", "#", "#", "#", "E","#"])

    return maze

def create_maze2():
    maze = []
    maze.append(["#","#", "#", "#", "#", " ", "#", "#", "#"])
    maze.append(["#","S", " ", " ", " ", " ", " ", " ", "#"])
    maze.append(["#"," ", "#", "#", " ", "#", "#", " ", "#"])
    maze.append(["#"," ", "#", " ", " ", " ", "#", " ", "#"])
    maze.append(["#"," ", "#", " ", "#", " ", "#", " ", "#"])
    maze.append(["#"," ", "#", " ", "#", " ", "#", "E", "#"])
    maze.append(["#"," ", "#", " ", "#", " ", "#", "#", "#"])
    maze.append(["#"," ", " ", " ", " ", " ", " ", " ", "#"])
    maze.append(["#","#", "#", "#", "#", "#", "#", " ", "#"])

    return maze

def random_maze(row_n, col_n):
    # keep track of coordinates that can be used as start and end points
    cand = []
    maze = []
    for i in range(row_n):
        row = []
        for j in range(col_n):
            if i != 0 and i != row_n-1 and j != 0 and j != col_n-1:
                sample = ['#', ' ', ' ']  # 1 in 3 chance of a stone tile
                tile = random.choice(sample)

                if tile != '#':
                    cand.append((i, j))
                row.append(tile)
            else:
                row.append('#')
        
        maze.append(row)

    s_idx, e_idx = random.sample(range(len(cand)), 2)
    s, e = cand[s_idx], cand[e_idx]
    maze[s[0]][s[1]] = 'S'
    maze[e[0]][e[1]] = 'E'

    return maze

def print_maze(maze):
    for row in maze:
        print(" ".join(row))

def main():
    maze = random_maze(10, 10)
    print_maze(maze)

if __name__ == '__main__':
    main()







