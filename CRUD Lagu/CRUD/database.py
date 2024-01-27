from .operasi import create_first_data

DB_NAME = "db.txt"
TEMPLATE = {
    'pk':"XXXXXX",
    'judul_lagu':" "*255,
    'penyanyi':" "*255,
    'tahun_rilis':"yyyy",
    'tgl_ditambahkan':"yyyy-mm-dd"
}

def init_console():
    try:
        with open(DB_NAME, "r") as file:
            print("Database ditemukan")
            print("Init done")
    except:
        print("Database tidak ditemukan, dibuat database baru")
        create_first_data()