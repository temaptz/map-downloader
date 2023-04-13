from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import pathlib
import config
import time
import re


def take(
        bottom_left_lon: float,
        bottom_left_lat: float,
        top_right_lon: float,
        top_right_lat: float,
        lon_number: int,
        lat_number: int
) -> [[float, float], [float, float]]:
    d = DesiredCapabilities.CHROME
    d['goog:loggingPrefs'] = {'browser': 'ALL'}
    driver = webdriver.Chrome(desired_capabilities=d)
    driver.set_window_size(config.map_width, config.map_height + 124)  # 124 - тестовое по
    file_path = pathlib.Path(__file__).parent.resolve().joinpath('template').joinpath('index.html')
    file_url = 'file:///' \
               + str(file_path) \
               + '?width=' + str(config.map_width) \
               + '&height=' + str(config.map_height) \
               + '&bottom_left_lat=' + str(bottom_left_lat) \
               + '&bottom_left_lon=' + str(bottom_left_lon) \
               + '&top_right_lat=' + str(top_right_lat) \
               + '&top_right_lon=' + str(top_right_lon) \
               + '&apiKey=' + config.api_key

    correct_bottom_left_lon = bottom_left_lon
    correct_bottom_left_lat = bottom_left_lat
    correct_top_right_lon = top_right_lon
    correct_top_right_lat = top_right_lat

    driver.get(file_url)

    time.sleep(config.map_wait_timeout_sec)
    # try:
    #     WebDriverWait(driver, 60).until(
    #         EC.presence_of_element_located((By.ID, "ready"))
    #     )
    # except:
    #     print('Error waiting page')

    for entry in driver.get_log('browser'):
        if entry['message']:
            match_bottom_left_lon = re.search(r'BOTTOM LEFT LON: (\d+\.\d+)', entry['message'])
            match_bottom_left_lat = re.search(r'BOTTOM LEFT LAT: (\d+\.\d+)', entry['message'])
            match_top_right_lon = re.search(r'TOP RIGHT LON: (\d+\.\d+)', entry['message'])
            match_top_right_lat = re.search(r'TOP RIGHT LAT: (\d+\.\d+)', entry['message'])

            if (match_bottom_left_lon and match_bottom_left_lon[1]):
                correct_bottom_left_lon = float(match_bottom_left_lon[1])

            if (match_bottom_left_lat and match_bottom_left_lat[1]):
                correct_bottom_left_lat = float(match_bottom_left_lat[1])

            if (match_top_right_lon and match_top_right_lon[1]):
                correct_top_right_lon = float(match_top_right_lon[1])

            if (match_top_right_lat and match_top_right_lat[1]):
                correct_top_right_lat = float(match_top_right_lat[1])

    driver.get_screenshot_as_file('screens/img_' + str(lat_number) + '-' + str(lon_number) + '.png')
    driver.quit()

    return get_bounds_by_points(
        bottom_left_lon=correct_bottom_left_lon,
        bottom_left_lat=correct_bottom_left_lat,
        top_right_lon=correct_top_right_lon,
        top_right_lat=correct_top_right_lat
    )


def get_bounds_by_points(
        bottom_left_lon: str,
        bottom_left_lat: str,
        top_right_lon: str,
        top_right_lat: str,

) -> [[float, float], [float, float]]:
    return [[bottom_left_lon, bottom_left_lat], [top_right_lon, top_right_lat]]


def get_points_by_bounds(
        bounds: [[float, float], [float, float]]
) -> {
    'bottom_left_lon': float,
    'bottom_left_lat': float,
    'top_right_lon': float,
    'top_right_lat': float,
}:
    return {
        'bottom_left_lon': bounds[0][0],
        'bottom_left_lat': bounds[0][1],
        'top_right_lon': bounds[1][0],
        'top_right_lat': bounds[1][1]
    }

def print_bounds_diff(
        a: [[float, float], [float, float]],
        b: [[float, float], [float, float]]
) -> {
    'bottom_left_lon': float,
    'bottom_left_lat': float,
    'top_right_lon': float,
    'top_right_lat': float,
}:
    return {
        'bottom_left_lon': a[0][0] - b[0][0],
        'bottom_left_lat': a[0][1] - b[0][1],
        'top_right_lon': a[1][0] - b[1][0],
        'top_right_lat': a[1][1] - b[1][1]
    }
