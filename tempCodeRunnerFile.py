import numpy as np
import matplotlib.pyplot as plt
# 0 = path (white), 1 = wall (black)
maze = np.array([
    [1,0,1,1,1,1,1,1,1,0,1,1],
    [1,0,1,1,1,1,1,1,1,0,1,1],
    [1,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,1,1,1,1,1,1,1,1,0,1],
    [1,0,1,0,0,0,0,0,0,1,1,1],
    [1,0,0,0,1,1,1,1,1,1,1,1],
    [1,0,1,0,1,1,1,0,1,1,1,1],
    [1,0,1,0,0,0,1,0,1,1,1,1],
    [1,0,1,1,1,0,0,0,0,0,0,1],
    [1,0,1,1,1,1,1,1,1,1,0,1],
    [0,0,1,1,1,1,1,0,0,0,0,1]
], dtype=int)
# Start (A) and Goal (B)
start = (10, 0)
goal  = (6, 7)
fig, ax = plt.subplots(figsize=(8, 7))
ax.imshow(maze, cmap="gray_r", interpolation="nearest")
# Draw borders around every cell
rows, cols = maze.shape
ax.set_xticks(np.arange(-0.5, cols, 1), minor=True)
ax.set_yticks(np.arange(-0.5, rows, 1), minor=True)
ax.grid(which="minor", color="gray", linestyle="-", linewidth=0.8)
ax.text(start[1], start[0], "A", ha="center", va="center", color="blue", fontsize=16)
ax.text(goal[1],  goal[0],  "B", ha="center", va="center", color="red",  fontsize=16)
plt.show()
