import os
import sys


source_dir_path = None
jpeg_dir_path = None
raw_format = None
raw_format_path = None

if len(sys.argv) > 2:
    userhome_desktop = os.path.expanduser("~") + "/Desktop/"
    source_dir_path = userhome_desktop + sys.argv[1]

    jpeg_dir_path = userhome_desktop + "JPEG"

    raw_format = sys.argv[2]
    raw_format_path = userhome_desktop + raw_format

else:
    print("Usage: <source directory name> <RAW format (e.g. NEF, CLS)>\n",
          "Make sure source directory is in the Desktop", file=sys.stderr)
    sys.exit(1)


if not os.path.isdir(source_dir_path):
    print("Please enter a valid directory on the Desktop", file=sys.stderr)
    sys.exit(1)




if not os.path.exists(raw_format_path):
    os.mkdir(raw_format_path)
if not os.path.exists(jpeg_dir_path):
    os.makedirs(jpeg_dir_path)



