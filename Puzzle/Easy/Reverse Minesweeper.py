mines = []
w = int(input())
h = int(input())
for i in range(h):
    line = input()
    line_tmp = []
    for c in line:
        line_tmp.append(c)
    mines.append(line_tmp)

reveal = []

for i in range(h):
    line_tmp = ""
    for j in range(w):
        score = "."
        min_i = max(0, i - 1)
        max_i = min(h, i + 2)
        min_j = max(0, j - 1)
        max_j = min(w, j + 2)
        if mines[i][j] == "x":
            line_tmp += "."
            continue
        for x in range(min_i, max_i):
            for y in range(min_j, max_j):
                if x == i and y == j:
                    continue
                else:
                    if mines[x][y] == "x":
                        if score == ".":
                            score = 0
                        score += 1
        line_tmp += str(score)
    reveal.append(line_tmp)


for l in reveal:
    print(l)
