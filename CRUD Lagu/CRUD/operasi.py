from . import database, util
import os

def create_first_data():
    data = database.TEMPLATE.copy()
    data['pk'] = util.init_pk(6)
    data['judul_lagu'] = str(input("Judul Lagu\t: "))
    data['penyanyi'] = str(input("Nama Penyanyi\t: "))
    data['tahun_rilis'] = int(input("Tahun Rilis\t: "))
    data['tgl_ditambahkan'] = util.init_tgl_ditambahkan()
    
    tulis_data = f"{data['pk']}, {data['judul_lagu']}, {data['penyanyi']}, {data['tahun_rilis']}, {data['tgl_ditambahkan']}\n"
    
    try:
        with open(database.DB_NAME, "w", encoding='utf-8') as file:
            file.write(tulis_data)
            print("Data pertama berhasil ditambahkan ke database")
    except:
        print("Data pertama gagal ditambahkan ke database")
        
def read()->str:
    try:
        with open(database.DB_NAME, 'r') as file:
            baca_data = file.readlines()
            return baca_data
    except:
        print("Database gagal dibuka")
        
def write_one_line(no_lagu:int):
    baca_data = read()
    for index, data in enumerate(baca_data):
        data_split = data.split(',')
        nomor = index + 1
        judul = data_split[1]
        penyanyi = data_split[2]
        tahun_rilis = data_split[3]
        
        if index == no_lagu - 1:
            print(f"Data Lagu yang Akan Dihapus\n")
            print(f"Nomor Lagu  \t:  {nomor}")
            print(f"Judul Lagu  \t: {judul}")
            print(f"Penyanyi    \t: {penyanyi}")
            print(f"Tahun Rilis \t: {tahun_rilis}")
    
    print("====================================")
    print("\t   Lagu Update")
    data = database.TEMPLATE.copy()
    data['pk'] = util.init_pk(6)
    data['judul_lagu'] = str(input("Judul Lagu\t: "))
    data['penyanyi'] = str(input("Nama Penyanyi\t: "))
    data['tahun_rilis'] = int(input("Tahun Rilis\t: "))
    data['tgl_ditambahkan'] = util.init_tgl_ditambahkan()
    
    tulis_data = f"{data['pk']}, {data['judul_lagu']}, {data['penyanyi']}, {data['tahun_rilis']}, {data['tgl_ditambahkan']}\n"
    
    print("====================================")
    is_update = str(input("Apakah Yakin Lagu Akan Diupdate? (y/n) : "))
    print("====================================")
    if is_update == 'y' or is_update == 'Y':
        update(no_lagu, tulis_data)
    
def update(no_lagu:int, data:str):
    try:
        with open(database.DB_NAME, "r") as file:
            buffer = 0
            while True:
                data_baca = file.readline()
                if len(data_baca) == 0:
                    break
                elif buffer == no_lagu - 1:
                     with open("dummy.txt", "a", encoding='utf-8') as dummy:
                        dummy.write(data)
                else:
                     with open("dummy.txt", "a", encoding='utf-8') as dummy:
                        dummy.write(data_baca)
                buffer += 1
        os.replace("dummy.txt", database.DB_NAME)
        print("Lagu Berhasil Diupdate")
    except Exception as e:
        print("Lagu Gagal Diupdate")
        print(e)
    print("====================================")

def read_one_line(no_lagu:int):
    baca_data = read()
    for index, data in enumerate(baca_data):
        data_split = data.split(',')
        nomor = index + 1
        judul = data_split[1]
        penyanyi = data_split[2]
        tahun_rilis = data_split[3]
        
        if index == no_lagu - 1:
            print(f"Data Lagu yang Akan Dihapus\n")
            print(f"Nomor Lagu  \t:  {nomor}")
            print(f"Judul Lagu  \t: {judul}")
            print(f"Penyanyi    \t: {penyanyi}")
            print(f"Tahun Rilis \t: {tahun_rilis}")
            
            print("====================================")
            is_delete = str(input("Apakah Yakin Lagu akan Dihapus? (y/n) : "))
            print("====================================")
            if is_delete == "Y" or is_delete == "y":
                delete(no_lagu)

def delete(no_lagu:int):
    try:
        with open(database.DB_NAME, "r") as file:
            buffer = 0
            while True:
                data_baca = file.readline()
                if len(data_baca) == 0:
                    break
                elif buffer == no_lagu - 1:
                    pass 
                else:
                     with open("dummy.txt", "a", encoding='utf-8') as dummy:
                        dummy.write(data_baca)
                buffer += 1
        os.replace("dummy.txt", database.DB_NAME)
        print("Lagu Berhasil Dihapus")
    except Exception as e:
        print("Lagu Gagal Dihapus")
        print(e)
    print("====================================")
        