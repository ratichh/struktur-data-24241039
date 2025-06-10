# Membuat node baru
def buat_node(data):
    return {'data': data, 'prev': None, 'next': None}

# Menambahkan node di akhir
def tambah_node_akhir(head, data):
    new_node = buat_node(data)
    if head is None:
        return new_node
    current = head
    while current['next'] is not None:
        current = current['next']
    current['next'] = new_node
    new_node['prev'] = current
    return head

# Menampilkan isi doubly linked list
def cetak_dll(head):
    current = head
    print('NULL ← ', end='')
    while current is not None:
        print(current['data'], end=' ⇄ ')
        current = current['next']
    print('NULL')

# Menghapus node awal
def hapus_awal(head):
    if head is None:
        print("Linked list kosong.")
        return None
    print(f"Node dengan data '{head['data']}' dihapus dari awal.")
    head = head['next']
    if head is not None:
        head['prev'] = None
    return head

# Menghapus node akhir
def hapus_akhir(head):
    if head is None:
        print("Linked list kosong.")
        return None
    if head['next'] is None:
        print(f"Node dengan data '{head['data']}' dihapus dari akhir.")
        return None
    current = head
    while current['next'] is not None:
        current = current['next']
    print(f"Node dengan data '{current['data']}' dihapus dari akhir.")
    current['prev']['next'] = None
    return head

# Menghapus node berdasarkan nilai data
def hapus_berdasarkan_data(head, data):
    if head is None:
        print("Linked list kosong.")
        return None
    current = head

    # Jika data ada di head
    if current['data'] == data:
        print(f"Node dengan data '{data}' dihapus dari awal.")
        return hapus_awal(head)

    # Cari node dengan data yang cocok
    while current is not None and current['data'] != data:
        current = current['next']

    if current is None:
        print(f"Data '{data}' tidak ditemukan.")
        return head

    # Jika node berada di tengah atau akhir
    print(f"Node dengan data '{data}' dihapus.")
    if current['next'] is not None:
        current['next']['prev'] = current['prev']
    if current['prev'] is not None:
        current['prev']['next'] = current['next']
    return head

# ----------------------------
# Penerapan (Testing Program)
# ----------------------------

# Membuat linked list awal
head = None
for data in [10, 20, 30, 40, 50]:
    head = tambah_node_akhir(head, data)

print("Isi Awal Linked List:")
cetak_dll(head)

# Hapus node awal
head = hapus_awal(head)
cetak_dll(head)

# Hapus node akhir
head = hapus_akhir(head)
cetak_dll(head)

# Hapus berdasarkan data
head = hapus_berdasarkan_data(head, 30)
cetak_dll(head)
