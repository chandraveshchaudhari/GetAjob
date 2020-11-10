"""This is unique to LinkedIn and all funtions are written with respect to LinkedIn"""
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
# from selenium.webdriver.support.expected_conditions import presence_of_element_located
# from selenium.webdriver.support import expected_conditions as EC
import lazy_unemployed_want_job.browserSetup as bs
import lazy_unemployed_want_job.utils as u
import lazy_unemployed_want_job.loadData as d

loginButtonElementXpath = "//button[@class='sign-in-form__submit-button' and @type='submit']"
urlOne = "https://www.linkedin.com/jobs/search/"
jobSearchButton = "//button[@class='jobs-search-box__submit-button artdeco-button  artdeco-button--2 artdeco-button--secondary']"
applyFilter = '//*[@aria-label="Filter results by: LinkedIn Features"]/div/fieldset/div/div/button[2]'
linkedInFeature = '//*[@aria-label="Filter results by: LinkedIn Features"]'
easyApplyButton = '//*[@aria-label="Filter results by: LinkedIn Features"]/div/fieldset/div/ul/li[1]/label'
positionElement = '//input[contains(@id, "jobs-search-box-keyword-id-ember54")]'
locationElement = '//input[contains(@id, "jobs-search-box-location-id-ember54")]'


def find_linkedin_jobs_link_id(driver):
    links = driver.find_elements_by_xpath('//div[@data-job-id]')
    print(links)
    for link in links:
        children = link.find_elements_by_xpath('.//a[@data-control-id]')
        print(children)
        for child in children:
            temp = link.get_attribute("data-job-id")
            temp1 = child.get_attribute("href")
            print(temp1)
            print(temp)


def get_easy_apply_button(self):
    try:
        button = driver.find_elements_by_xpath(
            '//button[contains(@class, "jobs-apply")]/span[1]')
        easyApplyButton = button[0]
    except:
        easyApplyButton = False
    return easyApplyButton


def easy_apply_filter(driver):
    easyApplyFilter = '//*[@id="ember115"]/li[1]/label/p/span[1]'
    button = driver.find_element(By.XPATH, easyApplyFilter)
    button.click()


# setup and login in linkedIn
bs.browser_options()
driver = bs.install_driver()
data = d.get_data()
u.website_login(driver, data['LinkedIn']['url'], "session_key", data['LinkedIn']['username'], "session_password", data['LinkedIn']['password'], loginButtonElementXpath)
bs.sleep(bs.random_time())
bs.avoid_lock()

# linkedIn easy apply filter
driver.maximize_window()
driver.get(urlOne)
u.button_click_by_xpath(driver, linkedInFeature)
bs.sleep(bs.random_time())
u.button_click_by_xpath(driver, easyApplyButton)
bs.sleep(bs.random_time())
u.button_click_by_xpath(driver, applyFilter)
bs.avoid_lock()

# this is job search
inputBox = driver.find_element(By.XPATH, positionElement)
inputBox.clear()
inputBox.send_keys(str(data['positions'][0]))
inputBox.send_keys(Keys.TAB)
bs.sleep(bs.random_time())
inputBox = driver.find_element(By.XPATH, locationElement)
inputBox.clear()
inputBox.send_keys(str(data['locations'][0]))
bs.sleep(bs.random_time())
u.button_click_by_xpath(driver, jobSearchButton)
bs.sleep(bs.random_time())
bs.scroll_page(driver)
find_linkedin_jobs_link_id(driver)

