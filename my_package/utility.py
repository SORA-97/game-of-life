import random
from my_package.constants import *

class MyClass:
    def __init__(self):
        self.grid = self.set_grid()
        self.copied_grid = list(self.grid)
        self.speed = MIDDLE_SPEED
        self.generation = 0
    
    def set_grid(self):
        return [[DEATH for _ in range(COLS)] for _ in range(ROWS)]
    
    def get_grid(self):
        return self.grid
    
    def get_speed(self):
        return self.speed
    
    def reset_generation(self):
        self.generation = 0
    
    def speed_up(self):
        if self.speed == LOW_SPEED:
            self.speed = MIDDLE_SPEED
        elif self.speed == MIDDLE_SPEED:
            self.speed = HIGH_SPEED
        elif self.speed == HIGH_SPEED:
            self.speed = EXTREME_SPEED
        elif self.speed == EXTREME_SPEED:
            self.speed = self.speed
    
    def speed_down(self):
        if self.speed == EXTREME_SPEED:
            self.speed = HIGH_SPEED
        elif self.speed == HIGH_SPEED:
            self.speed = MIDDLE_SPEED
        elif self.speed == MIDDLE_SPEED:
            self.speed = LOW_SPEED
        elif self.speed == LOW_SPEED:
            self.speed = self.speed

    def mouse_draw(self, pos):
        x, y = pos
        col, row = x // CELL_SIZE, y // CELL_SIZE
        if 0 <= col < COLS and 0 <= row < ROWS:
            self.grid[row][col] = LIFE if self.grid[row][col] == DEATH else DEATH
    
    def kill_all(self):
        self.grid = [[DEATH for _ in range(COLS)] for _ in range(ROWS)]
        self.reset_generation()
    
    def random_spawn(self):
        self.grid = [[LIFE if random.random() < SPAWN_RATE else DEATH for _ in range(COLS)] for _ in range(ROWS)]
        self.reset_generation()
    
    def copy_grid(self):
        self.copied_grid = list(self.grid)

    def paste_grid(self):
        self.grid = list(self.copied_grid)
        self.reset_generation()
    
    def create_design_codes(self):
        code = []
        for row in range(ROWS):
                for col in range(COLS):
                    if self.grid[row][col] == LIFE:
                        code += [(row, col)]
        
        if not code:
            return []
        
        min_r = min(r for r, c in code)
        min_c = min(c for r, c in code)
        adjusted_code = [(r - min_r, c - min_c) for r, c in code]

        return adjusted_code

    # 位置指定と回転・反転機能欲しい
    def draw_design(self, code):
        for lr, lc in code:
            nr, nc = lr + 20, lc + 20
            if nr >= ROWS or nc >= COLS:
                continue
            else:
                self.grid[nr][nc] = LIFE

    def count_neighbors(self, row, col):
        count = 0
        for dr, dc in DIRECTIONS:
            nr, nc = row + dr, col + dc
            if 0 <= nr < ROWS and 0 <= nc < COLS and self.grid[nr][nc] == LIFE:
                count += 1
        
        return count

    def move_cells(self):
        new_grid = [row[:] for row in self.grid]
        for row in range(ROWS):
            for col in range(COLS):
                if self.count_neighbors(row, col) == 3 or self.grid[row][col] == LIFE and self.count_neighbors(row, col) == 2:
                    new_grid[row][col] = LIFE
                else:
                    new_grid[row][col] = DEATH

        self.grid = list(new_grid)
    
    def count_generation(self, moving):
        if moving:
            self.generation += 1
        
        return self.generation

    def count_lives(self):
        return sum(row.count(LIFE) for row in self.grid)
    