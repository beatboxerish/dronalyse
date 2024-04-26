from dronalyse.utils.airdata_utils import get_airdata_files_from_folder


class AirdataDataLoader:

    def __init__(self, airdata_folders):
        """Initializes AirdataDataLoader class to load and play with airdata-based data"""
        self.airdata_folders = airdata_folders  # folders containing images
        self.all_airdata_files = []

        for airdata_folder in airdata_folders:
            list_of_files = get_airdata_files_from_folder(airdata_folder)
            self.all_airdata_files.extend(list_of_files)
