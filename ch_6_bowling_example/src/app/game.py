class Game:
    def __init__(self):
        self._score = 0
        self._throws = []

    def score(self) -> int:
        return sum(self._throws)

    def add_throw(self, num_of_pins: int):
        self._throws.append(num_of_pins)

    def score_at_frame(self, frame: int) -> int:
        first_throw_index = (frame * 2) - 2
        previous_frames_score = sum(self._throws[:first_throw_index])
        downed_pins = sum(self._throws[first_throw_index : first_throw_index + 2])

        if downed_pins == 10:
            return (
                previous_frames_score
                + downed_pins
                + self._throws[first_throw_index + 2]
            )
        else:
            return previous_frames_score + downed_pins


class Frame_2:
    def __init__(self):
        self.next_frame: Frame_2 | None = None
        self.first_throw: int | None = None
        self.second_throw: int | None = None

    @property
    def first_throw_score(self) -> int:
        return self.first_throw or 0

    @property
    def second_throw_score(self) -> int:
        return self.second_throw or 0

    @property
    def next_frame_second_throw(self) -> int:
        return self.next_frame.second_throw_score if self.next_frame else 0

    @property
    def next_throw(self) -> int:
        return self.next_frame.first_throw_score if self.next_frame else 0

    @property
    def second_next_throw(self) -> int:
        if self.next_frame:
            if self.next_frame.is_strike:
                return self.next_frame.next_throw
            else:
                return self.next_frame.second_throw
        else:
            return 0

    @property
    def score(self) -> int:
        if self.is_strike:
            return 10 + self.next_throw + self.second_next_throw
        elif self.is_spare:
            return 10 + self.next_throw
        else:
            return self.first_throw_score + self.second_throw_score

    @property
    def is_strike(self) -> bool:
        return self.first_throw_score == 10

    @property
    def is_spare(self) -> bool:
        return self.first_throw_score + self.second_throw_score == 10

    @property
    def is_full(self) -> bool:
        return self.first_throw is not None and self.second_throw is not None

    def add_throw(self, num_of_pins: int):
        if self.first_throw is None:
            self.first_throw = num_of_pins
        elif self.second_throw is None:
            self.second_throw = num_of_pins
        else:
            raise ValueError("Frame is already full")


class Game_2:
    def __init__(self):
        self._frames = []
        self._first_throw: bool = True

    @property
    def score(self) -> int:
        return self.score_at_frame(len(self._frames))

    @property
    def last_frame(self) -> Frame_2:
        return self._frames[-1] if self._frames else None

    def link_new_frame(self, frame: Frame_2):
        if self.last_frame:
            self.last_frame.next_frame = frame

    @property
    def current_frame(self) -> Frame_2:
        if self._first_throw:
            new_frame = Frame_2()
            self.link_new_frame(new_frame)
            self._frames.append(new_frame)
            return new_frame
        else:
            return self._frames[-1]

    @property
    def current_frame_number(self) -> int:
        if self._first_throw:
            return len(self._frames) + 1
        else:
            return len(self._frames)

    def add_throw(self, num_of_pins: int):
        self.current_frame.add_throw(num_of_pins)

        if not self._first_throw or num_of_pins == 10:
            self._first_throw = True
        else:
            self._first_throw = False

    def score_at_frame(self, frame: int) -> int:
        return sum(frame.score for frame in self._frames[:frame])
