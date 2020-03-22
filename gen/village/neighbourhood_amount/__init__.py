import random

NEIGHBOURHOOD_SIZE_TO_RANGE = {
    'tiny':         (  1,   2),
    'small':        (  5,   8),
    'medium':       ( 15,  20),
    'average':      ( 35,  45),
    'big':          ( 90, 140),
    'huge':         (250, 400),
    'humongous':    (800, 999)
}

def get_neighbourhood_amount(seed, size):
    random.seed(seed)
    sizes = NEIGHBOURHOOD_SIZE_TO_RANGE[size]
    return random.randint(*sizes)
