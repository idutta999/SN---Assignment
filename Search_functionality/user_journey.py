from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

driver = webdriver.Chrome(executable_path=r"D:\Drivers\Chrome Driver 2.37\chromedriver.exe")
wait = WebDriverWait(driver, 5)
driver.maximize_window()

try:
    driver.get('https://link.springer.com/')
    driver.implicitly_wait(5)

    print driver.title
    assert "Home - Springer" in driver.title

    # driver.find_element_by_class_name('text ui-autocomplete-input').send_keys('Economics')
    driver.find_element_by_id('query').send_keys('Economics')
    driver.find_element_by_class_name('search-submit').click()
    driver.implicitly_wait(5)

    val1 = driver.find_element_by_id('number-of-search-results-and-search-terms').text

    assert "Economics" in val1

    driver.close()

except Exception as e:
    print e
    driver.close()





