from __future__ import annotations
from typing import Callable
from data import Data
import algorithms as alg
from enum import Enum


class Algs(Enum):
    PARITY_CHECKING = alg.ParityChecking
    CHECKSUM = alg.Checksum
    CRC = alg.CRC
    HAMMING_CODE = alg.HammingCode


use_algorithm: Callable[[Algs, Data], alg.Algorithm] = lambda x, y: x.value(y)


def main() -> None:
    """Start >>>"""

    create_divider()

    # obtain the data
    data: Data = Data("0")
    print(f"original:  {data.content}")

    # prepare the data
    used_algorithm: alg.Algorithm = use_algorithm(Algs.PARITY_CHECKING, data)

    used_algorithm.prepare()
    print(f"prepared:  {data.content}")

    #'send' the data
    data.send(1)
    print(f"sent:      {data.content}")

    # retrieve the data
    valid: bool = used_algorithm()
    if valid:
        print("valid data")
    else:
        print(f"retrieved: {data.content}")

    create_divider()


def create_divider() -> None:
    """prints out a divider line"""

    DIV: str = "-" * 75

    print(DIV)


if __name__ == "__main__":
    main()
