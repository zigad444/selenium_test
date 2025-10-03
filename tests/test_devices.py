from pages.login_page import LoginPage
from selenium.webdriver.common.by import By
from utilities.logger import Logger
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

logger = Logger.log_generator()

def test_all_devices(driver):
    logger.info('Testing devices')
    login_page = LoginPage(driver)
    login_page.load("https://app-test.ngen.si/")
    login_page.login("ziga.drobic@ngen-group.eu", "Drozig444")

    logger.info('We list down all the devices available after successful login')
    show_room = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//div[text()='H3 PRO Show Room']"))
    )
    show_room.click()
    logger.info("Show room reached")