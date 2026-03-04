#!/usr/bin/env python3
"""Selenium aimbot for target-practice using Selenium pointer actions.

Behavior:
- Opens the hosted game in Chrome.
- Recenters to viewport center before each shot and clicks.
- Prints the final achieved score.
- Keeps the browser open until user confirms exit.
"""

from __future__ import annotations

import time # for sleeping if you want to.

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

def main() -> None:

    driver = webdriver.Chrome(options=webdriver.ChromeOptions())
    wait = WebDriverWait(driver, 15)

    try:
        driver.get("https://recursion.ninja/target-practice")

        hud_score = wait.until(EC.presence_of_element_located((By.ID, "hudScore")))
        hud_time  = wait.until(EC.presence_of_element_located((By.ID, "hudTime")))
        hud_shots = wait.until(EC.presence_of_element_located((By.ID, "hudShots")))

        body_tag = wait.until(EC.presence_of_element_located((By.TAG_NAME, "body")))

        actions = ActionChains(driver)
        actions.w3c_actions.pointer_action._duration = 0 # no delay betwenn ActionChain events


####################################################################################################
########                                                                                    ########
####       CODE ABOVE IS SACRED; DO NOT ALTER LEST YOU UNLEASH ACCURSED UNUTTERABLE CHAOS       ####
########                                                                                    ########
####################################################################################################


        # STEP 1:
        # The body tag covers the entire browser window.
        # Hence, the center of the bullseye lies at the center of the body tag.
        #
        # Above is the Element for the body tag of the webpage.
        # You can read the documentation for interacting with
        # Elements from Selenium at the floowing URL:
        #     https://www.selenium.dev/documentation/webdriver/elements/information/#size-and-position
        #
        # We are concerned with the size and position of the body tag.
        # We can get the body tag's bounding rectangle from the "rect" property.
        # We can then get the width and height from the rectangle.
        #
        # You must find the center coordinates of the body tag.
        body_rectangle = body_tag.rect
        body_width     = body_rectangle["width"]
        body_height    = body_rectangle["height"]

        body_center_x = int(round(body_width  / 2))
        body_center_y = int(round(body_height / 2))


        # STEP 2:
        # Loop through the five shots, hitting the center bullseye each time.
        #
        # Above is an ActionChain named "action" that can be used
        # to construct a sequence of actions sent to the browser.
        # You can read more about ActionChain and mouse events here:
        # https://www.selenium.dev/documentation/webdriver/actions_api/mouse/#move-by-offset
        #
        # Use the following to shoot in the center of the browser window:
        #   - actions : ActionChain
        #   - body_tag : Element
        #   - body_center_x : Int
        #   - body_center_y : Int
        #   - move_to_element_with_offset : Element -> Int -> Int -> Event
        #   - click : Element -> Event
        #   - perform : Event
        for i in range(5):
            continue


        # STEP 3:
        # Ensure that your script *reliably* acheives the required score.
        #
        # Keep on tinkering until you get it to work!
        # Remember you can:
        #   - Read the Selenium documentation
        #   - Lookup information using a search engine
        #   - Email the instructor (last resort)


####################################################################################################
########                                                                                    ########
####       CODE BELOW IS SACRED; DO NOT ALTER LEST YOU UNLEASH ACCURSED UNUTTERABLE CHAOS       ####
########                                                                                    ########
####################################################################################################


        wait.until(lambda d: d.find_element(By.ID, "hudShots").text.strip().startswith("5/"))
        elapsed_ms  = hud_time.text.strip()
        final_score = hud_score.text.strip()

        print(f"Shot spread time (1st->5th): {elapsed_ms} ms")
        print(f"Achieved score: {final_score}")
        input("Press Enter to close the browser window and terminate the script...")

    finally:
        driver.quit()


if __name__ == "__main__":
    main()
