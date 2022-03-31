from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


driver = webdriver.Chrome(r"E:\\Automation\\TestAutomation\\Drivers\\chromedriver.exe")
driver.get("https://espn.com")
driver.maximize_window()
driver.find_element(by=By.XPATH, value="(//button[@class='button-alt med'])[1]").click()
driver.implicitly_wait(7)
driver.switch_to.frame("disneyid-iframe")
driver.find_element(by=By.XPATH, value="(//span[@class='input-wrapper']/input[1])[1]").send_keys("sairamsinghrajput@gmail.com")
driver.find_element(by=By.XPATH, value="(//span[@class='input-wrapper']/input[1])[2]").send_keys("Sairam@156")
driver.find_element(by=By.XPATH, value="//button[@class='btn btn-primary btn-submit ng-isolate-scope']").click()
driver.implicitly_wait(10)
driver.close()