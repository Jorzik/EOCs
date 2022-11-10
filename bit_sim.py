from random import randrange


def main() -> None:
    """Start >>>"""

    AMOUNT_TO_FLIP: int = 2

    # get input (possibly through files)
    bits_in: str

    bits_in = get_bits()

    # flip bits
    bits_flipped: str

    bits_flipped = flip_bits(bits_in, AMOUNT_TO_FLIP)

    print(bits_in)
    print(bits_flipped)

    # fix shit


def get_bits() -> str:
    """returns a bytearray that is a result of a conversion of the given input"""

    str_in: str
    bits_in: str

    str_in = get_input()

    # -> here goes code that converts the received input-string into a byte array

    bits_in = str_in

    return bits_in


def get_input() -> str:
    """returns the input in a string format"""

    input: str

    # -> here goes the code to receive the input

    input = "0100111010"

    return input


def flip_bits(bits: str, amount_to_flip: int) -> str:
    """alg to flip the bits"""

    flipped_indexes: list[int] = []

    for i in range(amount_to_flip):
        # get a random index to flip
        ind_to_flip, flipped_indexes = get_index_to_flip(len(bits), flipped_indexes)

        # get the bits with the chosen bit inverted
        bits = flip(bits, ind_to_flip)

    return bits


def get_index_to_flip(
    input_length: int, flipped_indexes: list[int]
) -> tuple[int, list[int]]:
    """returns the index to flip plus the updated list"""

    random_index: int
    av_inds: list[int] = [
        ind for ind in list(range(input_length)) if ind not in flipped_indexes
    ]

    random_index = av_inds[randrange(len(av_inds))]

    # update the list to include the new index
    flipped_indexes.append(random_index)

    return random_index, flipped_indexes


def flip(bits: str, index_to_flip: int) -> str:
    """flips one bit"""

    part_1: str
    part_2: str
    bit_to_flip: str

    # divide the string into all the parts
    part_1 = bits[:index_to_flip]
    part_2 = bits[(index_to_flip + 1) :]
    bit_to_flip = bits[index_to_flip]

    # invert the bit and create the new string
    new_bit: str
    new_str: str

    new_bit = invert_bit(bit_to_flip)
    new_str = part_1 + new_bit + part_2

    return new_str


def invert_bit(bit: str) -> str:
    """inverts the given bit"""

    if bit == "0":
        return "1"

    return "0"


if __name__ == "__main__":
    main()
