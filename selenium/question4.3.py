from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()

url = "https://demoqa.com/select-menu"
driver.get(url)

options = driver.find_elements_by_xpath("//*[@id='oldSelectMenu']")

print("Iteration of list----")
for option in options:
    print(option.text)

driver.close()