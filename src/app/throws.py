from app.throw import Throw, EmptyNode


class Throws:
    def __init__(self):
        self._first = EmptyNode()
        self._last = self._first

    def add(self, num_of_pins: int):
        if not self._first:
            self._first = Throw(num_of_pins)
            self._last = self._first
        else:
            self._last.next = num_of_pins
            self._last = self._last.next

    @property
    def first(self):
        return self._first
