# Node sebagai elemen linked list
def buat_node(data):
    return {"data": data, "next": None}

# Fungsi-fungsi stack
def push(stack, data, kapasitas):
    if ukuran(stack) >= kapasitas:
        print("Stack sudah penuh!")
        return stack
    node_baru = buat_node(data)
    node_baru["next"] = stack
    stack = node_baru
    tampilkan_stack(stack)
    return stack

def pop(stack):
    if stack is None:
        print("Stack kosong!")
        return stack
    print(f"Elemen {stack['data']} dihapus dari stack.")
    stack = stack["next"]
    tampilkan_stack(stack)
    return stack

def ukuran(stack):
    count = 0
    while stack is not None:
        count += 1
        stack = stack["next"]
    return count

def puncak(stack):
    if stack is None:
        print("Stack kosong!")
    else:
        print(f"Elemen puncak stack: {stack['data']}")

def cek_penuh(stack, kapasitas):
    if ukuran(stack) >= kapasitas:
        print("Stack penuh!")
    else:
        print("Stack belum penuh.")

def tampilkan_stack(stack):
    elemen = []
    while stack is not None:
        elemen.append(stack["data"])
        stack = stack["next"]
    elemen.reverse()
    print("Stack :", elemen)

# Program utama
def main():
    kapasitas = int(input("Tentukan berapa kapasitas stack : "))
    stack = None

    while True:
        print("\nPilih menu berikut ini : ")
        print("1. Menambah isi stack")
        print("2. Menghapus isi stack")
        print("3. Cek Ukuran Stack saat ini")
        print("4. Cek Puncak Stack")
        print("5. Cek Stack Full")
        print("6. Keluar")
        pilihan = input("\nMasukkan pilihan anda : ")

        if pilihan == '1':
            while True:
                data = input("\nMasukkan isi stack : ")
                stack = push(stack, data, kapasitas)
                lanjut = input("\nMenambah isi Stack Pilih [Ya/Tidak] : ")
                if lanjut.lower() != 'ya':
                    break

        elif pilihan == '2':
            stack = pop(stack)

        elif pilihan == '3':
            print(f"Ukuran stack saat ini: {ukuran(stack)}")

        elif pilihan == '4':
            puncak(stack)

        elif pilihan == '5':
            cek_penuh(stack, kapasitas)

        elif pilihan == '6':
            print("Keluar dari program.")
            break

        else:
            print("Pilihan tidak valid!")

# Jalankan program
if __name__ == "__main__":
    main()