from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pathlib
import config

def take_screenshot(
        bottom_left_lat: str,
        bottom_left_lon: str,
        top_right_lat: str,
        top_right_lon: str,
        lon_number: int,
        lat_number: int
):
    driver = webdriver.Chrome()
    driver.set_window_size(1024, 640 + 124) # 124 - тестовое по
    file_path = pathlib.Path(__file__).parent.resolve().joinpath('index.html')
    file_url = 'file:///' + str(file_path) + '?width=1024&height=640&aLat=' + bottom_left_lat + '&aLon=' + bottom_left_lon + '&bLat=' + top_right_lat + '&bLon=' + top_right_lon + '&apiKey=' + config.api_key

    print('File URL', file_url)

    driver.get(file_url)

    try:
        WebDriverWait(driver, 60).until(
            EC.presence_of_element_located((By.ID, "ready"))
        )
        print('Map loaded')
    except:
        print('Error waiting page')

    driver.get_screenshot_as_file('screens/img_' + str(lat_number) + '-' + str(lon_number) + '.png')
    driver.quit()
    print('Screenshot done')