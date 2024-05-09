from app.frame import Frame, StrikeFrame, SpareFrame, OpenFrame, IncompleteFrame


class Throws:
    def __init__(self):
        self._throws = []

    def add_throw(self, num_of_pins: int):
        self._throws.append(num_of_pins)

    def get_throw(self, index: int) -> int:
        return self._throws[index] if index < len(self._throws) else 0


class Game:
    def __init__(self):
        self._throws = []

    @property
    def _frames(self) -> list[Frame]:
        return self._get_frames(self._throws)

    def _get_frames(self, throws: list[int]) -> list[Frame]:
        _frames_list = []
        i = 0
        while i < len(throws):
            new_frame = None
            if throws[i] == 10:
                new_frame = StrikeFrame(
                    next_throw=throws[i + 1] if i + 1 < len(throws) else 0,
                    second_next_throw=throws[i + 2] if i + 2 < len(throws) else 0,
                )
                _frames_list.append(new_frame)
                i += 1
            elif i == len(throws) - 1:
                new_frame = IncompleteFrame(first_throw=throws[i])
                _frames_list.append(new_frame)
                i += 1
            elif throws[i] + throws[i + 1] == 10:
                new_frame = SpareFrame(
                    next_throw=throws[i + 2] if i + 2 < len(throws) else 0,
                )
                _frames_list.append(new_frame)
                i += 2
            else:
                new_frame = OpenFrame(first_throw=throws[i], second_throw=throws[i + 1])
                _frames_list.append(new_frame)
                i += 2

            if len(_frames_list) > 1:
                _frames_list[-2].next_frame = new_frame

        return _frames_list

    @property
    def score(self) -> int:
        return self.score_at_frame(len(self._frames))

    @property
    def last_frame(self) -> Frame:
        return self._frames[-1] if self._frames else None

    @property
    def last_frame_complete(self) -> bool:
        return (not self.last_frame) or self.last_frame.is_full

    @property
    def current_frame_number(self) -> int:
        return len(self._frames) + 1 if self.last_frame_complete else len(self._frames)

    def add_throw(self, num_of_pins: int):
        self._throws.append(num_of_pins)

    def score_at_frame(self, frame: int) -> int:
        return sum(frame.score for frame in self._frames[:frame])
