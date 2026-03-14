from selenium import webdriver
from selenium.webdriver.common.by import By

opts = webdriver.ChromeOptions()
opts.add_experimental_option('detach', True)
driver = webdriver.Chrome(options=opts)

driver.get('https://the-internet.herokuapp.com/login')
driver.maximize_window()

uname = driver.find_element(By.CSS_SELECTOR, 'input[name="username"]')
print('username is working fine!')

pwd = driver.find_element(By.CSS_SELECTOR, '#password')
print('password is working fine!')

login = driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]')
print('login is working fine!')

footer_link = driver.find_element(By.CSS_SELECTOR, 'div[class ="large-4 large-centered columns"] div[style="text-align: center;"]  a[href*="elemental"]')
print('Working Fine!')
driver.quit()