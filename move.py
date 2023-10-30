import os
import shutil

from_dir="C102_assets-main"
to_dir="C102_assets-main"

list_off_files=os.listdir(from_dir)

for file_name in list_off_files:
    name,extension = os.path.splitext(file_name)
    