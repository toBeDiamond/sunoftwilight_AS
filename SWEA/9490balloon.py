# T = int(input())
#
# for tc in range(1, T+1):
#     N, M = map(int, input().split())
#     arr = [list(map(int, input().split())) for _ in range(N)]
#
#     di = [0, 1, 0, -1]
#     dj = [1, 0, -1, 0]
#
#     max_f = 0
#
#     for i in range(N):
#         for j in range(M):
#             total = arr[i][j]
#             for k in range(4):
#                 for m in range(1, arr[i][j]+1):
#                     ni = i + di[k] * m
#                     nj = j + dj[k] * m
#                     if 0 <= ni < N and 0 <= nj < M:
#                         total += arr[ni][nj]
#                 if max_f < total:
#                     max_f = total
#
#     print(f'#{tc} {max_f}')


# 0813
T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]

    max_sum = 0

    for i in range(N):
        for j in range(M):
            sum_of = arr[i][j]
            for k in range(4):
                for p in range(1, arr[i][j]+1):
                    ni = i + di[k] * p
                    nj = j + dj[k] * p

                    if 0 <= ni < N and 0 <= nj < M:
                        sum_of += arr[ni][nj]

            if max_sum < sum_of:
                max_sum = sum_of

    print(f'#{tc} {max_sum}')