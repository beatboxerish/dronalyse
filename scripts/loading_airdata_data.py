from dronalyse.loaders.airdata_data_loader import AirdataDataLoader

airdata_folders = ["/Users/ishannangia/Desktop/TfW/photogrammetry expt/airdata/"]
keys_for_airdata = ["datetime(utc)", "latitude", "longitude",
                   'height_above_takeoff(meters)', 'height_above_ground_at_drone_location(meters)',
                   'height_sonar(meters)', 'isPhoto', 'isVideo']

float_cols = ['latitude', 'longitude', 'height_above_takeoff(meters)',
              'height_above_ground_at_drone_location(meters)', 'height_sonar(meters)', 'isPhoto']
dt_cols = ["datetime(utc)"]
dt_formats = ['%Y-%m-%d %H:%M:%S']

adl = AirdataDataLoader(airdata_folders)
adl.load_data()
adl.preprocess_cols(float_cols, dt_cols, dt_formats)
