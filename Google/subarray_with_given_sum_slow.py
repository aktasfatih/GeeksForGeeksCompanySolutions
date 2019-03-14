# This is the slow approach.
T = int(input())
for t in range(0, T):
    N, S = map(int, input().split())
    A = list(map(int, input().split()))
    Found = False
    for i, k in ((i, k) for i in range(0, N) for k in range(0, N)):
        if sum(A[i:k]) == S:
            print(i+1, k)
            Found = True
            break
    if not Found:
        print(-1)
