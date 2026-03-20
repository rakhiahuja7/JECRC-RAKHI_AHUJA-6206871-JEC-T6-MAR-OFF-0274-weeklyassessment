from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


opts=webdriver.ChromeOptions()
opts.add_experimental_option('detach',True)
driver=webdriver.Chrome(options=opts)

driver.get('https://www.google.com/')
driver.maximize_window()

search1=driver.find_element(By.ID,'APjFqb')
search1.send_keys('Selenium Python')

wait = WebDriverWait(driver, 10)
search_suggestion=wait.until(EC.visibility_of_all_elements_located((By.XPATH, '//ul[@role="listbox"]/child::li')))

for item in search_suggestion:
    print(item.text)

click_item=wait.until(EC.element_to_be_clickable((By.XPATH,'//ul[@role="listbox"]/child::li[4]')))
click_item.click()

print(driver.current_url)
print('completed')