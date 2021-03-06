import collections
import contextlib
import curses
from typing import Dict
from typing import Generator

from babi.hl.interface import HL
from babi.hl.interface import HLs
from babi.list_spy import SequenceNoSlice

HIGHLIGHT = curses.A_REVERSE | curses.A_DIM


class Replace:
    include_edge = True

    def __init__(self) -> None:
        self.regions: Dict[int, HLs] = collections.defaultdict(tuple)

    def highlight_until(self, lines: SequenceNoSlice, idx: int) -> None:
        """our highlight regions are populated in other ways"""

    def touch(self, lineno: int) -> None:
        """our highlight regions are populated in other ways"""

    @contextlib.contextmanager
    def region(self, y: int, x: int, end: int) -> Generator[None, None, None]:
        self.regions[y] = (HL(x=x, end=end, attr=HIGHLIGHT),)
        try:
            yield
        finally:
            del self.regions[y]
