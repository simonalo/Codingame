# light_x: the X position of the light of power
# light_y: the Y position of the light of power
# initial_tx: Thor's starting X position
# initial_ty: Thor's starting Y position

light_x, light_y, initial_tx, initial_ty = [int(i) for i in input().split()]

thorX = initial_tx
thorY = initial_ty

while True:
    remaining_turns = int(input())  # The remaining amount of turns Thor can move. Do not remove this line.
    direction = ""

    if thorY > light_y:
        direction += "N"
        thorY -= 1
    elif thorY < light_y:
        direction += "S"
        thorY += 1

    if thorX > light_x:
        direction += "W"
        thorX -= 1
    elif thorX < light_x:
        direction += "E"
        thorX += 1

    print(direction)
