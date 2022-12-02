from __future__ import annotations
from typing import Callable
from data import Data
import algorithms as alg
from enum import Enum
import numpy as np


class Algs(Enum):
    PARITY_CHECKING = alg.ParityChecking
    CHECKSUM = alg.Checksum
    CRC = alg.CRC
    HAMMING_CODE = alg.HammingCode


use_algorithm: Callable[[Algs, Data], alg.Algorithm] = lambda x, y: x.value(y)


def main() -> None:
    """Start >>>"""

    AMOUNT_OF_ERRORS: int = 1
    data_milestones: dict[str, np.ndarray] = {}

    create_divider()

    # obtain the data
    data: Data
    data, data_milestones = obtain_data(data_milestones=data_milestones)

    # prepare the data
    used_algorithm: alg.Algorithm
    used_algorithm, data_milestones = prepare_data(
        data=data, data_milestones=data_milestones
    )

    #'send' the data
    data.send(AMOUNT_OF_ERRORS)
    data_milestones["transferred_data"] = data.content

    # retrieve the data
    data_milestones = retrieve_data(
        used_algorithm=used_algorithm, data=data, data_milestones=data_milestones
    )

    # display the results
    print(f"original:  {data_milestones['original_data']}")
    print(f"prepared:  {data_milestones['prepared_data']}")
    print(f"sent:      {data_milestones['transferred_data']}")
    print(f"retrieved: {data_milestones['received_data']}")

    create_divider()


def obtain_data(data_milestones: dict) -> tuple:
    """obtains the data and returns the first milestone"""

    # create a data instance
    data: Data = Data("0")

    # store a data milestone
    data_milestones["original_data"] = data.original

    return data, data_milestones


def prepare_data(data: Data, data_milestones: dict) -> tuple:
    """decides what algorithm will be used and returns the second milestone"""

    # create an instance of the chosen algorithm
    used_algorithm: alg.Algorithm = use_algorithm(Algs.PARITY_CHECKING, data)

    # prepare the data
    used_algorithm.prepare()

    # store a data milestone
    data_milestones["prepared_data"] = data.content

    return used_algorithm, data_milestones


def retrieve_data(
    used_algorithm: alg.Algorithm, data: Data, data_milestones: dict
) -> dict:
    """(tries) to retrieve the data and returns the third milestone"""

    valid: bool

    # try-except serves for catching errors related to
    # the algorithm not being designed for handling larger amounts of errors
    try:
        valid = used_algorithm()
    except:
        print("algorithm could not retrieve the data")
        valid = False

    # handles the result of the error detection
    if valid:
        print("valid data")
        return data_milestones

    # stores a milestone of the data
    data_milestones["received_data"] = data.content
    return data_milestones


def create_divider() -> None:
    """prints out a divider line"""

    DIV: str = "-" * 75

    print(DIV)


if __name__ == "__main__":
    main()
