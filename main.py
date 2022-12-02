from __future__ import annotations
from typing import Callable
from data import Data
import algorithms as alg
from enum import Enum
import numpy as np


class AlgorithmPicker(Enum):
    PARITY_CHECKING = alg.ParityChecking
    CHECKSUM = alg.Checksum
    CRC = alg.CRC
    HAMMING_CODE = alg.HammingCode


use_algorithm: Callable[[AlgorithmPicker, Data], alg.Algorithm] = lambda x, y: x.value(
    y
)


def main() -> None:
    """Start >>>"""

    AMOUNT_OF_ERRORS: int = 1
    data_milest: dict[str, np.ndarray] = {}

    create_divider()

    # obtain the data
    data: Data
    data, data_milest = obtain_data(data_milest=data_milest)

    # prepare the data
    used_alg: alg.Algorithm
    used_alg, data_milest = prepare_data(data=data, data_milest=data_milest)

    #'send' the data
    data.send(AMOUNT_OF_ERRORS)
    data_milest["transferred_data"] = data.content.copy()

    # retrieve the data
    data_milest = retrieve_data(used_alg=used_alg, data=data, data_milest=data_milest)

    # display the results
    print(f"original:  {data_milest['original_data']}")
    print(f"prepared:  {data_milest['prepared_data']}")
    print(f"sent:      {data_milest['transferred_data']}")
    print(f"retrieved: {data_milest['received_data']}")

    create_divider()


def obtain_data(data_milest: dict) -> tuple:
    """obtains the data and returns the first milestone"""

    # create a data instance
    data: Data = Data("0")

    # store a data milestone
    data_milest["original_data"] = data.original

    return data, data_milest


def prepare_data(data: Data, data_milest: dict) -> tuple:
    """decides what algorithm will be used and returns the second milestone"""

    # create an instance of the chosen algorithm
    used_alg: alg.Algorithm = use_algorithm(AlgorithmPicker.PARITY_CHECKING, data)

    # prepare the data
    used_alg.prepare()

    # store a data milestone
    data_milest["prepared_data"] = data.content.copy()

    return used_alg, data_milest


def retrieve_data(used_alg: alg.Algorithm, data: Data, data_milest: dict) -> dict:
    """(tries) to retrieve the data and returns the third milestone"""

    valid: bool

    # try-except serves for catching errors related to
    # the algorithm not being designed for handling larger amounts of errors
    try:
        valid = used_alg()
    except:
        print("algorithm could not retrieve the data")
        valid = False

    # handles the result of the error detection
    if valid:
        print("valid data")
        return data_milest

    # stores a milestone of the data
    data_milest["received_data"] = data.content.copy()
    return data_milest


def create_divider() -> None:
    """prints out a divider line"""

    DIV: str = "-" * 75

    print(DIV)


if __name__ == "__main__":
    main()
