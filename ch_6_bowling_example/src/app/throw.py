class Throw:
    def __init__(self, num_of_pins: int):
        self.num_of_pins = num_of_pins
        self._next = None

    def __eq__(self, other):
        return self.num_of_pins == other

    def __add__(self, other):
        return self.num_of_pins + other.num_of_pins

    @property
    def next(self):
        return self._next

    @next.setter
    def next(self, next_throw: int):
        self._next = Throw(next_throw)

    @property
    def second_next(self):
        return self._next.next if self._next else None
