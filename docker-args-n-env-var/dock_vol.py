import io
import os
from pathlib import Path
import argparse

def dock_vol(val, arg_val):
    file_path = Path("./data/dock_vol.txt")

    print(f"current_dir: {os.getcwd()}") 
    print(f"subsequent_dir: {os.listdir(os.getcwd())}")   

    number = input("Do you want to continue: ")

    if not file_path.exists():
        print("file doesn't exists")
        
        with file_path.open("w") as f:
            f.write(str(val+arg_val).encode())
        print(f"file created and written with {val+arg_val}")
    else:
        with file_path.open("rb+") as f:
            data = f.read()
            new_data = int(data) + arg_val + val
            print(data)
            f.seek(0)
            f.write(str(new_data).encode())
        print(f"file created and written with {val+arg_val}")

    f.close()

if __name__ == '__main__':
    val = int(os.environ.get("docker_val"))
    parser = argparse.ArgumentParser()
    parser.add_argument("arg_val", type=int, default=1)
    parser.add_argument("build_time_arg", type=int, default=1)
    args = parser.parse_args()
    dock_vol(val, args.arg_val)