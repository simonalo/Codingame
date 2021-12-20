w, h = [int(i) for i in input().split()]
n = int(input())  # maximum number of turns before game over.
x0, y0 = [int(i) for i in input().split()]
min_x = 0
min_y = 0
max_x = w - 1
max_y = h - 1
cent_x = x0
cent_y = y0

# game loop
while True:
    bomb_dir = input()  # the direction of the bombs from batman's current location (U, UR, R, DR, D, DL, L or UL)

    if bomb_dir == "U":
        max_y = cent_y - 1
        cent_y = (cent_y + min_y) // 2
    elif bomb_dir == "UR":
        min_x = cent_x + 1
        max_y = cent_y - 1
        cent_y = (cent_y + min_y) // 2
        cent_x = (cent_x + max_x) // 2 + 1
    elif bomb_dir == "R":
        min_x = cent_x + 1
        cent_x = (cent_x + max_x) // 2 + 1
    elif bomb_dir == "DR":
        min_x = cent_x + 1
        min_y = cent_y + 1
        cent_y = (cent_y + max_y) // 2 + 1
        cent_x = (cent_x + max_x) // 2 + 1
    elif bomb_dir == "D":
        min_y = cent_y + 1
        cent_y = (cent_y + max_y) // 2 + 1
    elif bomb_dir == "DL":
        max_x = cent_x - 1
        min_y = cent_y + 1
        cent_y = (cent_y + max_y) // 2 + 1
        cent_x = (min_x + cent_x) // 2
    elif bomb_dir == "L":
        max_x = cent_x - 1
        cent_x = (min_x + cent_x) // 2
    elif bomb_dir == "UL":
        max_x = cent_x - 1
        max_y = cent_y - 1
        cent_y = (cent_y + min_y) // 2
        cent_x = (min_x + cent_x) // 2

    # the location of the next window Batman should jump to.
    print("{} {}".format(cent_x, cent_y))
