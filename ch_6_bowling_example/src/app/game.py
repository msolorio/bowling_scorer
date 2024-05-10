from app.frames import Frames
from app.frame import Frame


class Throws:
    def __init__(self):
        self._throws = []

    def add_throw(self, num_of_pins: int):
        self._throws.append(num_of_pins)

    def get_throw(self, index: int) -> int:
        return self._throws[index] if index < len(self._throws) else 0

    # get next throw

    # get next next throw


# possible Throw class that knows its next throw and next next throw


class Game:
    def __init__(self):
        self._throws = []

    @property
    def _frames(self) -> list[Frame]:
        return Frames(self._throws)

    @property
    def score(self) -> int:
        return self.score_at_frame(len(self._frames))

    @property
    def current_frame_number(self) -> int:
        return self._frames.current_frame_number

    def add_throw(self, num_of_pins: int):
        self._throws.append(num_of_pins)

    def score_at_frame(self, frame: int) -> int:
        return sum(frame.score for frame in self._frames[:frame])
