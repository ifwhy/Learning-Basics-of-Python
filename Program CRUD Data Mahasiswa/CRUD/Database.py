from . import Operasi
DB_NAME = "db.txt"
TEMPLATE = {
    'pk':'XXXXXX',
    'nama':' '*255,
    'nim':' '*10,
    'prodi':' '*255,
    'fakultas':''*255,
    'date_add':'yyyy-mm-dd'
}

def init_console():
    try:
        with open(DB_NAME, "r") as file:
            print("Database berhasil ditemukan")
            print("Init done")
    except:
        print("Database tidak ditemukan")
        Operasi.create_first_data()
        