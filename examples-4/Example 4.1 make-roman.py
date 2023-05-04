import sys

def int_to_roman(input):
    """ Convert an integer to a Roman numeral. """

    ints = (1000, 900,  500, 400, 100,  90, 50,  40, 10,  9,   5,  4,   1)
    nums = ('M',  'CM', 'D', 'CD','C', 'XC','L','XL','X','IX','V','IIII','I')
    result = []
    for i in range(len(ints)):
        count = int(input / ints[i])
        result.append(nums[i] * count)
        input -= ints[i] * count
    return ''.join(result)

if __name__ == "__main__":
    try:
        number = int(sys.argv[1])
    except (IndexError, ValueError):
        print(f"Syntax: {sys.argv[0]} <number>")
        sys.exit(1)
    print(f"{number} in Roman numerals is {int_to_roman(number)}")
