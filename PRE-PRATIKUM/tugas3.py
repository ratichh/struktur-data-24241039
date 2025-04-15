def fibonacci(n):
    a, b = 1, 1
    result = []
    for _ in range(n):
        result.append(a)
        a, b = b, a + b
    return result

# Input dari pengguna
jumlah_deret = int(input("Masukkan jumlah deret Fibonacci: "))
deret = fibonacci(jumlah_deret)

# Tampilkan hasil
print(", ".join(map(str, deret)))