from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Create a Chrome browser instance
driver = webdriver.Chrome()

# Open Google
driver.get("https://www.google.com")

# Wait for the page to load
time.sleep(2)

# Find the search box element (by name='q')
search_box = driver.find_element(By.NAME, "q")

# Type a query into the search box
search_box.send_keys("Jenkins CI/CD pipeline tutorial")

# Press Enter to search
search_box.send_keys(Keys.RETURN)

# Wait a few seconds to let results load
time.sleep(3)

# Print the page title
print("Page title after search:", driver.title)

# Close the browser
driver.quit()
