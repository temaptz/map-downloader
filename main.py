import functions

# Точка А - слева внизу В - справа вверху
coordinates_left_bottom = [61.806860, 34.316294]
coordinates_right_top = [61.816007, 34.335585]

# Шаг
deltaLon = 0.0008122259952116906
deltaLat = 0.0027465820312428946

bottom_left_lon = coordinates_left_bottom[0]
bottom_left_lat = coordinates_left_bottom[1]
lonIterator = 0
latIterator = 0

while bottom_left_lat < coordinates_right_top[1]:
    while bottom_left_lon < coordinates_right_top[0]:
        functions.take_screenshot(
            bottom_left_lon=str(bottom_left_lon),
            bottom_left_lat=str(bottom_left_lat),
            top_right_lon=str(bottom_left_lon + deltaLon),
            top_right_lat=str(bottom_left_lat + deltaLat),
            lon_number=lonIterator,
            lat_number=latIterator
        )
        lonIterator += 1
        bottom_left_lon += deltaLon

    latIterator += 1
    bottom_left_lon = coordinates_left_bottom[0]
    bottom_left_lat += deltaLat
