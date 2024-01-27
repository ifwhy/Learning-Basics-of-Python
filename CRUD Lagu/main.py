import CRUD as CRUD
import os

if __name__ == "__main__":
    CRUD.init_console()
    while(True):
        match os.name:
            case "posix": os.system("clear")
            case "nt": os.system("cls")
            
        print("         PROGRAM CRUD LAGU")
        print("      BY : IVAN WAHYU NUGROHO")
            
        print("====================================")
        print("1. Read Data")
        print("2. Create Data")
        print("3. Update Data")
        print("4. Delete Data")
        print("====================================")
        user_choice = int(input("Pilih Menu : "))
        
        match user_choice:
            case 1: CRUD.read_data()
            case 2: CRUD.write_data()
            case 3: CRUD.update_data()
            case 4: CRUD.delete_data()
        
        is_done = str(input("Apakah Selesai? (y/n) : "))
        if is_done == "Y" or is_done == "y":
            break