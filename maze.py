import pygame
import random
from const import *
import const


# Random seed
random.seed(2345)


def set_animation_speed() -> None:
    # change the speed in file const.py
    pygame.time.delay(SPEED)
    pygame.display.update()


# Show cost of non-brick nodes, turn ON/OFF by
def show_node_cost(node, sc: pygame.Surface):
    if MODE is OFF:
        return

    if not node.is_brick and node.cost is not None:
        font = pygame.font.Font(None, 24)
        cost_text = font.render(str(node.cost), True, BLACK)
        sc.blit(cost_text, node.rect.topleft)


# Set random cost for each node - which is not brick, values from 1-10
def generate_random_costs(search_space):
    for node in search_space.grid_cells:
        if not node.is_brick:
            node.cost = random.randint(1, 10)


class Node:
    # a is side of the square
    def __init__(self, x, y, a, id, is_brick=False) -> None:
        self.rect = pygame.Rect(x, y, a, a)
        self.is_brick = is_brick
        self.color = BLACK if self.is_brick else WHITE
        self.id = id
        self.cost = None  # Add attribute: cost of each none-brick node

    def draw(self, sc: pygame.Surface) -> None:
        pygame.draw.rect(sc, self.color, self.rect)

        # Show cost of non-brick nodes
        show_node_cost(self, sc)

    def _set_color(self, color):
        self.color = color

    def set_color(self, color, sc: pygame.Surface):
        self.color = color
        self.draw(sc)


# Parse data from txt file
def read_input_file(filename):
    with open(filename, 'r') as file:
        global const
        lines = file.readlines()

        # get tokens from line 1
        tokens = [int(num) for num in lines[0].split(',')]

        # set maze's limit
        const.ROWS = tokens[0]
        const.COLS = tokens[1]

        # const.ROWS = 22
        # const.COLS = 30

        # set maze resolution
        const.RES = 27.5 * const.COLS, 27.5 * const.ROWS

        # get tokens from line 2
        tokens = [int(num) for num in lines[1].split(',')]

        # turn start & goal node from matrix coordinates into list coordinates
        const.START = tokens[0] * const.COLS + tokens[1]
        const.GOAL = tokens[2] * const.COLS + tokens[3]
        # get number of polygons & list of polygons
        num_polygons = int(lines[2])
        polygons: list[list[Node]] = []

        for i in range(3, 3 + num_polygons):
            polygon_tokens = [int(num) for num in lines[i].split(',')]
            nodes: list[Node] = []
            for j in range(0, len(polygon_tokens) - 1):
                is_brick = True
                x = polygon_tokens[j]
                y = polygon_tokens[j + 1]
                nodes.append(Node(y * (A + A1) + BOUND, x * (A + A1) + BOUND, A, x * COLS + y, is_brick))
                j = j + 1
            polygons.append(nodes)
    return polygons


class SearchSpace:
    def __init__(self, polygons) -> None:
        # create list of nodes & turn into matrix
        self.grid_cells: list[Node] = []
        for i in range(const.ROWS):
            for j in range(const.COLS):
                # define the brick's appearing
                is_brick = True if random.randint(1, 3) == 1 else False
                self.grid_cells.append(Node(j * (A + A1) + BOUND, i * (A + A1) + BOUND, A, i * const.COLS + j, is_brick))

        # set index & color for start & goal node
        self.start: Node = self.grid_cells[const.START]
        self.start.is_brick = False
        self.start._set_color(ORANGE)
        self.goal: Node = self.grid_cells[const.GOAL]
        self.goal.is_brick = False
        self.goal._set_color(PURPLE)

    def draw(self, sc: pygame.Surface):
        for node in self.grid_cells:
            node.draw(sc)
        pygame.display.flip()

    def get_length(self):
        return len(self.grid_cells)

    def is_goal(self, node: Node):
        return node.id == self.goal.id

    def get_neighbors(self, node: Node) -> list[Node]:
        x, y = node.id % const.COLS, node.id // const.COLS

        # define the directions of agent
        up = (y - 1) * const.COLS + x if y - 1 >= 0 else None
        down = (y + 1) * const.COLS + x if y + 1 < const.ROWS else None
        left = y * const.COLS + (x - 1) if x - 1 >= 0 else None
        right = y * const.COLS + (x + 1) if x + 1 < const.COLS else None

        left_up = (y - 1) * const.COLS + (x - 1) if y - 1 >= 0 and x - 1 >= 0 else None
        left_down = (y + 1) * const.COLS + (x - 1) if y + 1 < const.ROWS and x - 1 >= 0 else None
        right_up = (y - 1) * const.COLS + (x + 1) if y - 1 >= 0 and x + 1 < const.COLS else None
        right_down = (y + 1) * const.COLS + (x + 1) if y + 1 < const.ROWS and x + 1 < const.COLS else None

        directions = [left_up, left, left_down, down, right_down, right, right_up, up]
        # directions = [left, down, right, up]  # 4 directions version

        neighbors = []
        for dir_ in directions:
            if dir_ is not None and not self.grid_cells[dir_].is_brick:
                neighbors.append(self.grid_cells[dir_])

        return neighbors

