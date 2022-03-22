# Problem 16:
#     Power Digit Sum
#
# Description:
#     2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
#
# What is the sum of the digits of the number 2^1000?

from math import floor, log10


def main(n):
    """
    Returns the sum of the digits of the number 2^n.

    Args:
        n (int): Natural number

    Returns:
        Sum of digits of 2^n

    Raises:
        AssertError: if incorrect params are given
    """
    assert type(n) == int and n > 0

    # To prevent overflow for large powers of 2,
    #   maintain a decimal representation of 2^i
    #   as an array of digits (in reverse)
    full_digit_count = floor(n * log10(2)) + 1
    digits = [0 for _ in range(full_digit_count)]  # 1's digit, 10's digit, etc

    # Linearly iterate up the powers of 2
    # NOTE:
    #   Might be quicker by squaring numbers (doubling powers)
    #     and multiplying to get final number.
    #   But I'm being lazy and don't want to implement long multiplication.
    p = 0
    digits[0] = 1  # Begin with 2^0
    digit_count = 1  # To shorten the iterations
    while p < n:
        carried = 0
        for i in range(digit_count):
            carried, digits[i] = divmod(2 * digits[i] + carried, 10)
        if carried != 0:
            digits[digit_count] = carried
            digit_count += 1
        p += 1
    return sum(digits)


if __name__ == '__main__':
    num = int(input('Enter a natural number: '))
    power_sum = main(num)
    print('Sum of digits of 2^{}:'.format(num))
    print('  {}'.format(power_sum))
