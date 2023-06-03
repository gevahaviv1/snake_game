from typing import Tuple


class Node:
    """
    This class represent Node.
    Each Node have data, next and prev.
    """

    def __init__(self, data: Tuple[int, int] = None) -> None:
        """
        This function initialize all values for single Node instance.
        None by default.
        :param data: The instance data, type Tuple[int, int].
        """
        self._data = data
        self._next = None
        self._prev = None

    def set_data(self, data: Tuple[int, int]) -> None:
        """
        This function set data in self._data parameter of the instance.
        :param data: The data we want to put, type Tuple[int, int].
        :return: None.
        """
        self._data = data

    def get_data(self) -> Tuple[int, int]:
        """
        This function return the instance data.
        :return: self._data, type Tuple[int, int].
        """
        return self._data

    def set_next(self, next) -> None:
        """
        This function set the next instance of the current instance.
        :param next: The next instance, type Node.
        :return: None.
        """
        self._next = next

    def get_next(self):
        """
        This function return the next instance of the current instance.
        :return: self._next, type Node.
        """
        return self._next

    def set_prev(self, prev) -> None:
        """
        This function set the previous instance of the current instance.
        :param prev: The previous instance, type Node.
        :return: None
        """
        self._prev = prev

    def get_prev(self):
        """
        This function return the previous instance of the current instance.
        :return: self._prev, type Node.
        """
        return self._prev
