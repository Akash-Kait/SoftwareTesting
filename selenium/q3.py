from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys


driver = webdriver.Chrome()
driver.get("http://www.facebook.com")

#check the title of a window using Selenium WebDriver.
title = driver.title
print(title)