from . import Database, Util
import os

def create_first_data():
    nama  = str(input("Nama   : "))
    NIM  =  str(input("NIM    : "))
    prodi = str(input("Prodi  : "))
    fakultas = str(input("Fakultas  : "))
    
    data = Database.TEMPLATE.copy()
    data['pk'] = Util.random_pk(6)
    data['nama'] = nama
    data['nim'] = NIM
    data['prodi'] = prodi 
    data['fakultas'] = fakultas 
    data['date_add'] = Util.get_current_time()
    
    tulis = f"{data['pk']}, {data['nama']}, {data['nim']}, {data['prodi']}, {data['fakultas']},{data['date_add']}\n"
    
    try:
        with open(Database.DB_NAME, 'w', encoding='utf-8') as file:
            file.write(tulis)
            print("Data berhasil diinput ke database")
    except:
        print("Database Tidak Berhasil Diinisiasi")

def read():
    try:
        with open(Database.DB_NAME, "r") as file:
            data = file.readlines()
            return data
    except:
        print("Data gagal dibaca dari database")

def read_one_line_for_delete(no_buku:int)->str:
    data_str = read()
    for index, data in enumerate(data_str):
        data_split = data.split(", ")
        nama = data_split[1]
        nim = data_split[2]
        prodi = data_split[3]
        fakultas = data_split[4]
        
        if index == no_buku-1:
            print("Data Mahasiswa   : (Akan Dihapus)")
            print(f"Nama Lengkap     : {nama}")
            print(f"NIM              : {nim}")
            print(f"Program Studi    : {prodi}")
            print(f"Fakultas         : {fakultas}")
            print("="*100)
            
            is_delete = str(input("Apakah anda yakin ingin menghapus data ini? (y/n) : "))
            
            if is_delete == "y" or is_delete == "Y":
                delete(no_buku)
            else:
                print("Data Gagal dihapus")
            break            
    else:
        print("Data tidak ditemukan")

def writes(data:str):
    try:
        with open(Database.DB_NAME, 'a', encoding='utf-8') as file:
            file.write(data)
            print("="*100)
            print("Data berhasil ditulis ke database")
            print("="*100)
    except:
        print("Data gagal ditulis ke database")

def delete(no_buku):
    try:
        with open(Database.DB_NAME, "r") as file:
            buffer = 0
            while True:
                content = file.readline()
                if len(content) == 0:
                    break 
                elif buffer == no_buku-1:
                    pass 
                else:
                    with open("dummy.txt", 'a', encoding='utf-8') as dummy:
                        dummy.write(content)
                buffer += 1
        os.replace("dummy.txt", Database.DB_NAME)
        print("Data berhasil dihapus")
    except Exception as e:
        print("Data gagal dihapus dari database")
        print(e)
        
def write_one_line_for_update(no_buku:int)->str:
    data_str = read()
    for index, data in enumerate(data_str):
        data_split = data.split(", ")
        nama = data_split[1]
        nim = data_split[2]
        prodi = data_split[3]
        fakultas = data_split[4]
        
        if index == no_buku-1:
            pk = Util.random_pk(6)
            print("Data Mahasiswa   : (Akan Diupdate)")
            nama =     str(input("Nama Lengkap     : "))
            nim =      str(input("NIM              : "))
            prodi =    str(input("Program Studi    : "))
            fakultas = str(input("Fakultas         : "))
            date_add = Util.get_current_time()
            print("="*100)
            
            data = f"{pk}, {nama}, {nim}, {prodi}, {fakultas}, {date_add}\n"
            is_update = str(input("Apakah anda yakin ingin mengupdate data ini? (y/n) : "))
            
            if is_update == "y" or is_update == "Y":
                update(no_buku, data)
                print("Data berhasil diupdate")
            else:
                print("Data Gagal dihapus")
            break            
    else:
        print("Data tidak ditemukan")

def update(no_buku:int, data:str)->str:
    try:
        with open(Database.DB_NAME, "r") as file:
            buffer = 0
            while True:
                content = file.readline()
                if len(content) == 0:
                    break
                elif buffer == no_buku-1:
                    with open("dummy.txt", 'a', encoding='utf-8') as dummy:
                        dummy.write(data)
                else:
                    with open("dummy.txt", 'a', encoding='utf-8') as dummy:
                        dummy.write(content)
                buffer += 1
        os.replace("dummy.txt", Database.DB_NAME)
    except:
        print("Data gagal diupdate ke database")
    