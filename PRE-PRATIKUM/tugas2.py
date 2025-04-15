# Program untuk menampilkan deret bilangan genap

# Input jumlah deret
jumlah = int(input("Jumlah deret: "))

# Inisialisasi deret genap
deret_genap = []

# Loop untuk menghasilkan deret genap
for i in range(1, jumlah + 1):
    deret_genap.append(i * 2)

# Tampilkan hasil
print("Output:", ",".join(map(str, deret_genap)))