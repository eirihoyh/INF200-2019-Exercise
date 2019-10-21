def squares_by_comp(n):
    return [k ** 2 for k in range(n) if k % 3 == 1]


def squares_by_loop(n):
    """makes a for-loop and does the same as squares_by_comp function"""
    list_ = []
    for k in range(n):
        if k % 3 == 1:
            list_.append(k ** 2)
    return list_


if __name__ == "__main__":
    if squares_by_comp(2) != squares_by_loop(2):
        print("ERROR!")
