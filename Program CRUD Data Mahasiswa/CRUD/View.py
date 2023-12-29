from . import Operasi, Util
def read_data():
    data_str = Operasi.read()
    index = "No."
    nama = "Nama Lengkap"
    nim = "NIM"
    prodi = "Program Studi"
    fakultas = "Fakultas"
    
    # Header
    print("="*100)
    print(f"{index:4} | {nama:40} | {nim:10} | {prodi:25} | {fakultas:20}")
    print("="*100)
    
    # Data
    for index, data in enumerate(data_str):
        data_split = data.split(", ")
        nama = data_split[1]
        nim = data_split[2]
        prodi = data_split[3]
        fakultas = data_split[4]
        
        print(f"{index+1:4} | {nama:40} | {nim:10} | {prodi:25} | {fakultas:20}")
    
    # Footer
    print("="*100)

def write_data():
    pk = Util.random_pk(6)
    nama =     str(input("Nama Lengkap     : "))
    nim =      str(input("NIM              : "))
    prodi =    str(input("Program Studi    : "))
    fakultas = str(input("Fakultas         : "))
    date_add = Util.get_current_time()
    
    data = f"{pk}, {nama}, {nim}, {prodi}, {fakultas}, {date_add}\n"
    Operasi.writes(data)

def delete_data():
    read_data()
    no_buku = int(input(("No. Mahasiswa yang akan dihapus : ")))
    print("="*100)
    Operasi.read_one_line_for_delete(no_buku)
    print("="*100)

def update_data():
    read_data()
    no_buku = int(input(("No. Mahasiswa yang akan diupdate : ")))
    print("="*100)
    Operasi.write_one_line_for_update(no_buku)
    print("="*100)