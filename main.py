from algos import *
import argparse
import const
def main(algo: str):
    global const
    your_name = '21120082/21120060'
    pygame.init()
    pygame.display.set_caption(f'{your_name} - {algo}')

    # get polygon list from file
    polygons = read_input_file("input.txt")

    sc = pygame.display.set_mode(const.RES)
    clock = pygame.time.Clock()
    sc.fill(pygame.color.Color(DARK_GREY))
    g = SearchSpace(polygons, sc)
    generate_random_costs(g)
    g.draw(sc)
    clock.tick(FPS)

    # Change the Algorithm here
    if algo == 'DFS':
        DFS(g, sc)
    elif algo == 'BFS':
        BFS(g, sc)
    elif algo == 'UCS':
        UCS(g, sc)
    elif algo == 'A*':
        print(g.goal.id)
        AStar(g, sc, g.start, g.goal)
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
    parser.add_argument('--algo', type=str, help='Enter search algorithm', default='A*')

    args = parser.parse_args()
    main(args.algo)
