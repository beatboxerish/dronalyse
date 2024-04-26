from glob import glob
import os

# TODO: there might other formats too. Check and update.
AIRDATA_FILE_FORMATS = ["csv"]


def get_airdata_files_from_folder(folder):
    airdata_files = []
    for fmt in AIRDATA_FILE_FORMATS:
        airdata_files.extend(
            glob(os.path.join(folder, "*." + fmt))
        )
    return airdata_files
