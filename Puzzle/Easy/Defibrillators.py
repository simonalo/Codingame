import math

lon = float(input().replace(',', '.'))
lat = float(input().replace(',', '.'))
n = int(input())

dist_min = -1
nom = None

for i in range(n):
    _, nom_tmp, _, _, lon_tmp_str, lat_tmp_str = input().split(';')
    lon_tmp = float(lon_tmp_str.replace(',', '.'))
    lat_tmp = float(lat_tmp_str.replace(',', '.'))
    x = (lon - lon_tmp) * math.cos((lat + lat_tmp) / 2)
    y = (lat - lat_tmp)
    dist_tmp = math.sqrt(x ** 2 + y ** 2) * 6371

    if nom is None or dist_min > dist_tmp:
        nom = nom_tmp
        dist_min = dist_tmp

print(nom)
