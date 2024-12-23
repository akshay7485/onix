from selenium import webdriver

import time



# This is the actual test case

def test_portfolio_homepage():

    # Initialize the WebDriver (you can use Chrome, Firefox, etc.)

    driver = webdriver.Chrome()  # Make sure ChromeDriver is installed

    driver.get("http://172.31.5.148")  # Replace with the IP of your test server

    

    # Wait for the page to load

    time.sleep(2)

    

    # Check if the word "Portfolio" is in the title of the page

    assert "Portfolio" in driver.title

    

    # Optionally, check for other elements, like page content

    # For example:

    # assert "Welcome" in driver.page_source



    # Close the browser after the test

    driver.quit()
