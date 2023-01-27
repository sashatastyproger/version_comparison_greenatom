def comparison(a, b: str) -> int:
    if a > b:
        return 1
    elif a < b:
        return -1
    elif a == b:
        return 0


if __name__ == '__main__':
    a = input()
    b = input()
    print(comparison(a, b))