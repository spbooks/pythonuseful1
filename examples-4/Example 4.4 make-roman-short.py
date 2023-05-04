import sys

from roman import int_to_roman

if __name__ == "__main__":
    try:
        number = int(sys.argv[1])
    except (IndexError, ValueError):
        print(f"Syntax: {sys.argv[0]} <number>")
        sys.exit(1)
    print(f"{number} in Roman numerals is {int_to_roman(number)}")
