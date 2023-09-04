import sys
import os
from datetime import datetime


def create_dir() -> str:
    if "-f" in sys.argv:
        path = os.path.join(
            str(sys.argv[sys.argv.index("-d") + 1 : sys.argv.index("-f")])
        )
        if not os.path.exists(path):
            os.makedirs(path)
        return path
    path = os.path.join(str(sys.argv[sys.argv.index("-d") + 1 :]))
    if not os.path.exists(path):
        os.makedirs(path)
    return path


def write_proccess(file_to_write: str) -> None:
    with open(file_to_write, "a") as active_file:
        active_file.write(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        while True:
            write_line = input("Enter content line: ")
            if write_line == "stop":
                return
            active_file.write(write_line + "\n")


def write_file(path_file: str) -> None:
    if not os.path.exists(path_file):
        with open(path_file, "w"):
            write_proccess(path_file)
            return
    with open(path_file, "a") as f:
        f.write("\n")
    write_proccess(path_file)


def make_writings() -> None:
    if "-d" in sys.argv and "-f" in sys.argv:
        path = create_dir()
        write_file(f"{path}/{sys.argv[-1]}")
        return
    if "-d" in sys.argv:
        create_dir()
        return
    if "-f" in sys.argv:
        write_file(sys.argv[-1])
        return


if __name__ == "__main__":
    make_writings()
