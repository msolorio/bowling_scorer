from app.frame import FrameFactory, Frame


class Frames:
    def __init__(self, throws: list[int] = []):
        self._frames = []
        self._generate_frames(throws)

    def __repr__(self):
        return self._frames

    def _generate_frames(self, throws: list[int]) -> list[Frame]:
        i = 0
        while i < len(throws):
            self._frames.append(FrameFactory.new_frame(throws=throws, start_index=i))
            i = i + (1 if self._last_frame_is_single_throw else 2)

    @property
    def _last_frame_is_single_throw(self) -> bool:
        return self._frames[-1].is_single_throw

    @property
    def current_frame_number(self) -> bool:
        if not self._frames or self._frames[-1].is_full:
            return len(self._frames) + 1
        else:
            return len(self._frames)

    def __len__(self):
        return len(self._frames)

    def __getitem__(self, index):
        return self._frames[index]
