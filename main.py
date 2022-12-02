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
    d: Data = Data("0")
    print(f"original:  {d.d}")

    # prepare the data
    a: alg.Algorithm = use_algorithm(Algs.HAMMING_CODE, d)

    a.prepare()
    print(f"prepared:  {d.d}")

    #'send' the data
    d.send(0)
    print(f"sent:      {d.d}")

    # retrieve the data
    valid: bool = a()
    if valid:
        print("valid data")
    else:
        print(f"retrieved: {d.d}")

    create_divider()


def create_divider() -> None:
    """prints out a divider line"""

    DIV: str = "-" * 75

    print(DIV)


if __name__ == "__main__":
    main()
