import io
import os
from pathlib import Path

def dock_vol():
    file_path = Path("./data/dock_vol.txt")

    print(f"current_dir: {os.getcwd()}") 
    print(f"subsequent_dir: {os.listdir(os.getcwd())}")   

    number = input("Do you want to continue: ")

    if not file_path.exists():
        print("file doesn't exists")
        
        with file_path.open("x") as f:
            f.write(str(1))
    else:
        with file_path.open("rb+") as f:
            data = f.read()
            new_data = int(data) + 1
            print(data)
            f.seek(0)
            f.write(str(new_data).encode())
        print(f"file exists and updated {new_data}")

    f.close()

if __name__ == '__main__':
    dock_vol()