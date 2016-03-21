import re
import sys

lines = []
try:
    input = open(sys.argv[1], 'r')
    lines = input.readlines()
    input.close()

    output = open(sys.argv[2], 'w')
    for line in lines:
        # \((.|\n)*\)
        if re.search('\(|\)', line):
            continue
        subjectMatch = re.search('^[A-Z]*:', line)
        if subjectMatch:
            substring = subjectMatch.group(0) + " "
            newLine = line.replace(substring, "")
            output.write(newLine)
            continue
        output.write(line)
    output.close()
    print 'Subtitle trim complete!'
except IndexError:
    print 'Set an input and output file argument'
except IOError:
    print 'No such file exists!'