from abc import ABC, abstractmethod
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

    def split_data(self, n: int) -> list[str]:
        """splits the bit string into n-length parts"""

        spl_bits: list[str]

        # add spaces to the data
        amount_of_spaces: int = int(len(self.data.data) / n) - 1
        broken_down_data: list = list(self.data.data)
        for i in range(amount_of_spaces):
            broken_down_data.insert((i + 1) * n + i, " ")

        self.data.data = ""
        for c in broken_down_data:
            self.data.data += c

        spl_bits = self.data.data.split()
        self.data.data = self.data.data.replace(" ", "")

        return spl_bits

    def make_multiple_of_n(self, n: int) -> None:
        """makes sure the data has a length that is a multiple of n"""

        zeros_req: int = n - len(self.data.data) % n
        self.data.data = "0" * zeros_req + self.data.data


# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# An example of an algorithm (with nothing useful in it)


class ExampleAlgorithm(Algorithm):
    def __init__(self, data: Data) -> None:
        super().__init__(data)

    def prepare_bits_for_sending(self) -> None:
        """prepares the data (self.data.data) for sending"""

        # >>> this code serves as an example and achieves absolutely nothing

        # makes the data a multiple of 8
        self.make_multiple_of_n(8)

        # splits the data to create a list of all bytes
        bytes: list[str]

        bytes = self.split_data(8)

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
        spl_data: list = self.split_data(8)

        # add the parity bits
        self.add_parity_bits(spl_data)

        # create a complete string from the data
        for row in spl_data:
            n_data += row

        self.data.data = n_data

    def add_parity_bits(self, split_data: list) -> list:
        """adds the parity bits to the list"""

        # > map the one count
        one_count: list = list(map(ParityCheck.one_counter, split_data))

        # > add the right row
        bit: str

        for i in range(len(split_data)):
            bit = str(one_count[i])
            split_data[i] += bit

        # > add the bottom row
        row: str = ""
        for i in range(9):
            row += self.investigate_index(i, split_data)

        split_data.append(row)

        return split_data

    one_counter = lambda x: len([a for a in x if a == "1"]) % 2

    def investigate_index(self, index: int, split_data: list) -> str:
        """returns the amount of ones on the given index"""

        count: int = 0
        for r in split_data:
            if r[index] == "1":
                count += 1

        return str(count % 2)

    def __call__(self) -> str:

        spl_data: list = self.split_data(9)
        data: str = self.data.data

        # find errors
        wrong_horizontals: list = self.check_horizontally(spl_data)
        wrong_verticals: list = self.check_vertically(spl_data)

        # check if possible
        if min(len(wrong_horizontals), len(wrong_verticals)) != 1:
            return "not possible"

        for a in wrong_horizontals:
            for b in wrong_verticals:
                data = Data.flip_at(a * 9 + b, data)

        return data

    def check_horizontally(self, split_data: list) -> list[int]:
        """returns the indices of mistakes"""

        # map counter
        one_count: list = list(map(ParityCheck.one_counter, split_data))
        wrong_bits = [x for x, y in enumerate(one_count) if y == 1]

        return wrong_bits

    def check_vertically(self, split_data: list) -> list[int]:
        """returns the indices of mistakes"""

        wrong_bits: list = []
        for i in range(9):
            if self.investigate_index(i, split_data) == "1":
                wrong_bits.append(i)

        return wrong_bits


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
