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
        self.data: Data = data

    @abstractmethod
    def prepare(self) -> None:
        """prepares the data for sending"""

    @abstractmethod
    def __call__(self) -> bool:
        """'solves' the data"""

    def make_multiple_of(self, n: int) -> None:
        """adds bits to make self.data a multiple of n"""

        amount: int = n - len(self.data.content) % n

        self.data.content = np.hstack((np.zeros(amount, dtype=int), self.data.content))

    def split_data(self, n: int) -> np.ndarray:
        """splits the data into n-length parts"""

        amount: int = int(len(self.data.content) / n)

        return self.data.content.reshape((amount, n))


class ParityChecking(Algorithm):
    def __init__(self, data: Data) -> None:
        super().__init__(data)

    def prepare(self) -> None:
        # make multiple of 8
        self.make_multiple_of(8)

        # split the data
        split_up_data: np.ndarray = self.split_data(8)

        # calculate the right parity bits
        r_side: np.ndarray = split_up_data.sum(1, dtype=int) % 2
        data_with_r_parity: np.ndarray = np.hstack(
            (split_up_data, r_side.reshape((split_up_data.shape[0], 1)))
        )

        # calculate the bottom parity bits
        bottom: np.ndarray = data_with_r_parity.sum(0, dtype=int) % 2
        data_with_par: np.ndarray = np.vstack((data_with_r_parity, bottom))

        self.data.content = data_with_par.flatten()

    def __call__(self) -> bool:

        # split the array
        split_up_data: np.ndarray = self.split_data(9)

        # check the right side
        r_side: np.ndarray = (
            split_up_data.sum(1, dtype=int).reshape((split_up_data.shape[0], 1)) % 2
        )

        # check the bottom
        bottom: np.ndarray = split_up_data.sum(0, dtype=int) % 2

        # generate a T F grid
        grid: np.ndarray = np.ones(split_up_data.shape, dtype=int)
        grid *= r_side
        grid *= bottom

        # validate
        if r_side.sum() + bottom.sum() == 0:
            return True

        # check if possible
        if grid.sum() == 0:
            print("not possible")
            return False

        # flip the incorrect bits
        v_flip = np.vectorize(lambda x: not x)
        split_up_data[grid.astype(bool)] = v_flip(split_up_data[grid.astype(bool)])

        # remove the parity bits
        split_up_data = np.delete(split_up_data, split_up_data.shape[1] - 1, axis=1)
        split_up_data = np.delete(split_up_data, split_up_data.shape[0] - 1, axis=0)

        self.data.content = split_up_data.flatten()

        st_ind: int = np.where(self.data.content == 1)[0][0]
        self.data.content = self.data.content[st_ind:]
        return False


class CRC(Algorithm):
    def __init__(self, data: Data) -> None:
        super().__init__(data)


    def prepare(self) -> None:
        """prepares the data for sending"""
        self.dat = self.data.content
        key = input("Key: ")
        arr_key = np.array([int(char) for char in key])
        self.mod2div(self.dat, arr_key)
        self.remainder_sender(self.dat, arr_key)
        pass


        #Performs Modulo-2 division
    def mod2div(self, divident, divisor):

        # Number of bits to be XORed at a time.
        len_divisor = divisor.size


        # Slicing the divident to appropriate length for particular step
        first_bits = divident[0: len_divisor]
        prep_div = np.hstack((divident, np.zeros(len_divisor-1)))

        i = 0
        while i < len(prep_div) - len_divisor:
            if first_bits[-4] == 0:
                #first_bit[0]
                first_bits = np.hstack((first_bits, prep_div[i + len_divisor]))
                i+=1
                continue
            else:
                #first_bit[1]

                n = np.logical_xor(first_bits[-4:], divisor)
                first_bits = np.hstack((n, prep_div[i + len_divisor]))
                i+=1

        return first_bits[-3:]

        # If the leftmost bit of the dividend (or the part used in each step) is 0, the step cannot use the regular divisor; we need to use anall-0s divisor.

        # For the last n bits, we have to carry it out
        # normally as increased value of pick will cause
        # Index Out of Bounds.






        #appends zeros to data
        #performs mod 2 division to get remainder
    def remainder_sender(self, data, key):

        l_key = len(key)
        appended_data = np.hstack((self.dat, np.zeros(l_key-1)))
        self.data.content = np.hstack((self.dat, self.mod2div(appended_data, key)[-3:]))





    def __call__(self) -> bool:
        """(tries) to retrieve the original data"""
        #appends remainder of the sender to the original data
        #performs mod 2 division to get the  final remainder


        key = input("Key: ")
        arr_key = np.array([int(char) for char in key])
        self.remainder_receiver(self.dat, arr_key)

    def remainder_receiver(self, data, key):

        remainder_CRC = self.mod2div(self.data.content,key)
        if remainder_CRC[-3:].sum() == 0:
            return True
        else:
            return False

