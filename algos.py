from queue import PriorityQueue
from collections import deque
from maze import *


''''''''''''''''''''''''
full_polygons: list[list[int]] = []


def swap(a, b):
    return b, a


def DFS(g: SearchSpace, sc: pygame.Surface, start: Node, goal: Node):
    print('Implement DFS algorithm')

    # The set which contains the nodes that could be visited
    open_set = [start.id]

    # The set which contains the visited nodes
    closed_set = []

    # father[x] = y means that you can go to node y from x. It would help you on
    # tracing the path when you reach the goal
    father = [-1] * g.get_length()

    # Save the previous node of the current one - optimize the BLUE coloring stage
    previous_node = start

    # Repeat until goal is found or list of nodes that could be visited is empty
    while open_set:
        current_node_id = open_set.pop()
        current_node = g.grid_cells[current_node_id]

        # Push current node into visited nodes list
        closed_set.append(current_node_id)

        # Set the color of the visited nodes - BLUE
        # previous_node.set_color(BLUE, sc)

        if g.is_target(current_node, goal):
            break

        # Set color for current node - YELLOW
        # current_node.set_color(YELLOW, sc)

        for neighbor in g.get_neighbors(current_node):
            neighbor_id = neighbor.id

            if neighbor_id not in closed_set and neighbor_id not in open_set:
                open_set.append(neighbor_id)
                father[neighbor_id] = current_node_id

                # Set color for all nodes that could be visited - RED
                # neighbor.set_color(RED, sc)

        # Save current node to color it BLUE in the next while loop
        previous_node = current_node

        # Manual adjust animation speed
        # set_animation_speed()

        # Update start and goal node
    start.set_color(ORANGE, sc)
    goal.set_color(PURPLE, sc)
    font = pygame.font.Font(None, 24)
    text = font.render("S", True, WHITE)
    sc.blit(text, text.get_rect(center=start.rect.center).topleft)
    text = font.render("G", True, WHITE)
    sc.blit(text, text.get_rect(center=goal.rect.center).topleft)

    # Trace back the path from the goal node to the start node
    path = []
    current_node_id = goal.id

    while current_node_id != -1:
        path.append(current_node_id)
        current_node_id = father[current_node_id]
    path.reverse()

    # Draw the path with '+' symbols
    for i in range(1, len(path) - 1):
        node = g.grid_cells[path[i]]
        font = pygame.font.Font(None, 24)
        text = font.render(PATH_MARK, True, BLACK)
        sc.blit(text, text.get_rect(center=node.rect.center).topleft)
        set_animation_speed()


''''''''''''''''''''''''


# Using double-ended-queue
def BFS(g: SearchSpace, sc: pygame.Surface, start: Node, goal: Node):
    print('Implement BFS algorithm')

    # The set which contains the nodes that could be visited
    open_set = deque([start.id])

    # The set which contains the visited nodes
    closed_set = set()

    # father[x] = y means that you can go to node y from x. It would help you on
    # tracing the path when you reach the goal
    father = [-1] * g.get_length()

    # Save the previous node of the current one - optimize the BLUE coloring stage
    previous_node = start

    while open_set:
        current_node_id = open_set.popleft()  # Sử dụng popleft() thay vì pop(0)
        current_node = g.grid_cells[current_node_id]

        if current_node_id in closed_set:
            continue

        # Push current node into visited nodes set
        closed_set.add(current_node_id)

        # Set the color of the visited nodes - BLUE
        # previous_node.set_color(BLUE, sc)

        if g.is_target(current_node, goal):
            break

        # Set color for current node - YELLOW
        # current_node.set_color(YELLOW, sc)

        for neighbor in g.get_neighbors(current_node):
            neighbor_id = neighbor.id

            if neighbor_id not in closed_set and neighbor_id not in open_set:
                open_set.append(neighbor_id)
                father[neighbor_id] = current_node_id

                # Set color for all nodes that could be visited - RED
                # neighbor.set_color(RED, sc)

        # Save current node to color it BLUE in the next while loop
        previous_node = current_node

        # Manual adjust animation speed
        # set_animation_speed()

    # Update start and goal node
    start.set_color(ORANGE, sc)
    goal.set_color(PURPLE, sc)
    font = pygame.font.Font(None, 24)
    text = font.render("S", True, WHITE)
    sc.blit(text, text.get_rect(center=start.rect.center).topleft)
    text = font.render("G", True, WHITE)
    sc.blit(text, text.get_rect(center=goal.rect.center).topleft)

    # Trace back the path from the goal node to the start node
    path = []
    current_node_id = goal.id

    while current_node_id != -1:
        path.append(current_node_id)
        current_node_id = father[current_node_id]
    path.reverse()

    # Draw the path with '+' symbols
    for i in range(1, len(path) - 1):
        node = g.grid_cells[path[i]]
        font = pygame.font.Font(None, 24)
        text = font.render(PATH_MARK, True, BLACK)
        sc.blit(text, text.get_rect(center=node.rect.center).topleft)
        set_animation_speed()


