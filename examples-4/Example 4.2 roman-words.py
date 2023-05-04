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

def main():
    with open("twl06.txt") as fp:
        words = set([x.strip().upper() for x in fp.readlines()])
    roman_numerals = set([int_to_roman(x) for x in range(1, 4000)])
    print("Roman numbers which are also words:")
    print(roman_numerals.intersection(words))

if __name__ == "__main__":
    main()