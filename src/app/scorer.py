import abc

from app.throw import AbstractThrowNode


class AbstractScorer(abc.ABC):
    def __init__(self, starting_throw: AbstractThrowNode):
        self.starting_throw = starting_throw

    @property
    @abc.abstractmethod
    def score(self) -> int:
        pass


class StrikeScorer(AbstractScorer):
    @property
    def strike_base_score(self) -> int:
        return 10

    @property
    def score(self) -> int:
        return int(
            self.strike_base_score
            + self.starting_throw.next
            + self.starting_throw.second_next
        )


class SpareScorer(AbstractScorer):
    @property
    def spare_base_score(self) -> int:
        return 10

    @property
    def score(self) -> int:
        return int(self.spare_base_score + self.starting_throw.second_next)


class IncompleteFrameScorer(AbstractScorer):
    @property
    def score(self) -> int:
        return int(self.starting_throw)


class OpenFrameScorer(AbstractScorer):
    @property
    def score(self) -> int:
        return int(self.starting_throw + self.starting_throw.next)
