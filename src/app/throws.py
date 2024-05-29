from app.throw import ThrowFactory


class Throws:
    def __init__(self, throw_factory=ThrowFactory):
        self._throw_factory = throw_factory
        self._first = throw_factory.new_throw()
        self._last = self._first

    def add(self, num_of_pins: int):
        if not self._first:
            self._first = self._throw_factory.new_throw(num_of_pins)
            self._last = self._first
        else:
            self._last.next = num_of_pins
            self._last = self._last.next

    @property
    def first(self):
        return self._first
