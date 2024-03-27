from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

chrome_options = Options()
chrome_options.add_argument("--headless")
driver = webdriver.Chrome(options=chrome_options)

driver.get("https://YOURSCHOOLEXTENSIONHERE.managebac.com/student")

def login(email, password):
    username = driver.find_element(By.ID, "session_login")
    username.clear()
    username.send_keys(email)
    password = driver.find_element(By.ID, "session_password")
    password.clear()
    password.send_keys(password)
    driver.find_element(By.NAME, "commit").click()
    return driver.get_cookies()

cookies = login()
session_cookie = next((cookie for cookie in cookies if cookie['name'] == '_managebac_session'), None)
if session_cookie:
    value = session_cookie['value']
    print(value) # this just prints the value of the _managebacsession cookie, but you can modify what you get on the line that defines the session_cookie
else:
    print("Session cookie not found")

driver.quit()
