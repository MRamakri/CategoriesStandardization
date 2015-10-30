__author__ = 'manikandan'


def pad_zeroes(upc_str):
    """
    Pads zeroes to the beginning of the UPC to make the length 11 characters,
    allowing for one digit checksum
    :param upc_str: Raw UPC input without Zero padding or Checksum, String
    :return: zero_padded_upc: Zero padded UPC value, String
    """
    missing_digits = len(upc_str)
    if missing_digits < 12:
        zero_padded_upc = upc_str
        for i in range(12 - missing_digits - 1):
            zero_padded_upc = "0" + zero_padded_upc
    return zero_padded_upc

def add_check_digit(zero_padded_upc):
    """
    Calculates the cheksum digit for the provided 11 digit UPC and converts
    it to 12 digit UPCA
    :param zero_padded_upc: Zero padded UPC, String
    :return: upca: 12 digit UPCA with checksum digit
    """
    if len(zero_padded_upc) != 11:
        raise Exception("Invalid length")

    odd_sum = 0
    even_sum = 0
    for i in range(0, 10, 2):
        odd_sum += int(zero_padded_upc[i])
        even_sum += int(zero_padded_upc[i+1])
    odd_sum += int(zero_padded_upc[10])
    check_digit = 10 - ((odd_sum * 3 + even_sum) % 10)
    upca = zero_padded_upc + str(check_digit)
    return upca

if __name__ == "__main__":
    upc = "60265217156"
    print(upc)
    zupc = pad_zeroes(upc)
    print(zupc)
    upca = add_check_digit(zupc)
    print(upca)
