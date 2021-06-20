def text_to_json(text, newline='\n', delimiter=',', quotechar='"', escapechar='\\', removequote=True):
    records = []
    headers = []
    fields = []
    errors = []
    newlinesize = len(newline)
    startfield = 0
    quoteisopen = False
    escapeon = False
    jump = 0
    linenr = 0

    def addfield():
        string = text[startfield:x]
        if removequote:
            string = string.strip()
            i = len(string) -1
            if (i > 1) and (string[0] == quotechar) and (string[i] == quotechar):
                string = string[1:i]
        fields.append(string)

    def addline():
        if len(headers) != len(fields):
            errors.append('{}: {}'.format(linenr+1, fields))
            return False
        record = {}
        for i, key in enumerate(headers):
            record[key] = fields[i]
        records.append(record)
        return True

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
            addfield()
            startfield = x + 1
        elif (text[x:x+newlinesize] == newline) and (not quoteisopen):
            linenr += 1
            addfield()
            startfield = x + newlinesize
            if linenr == 1:
                headers = fields
            else:
                addline()
            fields = []
            jump = newlinesize -1
    if x > startfield:
        addfield()
    if len(fields) > 0:
        addline()
    return records, errors
