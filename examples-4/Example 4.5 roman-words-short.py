import roman

def main():
    with open("twl06.txt") as fp:
        words = set([x.strip().upper() for x in fp.readlines()])
    roman_numerals = set([roman.int_to_roman(x) for x in range(1, 4000)])
    print("Roman numbers which are also words:")
    print(roman_numerals.intersection(words))

if __name__ == "__main__":
    main()