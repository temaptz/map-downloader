import screenshot
import images

# Точки между которыми нужно просматривать карту
coordinates_left_bottom = [61.800829, 34.297632]
coordinates_right_top = [61.820178, 34.362048]

# Шаг
delta_lon = 0.0009 # 0.0008121323331948815
delta_lat = 0.003 # 0.0027465820312428946

source_coordinates = screenshot.get_points_by_bounds([coordinates_left_bottom, coordinates_right_top])

bottom_left_lon = coordinates_left_bottom[0]
bottom_left_lat = coordinates_left_bottom[1]
lon_iterator = 0
lat_iterator = 0

# while bottom_left_lat < source_coordinates['top_right_lat']:
#     while bottom_left_lon < coordinates_right_top[0]:
#         print('Will take screenshot with bounds', bottom_left_lon, screenshot.get_bounds_by_points(
#             bottom_left_lon=bottom_left_lon,
#             bottom_left_lat=bottom_left_lat,
#             top_right_lon=bottom_left_lon + delta_lon,
#             top_right_lat=bottom_left_lat + delta_lat
#         ))
#
#         correct_bounds = screenshot.take(
#             bottom_left_lon=bottom_left_lon,
#             bottom_left_lat=bottom_left_lat,
#             top_right_lon=bottom_left_lon + delta_lon,
#             top_right_lat=bottom_left_lat + delta_lat,
#             lon_number=lon_iterator,
#             lat_number=lat_iterator
#         )
#
#         # print('Taken screenshot with bounds', correct_bounds)
#
#         lon_iterator += 1
#         correct_points = screenshot.get_points_by_bounds(correct_bounds)
#         print('SCREEN TAKEN:', bottom_left_lon, (bottom_left_lon + delta_lon))
#         print('DELTA LON:', (bottom_left_lon - correct_points['bottom_left_lon']))
#         # bottom_left_lon = correct_points['bottom_left_lon']
#         # bottom_left_lat = correct_points['bottom_left_lat']
#         bottom_left_lon += delta_lon
#
#     lon_iterator = 0
#     lat_iterator += 1
#     bottom_left_lon = coordinates_left_bottom[0]
#     bottom_left_lat += delta_lat

images.concat(10)
