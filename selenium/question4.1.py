from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()

url = "https://demoqa.com/select-menu"
driver.get(url)

dropdown = driver.find_element_by_xpath("//select[@id='oldSelectMenu']/option[text()='White']")
dropdown_select = dropdown.click()

time.sleep(6)
driver.close()
