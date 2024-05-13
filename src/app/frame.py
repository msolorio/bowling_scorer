import abc

from app.throw import Throw
from app.scorer import (
    AbstractScorer,
    StrikeScorer,
    SpareScorer,
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
    def is_full(self) -> bool:
        completed_throws = 0
        throw = self.starting_throw
        while throw:
            completed_throws += 1
            throw = throw.next
        return completed_throws >= self.num_of_throws

    @property
    @abc.abstractmethod
    def scorer(self) -> AbstractScorer:
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
    def num_of_throws(self) -> bool:
        return 1


class SpareFrame(Frame):
    @property
    def scorer(self):
        return SpareScorer

    @property
    def num_of_throws(self) -> bool:
        return 2


class OpenFrame(Frame):
    @property
    def scorer(self):
        return OpenFrameScorer

    @property
    def num_of_throws(self) -> bool:
        return 2


class LastStrikeFrame(Frame):
    @property
    def scorer(self):
        return StrikeScorer

    @property
    def num_of_throws(self) -> bool:
        return 3


class LastSpareFrame(Frame):
    @property
    def scorer(self):
        return SpareScorer

    @property
    def num_of_throws(self) -> bool:
        return 3
