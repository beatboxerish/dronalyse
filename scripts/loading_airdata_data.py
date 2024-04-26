from dronalyse.loaders.airdata_data_loader import AirdataDataLoader

airdata_folders = ["/Users/ishannangia/Desktop/TfW/photogrammetry expt/airdata/"]
keys_for_airdata = ["datetime(utc)", "latitude", "longitude",
                   'height_above_takeoff(meters)', 'height_above_ground_at_drone_location(meters)',
                   'height_sonar(meters)', 'isPhoto', 'isVideo']

adl = AirdataDataLoader(airdata_folders)
adl.load_data()
