def tambah():
    from Model.Daftar_nilai import tambah_data
    while (True):
        print("MASUKKAN DATA MAHASISWA")
        nama = input("NAMA   : ")
        if nama == '':
            print('Nama tidak boleh kosong')
        else:
            break
    while (True):
        try:
            nim = int(input("NIM    : "))
            if nim == '':
                print('Masukan Nim dengan Angka')
        except ValueError:
            print('Masukan Nim dengan Angka')
        else:
            break
    while (True):
        try:
            tugas = int(input("TUGAS  : "))
            if tugas == '':
                print('Masukan TUGAS dengan Angka')
        except ValueError:
            print('Masukan TUGAS dengan Angka')
        else:
            break
    while (True):
        try:
            uts = int(input("UTS    : "))
            if uts == '':
                print('Masukan UTS dengan Angka')
        except ValueError:
            print('Masukan UTS dengan Angka')
        else:
            break
    while (True):
        try:
            uas = int(input("UAS    : "))
            if uas == '':
                print('Masukan UAS dengan Angka')
        except ValueError:
            print('Masukan UAS dengan Angka')
        else:
            break
    tambah_data(nama, nim, tugas, uts, uas)
    print("(1)Tambah, (2)Ubah, (3)Hapus, (4)Cari, (5)Lihat, (6)Keluar: ")

