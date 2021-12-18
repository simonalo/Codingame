n = int(input())
last = 1
total_sum = 1

for i in range(1, n, 2):
    for j in range(4):
        if n % 2 == 0 and i == n - 1 and j == 3:
            continue

        total_sum += (n - i) + last
        last = (n - i) + last

print(total_sum)
