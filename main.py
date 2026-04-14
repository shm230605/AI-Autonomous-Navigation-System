from simulation.environment import GridEnvironment
from src.path_planning import astar
from src.navigation import navigate

def main():
    print("Starting Autonomous Navigation System...")

    env = GridEnvironment(20, 20)

    start = (0, 0)
    goal = (19, 19)

    path = astar(env.grid, start, goal)

    if path:
        print("Path found!")
        navigate(env, path, start, goal)
    else:
        print("No path found!")

if __name__ == "__main__":
    main()