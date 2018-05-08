#!/usr/bin/env python

import os
import sys
import shutil


def py_mover():

    if len(sys.argv) > 2:
        userhome_desktop = os.path.expanduser("~") + "/Desktop/"

        source_dir_path = userhome_desktop + sys.argv[1]
        jpeg_dir_path = userhome_desktop + "JPEG"
        raw_format = str(sys.argv[2]).upper()
        raw_format_path = userhome_desktop + raw_format
    else:
        print("Usage: <source directory name> <RAW format (e.g. NEF, CRW)>\n",
              "Make sure source directory is in the Desktop", file=sys.stderr)
        return 1

    if not os.path.isdir(source_dir_path):
        print("Please enter a valid directory on the Desktop", file=sys.stderr)
        return 1

    # if RAW format folder or JPEG folder does not exists
    # it creates new folders on the Desktop
    if not os.path.exists(raw_format_path):
        print("Creating folder at " + raw_format_path)
        os.mkdir(raw_format_path)
    if not os.path.exists(jpeg_dir_path):
        print("Creating folder at " + jpeg_dir_path)
        os.makedirs(jpeg_dir_path)

    try:
        for file in os.listdir(source_dir_path):
            if file.upper().endswith(raw_format):
                shutil.move(source_dir_path+"/"+file, raw_format_path)
            elif file.upper().endswith("JPG"):
                shutil.move(source_dir_path+"/"+file, jpeg_dir_path)
    except Exception as e:
        print(e, file=sys.stderr)

    print("Done")


if __name__ == '__main__':
    py_mover()

