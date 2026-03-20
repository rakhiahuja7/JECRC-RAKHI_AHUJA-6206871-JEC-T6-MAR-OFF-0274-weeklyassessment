from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

opts = webdriver.ChromeOptions()
opts.add_experimental_option('detach', True)

driver = webdriver.Chrome(options=opts)

driver.get('https://www.amazon.in/')
driver.maximize_window()

wait = WebDriverWait(driver, 10)

assert "amazon.in" in driver.current_url, "url not found"
print('present!')

# print(driver.title)

# assert "Online Shopping" in driver.title, "url not found"
# print('present!')

category_dropdown = wait.until(EC.presence_of_element_located((By.XPATH, "//select[@id = 'searchDropdownBox']")))
select = Select(category_dropdown)

select.select_by_visible_text('Books')

harry_potter = wait.until(EC.visibility_of_element_located((By.ID, "twotabsearchtextbox")))
harry_potter.send_keys('Harry Potter', Keys.ENTER)

result_visibility = wait.until(EC.visibility_of_element_located((By.XPATH, '//div[@class = "s-desktop-width-max s-desktop-content s-opposite-dir s-wide-grid-style sg-row"]')))

titles = wait.until(EC.visibility_of_all_elements_located((By.XPATH, '//a[@class = "a-link-normal s-line-clamp-2 puis-line-clamp-3-for-col-4-and-8 s-link-style a-text-normal"]/descendant::h2/child::span')))
for i in range(0, 5):
    print(titles[i].text)

first_product = wait.until(EC.visibility_of_element_located((By.XPATH, '(//a[@class = "a-link-normal s-line-clamp-2 puis-line-clamp-3-for-col-4-and-8 s-link-style a-text-normal"]/descendant::h2/child::span)[1]')))
first_product.click()

print('its working')

driver.quit()