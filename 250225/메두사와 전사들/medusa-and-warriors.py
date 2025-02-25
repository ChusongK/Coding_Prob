from collections import deque

def in_range(ni, nj):
    return 0<=ni<N and 0<=nj<N

def see(d):
    di = [-1, 1, 0, 0]
    dj = [0, 0, -1, 1]
    s = []
    num = cnt = 0
    q = deque()
    ni, nj = bi, bj
    if d==2:    #좌
        while 0<nj:
            cnt+=1
            ni, nj = ni+di[d], nj+dj[d]
            for i in range(ni-cnt, ni+cnt+1):
                if in_range(i, nj):
                    s.append((i, nj))
                    if (i, nj) in war:
                        q.append((i, nj))
                        num+=1
        while q:
            ci, cj = q.popleft()
            cnt = 0
            if ci==bi:
                while 0<cj:
                    ci, cj = ci+di[d], cj+dj[d]
                    s.remove((ci,cj))
                    if (ci, cj) in war:
                        num-=1
            elif ci<bi:
                while 0<cj:
                    cnt+=1
                    ci, cj = ci + di[d], cj + dj[d]
                    for i in range(ci-cnt, ci+1):
                        if in_range(i, cj) and (i,cj) in s:
                            s.remove((i, cj))
                            if (i, cj) in war:
                                num-=1
            elif ci>bi:
                while 0<cj:
                    cnt+=1
                    ci, cj = ci + di[d], cj + dj[d]
                    for i in range(ci, ci+cnt+1):
                        if in_range(i, cj) and (i,cj) in s:
                            s.remove((i, cj))
                            if (i,cj) in war:
                                num -= 1

    if d==3:    #우
        while nj<N-1:
            cnt+=1
            ni, nj = ni+di[d], nj+dj[d]
            for i in range(ni-cnt, ni+cnt+1):
                if in_range(i, nj):
                    s.append((i, nj))
                    if (i, nj) in war:
                        q.append((i, nj))
                        num+=1
        while q:
            ci, cj = q.popleft()
            cnt = 0
            if ci==bi:
                while cj<N-1:
                    ci, cj = ci+di[d], cj+dj[d]
                    s.remove((ci,cj))
                    if (ci, cj) in war:
                        num-=1
            elif ci<bi:
                while cj<N-1:
                    cnt+=1
                    ci, cj = ci + di[d], cj + dj[d]
                    for i in range(ci-cnt, ci+1):
                        if in_range(i, cj) and (i,cj) in s:
                            s.remove((i, cj))
                            if (i, cj) in war:
                                num-=1
            elif ci>bi:
                while cj<N-1:
                    cnt+=1
                    ci, cj = ci + di[d], cj + dj[d]
                    for i in range(ci, ci+cnt+1):
                        if in_range(i, cj) and (i,cj) in s:
                            s.remove((i, cj))
                            if (i,cj) in war:
                                num -= 1

    if d==0:    #상
        while 0<ni:
            cnt+=1
            ni, nj = ni+di[d], nj+dj[d]
            for j in range(nj-cnt, nj+cnt+1):
                if in_range(ni, j):
                    s.append((ni, j))
                    if (ni, j) in war:
                        q.append((ni, j))
                        num+=1
        while q:
            ci, cj = q.popleft()
            cnt = 0
            if cj==bj:
                while 0<ci:
                    ci, cj = ci+di[d], cj+dj[d]
                    s.remove((ci,cj))
                    if (ci, cj) in war:
                        num-=1
            elif cj<bj:
                while 0<ci:
                    cnt+=1
                    ci, cj = ci + di[d], cj + dj[d]
                    for j in range(cj-cnt, cj+1):
                        if in_range(ci, j) and (ci,j) in s:
                            s.remove((ci, j))
                            if (ci, j) in war:
                                num-=1
            elif cj>bj:
                while 0<ci:
                    cnt+=1
                    ci, cj = ci + di[d], cj + dj[d]
                    for j in range(cj, cj+cnt+1):
                        if in_range(ci, j) and (ci,j) in s:
                            s.remove((ci, j))
                            if (ci, j) in war:
                                num -= 1

    if d==1:    #하
        while ni<N-1:
            cnt+=1
            ni, nj = ni+di[d], nj+dj[d]
            for j in range(nj-cnt, nj+cnt+1):
                if in_range(ni, j):
                    s.append((ni, j))
                    if (ni, j) in war:
                        q.append((ni, j))
                        num+=1
        while q:
            ci, cj = q.popleft()
            cnt = 0
            if cj==bj:
                while ci<N-1:
                    ci, cj = ci+di[d], cj+dj[d]
                    s.remove((ci,cj))
                    if (ci, cj) in war:
                        num-=1
            elif cj<bj:
                while ci<N-1:
                    cnt+=1
                    ci, cj = ci + di[d], cj + dj[d]
                    for j in range(cj-cnt, cj+1):
                        if in_range(ci, j) and (ci, j) in s:
                            s.remove((ci, j))
                            if (ci, j) in war:
                                num-=1
            elif cj>bj:
                while ci<N-1:
                    cnt+=1
                    ci, cj = ci + di[d], cj + dj[d]
                    for j in range(cj, cj+cnt+1):
                        if in_range(ci, j) and (ci, j) in s:
                            s.remove((ci, j))
                            if (ci, j) in war:
                                num -= 1

    return s, num

