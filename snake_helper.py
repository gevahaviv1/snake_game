from Node import Node
from Snake import Snake
from game_display import GameDisplay
from typing import List
from typing import Tuple
from Apple import Apple
from Bomb import Bomb
import game_parameters


def draw_snake(snake: Snake, gd: GameDisplay, bomb: Bomb, blast: List[Tuple[int, int]]) -> None:
    """
    This function draw the snake on the screen game.
    :param bomb:
    :param blast:
    :param gd: parameter from game_display.py, type GameDisplay.
    :param snake: The snake we want to draw.
    :return: None.
    """
    if not check_boundaries(snake):
        traveller = snake.get_head().get_prev()
    elif not snake_touch_bomb(snake, bomb):
        traveller = snake.get_head().get_prev()
    elif snake_in_blast(snake, blast):
        traveller = snake.get_head().get_prev()
    else:
        traveller = snake.get_head()
    while traveller is not None:
        gd.draw_cell(traveller.get_data()[0], traveller.get_data()[1], "black")
        traveller = traveller.get_prev()


def move_snake(snake: Snake, apple_eaten: int) -> bool:
    """
    This function move the snake on the screen game.
    If the snake ate an apple the function grow the size snake while is moving.
    If he succeeded return True otherwise return False.
    :param snake: The snake we want to move, type Snake.
    :param apple_eaten: 0 if the he didn't ate, otherwise the grow number, type int.
    :return: bool.
    """
    x = snake.get_head().get_data()[0]
    y = snake.get_head().get_data()[1]
    new_head = Node()

    if snake.get_direction() == 'Left':
        new_head.set_data((x - 1, y))
        snake.add_node(new_head)

    elif snake.get_direction() == 'Right':
        new_head.set_data((x + 1, y))
        snake.add_node(new_head)

    elif snake.get_direction() == 'Up':
        new_head.set_data((x, y + 1))
        snake.add_node(new_head)

    elif snake.get_direction() == 'Down':
        new_head.set_data((x, y - 1))
        snake.add_node(new_head)

    if apple_eaten == 0:
        snake.update_tail()

    return True


def snake_on_snake(snake: Snake) -> bool:
    """
    :param snake:
    :return:
    """
    x = snake.get_head().get_data()[0]
    y = snake.get_head().get_data()[1]
    return snake.is_in_snake((x, y), False)


def initialize_snake(snake: Snake) -> None:
    """
    This function initialize the snake on the game screen.
    The default snake: head - (10, 10), tail - (10, 8), length - 3, color - black.
    :return: None.
    """
    snake.add_node(Node((10, 8)))
    snake.add_node(Node((10, 9)))
    snake.add_node(Node((10, 10)))
    snake.set_length(3)
    snake.set_direction('Up')


def change_direction(snake: Snake, direction: str) -> None:
    """
    This function change the direction of the snake on the screen game.
    :param snake: The snake we want to change is direction, type Snake.
    :param direction: The new direction we want, type str.
    :return: None.
    """
    if direction == 'Right' and snake.get_direction() != 'Left':
        snake.change_direction('Right')
    elif direction == 'Left' and snake.get_direction() != 'Right':
        snake.change_direction('Left')
    elif direction == 'Down' and snake.get_direction() != 'Up':
        snake.change_direction('Down')
    elif direction == 'Up' and snake.get_direction() != 'Down':
        snake.change_direction('Up')


def check_boundaries(snake: Snake) -> bool:
    """
    This function checks that the snake is not out of boundaries.
    :param snake: The snake we check, type Snake.
    :return: bool.
    """
    x = snake.get_head().get_data()[0]
    y = snake.get_head().get_data()[1]

    if x < 0 or y < 0:
        return False
    if x > game_parameters.WIDTH - 1 or y > game_parameters.HEIGHT - 1:
        return False

    return True


def _new_apple_is_good(new_apple_x: int, new_apple_y: int, bomb: Bomb,
                       list_of_apples: List[Apple], blast: List[Tuple[int, int]]) -> bool:
    """
    :param new_apple_x:
    :param new_apple_y:
    :param bomb:
    :param list_of_apples:
    :param blast:
    :return:
    """
    count = 0
    if (new_apple_x, new_apple_y) == (bomb.get_x(), bomb.get_y()):
        return False
    for apple in list_of_apples:
        if (new_apple_x, new_apple_y) == (apple.get_x(), apple.get_y()):
            count += 1
    if count != 1:
        return False
    if (new_apple_x, new_apple_y) in blast:
        return False
    return True


