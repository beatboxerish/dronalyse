from exiftool import ExifToolHelper
import pandas as pd
from dronalyse.utils.general_utils import (get_select_metadata, append_information_to_dict,
                                           get_images_from_image_folder, preprocess_dtype_cols)


# TODO: allow using of single file instead of folders
# TODO: allow using of multiple file names instead of folders
class ImageMetadataLoader:

    def __init__(self, image_folders):
        """Initializes ImageLoader class to load and play with image metadata"""
        self.image_folders = image_folders  # folders containing images
        self.all_images = []
        self.all_images_dict = dict()

        for image_folder in image_folders:
            images = get_images_from_image_folder(image_folder)
            self.all_images.extend(images)

    def load_exif_data(self, metadata_keys=None):
        # read all images one by one and get all exif data
        self.all_images_dict = dict()

        for image_name in self.all_images:
            with ExifToolHelper() as et:
                metadata = et.get_metadata(image_name)[0]
                if metadata_keys:
                    metadata = get_select_metadata(metadata, metadata_keys)
                append_information_to_dict(self.all_images_dict, metadata)

    def get_exif_data_as_df(self, float_cols=None, dt_cols=None, dt_formats=None):
        df_image = pd.DataFrame(self.all_images_dict)
        if float_cols:
            df_image = preprocess_dtype_cols(df_image, float_cols)
        if dt_cols:
            df_image = preprocess_dtype_cols(df_image, dt_cols=dt_cols, dt_formats=dt_formats)
        return df_image


