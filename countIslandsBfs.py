# based on https://www.techiedelight.com/count-the-number-of-islands/
from collections import deque
from tkinter import *

root = Tk()

map = [
    [0, 0, 1, 0, 0, 0, 1, 1, 1, 1],
    [0, 0, 1, 0, 0, 0, 1, 0, 0, 0],
    [1, 1, 1, 1, 0, 0, 1, 0, 0, 0],
    [1, 0, 0, 1, 0, 0, 0, 0, 0, 0],
    [1, 1, 1, 1, 0, 0, 0, 1, 1, 1],
    [0, 1, 0, 1, 0, 0, 1, 1, 1, 1],
    [0, 0, 0, 0, 0, 1, 1, 1, 0, 0],
    [0, 0, 0, 1, 0, 0, 1, 1, 1, 0],
    [1, 0, 1, 0, 1, 0, 0, 1, 0, 0],
    [1, 1, 1, 1, 0, 0, 0, 1, 1, 1]
]

labels = [[None for x in range(len(map))] for y in range(len(map[0]))]

# Below lists detail all eight possible movements from a cell
# (top, right, bottom, left, and four diagonal moves)
row = [-1, -1, -1, 0, 1, 0, 1, 1]
col = [-1, 1, 0, -1, -1, 1, 0, 1]


# Function to check if it is safe to go to position (x, y)
# from the current position. The function returns false if (x, y)
# is not valid matrix coordinates or (x, y) represents water or
# position (x, y) is already processed.

def isSafe(x, y, processed):
    if x < 0 or (x >= len(processed)):
        return False

    if y < 0 or (y >= len(processed[0])):
        return False

    if map[x][y] == 0:
        return False

    if processed[x][y]:
        return False

    return True


def bfs(island, processed, i, j):
    # create an empty queue and enqueue source node
    q = deque()
    q.append((i, j))

    # mark source node as processed
    processed[i][j] = True
    map[i][j] = island

    # set the number of current island on the current node
    labels[i][j].config(text=island)

    # loop till queue is empty
    while q:
        # dequeue front node and process it
        x, y = q.popleft()

        # check for all eight possible movements from the current cell
        # and enqueue each valid movement
        for k in range(len(row)):
            # skip if the location is invalid, or already processed, or has water
            nextRow = x + row[k]
            nextCol = y + col[k]

            if isSafe(nextRow, nextCol, processed):
                # skip if the location is invalid, or it is already
                # processed, or consists of water
                processed[nextRow][nextCol] = True
                map[nextRow][nextCol] = island
                q.append((nextRow, nextCol))

                # set the number of current island to the next node
                labels[nextRow][nextCol].config(text=island)


def countIslands():
    # base case
    if not map or not len(map):
        return 0

    # `M × N` matrix
    (M, N) = (len(map), len(map[0]))

    # stores if a cell is processed or not
    processed = [[False for x in range(N)] for y in range(M)]

    island = 0

    for i in range(M):
        for j in range(N):
            # start BFS from each unprocessed node and increment island count
            if map[i][j] != 0 and not processed[i][j]:
                island = island + 1
                bfs(island, processed, i, j)

    return island


root.title("Breadth First Search")

for i in range(len(map)):
    for j in range(len(map[i])):

        # store the labels for each node
        value = map[i][j]
        label = Label(root, text=value, fg="#fff", padx=20, pady=20, font=("Sans Serif Bold", 20))
        labels[i][j] = label

        # set color if the node is land or water
        if value == 0:
            label.config(bg="#0000ff")
        else:
            label.config(bg="#90EE90")

        label.grid(row=i, column=j)

print("The count of islands is ", countIslands())

root.mainloop()
