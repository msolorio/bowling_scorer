from app.frame import FrameFactory, Frame
from app.throws import Throws
from app.throw import Throw


class Frames:
    def __init__(
        self,
        throws: Throws = None,
        frame_factory: FrameFactory = FrameFactory,
    ):
        self.frame_factory = frame_factory
        self._frames = []
        self._generate_frames(throws=throws)

    def __repr__(self):
        return self._frames

    @property
    def current_frame_number(self) -> bool:
        if not self._last_frame or self._last_frame.is_full:
            return len(self._frames) + 1
        else:
            return len(self._frames)

    def score_at_frame(self, frame_num: int) -> int:
        return sum(frame.score for frame in self._frames[:frame_num])

    def _generate_frames(self, throws: Throws = Throws()) -> list[Frame]:
        current_throw = throws.first
        while current_throw:
            self._add_frame(
                starting_throw=current_throw,
                frame_number=self.current_frame_number,
            )
            current_throw = self._reset_current_throw(current_throw)

    def _add_frame(self, starting_throw: Throw, frame_number: int):
        if len(self._frames) >= 10:
            return

        self._frames.append(
            self.frame_factory.new_frame(
                starting_throw=starting_throw,
                frame_number=frame_number,
            )
        )

    def _reset_current_throw(self, current_throw: Throw):
        i = 0
        while i < self._last_frame_num_of_throws:
            current_throw = current_throw.next
            i += 1
        return current_throw

    @property
    def _last_frame_num_of_throws(self) -> bool:
        return self._last_frame.num_of_throws if self._last_frame else 0

    @property
    def _last_frame(self) -> Frame:
        return self._frames[-1] if self._frames else False

    def __len__(self):
        return len(self._frames)

    def __getitem__(self, index):
        return self._frames[index]
