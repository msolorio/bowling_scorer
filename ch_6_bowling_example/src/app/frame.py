import abc

from app.throw import Throw


class FrameFactory:
    @staticmethod
    def new_frame(starting_throw: Throw) -> "Frame":
        if starting_throw == 10:
            frame = StrikeFrame
        elif starting_throw.next is None:
            frame = IncompleteFrame
        elif starting_throw + starting_throw.next == 10:
            frame = SpareFrame
        else:
            frame = OpenFrame

        return frame(starting_throw)


class Frame(abc.ABC):
    def __init__(self, starting_throw: Throw):
        self.starting_throw = starting_throw

    @property
    @abc.abstractmethod
    def score(self) -> int:
        pass

    @property
    @abc.abstractmethod
    def is_full(self) -> bool:
        pass

    @property
    @abc.abstractmethod
    def add_throw(self, num_of_pins: int):
        pass

    @property
    @abc.abstractmethod
    def num_of_throws(self) -> bool:
        pass


class StrikeFrame(Frame):
    @property
    def is_full(self) -> bool:
        return True

    @property
    def score(self) -> int:
        return (
            self.starting_throw
            + self.starting_throw.next
            + self.starting_throw.second_next
        )

    def add_throw(self, num_of_pins: int):
        raise ValueError("Frame is already full")

    @property
    def num_of_throws(self) -> bool:
        return 1


class SpareFrame(Frame):
    @property
    def is_full(self) -> bool:
        return True

    @property
    def score(self) -> int:
        return (
            self.starting_throw
            + self.starting_throw.next
            + self.starting_throw.second_next
        )

    def add_throw(self, num_of_pins: int):
        raise ValueError("Frame is already full")

    @property
    def num_of_throws(self) -> bool:
        return 2


class IncompleteFrame(Frame):
    @property
    def score(self) -> int:
        return self.starting_throw

    @property
    def is_full(self) -> bool:
        return False

    def add_throw(self, num_of_pins: int):
        self.second_throw = num_of_pins

    @property
    def num_of_throws(self) -> bool:
        return 1


class OpenFrame(Frame):
    @property
    def is_full(self) -> bool:
        return True

    @property
    def score(self) -> int:
        return self.starting_throw + self.starting_throw.next

    def add_throw(self, num_of_pins: int):
        raise ValueError("Frame is already full")

    @property
    def num_of_throws(self) -> bool:
        return 2
