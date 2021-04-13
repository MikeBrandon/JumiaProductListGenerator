from selenium import webdriver

PATH = "C:\Program Files\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("https://google.com")
print(driver.title)
driver.quit()