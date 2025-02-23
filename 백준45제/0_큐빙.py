import sys
sys.stdin = open('input.txt', 'r')

TC = int(input())
for tc in range(1, TC+1):
    st = 'ogwbry'
    c = []
    for ch in st:
        for _ in range(10):
            c.append(ch)

    _ = int(input())
    cmds = list(input().split())
    for cmd in cmds:
        if cmd=='B-':
            c[1:10]=c[3],c[6],c[9],c[2],c[5],c[8],c[1],c[4],c[7]
            (c[11],c[12],c[13],c[21],c[22],c[23],
             c[31],c[32],c[33],c[51],c[52],c[53])\
                =(c[51],c[52],c[53],c[11],c[12],c[13],
                  c[21],c[22],c[23],c[31],c[32],c[33])
        elif cmd=='B+':
            (c[11], c[12], c[13], c[21], c[22], c[23],
             c[31], c[32], c[33], c[51], c[52], c[53]) \
                = (c[21], c[22], c[23], c[31], c[32], c[33], c[51], c[52], c[53], c[11], c[12], c[13],)

    for i in (21, 24, 27):
        print("".join(c[i:i+3]))