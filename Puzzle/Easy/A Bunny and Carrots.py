# Find the number of covered side for mat[i][j].
def num_of_neighbour(mat, i, j):
    count = 0

    # UP
    if i > 0 and mat[i - 1][j]:
        count += 1

    # LEFT
    if j > 0 and mat[i][j - 1]:
        count += 1

    # DOWN
    if i < len(mat) - 1 and mat[i + 1][j]:
        count += 1

    # RIGHT
    if j < len(mat[0]) - 1 and mat[i][j + 1]:
        count += 1

    return count


# Returns sum of perimeter of shapes formed with 1s
def find_perimeter(mat):
    perimeter = 0

    # Traversing the matrix and finding ones to
    # calculate their contribution.
    for i in range(0, len(mat)):
        for j in range(0, len(mat[0])):
            if mat[i][j]:
                perimeter += (4 - num_of_neighbour(mat, i, j))

    return perimeter


def main():
    m, n = [int(i) for i in input().split()]

    perimeters = []
    carrots = [[1 for _ in range(n)] for _ in range(m)]
    t = int(input())

    for i in input().split():
        choices = int(i) - 1
        for j in range(m - 1, -1, -1):
            if carrots[j][choices] == 1:
                carrots[j][choices] = 0
                break
        perimeters.append(find_perimeter(carrots))
    for i in range(t):
        print(perimeters[i])


main()
