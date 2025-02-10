import sys
sys.stdin = open('input.txt', 'r')

N=9
smalls = [int(input()) for _ in range(N)]
for i in range(N-6):
    for j in range(i+1, N-5):
        for k in range(j+1, N-4):
            for l in range(k+1, N-3):
                for m in range(l+1, N-2):
                    for n in range(m+1, N-1):
                        for o in range(n+1, N):
                            tmp = []
                            for a in (i, j, k, l, m, n, o):
                                tmp.append(smalls[a])
                            if sum(tmp)==100:
                                tmp.sort()
                                for t in tmp:
                                    print(t)
                                exit(0)