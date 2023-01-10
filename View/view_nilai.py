from Model.Daftar_nilai import data

# mencetak hasil nilai
def cetak():
    print("|========================= DAFTAR DATA MAHASISWA =========================|")
    print("|=========================================================================|")
    print("| NO |      NAMA       |       NIM        | TUGAS |  UTS  |  UAS  | AKHIR |")
    print("|=========================================================================|")
    no = 1
    for tabel in data.values():
        print("|{0:3} | {1:15} | {2:16} | {3:5} | {4:5} | {5:5} | {6:5} |".format(no, tabel[0], tabel[1], tabel[2], tabel[3],  tabel[4],tabel[5]))
        no += 1
        print("|=========================================================================|")

# mencetak hasil pencarian
def cari():
    nama = input("Masukkan nama\t:")
    if nama in data.keys():
        print("\n|===================================================================|")
        print("|      NAMA       |       NIM        | TUGAS |  UTS  |  UAS  | AKHIR |")
        print("|===================================================================|")
        print("| {0:15} | {1:16} | {2:5} | {3:5} | {4:5} | {5:5} |"
              .format(nama, data[nama][1], data[nama][2],data[nama][3], data[nama][4], data[nama][5]))
        print("|===================================================================|")
        print("\n(1)Tambah, (2)Ubah, (3)Hapus, (4)Cari, (5)Lihat, (6)Keluar: ")
    else:
        print("===========================")
        print("| Data {} tidak ditemukan |".format(nama))
        print("===========================")

