import abc

from app.throw import Throw
from app.scorer import (
    AbstractScorer,
    StrikeScorer,
    SpareScorer,
    IncompleteFrameScorer,
    OpenFrameScorer,
)


class FrameFactory:
    @staticmethod
    def new_frame(starting_throw: Throw, frame_number: int) -> "Frame":
        if frame_number == 10 and starting_throw.is_strike:
            frame = LastStrikeFrame
        elif frame_number == 10 and starting_throw.is_spare:
            frame = LastSpareFrame
        elif starting_throw.is_strike:
            frame = StrikeFrame
        elif starting_throw.is_spare:
            frame = SpareFrame
        elif not starting_throw.next:
            frame = IncompleteFrame
        else:
            frame = OpenFrame

        return frame(starting_throw)


class Frame(abc.ABC):
    def __init__(self, starting_throw: Throw):
        self.starting_throw = starting_throw

    @property
    def score(self) -> int:
        return self.scorer(self.starting_throw).score

    @property
    @abc.abstractmethod
    def scorer(self) -> AbstractScorer:
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
    def scorer(self):
        return StrikeScorer

    @property
    def is_full(self) -> bool:
        return True

    @property
    def num_of_throws(self) -> bool:
        return 1


class SpareFrame(Frame):
    @property
    def scorer(self):
        return SpareScorer

    @property
    def is_full(self) -> bool:
        return True

    @property
    def num_of_throws(self) -> bool:
        return 2


class IncompleteFrame(Frame):
    @property
    def scorer(self):
        return IncompleteFrameScorer

    @property
    def is_full(self) -> bool:
        return False

    @property
    def num_of_throws(self) -> bool:
        return 1


class OpenFrame(Frame):
    @property
    def scorer(self):
        return OpenFrameScorer

    @property
    def is_full(self) -> bool:
        return True

    @property
    def num_of_throws(self) -> bool:
        return 2


def ThreeThrowFrame(_scorer):
    class ThreeThrowFrame(Frame):
        @property
        def scorer(self):
            return _scorer

        @property
        def is_full(self) -> bool:
            return bool(self.starting_throw.second_next)

        @property
        def num_of_throws(self) -> bool:
            return 3

    return ThreeThrowFrame


LastStrikeFrame = ThreeThrowFrame(StrikeScorer)
LastSpareFrame = ThreeThrowFrame(SpareScorer)
