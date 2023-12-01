import heapq
class Node:
    def __init__(self, x, y, cost, parent=None):
        self.x = x
        self.y = y
        self.cost = cost
        self.parent = parent
    def __lt__(self, other):
        return self.cost < other.cost
def heuristic(node, goal):
    return abs(node.x - goal.x) + abs(node.y - goal.y)
def astar(grid, start, goal):
    open_set = []
    closed_set = set()
    start_node = Node(start[0], start[1], 0)
    goal_node = Node(goal[0], goal[1], 0)
    heapq.heappush(open_set, start_node)
    while open_set:
        current_node = heapq.heappop(open_set)
        if (current_node.x, current_node.y) == (goal_node.x, goal_node.y):
            path = []
            while current_node:
                path.append((current_node.x, current_node.y))
                current_node = current_node.parent
            return path[::-1]
        closed_set.add((current_node.x, current_node.y))
        for neighbor in get_neighbors(grid, current_node):
            if (neighbor.x, neighbor.y) in closed_set:
                continue
            neighbor_cost = current_node.cost + neighbor.cost
            if neighbor not in open_set or neighbor_cost < neighbor.cost:
                neighbor.cost = neighbor_cost
                neighbor.parent = current_node
                if neighbor not in open_set:
                    heapq.heappush(open_set, neighbor)
    return None 
def get_neighbors(grid, node):
    neighbors = []
    for i, j in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        x, y = node.x + i, node.y + j
        if 0 <= x < len(grid) and 0 <= y < len(grid[0]) and grid[x][y] != -1:
            neighbors.append(Node(x, y, grid[x][y] + node.cost, node))
    return neighbors
grid = [
    [1, 1, 1, 1, 1],
    [1, -1, 1, -1, 1],
    [1, 1, 1, 1, 1],
    [1, 1, -1, 1, 1],
    [1, 1, 1, 1, 1]
]
start = (0, 0)
goal = (4, 4)
path = astar(grid, start, goal)
if path:
    print("Path found:", path)
else:
    print("No path found")
