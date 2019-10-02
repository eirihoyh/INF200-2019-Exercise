

def test_letter_freq_counts_on_sample_strings():
    count = letter_freq('a')
    assert count['a'] == 1

    count = letter_freq('ab')
    assert count['a'] == 2

    count = letter_freq[]