def search():
    q = deque()
    q.append((ei, ej))
    v[ei][ej] = 1
    while q:
        ci, cj = q.popleft()
        if (ci, cj)==(bi, bj):
            return
        for di, dj in ((-1,0),(1,0),(0,-1),(0,1)):
            ni, nj = ci+di, cj+dj
            if in_range(ni, nj) and arr[ni][nj]==0 and not v[ni][nj]:
                q.append((ni, nj))
                v[ni][nj] = v[ci][cj]+1
    print(-1)
    exit(0)

N, M = map(int, input().split())
bi, bj, ei, ej = map(int, input().split())
tmp = list(map(int, input().split()))
war = []
for _ in range(M):
    a = tmp.pop()
    b = tmp.pop()
    war.append((b, a))

arr = [list(map(int, input().split())) for _ in range(N)]

v = [[0]*N for _ in range(N)]
search()

while True:
    move_dist = rock = attk = 0
    for di, dj in ((-1,0),(1,0),(0,-1),(0,1)):
        ni,nj = bi+di, bj+dj
        if not in_range(ni, nj):
            continue
        if (ni,nj)==(ei,ej):
            print(0)
            exit(0)

        elif v[ni][nj]==v[bi][bj]-1:
            bi, bj = ni, nj
            while (bi, bj) in war:
                war.remove((bi, bj))
            break

    res = 0
    tmp_s = []
    for d in range(4):
        s, num = see(d)
        if num>res:
            res=num
            tmp_s = s
    tmp = war[:]
    for i, j in war:
        if (i, j) in tmp_s:
            rock+=1
            continue
        mn = abs(i-bi)+abs(j-bj)
        mi, mj = -1, -1
        for di, dj in ((-1,0),(1,0),(0,-1),(0,1)):
            ni, nj = i+di, j+dj
            dist = abs(ni-bi)+abs(nj-bj)
            if in_range(ni, nj) and dist<mn and (ni, nj) not in tmp_s:
                mn = dist
                mi, mj = ni, nj
        if mn!=abs(i-bi)+abs(j-bj):
            move_dist += 1
            tmp.remove((i, j))
            if (mi, mj)==(bi, bj):
                attk += 1
                continue
            else:
                tmp.append((mi, mj))
        else:
            continue
        mn = abs(mi-bi)+abs(mj-bj)
        fi, fj = 0, 0
        for di, dj in ((0,-1),(0,1),(-1,0),(1,0)):
            ni, nj = mi+di, mj+dj
            if (ni, nj)==(i, j):
                continue
            dist = abs(ni-bi)+abs(nj-bj)
            if in_range(ni, nj) and dist<mn and (ni, nj) not in tmp_s:
                mn = dist
                fi, fj = ni, nj
        if mn!=abs(mi-bi)+abs(mj-bj):
            move_dist += 1
            tmp.pop()
            if (fi, fj)==(bi, bj):
                attk += 1
            else:
                tmp.append((fi, fj))

    war = tmp
    print(move_dist, rock, attk)