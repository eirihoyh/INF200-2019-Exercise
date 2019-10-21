def bubble_sort(data):
    """Takes in a tuplet and sorts the numbers inside"""
    new_data = list(data)
    swap = True
    while swap:
        swap = False
        for i in range(len(new_data) - 1):
            if new_data[i] > new_data[i + 1]:
                temp = new_data[i]
                new_data[i] = new_data[i + 1]
                new_data[i + 1] = temp
                swap = True
    return new_data


if __name__ == "__main__":

    for data in ((), (1,), (1, 3, 8, 12), (12, 8, 3, 1), (8, 3, 12, 1)):
        print("{!s:>15} --> {!s:>15}".format(data, bubble_sort(data)))
