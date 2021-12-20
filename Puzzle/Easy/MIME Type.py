mime_table = {}
n = int(input())  # Number of elements which make up the association table.
q = int(input())  # Number q of file names to be analyzed.

for i in range(n):
    # ext: file extension
    # mt : MIME type.
    ext, mt = input().split()
    mime_table[ext.lower()] = mt

for i in range(q):
    filename = input()  # One file name per line.

    if '.' not in filename:
        print("UNKNOWN")
    else:
        pos = len(filename) - 1
        while filename[pos] != '.':
            pos -= 1

        ext_name = filename[pos + 1:].lower()

        if ext_name in mime_table:
            print(mime_table[ext_name])
        else:
            print("UNKNOWN")
