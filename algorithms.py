from abc import ABC, abstractmethod
from data import Data


class Algorithm(ABC):
    def __init__(self, data: Data) -> None:
        self.data: Data = data

    @abstractmethod
    def prepare_bits_for_sending(self) -> None:
        """prepares the bits for sending"""
        pass

    @abstractmethod
    def __call__(self) -> str:
        """runs the algorithm\n
        returns the 'fixed' bit-string"""
        pass

    def split_bits(self) -> list[str]:
        """splits the bit string into bytes"""

        spl_bits: list[str]

        spl_bits = self.data.data.split()

        return spl_bits


# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# An example of an algorithm (with nothing useful in it)


class TwoDimensional(Algorithm):
    def __init__(self, data: Data) -> None:
        super().__init__(data)

    def prepare_bits_for_sending(self) -> None:
        return super().prepare_bits_for_sending()

    def __call__(self) -> str:
        return super().__call__()
