def letter_freq(txt):
    """Takes in a text and counts how many times a character is used"""
    letter_counter = {}
    for letter in txt:
        if letter not in letter_counter:
            letter_counter[letter] = 1
        elif letter in letter_counter:
            letter_counter[letter] += 1
    return letter_counter


if __name__ == '__main__':
    text = input('Please enter text to analyse: ')

    frequencies = letter_freq(text)
    for letter, count in frequencies.items():
        print('{:3}{:10}'.format(letter, count))
