width = int(input())  # the number of cells on the X axis
height = int(input())  # the number of cells on the Y axis

grille = [[False for _ in range(width)] for _ in range(height)]

for i in range(height):
    line = input()  # width characters, each either 0 or .
    for j, chara in enumerate(line):
        if chara == "0":
            grille[i][j] = True

for i in range(height):
    for j, existe in enumerate(grille[i]):
        if existe:
            droite = "-1 -1"
            bas = "-1 -1"
            # On cherche le voisin à droite le plus proche
            for k in range(j + 1, width):
                if grille[i][k]:
                    droite = str(k) + " " + str(i)
                    break

            # On cherche le voisin en bas le plus proche
            for k in range(i + 1, height):
                if grille[k][j]:
                    bas = str(j) + " " + str(k)
                    break

            print(str(j) + " " + str(i) + " " + droite + " " + bas)
