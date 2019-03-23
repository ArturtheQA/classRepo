from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://www.google.com")
navigation=driver.find_elements(By.NAME,"q")
navigation.clear()
navigation.sendKeys("test")
