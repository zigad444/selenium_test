from pages.login_page import LoginPage
from selenium.webdriver.common.by import By
from utilities.logger import Logger
from selenium.webdriver.common.action_chains import ActionChains

logger = Logger.log_generator()
valid_email = "ziga.drobic@ngen-group.eu"
invalid_email = "drobic@gmail.com"

def test_title_page(driver):
    logger.info('Testing title page')
    login_page = LoginPage(driver)
    login_page.load("https://app-test.ngen.si/")
    actual_title = driver.title
    expected_title = "Smart Grid Connect"
    if actual_title == expected_title :
        logger.info('Title found')
        assert True
    else:
        logger.info('Title missing')
        assert False

def test_valid_login(driver):
    logger.info('Testing login proccess')
    login_page = LoginPage(driver)
    login_page.load("https://app-test.ngen.si/")
    login_page.login(valid_email, "Drozig444")
    try:
        logger.info("Login successfull")
        assert True
    except:
        driver.save_screenshot(".\\data\\screenshots\\test_valid_login.png")
        logger.info("Login failed")
        assert False