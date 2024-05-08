class Frame:
    def __init__(self):
        self.next_frame: Frame | None = None
        self.first_throw: int | None = None
        self.second_throw: int | None = None

    @property
    def first_throw_score(self) -> int:
        return self.first_throw or 0

    @property
    def second_throw_score(self) -> int:
        return self.second_throw or 0

    @property
    def next_throw_score(self) -> int:
        if self.next_frame:
            return self.next_frame.first_throw_score
        else:
            return 0

    @property
    def second_next_throw_score(self) -> int:
        if self.next_frame:
            if self.next_frame.is_strike:
                return self.next_frame.next_throw_score
            else:
                return self.next_frame.second_throw_score
        else:
            return 0

    @property
    def score(self) -> int:
        raise NotImplementedError

    @property
    def is_strike(self) -> bool:
        return self.first_throw_score == 10

    @property
    def is_full(self) -> bool:
        raise NotImplementedError

    def add_throw(self, num_of_pins: int):
        if self.first_throw is None:
            self.first_throw = num_of_pins
        elif self.second_throw is None:
            self.second_throw = num_of_pins
        else:
            raise ValueError("Frame is already full")


class StrikeFrame(Frame):
    def __init__(self):
        self.first_throw = 10
        self.second_throw = None

    @property
    def is_full(self) -> bool:
        return True

    @property
    def score(self) -> int:
        return 10 + self.next_throw_score + self.second_next_throw_score


class SpareFrame(Frame):
    def __init__(self, first_throw: int, second_throw: int):
        self.first_throw = first_throw
        self.second_throw = second_throw

    @property
    def is_full(self) -> bool:
        return True

    @property
    def score(self) -> int:
        return 10 + self.next_throw_score


class IncompleteFrame(Frame):
    def __init__(self, first_throw: int):
        self.first_throw = first_throw
        self.second_throw = None

    @property
    def score(self) -> int:
        return self.first_throw_score

    @property
    def is_full(self) -> bool:
        return False


class OpenFrame(Frame):
    def __init__(self, first_throw: int, second_throw: int):
        self.first_throw = first_throw
        self.second_throw = second_throw

    @property
    def is_full(self) -> bool:
        return True

    @property
    def score(self) -> int:
        return self.first_throw_score + self.second_throw_score


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
                new_frame = StrikeFrame()
                _frames_list.append(new_frame)
                i += 1
            elif i == len(throws) - 1:
                new_frame = IncompleteFrame(throws[i])
                _frames_list.append(new_frame)
                i += 1
            elif throws[i] + throws[i + 1] == 10:
                new_frame = SpareFrame(throws[i], throws[i + 1])
                _frames_list.append(new_frame)
                i += 2
            else:
                new_frame = OpenFrame(throws[i], throws[i + 1])
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
    def start_new_frame(self):
        return (not self.last_frame) or self.last_frame.is_full

    @property
    def current_frame_number(self) -> int:
        return len(self._frames) + 1 if self.start_new_frame else len(self._frames)

    def add_throw(self, num_of_pins: int):
        self._throws.append(num_of_pins)

    def score_at_frame(self, frame: int) -> int:
        return sum(frame.score for frame in self._frames[:frame])
