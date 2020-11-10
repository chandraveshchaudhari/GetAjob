"""
This is Browser setup for chrome and other functions to avoid IP ban....
"""
from selenium import webdriver

from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait

from selenium.webdriver.chrome.options import Options

import pyautogui
import time
import random


def install_driver():
    """
    Starts the chrome browser
    """
    return webdriver.Chrome(ChromeDriverManager().install())


def browser_options():
    """ Initial setup for hiding selenium to websites"""
    options = Options()
    options.add_argument("--start-maximized")
    options.add_argument("--ignore-certificate-errors")
    options.add_argument('--no-sandbox')
    options.add_argument("--disable-extensions")
    # Disable webDriver flags or you will be easily detectable
    options.add_argument("--disable-blink-features")
    options.add_argument("--disable-blink-features=AutomationControlled")
    return options


def driver_wait(driver, time):
    # Setup wait for later
    return WebDriverWait(driver, time)


def change_window(driver):
    """
    It changes the current window to last window in browser
    """
    # Store the ID of the original window
    originalWindow = driver.current_window_handle
    # ID of all windows
    allWindows = driver.window_handles
    neededWindow = allWindows[-1]
    # move to the last window
    if neededWindow != originalWindow:
        driver.switch_to.window(neededWindow)


def avoid_lock():
    """ this uses mouse and keyboard to act human is using the computer"""
    x, _ = pyautogui.position()
    pyautogui.moveTo(x + 200, pyautogui.position().y, duration=1.0)
    pyautogui.moveTo(x, pyautogui.position().y, duration=0.5)
    pyautogui.keyDown('ctrl')
    pyautogui.press('esc')
    pyautogui.keyUp('ctrl')
    pyautogui.press('esc')


def random_time():
    """this give randomTime between 5 and 15.3"""
    randomTime = random.uniform(5, 15.3)
    return randomTime


def sleep(Time):
    """this sleep for some time"""
    print(f"Sleeping for {round(Time, 1)}")
    time.sleep(Time)


def scroll_page(driver):
    """this scroll the page to load all of details"""
    scrollPage = 0
    while scrollPage < 4000:
        driver.execute_script("window.scrollTo(0,"+str(scrollPage)+" );")
        scrollPage += 200
    sleep(random_time())
