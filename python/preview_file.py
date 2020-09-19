with open('D:/IR/HWf/sogou/0019.out', 'r', encoding='utf-8') as f:
    i = 0
    for line in f:
        print(line.strip())
        i += 1
        if i > 100:
            exit(0)
