# 테트로미노 14500 백준

import sys

input = sys.stdin.readline

n, m = map(int, input().split())

tetromino = [
    # ㅡ
    [[0, 0], [0, 1], [0, 2], [0, 3]],
    [[0, 0], [1, 0], [2, 0], [3, 0]],
    # ㅁ
    [[0, 0], [0, 1], [1, 0], [1, 1]],
    # L
    [[0, 0], [1, 0], [2, 0], [2, -1]],
    [[0, 0], [0, -1], [1, 0], [2, 0]],
    [[0, 0], [1, 0], [2, 0], [2, 1]],
    [[0, 0], [1, 0], [2, 0], [0, 1]],
    [[0, 0], [0, -1], [0, -2], [1, 0]],
    [[0, 0], [-1, 0], [0, -1], [0, -2]],
    [[0, 0], [-1, 0], [0, 1], [0, 2]],
    [[0, 0], [1, 0], [0, 1], [0, 2]],
    # ∫
    [[0, 0], [1, 0], [1, 1], [2, 1]],
    [[0, 0], [0, 1], [-1, 1], [-1, 2]],
    [[0, 0], [1, 0], [1, -1], [2, -1]],
    [[0, 0], [0, 1], [1, 1], [1, 2]],
    # ㅓㅏㅜㅗ
    [[0, 0], [0, 1], [0, 2], [1, 1]],
    [[0, 0], [0, 1], [-1, 1], [1, 1]],
    [[0, 0], [0, 1], [0, 2], [-1, 1]],
    [[0, 0], [1, 0], [2, 0], [1, 1]],
]

board = [list(map(int, input().split())) for _ in range(n)]
res = 0

for i in range(n):
    for j in range(m):
        for tet in tetromino:
            sum_tet = 0
            for t in tet:
                x, y = i + t[0], j + t[1]
                if 0 <= x < n and 0 <= y < m:
                    sum_tet += board[x][y]
                else:
                    break
            res = max(res, sum_tet)
print(res)