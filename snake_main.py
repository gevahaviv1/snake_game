from game_display import GameDisplay
from Snake import Snake
import snake_helper
from Apple import Apple
from Bomb import Bomb


def main_loop(gd: GameDisplay) -> None:
    # Initialize snake.
    snake = Snake()
    snake_helper.initialize_snake(snake)

    # Initialize bomb.
    bomb = Bomb()
    bomb.create_bomb()
    while snake.is_in_snake((bomb.get_x(), bomb.get_y()), True):
        bomb.create_bomb()
    radius = -1
    bomb_time = bomb.get_time()
    blast = []

    # Initialize apples.
    list_of_apples = [Apple() for _ in range(3)]
    score = 0
    apple_eaten = 0
    game_on = True

    #  Start.
    snake_helper.draw_snake(snake, gd, bomb, blast)
    gd.draw_cell(bomb.get_x(), bomb.get_y(), 'red')
    apple_eaten, score, list_of_apples = snake_helper.update_apples_and_score(snake, gd, list_of_apples,
                                                                              score, apple_eaten, bomb, blast)
    for apple in list_of_apples:
        gd.draw_cell(apple.get_x(), apple.get_y(), 'green')
    gd.show_score(score)
    gd.end_round()

    while game_on:
        # Snake
        snake_helper.change_direction(snake, gd.get_key_clicked())
        snake_helper.move_snake(snake, apple_eaten)
        if snake_helper.snake_on_snake(snake):
            game_on = False
        if not snake_helper.check_boundaries(snake):
            game_on = False

        # Apples
        if snake_helper.no_place_for_apples_in_board(snake):
            game_on = False

        apple_eaten, score, list_of_apples = snake_helper.update_apples_and_score(snake, gd, list_of_apples,
                                                                                  score, apple_eaten, bomb, blast)
        for apple in list_of_apples:
            gd.draw_cell(apple.get_x(), apple.get_y(), 'green')

        snake_helper.draw_snake(snake, gd, bomb, blast)
        # Bomb
        if 1 < bomb_time:
            gd.draw_cell(bomb.get_x(), bomb.get_y(), 'red')

        bomb_time -= 1
        if bomb_time <= 0:
            radius += 1
            blast = snake_helper.explosion(gd, bomb, radius)

        if radius > bomb.get_radius():
            blast = []
            radius = 0
            if snake_helper.create_bomb(bomb, snake, list_of_apples):
                bomb.create_bomb()
            bomb_time = bomb.get_time()

        list_of_apples = snake_helper.bomb_hit_apples(snake, list_of_apples, blast)
        if snake_helper.snake_in_blast(snake, blast):
            game_on = False

        if not snake_helper.snake_touch_bomb(snake, bomb):
            game_on = False

        gd.end_round()
