def get_combinations(n, p):
    '''
    Get all combinations C(a, b) % p with a < n.
    '''
    C = []
    for _ in range(n):
        C.append([1 for _ in range(n)])
    for i in range(2, n):
        for j in range(1, i):
            C[i][j] = (C[i - 1][j] + C[i - 1][j - 1]) % p
    return C
