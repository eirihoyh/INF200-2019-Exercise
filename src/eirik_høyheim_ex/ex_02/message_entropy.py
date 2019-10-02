from math import log2


def letter_freq(txt):
    """Takes in a text and counts how many times a character is used"""
    lower_txt = txt.lower()
    letter_counter = {}
    for letter in lower_txt:
        if letter not in letter_counter:
            letter_counter[letter] = 1
        elif letter in letter_counter:
            letter_counter[letter] += 1
    return letter_counter


def entropy(message):
    counter = letter_freq(message)
    h = 0
    for n_i in counter.values():
        n = sum(counter.values())
        p_i = n_i / n
        h += -p_i * log2(p_i)

    return h


if __name__ == "__main__":
    for msg in '', 'aaaa', 'aaba', 'abcd', 'This is a short text.':
        print('{:25}: {:8.3f} bits'.format(msg, entropy(msg)))
