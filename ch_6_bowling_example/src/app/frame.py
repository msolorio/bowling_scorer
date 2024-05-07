class Frame:
    def __init__(self):
        self._score = 0

    def score(self) -> int:
        return self._score

    def add_throw(self, num_of_pins: int):
        self._score += num_of_pins


class Frame_2:
    pass
