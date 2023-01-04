# Python examples of scrapping with python and selenium

## Packages to install

All this packages are in requirements.txt

## How it works

### 1- Getting the drivers

This section is to make sure you have the drivers install in your OS or you need to install it

#### Options

##### 1.1 Option 1 - Installing from python

```python
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

    "Downloading the Chrome.exe"
    chrome_downloaded = ChromeService(ChromeDriverManager().install())
    chrome_browser = webdriver.Chrome(
        service=chrome_downloaded, options=options
    )
    chrome_browser.get("WEBSITE YOU ARE SCRAPPING")

    return chrome_browser

```

##### 1.2 Option 2 - Already install

```python
def get_driver():
    """Setting options to make browsing easier
    You can use the above to do the options
    """

    "Already install the Chrome.exe"
    driver = webdriver.Chrome(options=options)
    driver.get("WEBSITE YOU ARE SCRAPPING")

    return driver

```