''''''''''''''''''''''''


def UCS(g: SearchSpace, sc: pygame.Surface, start: Node, goal: Node):
    print('Implement UCS algorithm')

    # The set which contains the nodes that could be visited
    open_set = PriorityQueue()

    # Set the root node with a sum cost of 0
    open_set.put((0, start.id))

    # The set which contains the visited nodes
    closed_set = set()

    # father[x] = y means that you can go to node y from x. It would help you on
    # tracing the path when you reach the goal
    father = [-1] * g.get_length()
    cost = [float('inf')] * g.get_length()
    cost[start.id] = 0

    # Save the previous node of the current one - optimize the BLUE coloring stage
    previous_node = start

    while not open_set.empty():
        current_cost, current_node_id = open_set.get()

        if current_node_id in closed_set:
            continue

        current_node = g.grid_cells[current_node_id]
        closed_set.add(current_node_id)

        # Set the color of the visited nodes - BLUE
        # previous_node.set_color(BLUE, sc)

        # if g.is_target(current_node):
        #     break

        for neighbor in g.get_neighbors(current_node):
            neighbor_id = neighbor.id
            new_cost = cost[current_node_id] + neighbor.cost  # Sử dụng thuộc tính "chi phí"

            if new_cost < cost[neighbor_id]:
                cost[neighbor_id] = new_cost
                father[neighbor_id] = current_node_id
                open_set.put((new_cost, neighbor_id))

                # Set color of nodes that can be visited - RED
                # neighbor.set_color(RED, sc)

        # Save current node to color it BLUE in the next while loop
        previous_node = current_node

        # Manual adjust animation speed
        # set_animation_speed()

    # Update start and goal node
    start.set_color(ORANGE, sc)
    goal.set_color(PURPLE, sc)
    font = pygame.font.Font(None, 24)
    text = font.render("S", True, WHITE)
    sc.blit(text, text.get_rect(center=start.rect.center).topleft)
    text = font.render("G", True, WHITE)
    sc.blit(text, text.get_rect(center=goal.rect.center).topleft)

    # Trace back the path from the goal node to the start node
    path = []
    current_node_id = goal.id

    while current_node_id != -1:
        path.append(current_node_id)
        current_node_id = father[current_node_id]
    path.reverse()

    # Draw the path with '+' symbols
    for i in range(1, len(path) - 1):
        node = g.grid_cells[path[i]]
        font = pygame.font.Font(None, 24)
        text = font.render(PATH_MARK, True, BLACK)
        sc.blit(text, text.get_rect(center=node.rect.center).topleft)
        set_animation_speed()


''''''''''''''''''''''''


