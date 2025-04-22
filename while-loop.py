angka = int(input('Masukkan angka ganjil: '))
for i in range(1, angka + 1, 2):
    spasi = ' ' * ((angka - i) // 2)
    print(spasi + '*' * i)