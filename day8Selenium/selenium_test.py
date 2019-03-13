from selenium import webdriver
import time

driver = webdriver.Chrome()
# driver.maximize_window()

baseURL="https://www.google.com"

driver.get(baseURL)
driver.find_elements_by_class_name("gLFyf gsfi")