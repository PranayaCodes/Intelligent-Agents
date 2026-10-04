from collections import deque
import numpy as np
import matplotlib.pyplot as plt

# 0 = path, 1 = wall, coordinates are (row, col)
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
    [0,0,1,1,1,1,1,0,0,0,0,1],
])
rows, cols = maze.shape
start, goal = (10, 0), (6, 7)
dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]  # down, up, right, left

# Steps 1-3: nodes and edges
graph = {}
for r in range(rows):
    for c in range(cols):
        if maze[r, c] == 0:
            graph[(r, c)] = [(r+dr, c+dc) for dr, dc in dirs
                             if 0 <= r+dr < rows and 0 <= c+dc < cols
                             and maze[r+dr, c+dc] == 0]

print("nodes:", len(graph))
print("edges:", sum(len(v) for v in graph.values()) // 2)
assert all(a in graph[b] for a in graph for b in graph[a])  # symmetry check

# Step 4: traversal
def search(graph, start, goal, use_queue):
    frontier = deque([start])
    parent = {start: None}
    order = []
    while frontier:
        node = frontier.popleft() if use_queue else frontier.pop()
        order.append(node)
        if node == goal:
            break
        for n in graph[node]:
            if n not in parent:
                parent[n] = node
                frontier.append(n)
    path, n = [], goal
    while n is not None:
        path.append(n)
        n = parent[n]
    return order, path[::-1]

bfs_order, bfs_path = search(graph, start, goal, True)
dfs_order, dfs_path = search(graph, start, goal, False)

print("BFS order:", bfs_order, len(bfs_order))
print("BFS path:", bfs_path, "steps:", len(bfs_path) - 1)
print("DFS order:", dfs_order, len(dfs_order))
print("DFS path:", dfs_path, "steps:", len(dfs_path) - 1)

# Figure: explored order (yellow, numbered) and final path (green)
def draw(ax, order, path, title):
    ax.imshow(maze, cmap="gray_r", interpolation="nearest")
    ax.set_xticks(np.arange(-0.5, cols, 1), minor=True)
    ax.set_yticks(np.arange(-0.5, rows, 1), minor=True)
    ax.grid(which="minor", color="gray", linewidth=0.6)
    ax.tick_params(which="minor", length=0)
    for i, (r, c) in enumerate(order):
        if (r, c) not in (start, goal):
            ax.add_patch(plt.Rectangle((c-0.5, r-0.5), 1, 1, color="gold", alpha=0.7))
            ax.text(c, r, str(i+1), ha="center", va="center", fontsize=6)
    ax.plot([c for r, c in path], [r for r, c in path], color="green", linewidth=2.5)
    ax.text(start[1], start[0], "A", ha="center", va="center", color="blue", fontsize=13, fontweight="bold")
    ax.text(goal[1], goal[0], "B", ha="center", va="center", color="red", fontsize=13, fontweight="bold")
    ax.set_title(title)

fig, axs = plt.subplots(1, 2, figsize=(10, 4.6))
draw(axs[0], bfs_order, bfs_path, f"BFS: {len(bfs_order)} nodes explored, {len(bfs_path)-1}-step path")
draw(axs[1], dfs_order, dfs_path, f"DFS: {len(dfs_order)} nodes explored, {len(dfs_path)-1}-step path")
plt.tight_layout()
plt.savefig("bfs_dfs.png", dpi=200)  # saved next to your .py file
plt.show()