class Checksum(Algorithm):
   def __init__(self, data: Data) -> None:
       super().__init__(data)

   def sumsubstrings_and_overflow(self, arr): #arr should be an array

       digit_sum_list = []
       carry_s_list = []

       #for all the columns in the array, starting at column 16 moving to column 1
       for x in reversed(range(len(arr[0]))):

           current_sum = 0

           #add the carry from the previous column to the sum of the current column
           if carry_s_list:
               current_sum += int(carry_s_list[-1])

           for y in range(len(arr)): # for all the rows in the array
               #summing all numbers in one column of the array
               current_sum += arr[y][x]

           #digit sum is the number that should be below the current column as a result
           digit_sum = bin(current_sum)[2:][-1]
           digit_sum_list += [digit_sum]

           no_carry_bits = True
           #if the binary representation of the current sum, without the 0b part, has more than 1 number, there will be a carry
           if len(bin(current_sum)[2:])>1:
               no_carry_bits = False
               #the carry is the binary representation of the current sum, without the 0b part and without the last number (which is the digit sum already)
               carry = int(bin(current_sum)[2:-1],2)
               carry_s_list += [carry]
           #if the binary representation of the current sum, without the 0b part, has only 1 number, there won't be a carry (AKA the carry will be 0)
           elif len(bin(current_sum)[2:]) == 1:
               carry = 0
               carry_s_list += [carry]

       #getting the correct last 16 nrs of the sum of the 16 bit substrings of the data summed in array form
       correct_order_digit_sum_list = []
       start_index = len(digit_sum_list) -1
       for i in range(start_index,-1,-1):
           correct_order_digit_sum_list.append(int(digit_sum_list[i]))
       digit_sum_array = np.array(correct_order_digit_sum_list)

       #if there's no carry bits (so all the carry's were zero), there's no overflow
       if no_carry_bits == True:
           overflow_array = np.array([0 for i in range(16)])
           rows_amount = 1

       elif no_carry_bits == False:
           #the overflow is the binary representation of the carry (without the 0b part)
           overflow = bin(carry)[2:]
           #if that binary representation has less than 16 characters, the overflow array is padded with zero's on the left, and has the binary representation on the right
           if len(overflow) < 16:
               rows_amount = 1
               amount_of_zeros = 16 - len(overflow)
               overflow_array = np.array([0 for i in range(amount_of_zeros)])
               overflow_array = np.append(overflow_array,list(overflow))
               overflow_array = overflow_array.astype(int)
           elif len(overflow) == 16:
               #make it into array and add to previous
               overflow_array = np.array(list(overflow))
               overflow_array = overflow_array.astype(int)
               rows_amount = 1
           elif len(overflow) > 16:
               #make the overflow into arrays with 16 columns by adding zero's on the left of the last row
               if len(overflow)%16 == 0:
                   rows_amount = (len(overflow)//16)
                   overflow_array = np.array(list(overflow))
                   overflow_array = np.reshape(overflow_array,(rows_amount,16))
                   overflow_array = overflow_array.astype(int)
               elif len(overflow)%16 != 0:
                   amount_of_zeros = 16 - (len(overflow)%16)
                   zero_s_array = np.array([0 for i in range(amount_of_zeros)])
                   rows_amount = (len(overflow)//16) +1
                   overflow_array = np.array(list(overflow))
                   index_ = -16 + amount_of_zeros
                   overflow_array = np.insert(overflow_array, index_ ,zero_s_array)
                   overflow_array = np.reshape(overflow_array,(rows_amount,16))
                   overflow_array = overflow_array.astype(int)

       #make an array with the first row being the last 16 nrs of the result of the summed 16 bit length substrings of the data, and the other(s) being the overflow
       new_array = np.append([digit_sum_array],[overflow_array])
       new_array = np.reshape(new_array,((rows_amount+1),16))
       return new_array

   #function to get the one's complement of the first row of 0's and 1's in an array
   def the_ones_complement(self,x): #input should be an array with 0's and 1's
       the_complement = []
       for nr in x[0]:
           if int(nr) == 0:
               the_complement.append(1)
           elif int(nr) == 1:
               the_complement.append(0)
       the_complement = np.array(the_complement)
       return the_complement

   def prepare(self) -> None:
       """prepares the data for sending"""

       #preparing the data, wanted: array with 16 columns
       self.make_multiple_of(16)
       data_as_arr = self.split_data(16)

       def internet_checksum(summed_sub_strings):
           the_i_checksum = self.the_ones_complement(summed_sub_strings)
           return the_i_checksum

       #getting the resultant string and the overflow string
       digit_sum_and_overflow = self.sumsubstrings_and_overflow(data_as_arr)
       #result of adding the overflow to the resultant string
       summed_substrings = self.sumsubstrings_and_overflow(digit_sum_and_overflow)
       #in case there's new overflow from adding the previous overflow to the previous summed substrings
       while 1 in summed_substrings[1::]:
           summed_substrings = self.sumsubstrings_and_overflow(summed_substrings)

       #getting the internet checksum
       internet_checksum = internet_checksum(summed_substrings)

       #appending the internet checksum to the end of the data
       array_with_checksum = np.append([data_as_arr],[internet_checksum])
       array_with_checksum = np.reshape(array_with_checksum,(data_as_arr.shape[0]+1,16))

       self.data.content = array_with_checksum

       pass

   def _call_(self) -> bool:
       """(tries) to retrieve the original data"""

       #getting the sum of the received data
       digit_sum_and_overflow_receiveddata = self.sumsubstrings_and_overflow(self.data.content)
       summed_substrings_receiveddata = self.sumsubstrings_and_overflow(digit_sum_and_overflow_receiveddata)
       #in case there's new overflow from adding the previous overflow to the previous summed substrings
       while 1 in summed_substrings[1::]:
           summed_substrings = self.sumsubstrings_and_overflow(summed_substrings_receiveddata)

       complement_checksum_and_substrings = self.the_ones_complement(summed_substrings)

       #there should be no 1's in the data if it's correct
       if 1 in complement_checksum_and_substrings:
           print('An error has been detected.')
           return False
       elif 1 not in complement_checksum_and_substrings:
           print('No errors have been detected.')
           return True

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
        bit_array = self.data.content
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

        self.data.content = Data.str_to_data(arr)


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

        m = self.r

        r = Calc_ammount_of_redund_bits_needed(m)

        arr_old = self.data.content
        arr = "".join(str(i) for i in arr_old)
        
        r = self.r
  
        # this check the "fixed data" against the old data 
        correction = find_place_of_error(arr, r)
        if(correction==0):
            print("There is no error in the received message.")
        else:
            print("The position of error is ",len(arr)-correction+1,"from the left")
        
        arrar_new = Data.str_to_data(arr)

        place_of_wrong_bit = len(arrar_new)-correction
        wrong_bit = arrar_new[place_of_wrong_bit]


        if wrong_bit == 1:
            arrar_new[place_of_wrong_bit] = 0

        if wrong_bit == 0:
            self.data.content[place_of_wrong_bit] = 1



        pass
