def text_to_array(text, newline='\n', delimiter=',', quotechar='"', escapechar='\\'):
    lines = []
    fields = []
    newlinesize = len(newline)
    startfield = 0
    quoteisopen = False
    escapeon = False
    jump = 0
    for x in range(len(text)):
        if jump > 0:
            jump -= 1
            continue
        if escapeon:
            escapeon = False
            continue
        if text[x] == escapechar:
            escapeon = True
        elif text[x] == quotechar:
            quoteisopen = not quoteisopen
        elif (text[x] == delimiter) and (not quoteisopen):
            fields.append(text[startfield:x])
            startfield = x + 1
        elif (text[x:x+newlinesize] == newline) and (not quoteisopen):
            fields.append(text[startfield:x])
            startfield = x + newlinesize
            lines.append(fields)
            fields = []
            jump = newlinesize -1
    if x > startfield:
        fields.append(text[startfield:x])
    if len(fields) > 0:
        lines.append(fields)
    return lines