import math

w, h, t1, t2, t3 = [int(i) for i in input().split()]
delta1 = t2 - t1
delta2 = t3 - t2
dict_t1 = {}
dict_t2 = {}
pos3_board = [['.' for _ in range(w)] for _ in range(h)]

for i in range(h):
    pos1, pos2 = input().split()
    for j in range(w):
        if pos1[j] != '.':
            dict_t1[pos1[j]] = [i, j]
        if pos2[j] != '.':
            dict_t2[pos2[j]] = [i, j]

for altitude, coord1 in dict_t1.items():
    coord2 = dict_t2[altitude]
    deltaCoord = [coord2[0] - coord1[0], coord2[1] - coord1[1]]
    coord3 = [None, None]
    coord3[0] = coord2[0] + math.floor(deltaCoord[0] * (delta2 / delta1))
    coord3[1] = coord2[1] + math.floor(deltaCoord[1] * (delta2 / delta1))

    if coord3[0] < 0 or coord3[0] >= h or coord3[1] < 0 or coord3[1] >= w:
        continue
    elif pos3_board[coord3[0]][coord3[1]] == '.' or pos3_board[coord3[0]][coord3[1]] > altitude:
        pos3_board[coord3[0]][coord3[1]] = altitude

for line in pos3_board:
    print(''.join(line))
