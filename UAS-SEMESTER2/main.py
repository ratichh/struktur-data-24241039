# data belanja custemer

#input data customer
Nama = input ("masukan nama custemer :")
tanggal = input ("masukan tanggal belanja(YYYY-MM-DD):")

# input jumlah jenis barang
jumlah_barang = int(input("Berapa jenis barang yang dibeli:"))

#  Buat list kosong untuk menampung semua barang
daftar_barang = []

#  Minta data tiap barang
for i in range(jumlah_barang):
    print(f"\nMasukkan data barang ke-{i+1}:")
    
    # Minta nama barang
    nama_barang = input("  Nama barang       : ")
    
    # Minta harga satuan barang (angka desimal)
    harga_satuan = float(input("  Harga satuan (Rp) : "))
    
    # Minta jumlah barang (qty)
    jumlah = int(input("  Jumlah barang     : "))

    # Hitung subtotal (harga * jumlah)
    subtotal = harga_satuan * jumlah
    
    # Simpan data barang dalam dictionary (kamus)
    barang = {
        "nama": nama_barang,
        "harga": harga_satuan,
        "qty": jumlah,
        "subtotal": subtotal
    }

     # Tambahkan dictionary barang ke dalam list
    daftar_barang.append(barang)

  # cetak hasil belanja
print("\n========= DATA BELANJA =========")
print("Nama Customer :", Nama)
print("Tanggal       :", tanggal)
print("-------------------------------")
total_bayar = 0

# 5. Tampilkan semua barang
for barang in daftar_barang:
    print(f"{barang['nama']} - {barang['qty']} x {barang['harga']} = Rp {barang['subtotal']}")
    total_bayar += barang["subtotal"]

# 6. Tampilkan total bayar
print("-----------------------------")
print("Total Bayar: Rp", total_bayar)
print("=============================")

