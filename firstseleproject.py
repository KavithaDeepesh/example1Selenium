import time


from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get("https://www.saucedemo.com/")
driver.find_element(By.ID,'user-name').send_keys("standard_user")
driver.find_element(By.ID,"password").send_keys("secret_sauce")
driver.find_element(By.ID,"login-button").click()
# hamburgermenu
driver.find_element(By.ID,"react-burger-menu-btn").click()
driver.execute_script('window.open("https://saucelabs.com/")')
driver.implicitly_wait(3)
driver.close()
driver.switch_to.window(driver.window_handles[0])

driver.get("https://www.saucedemo.com/inventory.html")
driver.find_element(By.ID,"react-burger-menu-btn").click()

#logout test
driver.find_element(By.ID,'logout_sidebar_link').click()
# login again after logout
driver.find_element(By.ID,'user-name').send_keys("standard_user")
driver.find_element(By.ID,"password").send_keys("secret_sauce")
driver.find_element(By.ID,"login-button").click()
# driver.find_element(By.XPATH, "//button[@id='react-burger-cross-btn']").click()

#product
minicart = driver.find_element(By.XPATH,"//a[@class='shopping_cart_link']");
minicart.click()







# links = driver.find_elements(By.XPATH,"//nav[@class='bm-item-list']")
#
#
# for link in links:












time.sleep(10)

driver.quit()