from selenium import webdriver 
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup 
import time

gecko_driver_path = '/home/venus/geckodriver' 
firefox_binary_path = '/usr/bin/firefox'

firefox_options = webdriver.FirefoxOptions() 
firefox_options.binary_location = firefox_binary_path

service = Service(executable_path=gecko_driver_path) 
driver = webdriver.Firefox(options=firefox_options, service=service)

url = f"https://timesofindia.indiatimes.com" 
print(url)
driver.get(url)

driver.implicitly_wait(20)

sq = input("enter search query: ")
search = WebDriverWait(driver, 20).until(
    EC.element_to_be_clickable((By.CLASS_NAME, 'OG1TB'))
)
# search = driver.find_element_by_class_name('OG1TB')
search.click()

# search_input = driver.find_element_by_id("searchField")
search_input = WebDriverWait(driver, 20).until(
    EC.element_to_be_clickable((By.ID, 'searchField'))
)

search_input.send_keys(sq)
search_input.send_keys(Keys.RETURN) 
 

while True:
    try:
        loadmore = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.CLASS_NAME, 'IVNry'))
        )
        loadmore.click()
    except:
        break

page_source = driver.page_source 
soup = BeautifulSoup(page_source, 'html.parser')

elements = soup.find_all("div",attrs={'class':'uwU81'})

for d in elements:
    date=d.find("div",attrs={'class':'ZxBIG'})
    date = date.get_text()
    print(date)
