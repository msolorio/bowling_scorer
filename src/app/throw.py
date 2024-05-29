import abc


class ThrowFactory:
    @staticmethod
    def new_throw(num_of_pins=None):
        if num_of_pins is not None:
            return ThrowNode(num_of_pins)
        else:
            return EmptyNode()


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

    @abc.abstractmethod
    def xth_later_throw(self, x: int) -> "AbstractThrowNode":
        pass

    def __int__(self):
        return self.num_of_pins

    def __bool__(self):
        return True


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

    def xth_later_throw(self, x: int) -> "AbstractThrowNode":
        return self

    def __add__(self, other: AbstractThrowNode) -> AbstractThrowNode:
        return other

    def __radd__(self, other: AbstractThrowNode) -> AbstractThrowNode:
        return self.__add__(other)

    def __bool__(self):
        return False


class ThrowNode(AbstractThrowNode):
    def __init__(self, num_of_pins: int, empty_node=EmptyNode):
        self._num_of_pins = num_of_pins
        self._next = empty_node()

    def __eq__(self, other):
        return self._num_of_pins == other

    def __req__(self, other):
        return self.__eq__(other)

    def __add__(self, other: AbstractThrowNode) -> "ThrowNode":
        if isinstance(other, int):
            return ThrowNode(self._num_of_pins + other)

        return ThrowNode(self._num_of_pins + other.num_of_pins)

    def __radd__(self, other: AbstractThrowNode) -> "ThrowNode":
        return self.__add__(other)

    @property
    def num_of_pins(self):
        return self._num_of_pins

    @property
    def next(self):
        return self._next

    @next.setter
    def next(self, next_throw: int):
        if isinstance(next_throw, ThrowNode):
            self._next = next_throw
        else:
            self._next = ThrowNode(next_throw)

    @property
    def second_next(self):
        return self._next.next if self._next else self._next

    @property
    def is_strike(self) -> bool:
        return self.num_of_pins == 10

    @property
    def is_spare(self) -> bool:
        return self.num_of_pins + self._next.num_of_pins == 10

    @property
    def num_of_later_throws(self) -> int:
        num = 0
        throw = self.next
        while throw:
            num += 1
            throw = throw.next
        return num

    def xth_later_throw(self, x: int) -> "AbstractThrowNode":
        i = 0
        throw = self
        while i < x:
            i += 1
            throw = throw.next
        return throw
