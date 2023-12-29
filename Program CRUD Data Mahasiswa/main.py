import CRUD as CRUD
import os 

if __name__ == "__main__":
    CRUD.init_console()
    
    while True:
        sistem_operasi = os.name 
        match os.name:
            case "posix": os.system("clear")
            case "nt": os.system("cls")
        print("\t\t\tSELAMAT DATANG DI PROGRAM CRUD DATA MAHASISWA")
        print("\t\t\t\t  UNIVERSITAS SEBELAS MARET")
        print("="*100)
        print("1. Read Data")
        print("2. Create Data")
        print("3. Update Data")
        print("4. Delete Data")
        print("="*100)
        user_option = int(input("Masukkan Pilihan : "))
        
        match user_option:
            case 1: CRUD.read_data()
            case 2: CRUD.write_data()
            case 3: CRUD.update_data()
            case 4: CRUD.delete_data()
        
        is_done = str(input("Apakah Selesai? (y/n) : "))
        if is_done == "y" or is_done == "Y":
            break