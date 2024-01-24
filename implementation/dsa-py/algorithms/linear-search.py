def linear_search() -> bool:
    arr = [x for x in range(10)]
    target = 6
    for i in arr:
        if i == target:
            return True
    return False


if __name__ == "__main__":
    print(linear_search())