
def char_counts(textfilename):
    """Takes in a file and counts number of times a character is used"""
    file_opener = open(textfilename).read()

    liste = [0]*256

    for character in file_opener:
        i = ord(character)
        liste[i] += 1
    return liste


if __name__ == '__main__':
    filename = 'file_stats.py'
    frequencies = char_counts(filename)
    for code in range(256):
        if frequencies[code] > 0:
            character = ''
            if code >= 32:
                character = chr(code)

            print(
                '{:3}{:>4}{:6}'.format(
                    code, character, frequencies[code]
                )
            )
