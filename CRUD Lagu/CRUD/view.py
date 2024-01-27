from . import operasi, database, util

def read_data():
    baca_data = operasi.read()
    
    nomor = "No."
    judul = "Judul Lagu"
    penyanyi = "Penyanyi"
    tahun_rilis = "Tahun Rilis"
    
    # Header
    print("="*100)
    print(f'{nomor:2} | {judul:35} | {penyanyi:40} | {tahun_rilis:4}')
    print("="*100)
    
    # Data
    for index, data in enumerate(baca_data):
        data_split = data.split(',')
        nomor = index + 1
        judul = data_split[1]
        penyanyi = data_split[2]
        tahun_rilis = data_split[3]
        
        print(f"{nomor:3} | {judul:35} | {penyanyi:40} | {tahun_rilis:4}\n")
        
    # Footer
    print("="*100)

def write_data():
    print("====================================")
    print("MENAMBAHKAN DATA")
    print("====================================")
    data = database.TEMPLATE.copy()
    data['pk'] = util.init_pk(6)
    data['judul_lagu'] = str(input("Judul Lagu\t: "))
    data['penyanyi'] = str(input("Nama Penyanyi\t: "))
    data['tahun_rilis'] = int(input("Tahun Rilis\t: "))
    data['tgl_ditambahkan'] = util.init_tgl_ditambahkan()
    
    tulis_data = f"{data['pk']}, {data['judul_lagu']}, {data['penyanyi']}, {data['tahun_rilis']}, {data['tgl_ditambahkan']}\n"
    
    print("====================================")
    try:
        with open(database.DB_NAME, "a", encoding='utf-8') as file:
            file.write(tulis_data)
            print("Data berhasil ditambahkan ke database")
    except:
        print("Data gagal ditambahkan ke database")
    print("====================================")
    
def update_data():
    print("====================================")
    print("MENGUPDATE DATA")
    read_data()
    
    no_data_update = int(input("Nomor dari Lagu yang Akan Diupdate : "))
    print("====================================")
    operasi.write_one_line(no_data_update)
    
    
def delete_data():
    print("====================================")
    print("MENGHAPUS DATA")
    print("====================================")
    read_data()
    
    no_data_hapus = int(input("Nomor dari Lagu yang Akan Dihapus : "))
    print("====================================")
    operasi.read_one_line(no_data_hapus)