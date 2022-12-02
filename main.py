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
    data, data_milestones = obtain_data(data_milestones)

    # prepare the data
    used_algorithm: alg.Algorithm = use_algorithm(Algs.PARITY_CHECKING, data)

    used_algorithm.prepare()
    prepared_data: np.ndarray = data.content

    #'send' the data
    data.send(AMOUNT_OF_ERRORS)
    transferred_data: np.ndarray = data.content

    # retrieve the data
    valid: bool = used_algorithm()
    received_data: np.ndarray
    if valid:
        print("valid data")
    else:
        received_data = data.content

    # display the results
    print(f"original:  {data_milestones['original_data']}")
    print(f"prepared:  {prepared_data}")
    print(f"sent:      {transferred_data}")
    print(f"retrieved: {received_data}")

    create_divider()


def obtain_data(data_milestones: dict) -> tuple:
    """obtains the data and returns the first milestone"""

    data: Data = Data("0")
    data_milestones["original_data"] = data.original

    return data, data_milestones


def create_divider() -> None:
    """prints out a divider line"""

    DIV: str = "-" * 75

    print(DIV)


if __name__ == "__main__":
    main()
