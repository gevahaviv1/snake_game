import game_parameters


class Bomb:
    """
    This class represents the Bomb objects of the game.
    """
    def __init__(self) -> None:
        self._bomb = None

    def create_bomb(self) -> None:
        """
        This function creates new bomb object.
        :return: None.
        """
        self._bomb = game_parameters.get_random_bomb_data()

    def get_x(self) -> int:
        """
        This function returns the x coordinate of the bomb.
        :return: x coordinate, type int.
        """
        return self._bomb[0]

    def get_y(self) -> int:
        """
        This function returns the y coordinate of the bomb.
        :return: y coordinate, type int.
        """
        return self._bomb[1]

    def get_radius(self) -> int:
        """
        This function return the radius of the bomb explosion.
        :return: radius of the bomb explosion, type int.
        """
        return self._bomb[2]

    def get_time(self):
        """
        This function return the time of the bomb explosion.
        :return: time of the bomb explosion, type int.
        """
        return self._bomb[3]
