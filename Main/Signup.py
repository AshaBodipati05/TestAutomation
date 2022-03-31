from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


driver = webdriver.Chrome(r"E:\\Automation\\TestAutomation\\Drivers\\chromedriver.exe")
driver.get("https://espn.com")
driver.maximize_window()
print(driver.current_url)

driver.find_element(by=By.XPATH, value="(//button[@class='button med'])[1]").click()
driver.implicitly_wait(7)
driver.switch_to.frame("disneyid-iframe")

driver.find_element(by=By.XPATH, value="//div[@sequencekey='first-name']/label/span[2]/input").send_keys("Bodipati")
driver.find_element(by=By.NAME, value="lastName").send_keys("Asha")
driver.find_element(by=By.NAME, value="email").send_keys("ashabodipati19@gmail.com")
driver.find_element(by=By.NAME, value="newPassword").send_keys("xyzabcdfg123")
driver.find_element(by=By.XPATH, value="//button[@class='btn btn-primary ng-scope ng-isolate-scope']").click()
driver.implicitly_wait(10)
driver.close()


