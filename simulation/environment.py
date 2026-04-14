import pygame
import random

class GridEnvironment:
    def __init__(self, rows, cols):
        pygame.init()

        self.rows = rows
        self.cols = cols
        self.cell_size = 30

        self.width = cols * self.cell_size
        self.height = rows * self.cell_size

        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Autonomous Navigation Simulation")

        # Font for UI text
        self.font = pygame.font.SysFont("Arial", 20)

        # Create grid
        self.grid = [[0 for _ in range(cols)] for _ in range(rows)]

        self.add_obstacles()

    def add_obstacles(self):
        for _ in range(60):
            x = random.randint(0, self.rows - 1)
            y = random.randint(0, self.cols - 1)

            # Avoid blocking start (0,0) and goal (last cell)
            if (x, y) != (0, 0) and (x, y) != (self.rows-1, self.cols-1):
                self.grid[x][y] = 1

    def draw(self, path=None, current=None, start=None, goal=None,
             status="Running", time_taken=0):

        self.screen.fill((255, 255, 255))

        # Draw grid + obstacles
        for i in range(self.rows):
            for j in range(self.cols):

                rect = pygame.Rect(
                    j * self.cell_size,
                    i * self.cell_size,
                    self.cell_size,
                    self.cell_size
                )

                # Obstacles
                if self.grid[i][j] == 1:
                    pygame.draw.rect(self.screen, (0, 0, 0), rect)

                # Grid lines
                pygame.draw.rect(self.screen, (200, 200, 200), rect, 1)

        # Draw path (light green)
        if path:
            for (x, y) in path:
                rect = pygame.Rect(
                    y * self.cell_size,
                    x * self.cell_size,
                    self.cell_size,
                    self.cell_size
                )
                pygame.draw.rect(self.screen, (144, 238, 144), rect)

        # Draw start (blue)
        if start:
            rect = pygame.Rect(
                start[1] * self.cell_size,
                start[0] * self.cell_size,
                self.cell_size,
                self.cell_size
            )
            pygame.draw.rect(self.screen, (0, 0, 255), rect)

        # Draw goal (red)
        if goal:
            rect = pygame.Rect(
                goal[1] * self.cell_size,
                goal[0] * self.cell_size,
                self.cell_size,
                self.cell_size
            )
            pygame.draw.rect(self.screen, (255, 0, 0), rect)

        # Draw robot (current position)
        if current:
            rect = pygame.Rect(
                current[1] * self.cell_size,
                current[0] * self.cell_size,
                self.cell_size,
                self.cell_size
            )
            pygame.draw.rect(self.screen, (0, 150, 0), rect)

        # ---------------- UI TEXT ---------------- #

        # Path Length
        if path:
            path_text = self.font.render(f"Path Length: {len(path)}", True, (0, 0, 0))
            self.screen.blit(path_text, (10, 10))

        # Status
        status_text = self.font.render(f"Status: {status}", True, (0, 0, 255))
        self.screen.blit(status_text, (10, 35))

        # Time Taken
        time_text = self.font.render(f"Time: {time_taken:.2f} sec", True, (0, 0, 0))
        self.screen.blit(time_text, (10, 60))

        pygame.display.flip()