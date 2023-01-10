data= { }
def tambah_data (nama, nim , tugas, uts, uas) :
    print("DATA TELAH TERSIMPAN")
    nilaiakhir = round((float(tugas) * 0.3) + (float(uts) * 0.35) + (float(uas) * 0.35), 2)
    data[nama] = nama, nim, tugas, uts, uas,nilaiakhir

def ubah_data() :
    print("MENGUBAH DATA MAHASISWA")
    print("======================")
    nama = input("Masukan nama yang ingin diubah : ")
    if nama in data.keys():
        del data[nama]
        print("\n==========Inputkan Data Baru===========")
        from View.input_nilai import tambah
        tambah()
    else :
        print("======================")
        print("| Data {} tidak ditemukan |".format(nama))
        print("======================")
        print("(1)Tambah, (2)Ubah, (3)Hapus, (4)Cari, (5)Lihat, (6)Keluar: ")

def cari_data():
    print("MENCARI DATA MAHASISWA")
    print("======================")
    print("Masukan nama yang di cari : ")


def hapus_data():
    print("MENGHAPUS DATA MAHASISWA")
    print("======================")
    nama = input("Masukan nama yang ingin dihapus : ")
    if nama in data.keys():
        del data[nama]
        print('Nama Berhasil dihapus')
        return True
    else:
        print("===========================")
        print("| Data {} tidak ditemukan |".format(nama))
        print("===========================")
        print("(1)Tambah, (2)Ubah, (3)Hapus, (4)Cari, (5)Lihat, (6)Keluar: ")
        return False
