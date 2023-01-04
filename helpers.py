from datetime import datetime as dt
from selenium.webdriver.common.by import By


def clean_text(text):
    """Extract only the specific word from text
    Keyword arguments:
    text -- The text or number you need to get and nothing else
    Return: Value of the text or num clean
    """
    return text.replace("([\$\,\.\:])", " ")


def write_file(text):
    """Write input text into a text file"""
    file_name = f"{dt.now().strftime('%Y-$m-%d.%H-%M-%S')}.txt"
    with open(file_name, "wt") as f:
        f.write(text)
    # end open file


def scrapping_by_id(driver, value1):
    """By ID
    send_key has the value of what you need to write
    There is 2 ways to use by
    """

    "1rt- Way to get by id"
    driver.find_element(
        by="id",
        value=value1,
    ).send_keys("automated")
    "2nd- Way to get by id"
    driver.find_element(
        by="id",
        value="description",
    ).send_keys("automated")
    click_submit = driver.find_element(By.ID, "btn-submit")
    click_submit.click()
    "If you have a input one line use this like PASSWORD"
    # driver.find_element(
    #     by="id",
    #     value="description",
    # ).send_keys("automated" + Keys.RETURN)
