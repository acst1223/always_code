def read_lines(file):
    with open(file, 'r') as f:
        while True:
            st = f.readline()
            if not st:
                break
            if st == '\n':
                continue
            if st[-1] == '\n':
                st = st[: -1]
            yield st
