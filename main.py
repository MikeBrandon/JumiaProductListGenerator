from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

userInput = input("Enter Something You Want to Buy from Jumia: ")

PATH = "C:\Program Files\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("https://jumia.co.ke")
print(driver.title)

search = driver.find_element_by_xpath("/html/body/div[1]/header/section/div/form/div/input")
search.send_keys(userInput)
search.send_keys(Keys.RETURN)

try:
    catalog = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/main/div[2]/div[3]/section/div[1]"))
    )

    articles = catalog.find_elements_by_tag_name("article")
    number = 1
    name = ""

    data_file = open(userInput + ".txt", "w")
    data_file.write(userInput + " Jumia Store List\n")
    data_file.close()

    for article in articles:
        try:
            core = article.find_element_by_tag_name("a")
            info = core.find_element_by_class_name("info")
            name = info.find_element_by_class_name("name")
            price = info.find_element_by_class_name("prc")
            data_string = number.__str__() + ": " + name.text + " at " + price.text
            data_file = open(userInput + ".txt", "a")
            data_file.write(data_string + "\n")
            print(data_string)
            number = number + 1
        except:
            print("End of File")

    data_file.close()

    # pick = int(input("Pick a Product number You Wish to Buy (Pick 0 for none): "))
    # number = 1
    #
    # if pick > 0:
    #     for article in articles:
    #         if number == pick:
    #             core = article.find_element_by_tag_name("a")
    #             actions = ActionChains(driver)
    #             actions.move_to_element(core)
    #             actions.click()
    #             actions.perform()
    #             break
    #         number = number + 1
    #
    #     driver.implicitly_wait(15)

finally:
    driver.quit()