def update_apples_and_score(snake: Snake, gd: game_parameters, list_of_apples: List[Apple], score: int,
                            apple_eaten: int, bomb: Bomb, blast: List[Tuple[int, int]]) -> (int, int, List[Apple]):
    """
    This function updating the score on board and the value of the length that needs to add for the snake as
    a result from eating an apple in the game.
    The function updating the score value according to the score value for each apple that was eaten by the snake.
    :param blast:
    :param bomb:
    :param snake: object Snake.
    :param gd: file: game_parameters.py.
    :param list_of_apples: List that including all the apples.
    :param score:
    :param apple_eaten: the value of length to add as a result of apples eaten.
    :return: apple_eaten and score after updating, types: int, int.
    """
    if apple_eaten > 0:
        snake.set_length(snake.get_length() + 1)
        apple_eaten -= 1

    for apple in list_of_apples:

        if snake.get_head().get_data() == (apple.get_x(), apple.get_y()):
            score += apple.get_score()
            apple_eaten += 3
            while True:
                list_of_apples[list_of_apples.index(apple)].new_apple()
                new_apple_x = list_of_apples[list_of_apples.index(apple)].get_x()
                new_apple_y = list_of_apples[list_of_apples.index(apple)].get_y()

                if not snake.is_in_snake((new_apple_x, new_apple_y), True) and \
                        _new_apple_is_good(new_apple_x, new_apple_y, bomb, list_of_apples, blast):
                    break

    gd.show_score(score)

    return apple_eaten, score, list_of_apples


def snake_in_blast(snake: Snake, blast: List[Tuple[int, int]]) -> bool:
    """
    This function check if the blast hurt the snake.
    :param snake: The snake on the game screen, type Snake.
    :param blast: The blast of the explosion, type list.
    :return: bool.
    """
    for fragment in blast:
        if snake.is_in_snake(fragment, True):
            return True
    return False


def snake_touch_bomb(snake: Snake, bomb: Bomb) -> bool:
    """
    :param snake:
    :param bomb:
    :return:
    """
    if snake.is_in_snake((bomb.get_x(), bomb.get_y()), True):
        return False
    return True


def _bomb_hit_apples_helper(blast: List[Tuple[int, int]], apple: Apple) -> bool:
    """
    :param blast:
    :param apple:
    :return:
    """
    for fragment in blast:
        if (apple.get_x(), apple.get_y()) == fragment:
            return True
    return False


def bomb_hit_apples(snake: Snake, list_of_apples: List[Apple], blast: List[Tuple[int, int]]) -> List[Apple]:
    """
    :param snake:
    :param list_of_apples:
    :param blast:
    :return:
    """
    for apple in list_of_apples:
        if _bomb_hit_apples_helper(blast, apple):
            while True:
                list_of_apples[list_of_apples.index(apple)].new_apple()
                new_apple_x = list_of_apples[list_of_apples.index(apple)].get_x()
                new_apple_y = list_of_apples[list_of_apples.index(apple)].get_y()

                if not snake.is_in_snake((new_apple_x, new_apple_y), True):
                    break
    return list_of_apples


def explosion(gd, bomb, radius):
    """
    :param gd:
    :param bomb:
    :param radius:
    :return:
    """
    bomb_cells = []
    for u in range(40):
        for v in range(30):
            if abs(bomb.get_x() - u) + abs(bomb.get_y() - v) == radius:
                gd.draw_cell(u, v, 'orange')
                bomb_cells.append((u, v))

    return bomb_cells


def _new_bomb_is_good(new_bomb_x: int, new_bomb_y: int, list_of_apples: List[Apple]) -> bool:
    """
    :param new_bomb_x:
    :param new_bomb_y:
    :param list_of_apples:
    :return:
    """
    for apple in list_of_apples:
        if (apple.get_x(), apple.get_y()) == (new_bomb_x, new_bomb_y):
            return False
    return True


def create_bomb(bomb: Bomb, snake: Snake, list_of_apples: List[Apple]) -> bool:
    """
    :param bomb:
    :param snake:
    :param list_of_apples:
    :param blast:
    :return:
    """
    while True:
        new_bomb_x = bomb.get_x()
        new_bomb_y = bomb.get_y()

        if not snake.is_in_snake((new_bomb_x, new_bomb_y), True) and \
                _new_bomb_is_good(new_bomb_x, new_bomb_y, list_of_apples):
            return True


def no_place_for_apples_in_board(snake: Snake) -> bool:
    """
    :param snake:
    :return:
    """
    return (game_parameters.WIDTH * game_parameters.HEIGHT) - (snake.get_length() + 1) < 3
