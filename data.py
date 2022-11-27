from random import randrange


class Data:
    """class containing bits that are sent, flipped and corrected"""

    def __init__(self, file_name: str) -> None:
        """called whenever an instance of this class is created"""

        self.extract_bits_from_file(file_name)

        self.indexes_to_flip: list[int] = [
            x for x in range(len(self.data)) if self.data[x] != " "
        ]

    def extract_bits_from_file(self, file_name: str) -> None:
        """retrieves the data from the file, as a string of bits"""

        self.data: str

        # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
        # this function contains code that sets self.data equal
        # to a string of bits that has been retrieved from the given file

        # example:
        self.data = "111000111000"

        self.original: str = self.data

    def flip(self, amount: int) -> None:
        """flips the data and leaves behind the original to compare to"""

        # flip each bit
        ind_to_flip: int
        bit_to_flip: str

        part_1: str
        part_2: str
        flipped_bit: str

        for i in range(amount):
            # determine which bit to flip
            ind_to_flip = self.index_to_flip
            bit_to_flip = self.data[ind_to_flip]

            # flip the bit
            # > save the unaffected parts
            part_1 = self.data[:ind_to_flip]
            part_2 = self.data[(ind_to_flip + 1) :]
            flipped_bit = self.flip_a_bit(bit_to_flip)

            # > reconstruct the bitstring
            self.data = part_1 + flipped_bit + part_2

    @property
    def index_to_flip(self) -> int:
        """generates and returns an available index to flip"""

        # get length from the list of available indexes to
        # pick a random number out of it
        av_length: int
        av_ind: int
        ind_to_flip: int

        av_length = len(self.indexes_to_flip)
        av_ind = randrange(av_length)
        ind_to_flip = self.indexes_to_flip[av_ind]

        # remove if from the available indexes
        self.indexes_to_flip.remove(ind_to_flip)

        return ind_to_flip

    def flip_a_bit(self, bit: str) -> str:
        """flips the chosen bit"""

        if bit == "0":
            return "1"

        return "0"
