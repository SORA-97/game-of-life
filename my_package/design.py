gosper_glider_gun = [
    (0, 24), (1, 22), (1, 24), (2, 12), (2, 13), (2, 20), (2, 21), (2, 34), (2, 35), (3, 11), 
    (3, 15), (3, 20), (3, 21), (3, 34), (3, 35), (4, 0), (4, 1), (4, 10), (4, 16), (4, 20), 
    (4, 21), (5, 0), (5, 1), (5, 10), (5, 14), (5, 16), (5, 17), (5, 22), (5, 24), (6, 10), 
    (6, 16), (6, 24), (7, 11), (7, 15), (8, 12), (8, 13)
]

lightweight_spaceship = [
    (0, 0), (0, 3), (1, 4), (2, 0), (2, 4), (3, 1), (3, 2), (3, 3), (3, 4)
]

middleweight_spaceship = [
    (0, 2), (1, 0), (1, 4), (2, 5), (3, 0), (3, 5), (4, 1), (4, 2), (4, 3), (4, 4), 
    (4, 5)
]

heavyweight_spaceship = [
    (0, 2), (0, 3), (1, 0), (1, 5), (2, 6), (3, 0), (3, 6), (4, 1), (4, 2), (4, 3), 
    (4, 4), (4, 5), (4, 6)
]

puffers = [
    (0, 3), (1, 4), (2, 0), (2, 4), (3, 1), (3, 2), (3, 3), (3, 4), (7, 0), (8, 1), 
    (8, 2), (9, 2), (10, 2), (11, 1), (14, 3), (15, 4), (16, 0), (16, 4), (17, 1), (17, 2), 
    (17, 3), (17, 4)
]

vampire = [
    (0, 2), (0, 3), (0, 4), (1, 2), (1, 4), (2, 2), (2, 4), (3, 3), (4, 0), (4, 2), 
    (4, 3), (4, 4), (5, 1), (5, 3), (5, 5), (6, 3), (6, 6), (7, 2), (7, 4), (8, 2), 
    (8, 4)
]

def get_gosper_glider_gun():
    return gosper_glider_gun

def get_lightweight_spaceship():
    return lightweight_spaceship

def get_middleweight_spaceship():
    return middleweight_spaceship

def get_heavyweight_spaceship():
    return heavyweight_spaceship

def get_puffers():
    return puffers

def get_vampire():
    return vampire

# 回転・反転させたいから変数でよし
