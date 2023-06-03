import game_parameters


class Apple:
    """
    This class represents the Apple objects of the game.
    """
    def __init__(self) -> None:
        self._apple = game_parameters.get_random_apple_data()

    def new_apple(self) -> None:
        """
        This function creates new apple object.
        :return: None.
        """
        self._apple = game_parameters.get_random_apple_data()

    def get_x(self) -> int:
        """
        This function returns the x coordinate of the apple.
        :return: x coordinate, type int.
        """
        return self._apple[0]

    def get_y(self) -> int:
        """
        This function returns the y coordinate of the apple.
        :return: y coordinate, type int.
        """
        return self._apple[1]

    def get_score(self) -> int:
        """
        This function return the score value of the apple.
        :return: score value, type int.
        """
        return self._apple[2]
