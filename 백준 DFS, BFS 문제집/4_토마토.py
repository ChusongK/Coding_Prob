import sys
sys.stdin = open('input.txt', 'r')
from collections import deque

M, N, H = map(int, input().split())

arr = []

for k in range(H):
    tmp = []
    for j in range(N):
        tmp.append(list(map(int, input().split())))
    arr.append(tmp)

v = [[[0]*M for _ in range(N)] for _ in range(H)]
q = deque()
def in_range(nk, nj, ni):
    return 0<=nk<H and 0<=nj<N and 0<=ni<M

def bfs():
    while q:
        ck, cj, ci = q.popleft()
        for dk, dj, di in ((-1, 0, 0), (1, 0, 0), (0, -1, 0), (0, 1, 0), (0, 0, -1), (0, 0, 1)):
            nk, nj, ni = ck + dk, cj + dj, ci + di
            if in_range(nk, nj, ni) and arr[nk][nj][ni]==0 and not v[nk][nj][ni]:
                v[nk][nj][ni] = 1
                arr[nk][nj][ni] = arr[ck][cj][ci] + 1
                q.append((nk, nj, ni))

for k in range(H):
    for j in range(N):
        for i in range(M):
            if arr[k][j][i]==1 and not v[k][j][i]:
                q.append((k, j, i))
bfs()

for k in range(H):
    for j in range(N):
        for i in range(M):
            if arr[k][j][i]==0:
                print(-1)
                exit(0)

mx = 0
for k in arr:
    for j in k:
        mx = max(mx, max(j))

print(mx-1)

# 좋은 질문이에요! 왜 익은 토마토들이 **한 번에 모두 영향을 줘야 하는지**를 더 자세히 설명할게요.
#
# ### 시간 측정의 문제
#
# 토마토 문제에서의 목표는 **모든 토마토가 익을 때까지 걸리는 최소 시간**을 계산하는 것입니다. 만약 익은 토마토가 하나씩 순차적으로 영향을 준다면, 시간 계산이 실제 상황보다 더 길어질 수 있습니다.
#
# #### 예시로 다시 설명해 볼게요:
#
# 다음과 같은 상태가 있습니다:
#
# ```
# 1 0 0
# 0 0 0
# 0 0 1
# ```
#
# - `(0, 0)`과 `(2, 2)`에 익은 토마토가 있고, 나머지는 익지 않은 토마토예요.
#
# ##### 순차적으로 영향을 주는 경우:
#
# 1. **첫날**: `(0, 0)`에서만 영향을 줘서 `(0, 1)`과 `(1, 0)`이 익어요. 이 시점에서 `(2, 2)`는 아무것도 하지 않아요.
# 2. **둘째 날**: 이제 `(2, 2)`에서 영향을 줘서 `(1, 2)`와 `(2, 1)`이 익어요.
# 3. **셋째 날**: 이제야 중앙의 `(1, 1)`이 익어요.
#
# 총 3일이 걸렸죠?
#
# ##### 동시에 영향을 주는 경우 (올바른 방식):
#
# 1. **첫날**: `(0, 0)`과 `(2, 2)`가 **동시에** 영향을 줘서 `(0, 1)`, `(1, 0)`, `(1, 2)`, `(2, 1)`이 한 번에 익어요.
# 2. **둘째 날**: 이제 중앙의 `(1, 1)`이 익어요.
#
# 총 2일이면 모든 토마토가 익게 돼요.
#
# ### 왜 한 번에 모두 영향을 줘야 하나요?
#
# 1. **현실적 시뮬레이션**: 모든 익은 토마토들이 동시에 주변에 영향을 줘야 실제 상황을 정확히 시뮬레이션할 수 있습니다. 익은 토마토들은 하루 동안 동시에 익지 않은 토마토를 익히죠.
#
# 2. **최소 시간 계산**: 여러 익은 토마토가 동시에 영향을 줄 수 있게 해야 최소 시간을 계산할 수 있습니다. 순차적으로 처리하면, 불필요하게 시간이 더 오래 걸린다고 계산될 수 있습니다.
#
# 이 방식이 실제로 더 짧은 시간을 걸리게 하고, 문제의 의도에 맞는 최소 시간을 정확히 구할 수 있게 도와줍니다.
#
# 이제 이해가 되시나요?