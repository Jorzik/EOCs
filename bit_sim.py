from enum import Enum
from data import Data
import algorithms as algs


class CorrectionAlgs(Enum):
    TwoDimensional = algs.TwoDimensional


def main() -> None:
    """Start >>>"""

    AMOUNT_TO_FLIP: int = 2
    CHOSEN_ALG: type = CorrectionAlgs.TwoDimensional.value

    # get the data from the file
    data: Data = Data("no file")

    # instantiate the algorithm
    alg: algs.Algorithm

    alg = CHOSEN_ALG(data)

    # prepare the bits for sending
    alg.prepare_bits_for_sending()

    # 'send' the bits
    data.flip(AMOUNT_TO_FLIP)

    # fix the flipped bits
    result: str

    result = alg()

    # print shit
    print(data.original)
    print(data.data)
    print(result)


if __name__ == "__main__":
    main()
