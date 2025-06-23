# Membuat Stack
stack = []

# operasi Push (menambah elemen pada stack)
stack.append('A')
stack.append('B')
stack.append('C')
print ("Stack : ", stack)

# cek apakah stack kosong
if not bool(stack):
    print("Stack Kosong ")
else :
    print("Stack tidak kosong! ", stack)

# cek puncak stack
if not bool(stack):
    print("Stack Kosong!")
else:
    print("stack : ", stack)
    print("Top/Peek : ", stack[-1])

# operasi pop (menghapus, prinsip LIFO)
if len(stack) != 0:
    print("Pop : ", stack.pop())
    print("Stack saat ini : ", stack)
else :
    print("Stack Kosong!")

# operasi size (untuk mengetahui jumlah elemen dalam stack)
print("jumlah elemen dalam stack : ", len(stack))