from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time

def automate_using_selenium():
    # 1 Set up the WebDriver (Make sure you have the appropriate driver installed)
    driver = webdriver.Chrome()

    try:
        # 2 Navigate to a webpage
        driver.get("https://www.coursera.org/")

        # 3 Locate an element by its ID, class name, selector, XPath, etc.
        launch_a_new_career_button = webdriver.waits(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "a[href'='/career-academy']")))

        # 4 Perform actions on the element (click, send keys, etc.)
        launch_a_new_career_button.click()
        time.sleep(5)  # Wait for 5 seconds to see the result
        
        select_project_management = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "a[href*='/career-academy/project-management]'")))
        
        select_project_management.click()
        time.sleep(5)  # Wait for 5 seconds to see the result
        
        # 5:Verify and close the browser
        assert "cousera.org/career-academy" in driver.current_url, "Navigation to career academy page failed."
        
        input("Press Enter to close the browser...")
        
    finally:
        
        driver.quit()
        
automate_using_selenium()
        
      

  