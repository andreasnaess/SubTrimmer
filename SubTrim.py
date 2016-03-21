import re
import sys

lines = []
indexCount = 0
index = []
timestamp = []
subtitle = []

try:
    f = open(sys.argv[1], 'r')
    data = f.read()
    paragraphList = data.split("\n\n")
    for paragraph in paragraphList:
        paragraphLines = paragraph.split("\n")
        if not paragraphLines[0]:
            continue
        indexCount += 1
        index.append(str(indexCount))
        timestamp.append(paragraphLines[1])
        tempSub = ""
        parenthesesSeen = False
        for line in paragraphLines[2:]:
            if re.search('\(|\)', line):
                parenthesesSeen = True
                continue
            subjectMatch = re.search('^[A-Z]*:', line)
            if subjectMatch:
                substring = subjectMatch.group(0) + " "
                newLine = line.replace(substring, "")
                tempSub += newLine + '\n'
                continue
            tempSub += line + '\n'

        if not tempSub:
            if parenthesesSeen:
                index.pop()
                indexCount -= 1
                timestamp.pop()
                continue

        if tempSub:
            subtitle.append(tempSub)

    output = open(sys.argv[2], 'w')
    for x in range(len(index)):
        output.write(index[x] + '\n')
        output.write(timestamp[x] + '\n')
        output.write(subtitle[x] + '\n')

    output.close()
    print 'Subtitle trim complete!'
except IndexError, e:
    # print e
    print 'Set an input and output file argument'
except IOError, e:
    # print e
    print 'No such file exists!'
