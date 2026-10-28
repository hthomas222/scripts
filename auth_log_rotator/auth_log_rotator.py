import os
import shutil
import sys


def log_rotate(ui):
    size = os.path.getsize(ui)
    if size >= 1:
        new = ui + ".old"
        shutil.copy(ui, new)
        with open(ui, "w") as file:
            file.write("Log rotated successfully.")
        print("Log rotated successfully.")
    else:
        print("File is less than 1 megabyte.")
        sys.exit()


if __name__ == "__main__":
    ui = input("Enter log to test: ")
    log_rotate(ui)