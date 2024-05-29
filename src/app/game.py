from app.frames import Frames
from app.frame import Frame
from app.throws import Throws


class Game:
    def __init__(self, throws=Throws, frames=Frames):
        self._throws = throws()
        self._frames_creator = frames

    @property
    def _frames(self) -> list[Frame]:
        return self._frames_creator(throws=self._throws)

    @property
    def score(self) -> int:
        return self.score_at_frame(len(self._frames))

    @property
    def current_frame_number(self) -> int:
        return self._frames.current_frame_number

    def add_throw(self, num_of_pins: int):
        self._throws.add(num_of_pins)

    def score_at_frame(self, frame_num: int) -> int:
        return self._frames.score_at_frame(frame_num)
