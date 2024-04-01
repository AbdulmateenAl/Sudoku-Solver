from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service)

driver.maximize_window()

driver.get("https://sudoku.com/")

# WebDriverWait(driver, 5).until(
#     EC.presence_of_all_elements_located((By.CLASS_NAME, "gLFyf"))
# )

num_elem = driver.find_element(By.CLASS_NAME, "numpad-item")
num_elem.click()

time.sleep(5)

driver.quit()