# arr = [[[1,2],[2,3]],[[5,6],[8,9]]]
# arr = [list([]*2) for _ in range(2)]
arr = [[[] for _ in range(2)] for _ in range(2)]
arr = [[[] for _ in range(N)] for _ in range(N)]

# print()
arr[1][1].append(7)
for i in arr:
    print(i)
# print(arr[1][1])
#
# for i in arr:
#     print(i)
# print()
# for i in range(5):
#     for j in range(5):
#         print(arr[i][j])