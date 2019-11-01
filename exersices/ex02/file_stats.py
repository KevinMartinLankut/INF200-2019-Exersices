def char_counts(textfilename):
    with open(textfilename, 'r') as infile: #Using with open so I don't have to close it later
        sentences = infile.readline() #Saving the text into a variable
        counts = [0] * 256 #Making a list with a spot for all 255 character codes, filling them with 0's
        for c in sentences: #for every letter in the text
            counts[ord(c)] += 1 #Add +1 on the letters character code spot
    return counts #Returns the list

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