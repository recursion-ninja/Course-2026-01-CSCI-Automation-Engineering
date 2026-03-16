#!/usr/bin/env python3

import datefinder
import requests
import sys
import time
from collections import defaultdict
from collections import namedtuple
from datetime import date
from datetime import datetime, timedelta
from itertools import chain
from selenium import webdriver
from selenium.webdriver import ChromeOptions, FirefoxOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait as WebWait
from seleniumbase import Driver
from seleniumrequests import Chrome, Firefox

# Wait up to 15 second for the page to load
PATIENCE_SECS = 15

# Base URL
URL_ENTRY = "https://github.com"

def main():

    with webdriver.Firefox() as browser:

        browser.get("https://github.com/recursion-ninja/Course-2026-01-CSCI-Automation-Engineering/issues")

        # Wait for the page to load
        body = WebWait(browser, PATIENCE_SECS).until(
            EC.presence_of_element_located((By.TAG_NAME, "body"))
        )

        if "No results" in body.text and False:
            print("No open issues in the repository")
        else:
            issue_list = browser.find_elements( By.XPATH, '//div[@data-listview-component="items-list"]')[0]
            issues  = issue_list.find_elements(By.TAG_NAME, "li")
            for i in issues:
                print(i.text)
            print(len(issues))

        input("Patiently waiting")



if __name__ == "__main__":
    main()
