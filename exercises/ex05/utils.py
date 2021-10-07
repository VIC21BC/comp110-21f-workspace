"""List utility functions part 2."""

__author__ = "730449914"

integers: list[int] = []
integers_2: list[int] = [1, 2, 2, 0, -4]
integers_3: list[int] = [1, 2, 2, 0, -4]
integers_4: list[int] = [1, 2, 2, 0, -4]


def only_evens(a: list[int]) -> list[int]:
    """Find all even numbers in a list."""
    i: int = 0
    even_list: list[int] = []

    while i < len(a):
        if a[i] % 2 == 0:
            even_list.append(a[i])
        i += 1
    return even_list


def sub(b: list[int], c: int, d: int) -> list[int]:
    """Return a subset of a list."""
    i: int = 0
    sub_list: list[int] = []
    if c < 0:
        c = 0
    if d > len(b):
        d = len(b)
    if len(b) == 0 or c >= len(b) or d <= 0:
        return sub_list
    if c == c:
    
        while i < d - c:
            if c + i < d:
                sub_list.append(b[c + i])
            i += 1
    return sub_list


def concat(e: list[int], f: list[int]) -> list[int]:
    """Merch two lists into a new list."""
    i: int = 0
    i_2: int = 0
    concat_list: list[int] = []
    while i < len(e):
        if i < len(e):
            concat_list.append(e[i])
        i += 1

    while i_2 < len(f):
        if i_2 < len(f):
            concat_list.append(f[i_2])
        i_2 += 1
    return concat_list


if __name__ == "__main__":
    print(only_evens(integers))


if __name__ == "__main__":
    print(sub(integers_2, -1, 1))


if __name__ == "__main__":
    print(concat(integers_3, integers_4))