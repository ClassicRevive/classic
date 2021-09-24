#!/usr/bin/env python3

''' Using bfs to find shortest path to solve a maze '''

from collections import deque
from maze_generator import create_maze1, create_maze2, random_maze, print_maze

n = int(input('Number of rows: '))
m = int(input('Number of columns: '))

maze = random_maze(n, m)
maze1 = create_maze1()
maze2 = create_maze2()

# find start and endpoints in the maze
def find_s_e(maze):  # find start and endpoints for bfs path finding
    for r in range(len(maze)):
        for c in range(len(maze[0])):
            if maze[r][c] == 'S':
                s = (r, c)
            elif maze[r][c] == 'E':
                e = (r, c)

    return s, e


# print the maze given a path in a list of coordinates
def print_path(maze, path):
    new_maze = []

    for r in range(len(maze)):
        row = []
        for c in range(len(maze[0])):
            if (r, c) in path:  # if in path, add a + sign
                row.append("+")
            else:  # otherwise, add what was in the maze
                row.append(maze[r][c])

        new_maze.append(row)

    for r in new_maze:
        print(" ".join(r))


# backtrack after bfs has found the endpoint node in order to extract shortest path
def retrace_path(s, e, parents):
    path = [e]

    while path[-1] != s:
        path.append(parents[path[-1]])

    path.reverse()

    path = path[1:-1]  # remove start and end coordinates from path
    return path

# helper function to find neighbors of current node
def find_neighbors(maze, r, c):
    
    # directions
    dr = [-1, 1, 0, 0]
    dc = [0, 0, 1, -1]
    
    #print('searching')
    for i in range(4):

        rr = r + dr[i]
        cc = c + dc[i]

        #print(rr, cc)
        # border cases
        if rr < 0 or cc < 0:
            continue
        if rr >= R or cc >= C:
            #print("border")
            continue
        # rock case
        if maze[rr][cc] == '#':
            #print("rock")
            continue
        # already visited case
        if visited[rr][cc]:
            #print("visited")
            continue

        # (rr, cc) is a neighboring cell of (r, c)
        parents[(rr, cc)] = (r, c)
        queue.append((rr, cc))
        visited[rr][cc] = True
           
# Note that this could be done without the retracing if only number of moves is required
# but given that the graph is not large we can use this approach to get both path and distance


def find_path(maze):
    global R
    global C
    global queue
    global parents
    global visited

    # find start and finish points in the maze
    s, e = find_s_e(maze)
    R = len(maze)
    C = len(maze[0])

    # starting coordinate
    sr = s[0]
    sc = s[1]

    if maze[sr][sc] == '#':
        return 'invalid start position'

    if maze[e[0]][e[1]] == "#":
        return 'invalid end position'

    parents = {}
    visited = [[False for i in range(C)] for j in range(R)]

    # Queue for the bfs
    queue = deque()
    queue.append((sr, sc))
    visited[sr][sc] = True
    
    while len(queue) != 0:
        # check neighbors of the current coordinate
        (r, c) = queue.popleft()

        if (r, c) == e:
            reached_end = True
            path = retrace_path(s, e, parents)
            print_path(maze, path)
            return path
        
        find_neighbors(maze, r, c)

    print_maze(maze)
    print('no path found')

def main():
    find_path(maze)

if __name__ == '__main__':
    main()
