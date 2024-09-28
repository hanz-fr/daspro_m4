# Nama  : Raihan Fauzi Rakhman
# NIM   : 2403872
# Kelas : RPL 1C

num = [10,20,20,30,40,50,50,60]

# Buat menjadi dictionary karena dictionary tidak
# dapat mengandung item yang duplikat
num = list(dict.fromkeys(num))
print(num)