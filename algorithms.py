from abc import ABC, abstractmethod
import numpy as np
from data import Data

# ===========================================================================
#
#                               INFO
#
# ===========================================================================

# This is the algorithm file
# In here you can create your own algorithm

# To do so:
# 1. create a class with your algorithm name that inherits from the Algorithm meta class
# 2. overwrite the 'prepare_bits_for_sending' class and the '__call__' magic method
# 3. put your preparation code in the 'prepare_bits_for_sending' method
# 4. put your detect-and-fix code in the magic method

# You can make use of the split_data property to instantly get the data split into bytes
# If you want to copy a class as a template; copy the ExampleAlgorithm class


class Algorithm(ABC):
    """the base algorithm class"""

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

    @property
    def split_data(self) -> list[str]:
        """splits the bit string into bytes"""

        spl_bits: list[str]

        spl_bits = self.data.data.split()

        return spl_bits

    def make_multiple_of_n(self, n: int) -> None:
        """makes sure the data has a length that is a multiple of n"""

        zeros_req: int = 8 - len(self.data.data) % 8
        self.data.data = "0" * zeros_req + self.data.data


# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# An example of an algorithm (with nothing useful in it)


class ExampleAlgorithm(Algorithm):
    def __init__(self, data: Data) -> None:
        super().__init__(data)

    def prepare_bits_for_sending(self) -> None:
        """prepares the data (self.data.data) for sending"""

        # >>> this code serves as an example and achieves absolutely nothing

        # splits the data to create a list of all bytes
        bytes: list[str]

        bytes = self.split_data

        # adds and removes a bit
        for byte in bytes:
            byte += "0"

        for byte in bytes:
            byte = byte[:-1]

        # updates the data
        new_data: str = ""

        for byte in bytes:
            new_data += f"{byte} "

        # - [:-1] to remove the last space
        self.data.data = new_data[:-1]

    def __call__(self) -> str:
        """checks if there's an error in the 'received' data and fixes it\n
        returns the 'fixed' data - does not edit self.data.data"""

        # >>> this code serves as an example and is obviously not allowed

        # error detection
        error: bool = self.data.data != self.data.original

        # error correction
        fix: str

        if error:
            fix = self.data.original

        return fix


class ParityCheck(Algorithm):
    def __init__(self, data: Data) -> None:
        super().__init__(data)

    def prepare_bits_for_sending(self) -> None:
        """returns the bits in pairs of 8 + parity bit"""

        n_data: str = ""

        # make the data be a multiple of 8
        self.make_multiple_of_n(8)

        # get the data split
        spl_data: np.ndarray = np.array(self.split_data)

        # vectorize a one_counter
        one_counter = np.vectorize(lambda x: len([a for a in x if a == "1"]))
        count: np.ndarray = one_counter(spl_data)

        # add the parity bits
        bit: str

        for i in range(len(spl_data)):
            bit = str(count[i] % 2)
            spl_data[i] += bit

        # create a complete string from the data
        for row in spl_data:
            n_data += row

        self.data.data = n_data

    def __call__(self) -> str:

        x = "0"

        return x


class CRC(Algorithm):
    def __init__(self, data: Data) -> None:
        super().__init__(data)

    def prepare_bits_for_sending(self) -> None:

        pass

    def __call__(self) -> str:

        x = "0"

        return x


class Checksum(Algorithm):
    def __init__(self, data: Data) -> None:
        super().__init__(data)

        def prepare_bits_for_sending(self) -> None:

            pass

        def __call__(self) -> str:

            x = "0"

            return x


class HammingDistance(Algorithm):
    def __init__(self, data: Data) -> None:
        super().__init__(data)

    def prepare_bits_for_sending(self) -> None:

        pass

    def __call__(self) -> str:

        x = "0"

        return x
