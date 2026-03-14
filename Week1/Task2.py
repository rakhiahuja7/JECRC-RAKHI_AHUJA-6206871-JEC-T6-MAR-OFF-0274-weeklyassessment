from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.get("https://www.wikipedia.org/")

time.sleep(2)

search_box = driver.find_element(By.ID, "searchInput")
print("Search box found")

english_lang = driver.find_element(By.ID, "js-link-box-en")
print("English language found:", english_lang.text)

logo = driver.find_element(By.CLASS_NAME, "central-featured-logo")
print("Wikipedia logo found")

languages = driver.find_elements(By.CSS_SELECTOR, ".central-featured-lang")
print("Number of language links:", len(languages))

driver.back()
time.sleep(2)

driver.forward()
time.sleep(2)

driver.refresh()
time.sleep(2)

print("Final page title:", driver.title)

driver.quit()