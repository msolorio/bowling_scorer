import abc


class AbstractThrowNode(abc.ABC):
    @property
    @abc.abstractmethod
    def num_of_pins(self) -> int:
        pass

    @property
    @abc.abstractmethod
    def next(self) -> "AbstractThrowNode":
        pass

    @property
    @abc.abstractmethod
    def second_next(self) -> "AbstractThrowNode":
        pass

    @property
    @abc.abstractmethod
    def is_strike(self) -> bool:
        pass

    @property
    @abc.abstractmethod
    def is_spare(self) -> bool:
        pass

    def __int__(self):
        return self.num_of_pins

    def __bool__(self):
        return True


class Throw(AbstractThrowNode):
    def __init__(self, num_of_pins: int):
        self._num_of_pins = num_of_pins
        self._next = EmptyNode()

    def __eq__(self, other):
        return self._num_of_pins == other

    def __add__(self, other: AbstractThrowNode) -> "Throw":
        return Throw(self._num_of_pins + other.num_of_pins)

    def __radd__(self, other: AbstractThrowNode) -> "Throw":
        return self.__add__(other)

    @property
    def num_of_pins(self):
        return self._num_of_pins

    @property
    def next(self):
        return self._next

    @next.setter
    def next(self, next_throw: int):
        self._next = Throw(next_throw)

    @property
    def second_next(self):
        return self._next.next if self._next else self._next

    @property
    def is_strike(self) -> bool:
        return self._num_of_pins == 10

    @property
    def is_spare(self) -> bool:
        return self._num_of_pins + self._next.num_of_pins == 10


class EmptyNode(AbstractThrowNode):
    @property
    def num_of_pins(self):
        return 0

    @property
    def next(self):
        return self

    @property
    def second_next(self):
        return self

    @property
    def is_strike(self) -> bool:
        return False

    @property
    def is_spare(self) -> bool:
        return False

    def __add__(self, other: AbstractThrowNode) -> AbstractThrowNode:
        return other

    def __radd__(self, other: AbstractThrowNode) -> AbstractThrowNode:
        return self.__add__(other)

    def __bool__(self):
        return False
