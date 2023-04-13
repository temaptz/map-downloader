import os
import pathlib
import re
import cv2

def concat(scale_percent: int = 100):
    screens_path = pathlib.Path(__file__).parent.resolve().joinpath('screens')
    dir = os.listdir(str(screens_path))
    max_lat = None
    max_lon = None
    lat_iterator = 0
    lon_iterator = 0

    for file in dir:
        match = re.match(r'img_(\d+)-(\d+)', file)

        if (match and match[1] and match[2]):
            lat_number = int(match[1])
            lon_number = int(match[2])

            if (max_lat == None or lat_number > max_lat):
                max_lat = lat_number

            if (max_lon == None or lon_number > max_lon):
                max_lon = lon_number

    horizontal_list = []

    while (lat_iterator < max_lat):
        vertical_list = []

        while (lon_iterator < max_lon):
            img = str(screens_path.joinpath('img_'+str(lat_iterator)+'-'+str(lon_iterator)+'.png'))
            vertical_list.append(
                cv2.imread(img)
            )
            lon_iterator += 1

        concated_vertical = cv2.vconcat(list(reversed(vertical_list)))
        horizontal_list.append(concated_vertical)

        lat_iterator += 1
        lon_iterator = 0
        vertical_list = []

    concated_horizontal = cv2.hconcat(horizontal_list)

    width = int(concated_horizontal.shape[1] * scale_percent / 100)
    height = int(concated_horizontal.shape[0] * scale_percent / 100)

    resized = cv2.resize(concated_horizontal, (width, height), interpolation=cv2.INTER_AREA)

    cv2.imwrite(str(screens_path.joinpath('result.png')), resized)

    print('Images concatenated')
