power_lists = []

nb_horses = int(input())
for i in range(nb_horses):
    pi = int(input())
    power_lists.append(pi)

power_lists = sorted(power_lists)
diff_of_power = [power_lists[i + 1] - power_lists[i] for i in range(nb_horses) if i + 1 < nb_horses]

print(min(diff_of_power))
