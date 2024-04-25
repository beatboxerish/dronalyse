from dronalyse.loaders.image_metadata_loader import ImageMetadataLoader

# custom variables
image_folders = ["/Users/ishannangia/Desktop/TfW/photogrammetry expt/a2s/",
                 "/Users/ishannangia/Desktop/TfW/photogrammetry expt/mini2/"]
keys_for_metadata = [
    'File:FileName',
    'EXIF:CreateDate',
    'EXIF:GPSLatitude',
    'EXIF:GPSLongitude',
    'XMP:RelativeAltitude',
    'XMP:RelativeAltitude',
    'Composite:FOV',
    'EXIF:FocalLength',
    'EXIF:FocalLengthIn35mmFormat',
]
float_cols = ["EXIF:GPSLatitude", 'EXIF:GPSLongitude', 'XMP:RelativeAltitude',
              'Composite:FOV', 'EXIF:FocalLength', 'EXIF:FocalLengthIn35mmFormat']
dt_cols = ['EXIF:CreateDate']
dt_formats = ['%Y:%m:%d %H:%M:%S']
# ---

iml = ImageMetadataLoader(image_folders)
iml.load_exif_data(metadata_keys=keys_for_metadata)
df_image = iml.get_exif_data_as_df(float_cols=float_cols,
                                   dt_cols=dt_cols,
                                   dt_formats=dt_formats)

# localize dt column
df_image['EXIF:CreateDate'] = df_image['EXIF:CreateDate'].dt.tz_localize("Asia/Kolkata")

# round of cols
df_image['EXIF:GPSLatitude'] = df_image['EXIF:GPSLatitude'].round(6)
df_image['EXIF:GPSLongitude'] = df_image['EXIF:GPSLongitude'].round(6)
df_image.to_csv("../results/image.csv")
