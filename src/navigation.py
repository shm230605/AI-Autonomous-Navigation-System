import pygame
import time

def navigate(env, path, start, goal):
    running = True

    start_time = time.time()

    # Move step by step
    for step in path:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                return

        elapsed_time = time.time() - start_time

        env.draw(
            path=path,
            current=step,
            start=start,
            goal=goal,
            status="Moving...",
            time_taken=elapsed_time
        )

        time.sleep(0.1)

    # Final state (Reached Goal)
    final_time = time.time() - start_time

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        env.draw(
            path=path,
            current=goal,
            start=start,
            goal=goal,
            status="Reached Goal ✅",
            time_taken=final_time
        )