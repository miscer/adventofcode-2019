import itertools


def count_adjacent(digits: [str]) -> [int]:
    return [sum(1 for _ in g) for k, g in itertools.groupby(digits)]


def check_password(password: int) -> bool:
    digits = list(str(password))

    adjacent = count_adjacent(digits)

    if 2 not in adjacent:
        return False

    for i in range(0, len(digits) - 1):
        if digits[i] > digits[i + 1]:
            return False

    return True


assert check_password(112233)
assert check_password(111122)
assert not check_password(111111)
assert not check_password(223450)
assert not check_password(123789)
assert not check_password(123444)

passwords = range(168630, 718098)
matching = (check_password(password) for password in passwords)

print(sum(matching))
