import pygame
import random

# Ukuran layar
SCREEN_WIDTH = 300
SCREEN_HEIGHT = 600
BLOCK_SIZE = 30

# Warna
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
COLORS = [
    (0, 255, 255),  # Cyan
    (255, 165, 0),  # Orange
    (0, 0, 255),    # Blue
    (255, 0, 0),    # Red
    (128, 0, 128),  # Purple
    (0, 255, 0),    # Green
    (255, 255, 0)   # Yellow
]

# Bentuk Tetris
SHAPES = [
    [[1, 1, 1, 1]],  # I
    [[1, 1, 1], [0, 1, 0]],  # T
    [[1, 1], [1, 1]],  # O
    [[0, 1, 1], [1, 1, 0]],  # S
    [[1, 1, 0], [0, 1, 1]],  # Z
    [[1, 0, 0], [1, 1, 1]],  # L
    [[0, 0, 1], [1, 1, 1]]   # J
]

class Tetris:
    def __init__(self):
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Tetris")
        self.clock = pygame.time.Clock()
        self.board = [[0] * (SCREEN_WIDTH // BLOCK_SIZE) for _ in range(SCREEN_HEIGHT // BLOCK_SIZE)]
        self.current_shape, self.color_index = self.new_shape()
        self.current_x = SCREEN_WIDTH // BLOCK_SIZE // 2 - 1
        self.current_y = 0
        self.score = 0

    def new_shape(self):
        idx = random.randint(0, len(SHAPES) - 1)
        return SHAPES[idx], idx

    def rotate_shape(self, shape):
        return [list(row) for row in zip(*shape[::-1])]

    def draw_board(self):
        self.screen.fill(BLACK)
        for y in range(len(self.board)):
            for x in range(len(self.board[y])):
                if self.board[y][x] != 0:
                    pygame.draw.rect(self.screen, COLORS[self.board[y][x] - 1],
                                     (x * BLOCK_SIZE, y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))
        self.draw_shape()

    def draw_shape(self):
        for y, row in enumerate(self.current_shape):
            for x, value in enumerate(row):
                if value:
                    pygame.draw.rect(self.screen, COLORS[self.color_index],
                                     ((self.current_x + x) * BLOCK_SIZE, (self.current_y + y) * BLOCK_SIZE,
                                      BLOCK_SIZE, BLOCK_SIZE))

    def run(self):
        running = True
        while running:
            self.clock.tick(2)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        self.current_x -= 1
                        if self.check_collision():
                            self.current_x += 1
                    if event.key == pygame.K_RIGHT:
                        self.current_x += 1
                        if self.check_collision():
                            self.current_x -= 1
                    if event.key == pygame.K_DOWN:
                        self.current_y += 1
                        if self.check_collision():
                            self.current_y -= 1
                    if event.key == pygame.K_UP:
                        rotated = self.rotate_shape(self.current_shape)
                        old_shape = self.current_shape
                        self.current_shape = rotated
                        if self.check_collision():
                            self.current_shape = old_shape

            self.current_y += 1
            if self.check_collision():
                self.current_y -= 1
                self.merge_shape()
                self.clear_lines()
                self.current_shape, self.color_index = self.new_shape()
                self.current_x = SCREEN_WIDTH // BLOCK_SIZE // 2 - 1
                self.current_y = 0
                if self.check_collision():
                    print("Game Over. Score:", self.score)
                    running = False

            self.draw_board()
            pygame.display.flip()

    def check_collision(self):
        for y, row in enumerate(self.current_shape):
            for x, value in enumerate(row):
                if value:
                    new_x = self.current_x + x
                    new_y = self.current_y + y
                    if (new_x < 0 or new_x >= len(self.board[0]) or
                        new_y >= len(self.board) or
                        self.board[new_y][new_x] != 0):
                        return True
        return False

    def merge_shape(self):
        for y, row in enumerate(self.current_shape):
            for x, value in enumerate(row):
                if value:
                    self.board[self.current_y + y][self.current_x + x] = self.color_index + 1

    def clear_lines(self):
        lines_cleared = 0
        new_board = []
        for row in self.board:
            if all(row):
                lines_cleared += 1
            else:
                new_board.append(row)
        for _ in range(lines_cleared):
            new_board.insert(0, [0] * len(self.board[0]))
        self.board = new_board
        self.score += lines_cleared * 100

if __name__ == "__main__":
    pygame.init()
    game = Tetris()
    game.run()
    pygame.quit()