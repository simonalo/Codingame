l = int(input())
h = int(input())
t = input()


def make_board(height, width):
    """Make a board of height * width to print letters."""
    board = []
    for _ in range(height):
        board.append([""] * width)

    return board


def imprimer(text):
    """Display the letters of the text in ASCII art."""
    # Make a board with the letters in ascii art (there are 27 different symbols)
    letters_ascii = make_board(h, 27)

    for i in range(h):
        row = input()
        for j in range(27):
            letters_ascii[i][j] = row[j * l: (j + 1) * l]

    text = text.upper()
    n = len(text)
    art = make_board(h, n)  # Board to store our text in ascii art
    for i in range(n):
        code = ord(text[i])
        if code < 65 or code > 90:
            for j in range(h):
                art[j][i] = letters_ascii[j][26]
        else:
            for j in range(h):
                art[j][i] = letters_ascii[j][code % 65]

    # Display board
    for i in range(h):
        temp = ""
        for j in range(n):
            temp += art[i][j]
        print(temp)


imprimer(t)
