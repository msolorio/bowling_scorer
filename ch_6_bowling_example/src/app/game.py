from app.frames import Frames
from app.frame import Frame
from app.throw import Throw

# class Throws:
#     def __init__(self):
#         self._throws = []

#     def add_throw(self, num_of_pins: int):
#         self._throws.append(num_of_pins)

#     def get_throw(self, index: int) -> int:
#         return self._throws[index] if index < len(self._throws) else 0

#     # get next throw

#     # get next next throw


# possible Throw class that knows its next throw and next next throw


class Game:
    def __init__(self):
        self._throws = []
        self.first_throw = None
        self._last_throw = None

    @property
    def _frames(self) -> list[Frame]:
        return Frames(throws=self._throws, first_throw=self.first_throw)

    @property
    def score(self) -> int:
        return self.score_at_frame(len(self._frames))

    @property
    def current_frame_number(self) -> int:
        return self._frames.current_frame_number

    def add_throw(self, num_of_pins: int):
        self._throws.append(num_of_pins)

        if not self.first_throw:
            first_throw = Throw(num_of_pins)
            self.first_throw = first_throw
            self._last_throw = first_throw
        else:
            self._last_throw.next = num_of_pins
            self._last_throw = self._last_throw.next

        return

    def score_at_frame(self, frame: int) -> int:
        return sum(frame.score for frame in self._frames[:frame])
