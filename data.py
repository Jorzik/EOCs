from __future__ import annotations
import numpy as np
from typing import Callable


class Data:
    def __init__(self, origin: str) -> None:
        self.obtain_data(origin=origin)

    def obtain_data(self, origin: str) -> None:
        """retrieves the data from the origin"""

        file_data: str = self.from_file(origin=origin)

        self.d: np.ndarray = Data.str_to_data(file_data)

        # store original data for review
        self.o: np.ndarray = self.d.copy()

    def from_file(self, origin: str) -> str:
        """gets the data from the file as a string of bits"""

        file_open = open("tv_shows.txt") 
        text = file_open.read() 
        bin_string = "".join(format(ord(i), '08b') for i in text)
        origin = str(bin_string)

        return origin

    str_to_data: Callable[[str], np.ndarray] = lambda x: np.array([int(q) for q in x])

    def send(self, amount_to_flip: int) -> None:
        """flips the bits of itself"""

        if not amount_to_flip:
            return

        rng: np.random.Generator = np.random.default_rng()

        ind_to_flip: np.ndarray = np.hstack(
            (
                np.ones(shape=amount_to_flip, dtype=bool),
                np.zeros(shape=len(self.d) - amount_to_flip, dtype=bool),
            )
        )
        # shuffle the indices to flip
        rng.shuffle(ind_to_flip)

        # flip the chosen bits
        v_flip = np.vectorize(lambda x: not x)
        self.d[ind_to_flip] = v_flip(self.d[ind_to_flip])
