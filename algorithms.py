from __future__ import annotations
from abc import ABC, abstractmethod
import numpy as np
from data import Data

# Kleine tutorial ofso:
# --------------------
# 1. gooi je code voor het voorbereiding in je class in de "prepare" method
# 2. gooi je code voor het repareren in de __call__ method
# --------------------
# Er zijn al 2 methods gemaakt die je kan gebruiken:
# ---
# 1. self.make_multiple_of:
#    zorgt ervoor dat de data een lengte krijgt die precies door 'n' gedeelt kan worden
# 2. self.split_data:
#    returnt een 2d-array (als in moonstones) met een horizontale lengte van 'n'
# --------------------
# Tips:
# ---
# - weet dat je in een class werkt en dat je niet alles hoeft mee te geven in parameters
# - het maken van een func/method werkt ook net iets anders omdat je in een class werkt


class Algorithm(ABC):
    def __init__(self, data: Data) -> None:
        self.d: Data = data

    @abstractmethod
    def prepare(self) -> None:
        """prepares the data for sending"""

    @abstractmethod
    def __call__(self) -> None:
        """'solves' the data"""

    def make_multiple_of(self, n: int) -> None:
        """adds bits to make self.data a multiple of n"""

        amount: int = n - len(self.d.d) % n

        self.d.d = np.hstack((np.zeros(amount, dtype=int), self.d.d))

    def split_data(self, n: int) -> np.ndarray:
        """splits the data into n-length parts"""

        amount: int = int(len(self.d.d) / n)

        return self.d.d.reshape((amount, n))


class ParityChecking(Algorithm):
    def __init__(self, data: Data) -> None:
        super().__init__(data)

    def prepare(self) -> None:
        # make multiple of 8
        self.make_multiple_of(8)

        # split the data
        spl_d: np.ndarray = self.split_data(8)

        # calculate the right parity bits
        r: np.ndarray = spl_d.sum(1, dtype=int) % 2
        w_right_par: np.ndarray = np.hstack((spl_d, r.reshape((spl_d.shape[0], 1))))

        # calculate the bottom parity bits
        b: np.ndarray = w_right_par.sum(0, dtype=int) % 2
        w_tot_par: np.ndarray = np.vstack((w_right_par, b))

        self.d.d = w_tot_par.flatten()

    def __call__(self) -> None:
        # split the array
        spl_d: np.ndarray = self.split_data(9)

        # check the right side
        r: np.ndarray = spl_d.sum(1, dtype=int).reshape((spl_d.shape[0], 1)) % 2

        # check the bottom
        b: np.ndarray = spl_d.sum(0, dtype=int) % 2

        # generate a T F grid
        g: np.ndarray = np.ones(spl_d.shape, dtype=int)
        g *= r
        g *= b

        # check if possible
        if g.sum() == 0:
            print("not possible")
            return

        # remove the parity bits
        v_flip = np.vectorize(lambda x: not x)

        spl_d[g.astype(bool)] = v_flip(spl_d[g.astype(bool)])
        spl_d = np.delete(spl_d, spl_d.shape[1] - 1, axis=1)
        spl_d = np.delete(spl_d, spl_d.shape[0] - 1, axis=0)

        self.d.d = spl_d.flatten()

        st_ind: int = np.where(self.d.d == 1)[0][0]
        self.d.d = self.d.d[st_ind:]


class CRC(Algorithm):
    def __init__(self, data: Data) -> None:
        super().__init__(data)

    def prepare(self) -> None:
        """prepares the data for sending"""

        pass

    def __call__(self) -> None:
        """(tries) to retrieve the original data"""

        pass


class Checksum(Algorithm):
    def __init__(self, data: Data) -> None:
        super().__init__(data)

    def prepare(self) -> None:
        """prepares the data for sending"""

        pass

    def __call__(self) -> None:
        """(tries) to retrieve the original data"""

        pass


class HammingCode(Algorithm):
    def __init__(self, data: Data) -> None:
        super().__init__(data)

    def prepare(self) -> None:
        """prepares the data for sending"""

        pass

    def __call__(self) -> None:
        """(tries) to retrieve the original data"""

        pass
