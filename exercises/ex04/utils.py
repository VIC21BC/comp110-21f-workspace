"""List utility functions."""

__author__ = "730449914"

integers: list[int] = [1, 1, 1]
e_list_0: list[int] = []
e_list_1: list[int] = [1]
max_0: list[int] = [1, 3, 7, 20, 10]


def all(b: list[int], a: int) -> bool:
    """See if one integer equals all integers in a list."""
    i: int = 0

    while i < len(b):
        if a == b[i]:
            if i == len(b) - 1:
                if b[i] == b[len(b) - 1]:
                    return True
            i += 1
        else:
            return False

    return False


def is_equal(c: list[int], d: list[int]) -> bool:
    """See if one list equals the other list!"""
    i: int = 0

    if len(c) == 0 and len(d) == 0:
        return True
    if len(c) == 0 and len(d) > 0:
        return False
    if len(d) == 0 and len(c) > 0:
        return False
    while i < len(c) and i < len(d):
        if c[i] == d[i]:
            if i == len(c) - 1 and i == len(d) - 1:
                if len(c) == len(d):
                    if c[len(c) - 1] == d[len(d) - 1]:
                        return True
            i += 1
        else:
            return False

    return False


def max(input: list[int]) -> int:
    """Find the largest number!"""
    i: int = 0

    if len(input) == 0:
        raise ValueError("max() arg is an empty List")
    
    else:
        while i < len(input):
            j: int = i + 1
            while j < len(input):
                if input[i] > input[j]:
                    if j == len(input) - 1:
                        if input[i] >= input[len(input) - 1]:
                            return input[i]
                    j += 1 
                else:
                    j += len(input)
            i += 1
    return input[len(input) - 1]


if __name__ == "__main__":
    print(all(integers, 1))


if __name__ == "__main__":
    print(is_equal(e_list_0, e_list_1))


if __name__ == "__main__":
    print(max(max_0))