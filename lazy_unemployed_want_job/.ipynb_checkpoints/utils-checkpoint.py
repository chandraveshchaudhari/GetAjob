import re


def get_current_webpage(driver):
    """
    Args:
        driver: selenium driver for browser automation
    Returns:
        htmlSourceCode: complete html of page
    """
    htmlSourceCode = driver.page_source
    return htmlSourceCode


def snippet_html(wordSeenInWebsite: str, htmlText: str) -> str:
    """
    Args:
        wordSeenInWebsite: word that you see in input box on website
        htmlText: complete html of page
    Returns:
        snippetHtmlText: snippet of Html which has your element Name
    """
    wordSeenInWebsite=str(wordSeenInWebsite)
    regex = "<.+"+wordSeenInWebsite+".+>"
    snippetHtmlText = re.findall(regex, htmlText)
    snippetHtmlText = str(snippetHtmlText)
    return snippetHtmlText


def element_name_value_regex(elementName: str, snippetHtmlText: str):
    """
    Args:
        snippetHtmlText: snippet of Html which has your element Name
        elementName: ID, Name, Class etc. of html element
    Returns:
        elementNameAndValue: string of element name and it's value
    """
    elementName= elementName.lower()
    regex = str(elementName)+'="[\w-]+"'
    elementNameAndValue = re.findall(regex, snippetHtmlText)
    
    return elementNameAndValue


def element_value(elementNameValue):
    """
    Args:
        elementNameValue: element name and element value ex: id="ember51"
    Returns:
        elementValue: get element value ex: ember51
    """
    regex = '"[\w-]+"'
    elementValue = re.findall(regex, elementNameValue)
    elementValue = str(elementValue)
    regex1 = '[\w-]+'
    elementValue = re.findall(regex1, elementValue)
    
    return elementValue


def element_value_from_html(wordSeenInWebsite: str, htmlText: str, elementName: str) -> list:
    """
    Args:
        wordSeenInWebsite: word that you see in input box on website
        htmlText: complete html of page
        elementName: ID, Name, Class etc. of html element
    Returns:
        elementValue: get element value ex: ember51
    """
    snipperHtmlText = snippet_html(wordSeenInWebsite, htmlText)
    elementNameValue = element_name_value(elementName, snipperHtmlText)
    elementValue = element_value(str(elementNameValue))
    assert type(elementValue) is list
    
    return elementValue


def fill_input_on_webpage(driver, wordSeenInWebsite: str, htmlText: str, elementName: str, inputAnswer: str):
    """
    Description: this function fill the inputbox on webpage with the help of wordSeenInWebsite,
    with the inputAnswer.
    Args:
        wordSeenInWebsite: word that you see in input box on website
        htmlText: complete html of page
        elementName: ID, Name, Class etc. of html element
        inputAnswer: answer that you want to put in the inputbox of webpage
    """
    elementValue = element_value_from_html(wordSeenInWebsite, htmlText, elementName)
    for value in elementValue:
        try:
            print(value)
            print(type(value))
            inputBox = driver.find_element(By.ID, str(value))
            inputBox.send_keys(inputAnswer)
            print("executed")
        except Exception:
            print('passing')
            pass


def input_box_by_name(driver, name: str, answer: str):
    """Input answer in input box by searching element Name"""
    try:
        user_field = driver.find_element(By.NAME, name)
        user_field.send_keys(answer)
    except Exception:
        print(Exception)


def get_text_by_tag_name(driver, tag: str, text: str):
    """This function get all the text by searching all tag_name then click on specific button"""
    elements = driver.find_elements(By.TAG_NAME, tag)
    for element in elements:
        print(element.text)
        if element.text == text:
            print(element)
            element.click()
        else:
            print("Button couldn't be found")


def button_click_by_xpath(driver, ButtonElementXpath):
    """ ButtonElementXpath used to find and click on the button"""
    try:
        button = driver.find_element(By.XPATH, ButtonElementXpath)
        button.click()
    except Exception:
        print(Exception)


def sleep_after_n_job_try(n: int, job_try):
    """ sleep every n applications"""
    if job_try != 0 and job_try % n == 0:
        random_sleep(15 * random_time())
