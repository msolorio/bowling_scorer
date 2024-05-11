import abc

from app.throw import Throw


class FrameFactory:
    @staticmethod
    def new_frame(starting_throw: Throw, frame_number: int) -> "Frame":
        if frame_number == 10:
            frame = FrameFactory.new_final_frame(starting_throw)
        elif starting_throw.is_strike:
            frame = StrikeFrame
        elif not starting_throw.next:
            frame = IncompleteFrame
        elif starting_throw.is_spare:
            frame = SpareFrame
        else:
            frame = OpenFrame

        return frame(starting_throw)

    @staticmethod
    def new_final_frame(starting_throw: Throw) -> "Frame":
        if starting_throw.is_strike or starting_throw.is_spare:
            return LastFrameStrikeOrSpare
        elif starting_throw.next:
            return LastFrameOpenFrame
        else:
            return IncompleteFrame


class Frame(abc.ABC):
    def __init__(self, starting_throw: Throw):
        self.starting_throw = starting_throw

    @property
    @abc.abstractmethod
    def score(self) -> int:
        pass

    @property
    @abc.abstractmethod
    def is_full(self) -> bool:
        pass

    @property
    @abc.abstractmethod
    def num_of_throws(self) -> bool:
        pass


class StrikeFrame(Frame):
    @property
    def is_full(self) -> bool:
        return True

    @property
    def score(self) -> int:
        return int(
            self.starting_throw
            + self.starting_throw.next
            + self.starting_throw.second_next
        )

    @property
    def num_of_throws(self) -> bool:
        return 1


class SpareFrame(Frame):
    @property
    def is_full(self) -> bool:
        return True

    @property
    def score(self) -> int:
        return int(
            self.starting_throw
            + self.starting_throw.next
            + self.starting_throw.second_next
        )

    @property
    def num_of_throws(self) -> bool:
        return 2


class IncompleteFrame(Frame):
    @property
    def score(self) -> int:
        return int(self.starting_throw)

    @property
    def is_full(self) -> bool:
        return False

    @property
    def num_of_throws(self) -> bool:
        return 1


class OpenFrame(Frame):
    @property
    def is_full(self) -> bool:
        return True

    @property
    def score(self) -> int:
        return int(self.starting_throw + self.starting_throw.next)

    @property
    def num_of_throws(self) -> bool:
        return 2


class LastFrameOpenFrame(Frame):
    @property
    def is_full(self) -> bool:
        return True

    @property
    def score(self) -> int:
        return int(self.starting_throw + self.starting_throw.next)

    @property
    def num_of_throws(self) -> bool:
        return 2


class LastFrameStrikeOrSpare(Frame):
    @property
    def is_full(self) -> bool:
        return self.num_of_throws == 3

    @property
    def score(self) -> int:
        return int(
            self.starting_throw
            + self.starting_throw.next
            + self.starting_throw.second_next
        )

    @property
    def num_of_throws(self) -> bool:
        num = 0
        current_throw = self.starting_throw
        while current_throw:
            num += 1
            current_throw = current_throw.next
        return num
