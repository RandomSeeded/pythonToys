def is_isogram(string):
    D = {}
    for i in range(0, len(string)):
        letter = string[i].lower()
        if letter in D:
            return False
        else:
            D[letter] = True
        D[letter] = 1

    return True
