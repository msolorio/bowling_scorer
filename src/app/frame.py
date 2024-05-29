import abc

from app.throw import AbstractThrowNode
from app.scorer import (
    AbstractScorer,
    StrikeScorer,
    SpareScorer,
    OpenFrameScorer,
)


class FrameFactory:
    @staticmethod
    def new_frame(starting_throw: AbstractThrowNode, frame_number: int) -> "Frame":
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
    def __init__(self, starting_throw: AbstractThrowNode):
        self.starting_throw = starting_throw

    @property
    def score(self) -> int:
        return self.scorer(self.starting_throw).score

    @property
    def is_full(self) -> bool:
        return (1 + self.starting_throw.num_of_later_throws) >= self.total_throws

    @property
    @abc.abstractmethod
    def scorer(self) -> AbstractScorer:
        pass

    @property
    @abc.abstractmethod
    def total_throws(self) -> bool:
        pass


class StrikeFrame(Frame):
    @property
    def scorer(self):
        return StrikeScorer

    @property
    def total_throws(self) -> bool:
        return 1


class SpareFrame(Frame):
    @property
    def scorer(self):
        return SpareScorer

    @property
    def total_throws(self) -> bool:
        return 2


class OpenFrame(Frame):
    @property
    def scorer(self):
        return OpenFrameScorer

    @property
    def total_throws(self) -> bool:
        return 2


class LastStrikeFrame(Frame):
    @property
    def scorer(self):
        return StrikeScorer

    @property
    def total_throws(self) -> bool:
        return 3


class LastSpareFrame(Frame):
    @property
    def scorer(self):
        return SpareScorer

    @property
    def total_throws(self) -> bool:
        return 3
