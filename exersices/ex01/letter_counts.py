import collections as c
#Imported to use Counter() function. A Counter is a dict subclass for counting hashable objects.
#It is an unordered collection where elements are stored as dictionary keys and their counts are stored as dictionary values.
#Counts are allowed to be any integer value including zero or negative counts.

def letter_freq(text):
    text = text.lower() #Making string lower case
    cnt = c.Counter() #adds the counter dictionary
    for symbol in text:
        cnt[symbol] += 1 #For every letter in the string, add it and a 1, if it was already added then plus 1
    return cnt #Return the dict

if __name__ == '__main__':
    text = input('Please enter text to analyse: ')

    frequencies = letter_freq(text)
    for letter, count in sorted(frequencies.items()): #using preexisting function "sorted" to sort alphabetically
        print('{:3}{:10}'.format(letter, count))