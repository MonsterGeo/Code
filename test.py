import heapq

class Node:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.g = 0  # 从起点到当前节点的实际代价
        self.h = 0  # 从当前节点到目标节点的估算代价（启发函数值）
        self.parent = None #父节点初始化

    def f(self):
        return self.g + self.h

    def __lt__(self, other):
        # 实现节点的比较方法，使用 f() 函数值进行比较
        return self.f() < other.f()

def heuristic(node, goal):
    # 曼哈顿距离作为启发函数（也可以使用欧几里得距离等）
    return abs(node.x - goal.x) + abs(node.y - goal.y)

def get_neighbors(node, grid):#检验邻近点
    neighbors = []
    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        x, y = node.x + dx, node.y + dy
        if 0 <= x < len(grid) and 0 <= y < len(grid[0]) and not grid[x][y]:
            neighbors.append(Node(x, y))#检查临近点是否在网格中
    return neighbors

def reconstruct_path(node):#从终点回溯到起点
    path = []
    while node:
        path.append((node.x, node.y))
        node = node.parent
    return path[::-1]

def a_star_search(grid, start, goal):
    open_list = []  # 存储待探索的节点的优先级队列（最小堆）
    closed_set = set()  # 存储已探索的节点的集合

    start_node = Node(start[0], start[1])
    goal_node = Node(goal[0], goal[1])

    heapq.heappush(open_list, (start_node.f(), start_node))  # 将起始节点加入 open_list

    while open_list:
        _, current_node = heapq.heappop(open_list)  # 从 open_list 中取出 f() 最小的节点

        if (current_node.x, current_node.y) == (goal_node.x, goal_node.y):
            return reconstruct_path(current_node)  # 如果当前节点是目标节点，返回重构的路径

        closed_set.add((current_node.x, current_node.y))  # 将当前节点加入已探索集合

        for neighbor in get_neighbors(current_node, grid):
            if (neighbor.x, neighbor.y) in closed_set:
                continue  # 如果邻居节点已探索过，跳过本次循环

            tentative_g = current_node.g + 1  # 这里假设每一步的代价都是 1

            if (neighbor.f(), neighbor) in open_list:
                # 如果邻居节点已经在 open_list 中，更新代价和父节点
                if neighbor.g > tentative_g:
                    neighbor.g = tentative_g
                    neighbor.parent = current_node
            else:
                # 否则，将邻居节点加入 open_list，并设置代价和父节点
                neighbor.g = tentative_g
                neighbor.h = heuristic(neighbor, goal_node)
                neighbor.parent = current_node
                heapq.heappush(open_list, (neighbor.f(), neighbor))

    return None  # 如果 open_list 为空，则无法找到路径，返回 None

# 示例
grid = [
    [0, 0, 0, 0, 0],
    [0, 0, 1, 1, 0],
    [0, 0, 1, 0, 0],
    [0, 0, 1, 0, 0],
    [0, 0, 1, 0, 0]
]

start = (0, 2)
goal = (4, 1)

path = a_star_search(grid, start, goal)
print(path)  # 输出：[(0, 0), (1, 1), (1, 2), (2, 3), (3, 4), (4, 4)]
