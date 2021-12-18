while True:
    max_height = -1
    pos_max = 0

    # For each mountain we check if it is higher than the previous one
    for i in range(8):
        mountain_h = int(input())  # represents the height of one mountain.
        if mountain_h > max_height:
            max_height = mountain_h
            pos_max = i

    # The index of the mountain to fire on.
    print(pos_max)
