import pygame
from my_package.utility import MyClass
from my_package.constants import *
import my_package.design as design

class GameOfLife:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Game of Life")
        self.my = MyClass()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont(None, 36)
        self.running = True
        self.moving = False

    def control_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                self.my.mouse_draw(event.pos)
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.moving = not self.moving
                elif event.key == pygame.K_UP and self.moving:
                    self.my.speed_up()
                elif event.key == pygame.K_DOWN and self.moving:
                    self.my.speed_down()
                elif event.key == pygame.K_e and not self.moving:
                    self.my.kill_all()
                elif event.key == pygame.K_r and not self.moving:
                    self.my.random_spawn()
                elif event.key == pygame.K_c and not self.moving:
                    self.my.copy_grid()
                elif event.key == pygame.K_v and not self.moving:
                    self.my.paste_grid()
                elif event.key == pygame.K_p and not self.moving:
                    print(f"Code: {self.my.create_design_codes()}")
                elif event.key == pygame.K_1 and not self.moving:
                    self.my.draw_design(design.get_gosper_glider_gun())
                elif event.key == pygame.K_2 and not self.moving:
                    self.my.draw_design(design.get_lightweight_spaceship())
                elif event.key == pygame.K_3 and not self.moving:
                    self.my.draw_design(design.get_middleweight_spaceship())
                elif event.key == pygame.K_4 and not self.moving:
                    self.my.draw_design(design.get_heavyweight_spaceship())
                elif event.key == pygame.K_5 and not self.moving:
                    self.my.draw_design(design.get_puffers())
                elif event.key == pygame.K_6 and not self.moving:
                    self.my.draw_design(design.get_vampire())

    def draw_grid(self):
        grid = self.my.get_grid()
        for row in range(ROWS):
            for col in range(COLS):
                pygame.draw.rect(self.screen, grid[row][col],
                                (col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE))
                pygame.draw.rect(self.screen, (BORDER),
                                (col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE), 1)

    def display_text(self, text, text_x, text_y):
        text_surface = self.font.render(text, True, LIFE)
        self.screen.blit(text_surface, (text_x, text_y))

    def run(self):
        while self.running:
            self.screen.fill(BACK_GROUND)
            self.control_events()
            if self.moving: self.my.move_cells()
            self.draw_grid()
            self.display_text(f"Lives: {self.my.count_lives()}", TEXT_X, TEXT_Y)
            pygame.display.flip()
            self.clock.tick(self.my.get_speed())

        pygame.quit()
