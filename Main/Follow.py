from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


driver = webdriver.Chrome(r"E:\\Automation\\TestAutomation\\Drivers\\chromedriver.exe")
driver.get("https://espn.com")
driver.maximize_window()
print(driver.current_url)

print(driver.find_element(by=By.XPATH, value="(//div[@class='contentItem__header__headings'])[5]/h2"))

driver.find_element(by=By.XPATH, value="(//button[@class='button-alt sm'])[1]").click()
driver.implicitly_wait(15)
#driver.close()