from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
from helpers import clean_text, write_file

# Package to download Chrome automatic
from webdriver_manager.chrome import ChromeDriverManager

options = webdriver.ChromeOptions()


def get_driver():
    """Setting options to make browsing easier"""
    options.add_argument("disable-infobars")
    options.add_argument(
        "start-maximized"
    )  # Start the browser maximize in case the website change content when is smaller
    options.add_argument(
        "disable-dev-shm-usage"
    )  # Avoid issues when you interact with Linux OS
    options.add_argument("no-sandbox")
    options.add_argument("disable-blink-features=AutomationControlled")

    options.add_experimental_option(
        "detach", True
    )  # Keep browser open after python is run
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option(
        "excludeSwitches", ["enable-automation"]
    )  # Disable logging from USB problem
    """There is 2 options to use this
    1- It will install Chrome Driver for you
    2- You have Chrome driver already install
    """

    "Option 1 - Downloading the Chrome.exe"
    chrome_downloaded = ChromeService(ChromeDriverManager().install())
    chrome_browser = webdriver.Chrome(
        service=chrome_downloaded, options=options
    )
    chrome_browser.get("https://toscrape.com/")

    "Option 2 - You have Chrome driver install "
    # driver = webdriver.Chrome(service=chrome_browser, options=options)
    # driver.get("https://toscrape.com/")

    return chrome_browser


def main():
    driver = get_driver()

    while True:
        "XPATH"
        element = driver.find_element(
            by="xpath",
            value="/html/body/div/div[3]/div[2]/div[2]/table/tbody/tr[5]/td[2]",
        )  # Xpath can be extract from Inspect on the browser. Select > Copy> Copy Xpath
        text = str(clean_text(element.text))
        write_file(text)

        print(driver.current_url)
        sleep(3)


print(main())
