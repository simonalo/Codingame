n = int(input())  # the number of temperatures to analyse
temps = input()  # the n temperatures expressed as integers ranging from -273 to 5526


if n > 0:
    temperatures_list = list(map(int, temps.split()))
    nearest_to_zero = temperatures_list[0]  # We know that we have at least one temperature

    for i in range(1, n):
        if abs(temperatures_list[i]) < abs(nearest_to_zero):
            nearest_to_zero = temperatures_list[i]
        elif abs(temperatures_list[i]) == abs(nearest_to_zero):
            nearest_to_zero = max(temperatures_list[i], nearest_to_zero)

    print(nearest_to_zero)

else:
    print(0)
