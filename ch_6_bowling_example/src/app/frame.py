class Frame:
    def __init__(self):
        self.next_frame: Frame | None = None
        self.first_throw: int | None = None
        self.second_throw: int | None = None

    @property
    def score(self) -> int:
        raise NotImplementedError

    @property
    def is_full(self) -> bool:
        raise NotImplementedError

    @property
    def add_throw(self, num_of_pins: int):
        raise NotImplementedError


class StrikeFrame(Frame):
    def __init__(self, next_throw=0, second_next_throw=0):
        self._score = 10 + next_throw + second_next_throw

    @property
    def is_full(self) -> bool:
        return True

    @property
    def score(self) -> int:
        return self._score

    def add_throw(self, num_of_pins: int):
        raise ValueError("Frame is already full")


class SpareFrame(Frame):
    def __init__(self, next_throw=0):
        self._score = 10 + next_throw

    @property
    def is_full(self) -> bool:
        return True

    @property
    def score(self) -> int:
        return self._score

    def add_throw(self, num_of_pins: int):
        raise ValueError("Frame is already full")


class IncompleteFrame(Frame):
    def __init__(self, first_throw: int):
        self._score = first_throw

    @property
    def score(self) -> int:
        return self._score

    @property
    def is_full(self) -> bool:
        return False

    def add_throw(self, num_of_pins: int):
        self.second_throw = num_of_pins


class OpenFrame(Frame):
    def __init__(self, first_throw: int, second_throw: int):
        self._score = first_throw + second_throw

    @property
    def is_full(self) -> bool:
        return True

    @property
    def score(self) -> int:
        return self._score

    def add_throw(self, num_of_pins: int):
        raise ValueError("Frame is already full")
