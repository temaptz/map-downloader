import config
import screenshot
import images

source_coordinates = screenshot.get_points_by_bounds([config.coordinates_left_bottom, config.coordinates_right_top])

bottom_left_lon = config.coordinates_left_bottom[0]
bottom_left_lat = config.coordinates_left_bottom[1]
lon_iterator = 0
lat_iterator = 0

while bottom_left_lat < source_coordinates['top_right_lat']:
    while bottom_left_lon < config.coordinates_right_top[0]:
        print('Will take screenshot with bounds', bottom_left_lon, screenshot.get_bounds_by_points(
            bottom_left_lon=bottom_left_lon,
            bottom_left_lat=bottom_left_lat,
            top_right_lon=bottom_left_lon + config.map_delta_lon,
            top_right_lat=bottom_left_lat + config.map_delta_lat
        ))

        correct_bounds = screenshot.take(
            bottom_left_lon=bottom_left_lon,
            bottom_left_lat=bottom_left_lat,
            top_right_lon=bottom_left_lon + config.map_delta_lon,
            top_right_lat=bottom_left_lat + config.map_delta_lat,
            lon_number=lon_iterator,
            lat_number=lat_iterator,
            image_scale_percent=config.result_scale_percent
        )

        # print('Taken screenshot with bounds', correct_bounds)

        lon_iterator += 1
        correct_points = screenshot.get_points_by_bounds(correct_bounds)
        print('SCREEN TAKEN:', bottom_left_lon, (bottom_left_lon + config.map_delta_lon))
        print('DELTA LON:', (bottom_left_lon - correct_points['bottom_left_lon']))
        # bottom_left_lon = correct_points['bottom_left_lon']
        # bottom_left_lat = correct_points['bottom_left_lat']
        bottom_left_lon += config.map_delta_lon

    lon_iterator = 0
    lat_iterator += 1
    bottom_left_lon = config.coordinates_left_bottom[0]
    bottom_left_lat += config.map_delta_lat

images.concat()
