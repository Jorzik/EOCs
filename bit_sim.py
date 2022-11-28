from enum import Enum
from data import Data
import algorithms as algs

# ===========================================================================
#
#                               INFO
#
# ===========================================================================

# This is the main file
# In here, you will be able to run everything

# To add your own algorithm for handling error correction:
# 1. Create your algorithm in the algorithms.py file
# 2. add it to the CorrectionALgs Enum
# ~  *NAME* = algs.*ClassName*
# 3. In main(), set CHOSEN_ALG equal to your enum value
# ~  CHOSEN_ALG: type = CorrectionAlgs.*NAME*.value


class CorrectionAlgs(Enum):
    EXAMPLE_ALGORITHM = algs.ExampleAlgorithm
    PARITY_CHECK = algs.ParityCheck


def main() -> None:
    """Start >>>"""

    AMOUNT_TO_FLIP: int = 1
    CHOSEN_ALG: type = CorrectionAlgs.EXAMPLE_ALGORITHM.value

    # get the data from the file
    data: Data = Data("no file")

    # instantiate the algorithm
    alg: algs.Algorithm

    alg = CHOSEN_ALG(data)

    # prepare the bits for sending
    prepared_data: str

    alg.prepare_bits_for_sending()

    prepared_data = data.data

    # 'send' the bits
    data.flip(AMOUNT_TO_FLIP)

    # fix the flipped bits
    result: str

    result = alg()

    # print shit
    SEP_LINE: str = "---------------------------------"
    print(SEP_LINE)
    print(f"original data : {data.original}")
    print(f"prepared data : {prepared_data}")
    print(f"received data : {data.data}")
    print(f"corrected data: {result}")
    print(SEP_LINE)


if __name__ == "__main__":
    main()