def AStar(g: SearchSpace, sc: pygame.Surface, start: Node, goal: Node):
    print('Implement AStar algorithm')

    # The set which contains the nodes that could be visited
    open_set = PriorityQueue()

    # Set the root node with a sum cost of 0
    open_set.put((0, start.id))

    # The set which contains the visited nodes
    closed_set = set()

    # father[x] = y means that you can go to node y from x. It would help you on
    # tracing the path when you reach the goal
    father = [-1] * g.get_length()
    cost = [float('inf')] * g.get_length()
    cost[start.id] = 0

    # Save the previous node of the current one - optimize the BLUE coloring stage
    previous_node = start

    while not open_set.empty():
        current_cost, current_node_id = open_set.get()

        if current_node_id in closed_set:
            continue

        current_node = g.grid_cells[current_node_id]
        closed_set.add(current_node_id)

        # Set the color of the visited nodes - BLUE
        # previous_node.set_color(BLUE, sc)

        if g.is_target(current_node, goal):
            break

        # Set color for current node - YELLOW
        # current_node.set_color(YELLOW, sc)

        for neighbor in g.get_neighbors(current_node):
            neighbor_id = neighbor.id
            new_cost = cost[current_node_id] + neighbor.cost  # Sử dụng thuộc tính "chi phí"

            if new_cost < cost[neighbor_id]:
                cost[neighbor_id] = new_cost
                father[neighbor_id] = current_node_id

                # Estimate the remaining cost using a heuristic (e.g., Manhattan distance to the goal)
                remaining_cost = heuristic("Diagonal", neighbor, goal)
                total_cost = new_cost + remaining_cost
                open_set.put((total_cost, neighbor_id))

                # Set color of nodes that can be visited - RED
                # neighbor.set_color(RED, sc)

        # Save current node to color it BLUE in the next while loop
        previous_node = current_node

        # Manual adjust animation speed
        # set_animation_speed()

    # Update start and goal node
    start.set_color(ORANGE, sc)
    goal.set_color(PURPLE, sc)
    font = pygame.font.Font(None, 24)
    text = font.render("S", True, WHITE)
    sc.blit(text, text.get_rect(center=start.rect.center).topleft)
    text = font.render("G", True, WHITE)
    sc.blit(text, text.get_rect(center=goal.rect.center).topleft)

    # Trace back the path from the goal node to the start node
    path = []
    current_node_id = goal.id

    while current_node_id != -1:
        path.append(current_node_id)
        current_node_id = father[current_node_id]
    path.reverse()

    # Draw the path with '+' symbols
    for i in range(1, len(path) - 1):
        node = g.grid_cells[path[i]]
        font = pygame.font.Font(None, 24)
        text = font.render(PATH_MARK, True, BLACK)
        sc.blit(text, text.get_rect(center=node.rect.center).topleft)
        set_animation_speed()


# implemented for A*
def heuristic(name, start, goal):
    if name == "Manhattan":
        # Manhattan Distance
        dx = start.rect.centerx - goal.rect.centerx
        dy = start.rect.centery - goal.rect.centery
        return abs(dx) + abs(dy)

    elif name == "Chebyshev":
        # Chebyshev Distance
        dx = start.rect.centerx - goal.rect.centerx
        dy = start.rect.centery - goal.rect.centery
        return max(abs(dx), abs(dy))

    elif name == "Diagonal":
        # Diagonal Distance
        dx = start.rect.centerx - goal.rect.centerx
        dy = start.rect.centery - goal.rect.centery
        return D * (abs(dx) + abs(dy)) + (D2 - 2 * D) * min(dx, dy)


def AStarForPolygon(g: SearchSpace, sc: pygame.Surface, polygon: list[int], start: Node, goal: Node):
    # The set which contains the nodes that could be visited
    open_set = PriorityQueue()

    # Set the root node with a sum cost of 0
    open_set.put((0, start.id))

    # The set which contains the visited nodes
    closed_set = set()

    # father[x] = y means that you can go to node y from x. It would help you on
    # tracing the path when you reach the goal
    father = [-1] * g.get_length()
    cost = [float('inf')] * g.get_length()
    cost[start.id] = 0

    while not open_set.empty():
        current_cost, current_node_id = open_set.get()

        if current_node_id in closed_set:
            continue

        current_node = g.grid_cells[current_node_id]
        closed_set.add(current_node_id)

        if g.is_target(current_node, goal):
            break

        for neighbor in g.get_neighbors_for_polygon(current_node):
            neighbor_id = neighbor.id
            new_cost = cost[current_node_id] + neighbor.cost  # Sử dụng thuộc tính "chi phí"

            if new_cost < cost[neighbor_id]:
                cost[neighbor_id] = new_cost
                father[neighbor_id] = current_node_id

                # Estimate the remaining cost using a heuristic (e.g., Manhattan distance to the goal)
                remaining_cost = heuristic("Diagonal", neighbor, goal)
                total_cost = new_cost + remaining_cost
                open_set.put((total_cost, neighbor_id))

        # Manual adjust animation speed
        # set_animation_speed()

    # Trace back the path from the goal node to the start node
    path = []
    current_node_id = goal.id

    while current_node_id != -1:
        path.append(current_node_id)
        current_node_id = father[current_node_id]
    path.reverse()

    # Draw the path by color them BLACK
    for i in range(len(path) - 1):
        end_node = g.grid_cells[path[i + 1]]
        end_node.is_brick = True
        end_node.set_color(BLACK, sc)
        # set_animation_speed()

        # update current polygon's node, except for initial ones
        if i != len(path) - 2:
            polygon.append(end_node.id)

    # Recolor start and goal node
    start.set_color(GREEN, sc)
    goal.set_color(GREEN, sc)

