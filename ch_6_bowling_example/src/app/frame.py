import abc


class FrameFactory:
    @staticmethod
    def new_frame(throws: list[int], start_index: int) -> "Frame":
        if throws[start_index] == 10:
            frame = StrikeFrame
        elif start_index == len(throws) - 1:
            frame = IncompleteFrame
        elif throws[start_index] + throws[start_index + 1] == 10:
            frame = SpareFrame
        else:
            frame = OpenFrame

        return frame(throws=throws, start_index=start_index)


class Frame(abc.ABC):
    def __init__(self, throws=[], start_index=0):
        self.throws = throws
        self.start_index = start_index

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
            10 + self.throws[self.start_index + 1] + self.throws[self.start_index + 2]
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
        return 10 + self.throws[self.start_index + 2]

    def add_throw(self, num_of_pins: int):
        raise ValueError("Frame is already full")

    @property
    def num_of_throws(self) -> bool:
        return 2


class IncompleteFrame(Frame):
    @property
    def score(self) -> int:
        return self.throws[self.start_index]

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
        return self.throws[self.start_index] + self.throws[self.start_index + 1]

    def add_throw(self, num_of_pins: int):
        raise ValueError("Frame is already full")

    @property
    def num_of_throws(self) -> bool:
        return 2
