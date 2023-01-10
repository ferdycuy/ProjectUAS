from Model.Daftar_nilai import cari_data,ubah_data,hapus_data
from View.view_nilai import cetak,cari
from View.input_nilai import tambah

print("|==================== PROGRAM INPUT DATA MAHASISWA ========================|")
print("|==========================================================================|")
print("(1)Tambah, (2)Ubah, (3)Hapus, (4)Cari, (5)Lihat, (6)Keluar: ")
while True:

    c = input("\nPilih Opsi: ")

    # KELUAR PROGRAM
    if c.lower() == '6':
        print("Terimkasi:)")
        ext = input("\nPress ENTER to exit")

        if ext == '':
            break
        else:
            break

    # TAMPILKAN LIST DATA
    elif c.lower() == '5':
        cetak()

    # MENAMBAH DATA
    elif c.lower() == '1':
        tambah()

    # EDIT DATA
    elif c.lower() == '2':
        ubah_data()

    # MENCARI DATA
    elif c.lower() == '4':
        cari_data()
        cari()

    # HAPUS DATA
    elif c.lower() == '3':
        hapus_data()

    else:
        print("pilih opsi sesuai diatas")
