from Node import Node
from typing import Tuple

class Snake:
    """
    This class represent Snake.
    Each Snake have head, tail, direction and length.
    """

    def __init__(self):
        """
        This function initialize all values for single Snake instance.
        None by default.
        """
        self._head = None
        self._tail = None
        self._direction = None
        self._length = None

    def add_node(self, node: Node) -> None:
        """
        This function add node to after the head.
        If the head is None, self._head = self._tail = node.
        :param node: The new node we want to add, type Node.
        :return: None.
        """
        if self._head is None:
            self._head = self._tail = node
        else:
            node.set_prev(self._head)
            self._head.set_next(node)
            self._head = node

    def get_head(self) -> Node:
        """
        This function return the head of the Snake.
        :return: self_.head, type Node.
        """
        return self._head

    def get_tail(self) -> Node:
        """
        This function return the tail of the Snake.
        :return: self._tail, type Node.
        """
        return self._tail

    def set_direction(self, direction: str) -> None:
        """
        This function set new direction for the Snake instance.
        :param direction: The new direction, type str.
        :return: None.
        """
        self._direction = direction

    def get_direction(self) -> str:
        """
        This function return the direction of the Snake.
        :return: self._direction, type str.
        """
        return self._direction

    def change_direction(self, direction: str) -> None:
        """
        This function change the direction of the Snake.
        :param direction: The new direction, type str.
        :return: None.
        """
        self._direction = direction

    def set_length(self, length: int) -> None:
        """
        This function set new length for the snake.
        :param length: The new length, type int.
        :return: None.
        """
        self._length = length

    def get_length(self) -> int:
        """
        This function return the length of the Snake.
        :return: self._length, type int.
        """
        return self._length

    def update_tail(self) -> None:
        """
        This function remove the tail and point's to the self._tail.get_next().
        Meaning new tail is equal self._tail.get_next().
        :return: None.
        """
        if self._tail.get_next() is not None:
            self._tail = self._tail.get_next()
            self._tail.get_prev().set_next(None)
            self._tail.set_prev(None)

    def is_in_snake(self, coordinates: Tuple[int, int], check_head: bool) -> bool:
        """
        This function check if the coordinates is filled by the snake.
        :param check_head:
        :param coordinates: The coordinates we want to check, type Tuple[int, int].
        :return: bool.
        """
        traveller = self._head
        if not check_head:
            traveller = self._head.get_prev()
        while traveller is not None:
            if (traveller.get_data()[0], traveller.get_data()[1]) == coordinates:
                return True
            traveller = traveller.get_prev()

        return False
