import sys

def search_uniques(word_buffer):
    col_dicts = []
    for row in word_buffer:
        for col in range(0, len(row)):
            if len(col_dicts) == col:
                col_dicts.append(dict())
            val = row[col]
            if val not in col_dicts[col]:
                col_dicts[col][val] = [row]
            else:
                col_dicts[col][val].append(row)

    for col in col_dicts:
        for key in col.keys():
            if len(col[key]) == 1:
                del col[key]

    return col_dicts

def read_file(filename,strip_header=True):
    with open(filename) as file:
        buffer = file.readlines()
    if strip_header:
        buffer = buffer[1:]
    for i in range(0,len(buffer)):
        buffer[i] = buffer[i].strip().split(',')
    return buffer

def main():
    if len(sys.argv) == 1:
        print "usage"

    cols = []
    strip_header = False

    files = []

    for arg in sys.argv[1:]:
        if arg == '-s':
            strip_header = True
        else:
            files.append((arg, strip_header,))
            strip_header = False

    buffer = []
    for file in files:
        buffer += read_file(file[0], file[1])

    col_dups = search_uniques(buffer)

    for icol in range(len(col_dups)):
        keys = col_dups[icol].keys()
        keys.sort()
        for key in keys:
            print "Col %d, Value %s:" % (icol, key)
            for row in col_dups[icol][key]:
                print "\t%s" % ','.join(row)

if __name__ == '__main__':
    main()

