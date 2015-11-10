def longest_run(string):
    print 'calculating longest run of',string
    maxStart = 0;
    maxEnd = 0;
    currStart = 0;
    currEnd = 0;
    currChar = '';
    for i in range(0, len(string)):
        if currChar == string[i]:
            currEnd = i
        else:
            currStart = i
            currEnd = i
            currChar = string[i]

        if currEnd - currStart > maxEnd - maxStart:
            maxEnd = currEnd
            maxStart = currStart

    return [maxStart, maxEnd]

print(longest_run('abc'))
print(longest_run('abbbbc'))
print(longest_run('abaccccc'))
print(longest_run('aaabc'))
print(longest_run('abcd'))
