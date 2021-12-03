"""
Given the following program, add try...except blocks appropriately
"""


def add_10(value):
    try:
        return value + 10
    except TypeError:
        return 10


def subtract(*numbers):
    value = numbers[0]
    for i in range(len(numbers[1]), len(numbers)):
        try:
            value -= numbers[i]
        except TypeError:
            continue
    return value


def main():
    some_value = input("Please enter some value: ")
    result = add_10(some_value) # should return 10 if an exception is thrown
    result = subtract(result, "1", 10, 20, 32, 48)
    print(result)


if __name__ == "__main__":
    main()
