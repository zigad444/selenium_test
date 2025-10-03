from pages.login_page import LoginPage
from selenium.webdriver.common.by import By
from utilities.logger import Logger
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

logger = Logger.log_generator()

def test_relays(driver):
    logger.info('Testing relays')
    login_page = LoginPage(driver)
    login_page.load("https://app-test.ngen.si/")
    actions = ActionChains(driver)
    
    #make sure the selected language is English
    language_button = (By.ID, "headlessui-listbox-button-:r0:")
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(language_button)
    ).click()

    english = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//span[text()='English']"))
    )
    english.click()

    login_page.login("ziga.drobic@ngen-group.eu", "Drozig444")

    device_name = "H3 PRO Show Room"
    show_room = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, f"//div[text()='{device_name}']"))
    )
    show_room.click()

    time.sleep(3)
    relay_img = "/assets/relayControl-hzuZR5GK.png"
    relay_management = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, f"//img[contains(@src, '{relay_img}')]"))
    )

    actions.move_to_element(relay_management).click().perform()
    time.sleep(3)

            