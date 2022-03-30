

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


driver = webdriver.Chrome(r"E:\\Automation\\TestAutomation\\Drivers\\chromedriver.exe")
driver.get("https://espn.com")
driver.find_element(by=By.ID, value="global-search-trigger").click()
driver.implicitly_wait(15)
driver.find_element(by=By.XPATH, value="//div[@class='global-search-input-wrapper']/input[1]").send_keys("Manchester United")
driver.implicitly_wait(10)
driver.find_element(by=By.XPATH, value="//div[@class='global-search-input-wrapper']/input[2]").click()

print(driver.title)
driver.close()