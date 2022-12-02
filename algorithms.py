from __future__ import annotations
from abc import ABC, abstractmethod
import numpy as np
from data import Data

# Kleine tutorial ofso:
# --------------------
# 1. gooi je code voor het voorbereiding in je class in de "prepare" method
# 2. gooi je code voor het repareren in de __call__ method
# --------------------
# Er zijn al 2 methods gemaakt die je kan gebruiken:
# ---
# 1. self.make_multiple_of:
#    zorgt ervoor dat de data een lengte krijgt die precies door 'n' gedeelt kan worden
# 2. self.split_data:
#    returnt een 2d-array (als in moonstones) met een horizontale lengte van 'n'
# --------------------
# Tips:
# ---
# - weet dat je in een class werkt en dat je niet alles hoeft mee te geven in parameters
# - het maken van een func/method werkt ook net iets anders omdat je in een class werkt


class Algorithm(ABC):
    def __init__(self, data: Data) -> None:
        self.d: Data = data

    @abstractmethod
    def prepare(self) -> None:
        """prepares the data for sending"""

    @abstractmethod
    def __call__(self) -> bool:
        """'solves' the data"""

    def make_multiple_of(self, n: int) -> None:
        """adds bits to make self.data a multiple of n"""

        amount: int = n - len(self.d.d) % n

        self.d.d = np.hstack((np.zeros(amount, dtype=int), self.d.d))

    def split_data(self, n: int) -> np.ndarray:
        """splits the data into n-length parts"""

        amount: int = int(len(self.d.d) / n)

        return self.d.d.reshape((amount, n))


class ParityChecking(Algorithm):
    def __init__(self, data: Data) -> None:
        super().__init__(data)

    def prepare(self) -> None:
        # make multiple of 8
        self.make_multiple_of(8)

        # split the data
        spl_d: np.ndarray = self.split_data(8)

        # calculate the right parity bits
        r: np.ndarray = spl_d.sum(1, dtype=int) % 2
        w_right_par: np.ndarray = np.hstack((spl_d, r.reshape((spl_d.shape[0], 1))))

        # calculate the bottom parity bits
        b: np.ndarray = w_right_par.sum(0, dtype=int) % 2
        w_tot_par: np.ndarray = np.vstack((w_right_par, b))

        self.d.d = w_tot_par.flatten()

    def __call__(self) -> bool:

        # split the array
        spl_d: np.ndarray = self.split_data(9)

        # check the right side
        r: np.ndarray = spl_d.sum(1, dtype=int).reshape((spl_d.shape[0], 1)) % 2

        # check the bottom
        b: np.ndarray = spl_d.sum(0, dtype=int) % 2

        # generate a T F grid
        g: np.ndarray = np.ones(spl_d.shape, dtype=int)
        g *= r
        g *= b

        # validate
        if r.sum() + b.sum() == 0:
            return True

        # check if possible
        if g.sum() == 0:
            print("not possible")
            return False

        # flip the incorrect bits
        v_flip = np.vectorize(lambda x: not x)
        spl_d[g.astype(bool)] = v_flip(spl_d[g.astype(bool)])

        # remove the parity bits
        spl_d = np.delete(spl_d, spl_d.shape[1] - 1, axis=1)
        spl_d = np.delete(spl_d, spl_d.shape[0] - 1, axis=0)

        self.d.d = spl_d.flatten()

        st_ind: int = np.where(self.d.d == 1)[0][0]
        self.d.d = self.d.d[st_ind:]
        return False


class CRC(Algorithm):
    def __init__(self, data: Data) -> None:
        super().__init__(data)

    def prepare(self) -> None:
        """prepares the data for sending"""

        pass

    def __call__(self) -> bool:
        """(tries) to retrieve the original data"""

        pass


class Checksum(Algorithm):
    def __init__(self, data: Data) -> None:
        super().__init__(data)

    def prepare(self) -> None:
        """prepares the data for sending"""

        pass

    def __call__(self) -> bool:
        """(tries) to retrieve the original data"""

        pass


class HammingCode(Algorithm):
    def __init__(self, data: Data) -> None:
        super().__init__(data)

    def prepare(self) -> None:
        def Calc_ammount_of_redund_bits_needed(m):

            # calculates the ammount of redundant bits needed to get the hammingdisntance with the formula below
            # returns that ammount

            for i in range(m):
                if 2**i >= m + i + 1:
                    return i

        def place_of_redund_bits_in_string(data, r):

            # Redundancy bits are placed at the positions
            # ammount of bits comes from above

            j = 0
            k = 1
            m = len(data)
            res = ""

            # If position is a power of 2 then  it inserts a '0'

            for i in range(1, m + r + 1):
                if i == 2**j:
                    res = res + "0"
                    j += 1
                else:
                    res = res + data[-1 * k]
                    k += 1

            # the the whole strig is reversed, as you count backwords in bitstrigns

            return res[::-1]

        # this caclulates the hamming distane and makes the exstra bits a 1 or a 0

        def calc_par_bit_vallue(arr, r):
            n = len(arr)

            # for every added bit
            for i in range(r):
                val = 0
                for j in range(1, n + 1):

                    # calculates the hamming distance and makes it a 0 or 1

                    if j & (2**i) == (2**i):
                        val = val ^ int(arr[-1 * j])
                        # -1 * j bc the string is backwards

                # adds the string together again
                arr = arr[: n - (2**i)] + str(val) + arr[n - (2**i) + 1 :]
            return arr

        # Enter the data to be transmitted, makes it a usable string
        bit_array = self.d.d
        data = "".join(str(i) for i in bit_array)

        # Calculate the no of Redundant Bits Required
        m = len(data)
        self.r = Calc_ammount_of_redund_bits_needed(m)
        r = self.r

        # Determine the positions of Redundant Bits
        arr = place_of_redund_bits_in_string(data, r)

        # Determine the parity bits vallue
        arr = calc_par_bit_vallue(arr, r)

        # sets self.d.d to the new array to send to next step

        dd = np.array([x for x in arr])
        self.d.d = dd

        pass

    def __call__(self) -> bool:
        def Calc_ammount_of_redund_bits_needed(m):

            # calculates the ammount of redundant bits needed to get the hammingdisntance with the formula below
            # returns that ammount

            for i in range(m):
                if 2**i >= m + i + 1:
                    return i

        def find_place_of_error(arr, nr):
            n = len(arr)
            res = 0

            # Calculate parity bits again
            for i in range(nr):
                val = 0
                for j in range(1, n + 1):
                    if j & (2**i) == (2**i):
                        val = val ^ int(arr[-1 * j])

                # Create a binary no by appending
                # parity bits together.

                res = res + val * (10**i)

            # Convert binary to decimal
            return int(str(res), 2)

        arr = self.d.d

        # bit_array_receved = self.d.d
        # arr = "".join(str(i) for i in bit_array_receved)

        m = self.r

        r = Calc_ammount_of_redund_bits_needed(m)

        # this check the "fixed data" against the old data
        correction = find_place_of_error(arr, r)
        if correction == 0:
            return True
        else:
            print(
                "The position of error is ", len(arr) - correction + 1, "from the left"
            )
            return False
