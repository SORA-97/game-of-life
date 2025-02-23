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
                key = event.key

                if key == pygame.K_SPACE:
                    self.moving = not self.moving
                elif self.moving:
                    if key == pygame.K_UP:
                        self.my.speed_up()
                    elif key == pygame.K_DOWN:
                        self.my.speed_down()

                elif not self.moving:
                    actions = {
                        pygame.K_e: self.my.kill_all,
                        pygame.K_r: self.my.random_spawn,
                        pygame.K_c: self.my.copy_grid,
                        pygame.K_v: self.my.paste_grid,
                        pygame.K_p: lambda: print(f"Code: {self.my.create_design_codes()}")
                    }
                    if key in actions:
                        actions[key]()
                        return

                    designs = {
                        pygame.K_1: design.get_gosper_glider_gun,
                        pygame.K_2: design.get_lightweight_spaceship,
                        pygame.K_3: design.get_middleweight_spaceship,
                        pygame.K_4: design.get_heavyweight_spaceship,
                        pygame.K_5: design.get_puffers,
                        pygame.K_6: design.get_vampire,
                        pygame.K_7: design.get_breadcrumb_grenade,
                        pygame.K_8: design.get_pentadecathlon,
                        pygame.K_9: design.get_pulsar,
                        pygame.K_0: design.get_galaxy,
                    }
                    if key in designs:
                        self.my.draw_design(designs[key]())

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
            self.display_text(f"Generation: {self.my.count_generation(self.moving)}", GENERATION_X, GENERATION_Y)
            self.display_text(f"Lives: {self.my.count_lives()}", LIVES_X, LIVES_Y)
            pygame.display.flip()
            self.clock.tick(self.my.get_speed())

        pygame.quit()
