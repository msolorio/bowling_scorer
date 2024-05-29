from app.frame import FrameFactory, Frame
from app.throws import Throws


class Frames:
    def __init__(
        self,
        throws: Throws,
        frame_factory=FrameFactory,
    ):
        self.frame_factory = frame_factory
        self._frames = []
        self._generate_frames(throws=throws)

    def __repr__(self):
        return self._frames

    @property
    def current_frame_number(self) -> int:
        if self._starting_new_frame:
            return len(self._frames) + 1
        else:
            return len(self._frames)

    def score_at_frame(self, frame_num: int) -> int:
        return sum(frame.score for frame in self._frames[:frame_num])

    @property
    def _starting_new_frame(self) -> bool:
        return not self._frames or self._frames[-1].is_full

    def _generate_frames(self, throws) -> list[Frame]:
        current_throw = throws.first
        while current_throw:
            new_frame = self.frame_factory.new_frame(
                starting_throw=current_throw,
                frame_number=self.current_frame_number,
            )
            self._frames.append(new_frame)
            current_throw = current_throw.xth_later_throw(new_frame.total_throws)

    def __len__(self):
        return len(self._frames)

    def __getitem__(self, index):
        return self._frames[index]
