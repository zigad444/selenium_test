
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

@pytest.fixture
def driver():
    options = Options()
    driver = webdriver.Chrome()
    options.add_argument("--disable-notifications")
    options.add_argument("--disable-media-stream")  # Disable microphone/camera
    options.add_argument("--log-level=3")  # Suppresses most logs
    #options.add_argument("--headless")
    driver = webdriver.Chrome(options=options)
    try:
        yield driver
    finally:
        driver.quit()
      