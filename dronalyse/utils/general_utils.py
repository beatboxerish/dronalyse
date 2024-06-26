import pandas as pd
from glob import glob
import os

# TODO: Write all the image formats
# TODO: Centralise this variable
IMAGE_FORMATS = ["JPG"]


def get_select_metadata(metadata, keys_for_metadata):
    """
    Grab selected information from metadata
    :param metadata: exif data from drone image or video
    :param keys_for_metadata: names of keys that you want to grab values of
    :return: smaller metadata files with only selected keys
    """
    select_metadata = dict()
    for key in keys_for_metadata:
        select_metadata[key] = metadata[key]
    return select_metadata


def append_information_to_dict(main_dict, append_info_from_dict):
    """
    Add information append_info_from_dict to the main_dict keys
    :param main_dict: dict you want to update where each value will be a list getting information appended
    from append_info_from_dict
    :param append_info_from_dict: dictionary containing single values you want to append to main_dict values
    :return: updated main_dict
    """
    for k, v in append_info_from_dict.items():
        try:
            main_dict[k].append(v)
        except KeyError:
            main_dict[k] = [v]
    return main_dict


def preprocess_dtype_cols(df, float_cols=None, dt_cols=None, dt_formats=None):
    """
    Preprocess dataframe columns to change their types and more...
    :param df: pandas dataframe
    :param float_cols: list of column names that have to be converted to float columns
    :param dt_cols: list of column names that have to be converted to datetime columns
    :param dt_formats: list of datetime formats for each column
    :return: preprocessed dataframe
    """
    if float_cols:
        try:
            df[float_cols] = df[float_cols].astype(float)
        except:
            print("Error in changing dtype of float columns")
    if dt_cols:
        try:
            for idx, dt_col in enumerate(dt_cols):
                if dt_formats:
                    dt_format = dt_formats[idx]
                else:
                    dt_format = None
                df[dt_col] = pd.to_datetime(df[dt_col], format=dt_format)
        except:
            print("Error in changing dtype of datetime columns")
    return df


def get_images_from_image_folder(image_folder):
    images = []
    for fmt in IMAGE_FORMATS:
        images.extend(
            glob(os.path.join(image_folder, "*." + fmt))
        )
    return images
