import math
PLAYER_SPEED:int = 2
SCREEN_SIZE:tuple[int, int] = (1920, 1080)
BULLET_SIZE:tuple[int, int] = (10, 10)
BULLET_SPEED:int = 12
PLAYER_BULLET_COLOUR: tuple[int, int, int] = (0, 125, 255)
TOWER_BULLET_COLOUR: tuple[int, int, int] = (248, 26, 38)
PLAYER_BULLET_DAMAGE = 1
PLAYER_FIRE_RATE: int = 40
ENEMY_SPEED: int = 2
MAX_RADIUS_FROM_FLAG = math.sqrt((SCREEN_SIZE[0]/2)**2+(SCREEN_SIZE[1]/2)**2)
SCREEN_CENTRE: tuple[int, int] = (SCREEN_SIZE[0]//2, SCREEN_SIZE[1]//2)
TAB_COLOUR: str = "grey"
TAB_SELECT_COLOUR: str = "white"

WAVES = {
    1: (("g", 50),),
    2: (("g", 100),),
    3: (("g", 150),)
}

def getAngle(current: tuple[int, int], target: tuple[int, int]) -> float:
    tar_x, tar_y = target
    x_diff = current[0] - tar_x
    y_diff = current[1] - tar_y
    try:
        angle = math.atan(y_diff / x_diff)
        angle = math.pi - angle - 0.5 * math.pi
    except ZeroDivisionError:
        if tar_y > current[1]:
            angle = math.pi
        else:
            angle = 0
    if tar_x > current[0]:
        angle += math.pi
    return angle

def get_distance(pointA:tuple[int,int], pointB:tuple[int,int])->int:
    ab = (pointB[0]-pointA[0], pointB[1]-pointA[1])
    return int(math.sqrt(ab[0]**2+ab[1]**2))

