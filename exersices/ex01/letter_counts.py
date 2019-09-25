from collections import Counter


def letter_freq(text):
    text = text.lower()
    cnt = Counter()  # adds the counter dictionary
    for symbol in text:
        cnt[symbol] += 1  # For every letter in the string, add it and a 1, if it was already added then plus 1
    return cnt


if __name__ == '__main__':
    text = input('Please enter text to analyse: ')

    frequencies = letter_freq(text)
    for letter, count in sorted(frequencies.items()):
        print('{:3}{:10}'.format(letter, count))
