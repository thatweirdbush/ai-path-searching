from algos import *
import argparse
import const
def main(algo: str):
    global const
    your_name = '21120082/21120060'
    pygame.init()
    pygame.display.set_caption(f'{your_name} - {algo}')

    # get polygon list from file
    polygons, pickups = read_input_file("input.txt")

    sc = pygame.display.set_mode(const.RES)
    clock = pygame.time.Clock()
    sc.fill(pygame.color.Color(DARK_GREY))
    g = SearchSpace(polygons, pickups, sc)
    g.draw(sc)
    clock.tick(FPS)

    # rearrange nodes by distant to start node
    for i in range(len(pickups) - 1):
        for j in range(i + 1, len(pickups)):
            a = g.grid_cells[pickups[i]]
            b = g.grid_cells[pickups[j]]
            if heuristic("Manhattan", g.start, a) > heuristic("Manhattan", g.start, b):
                pickups[i], pickups[j] = pickups[j], pickups[i]

    starts: list[int] = [g.start.id]
    starts.extend(pickups)
    starts.append(g.goal.id)

    # Change the Algorithm here
    if algo == 'DFS':
        for i in range(0, len(starts) - 1):
            DFS(g, sc, g.grid_cells[starts[i]], g.grid_cells[starts[i + 1]])

    elif algo == 'BFS':
        for i in range(0, len(starts) - 1):
            BFS(g, sc, g.grid_cells[starts[i]], g.grid_cells[starts[i + 1]])

    elif algo == 'UCS':
        # must generate random cost (1-10) or else UCS would become BFS
        generate_random_costs(g)
        for i in range(0, len(starts) - 1):
            UCS(g, sc, g.grid_cells[starts[i]], g.grid_cells[starts[i + 1]])

    elif algo == 'A*':
        for i in range(0, len(starts) - 1):
            AStar(g, sc, g.grid_cells[starts[i]], g.grid_cells[starts[i + 1]])

    else:
        raise NotImplementedError('Not implemented')

    running = ON
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Search algorithms')
    parser.add_argument('--algo', type=str, help='Enter search algorithm', default='BFS')

    args = parser.parse_args()
    main(args.algo)
