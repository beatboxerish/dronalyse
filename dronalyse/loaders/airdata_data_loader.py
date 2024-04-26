import pandas as pd
from dronalyse.utils.airdata_utils import get_airdata_files_from_folder


class AirdataDataLoader:

    def __init__(self, airdata_folders):
        """Initializes AirdataDataLoader class to load and play with airdata-based data"""
        self.airdata_folders = airdata_folders  # folders containing images
        self.all_airdata_files = []
        self.all_airdata_df = None

        for airdata_folder in airdata_folders:
            list_of_files = get_airdata_files_from_folder(airdata_folder)
            self.all_airdata_files.extend(list_of_files)

    # TODO: standardise how different classes store data. Should be the same type of object.
    def load_data(self, airdata_keys=None):
        self.all_airdata_df = None
        # read all files one by one and get all data together
        for file_name in self.all_airdata_files:
            for airdata_file in self.all_airdata_files:
                current_df = pd.read_csv(airdata_file)
                self.all_airdata_df = pd.concat([self.all_airdata_df, current_df], axis=0)
            self.all_airdata_df.reset_index(drop=True, inplace=True)
            if airdata_keys:
                self.all_airdata_df = self.all_airdata_df[airdata_keys]
