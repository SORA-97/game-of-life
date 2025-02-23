# スケール設定
WIDTH, HEIGHT = 800, 600  # 画面サイズ
ROWS, COLS = 60, 80  # マス目の数
CELL_SIZE = WIDTH // COLS  # 1マスのサイズ

# 位置設定
GENERATION_X, GENERATION_Y = 10, HEIGHT - 70
LIVES_X, LIVES_Y = 10, HEIGHT - 40

# スポーン率設定
SPAWN_RATE = 0.15

# 速度設定
EXTREME_SPEED = 100
HIGH_SPEED = 24
MIDDLE_SPEED = 10
LOW_SPEED = 3

# 色設定
LIFE = (255, 255, 255) # 白
DEATH = (0, 0, 0) # 黒
BACK_GROUND = (200, 200, 200)
BORDER = (100, 100, 100)

# 周囲マスの定義
DIRECTIONS = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
