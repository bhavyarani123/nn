from selenium import webdriver
import time
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path=r"C:\Users\bhavy\PycharmProjects\amazon\drivers\chromedriver.exe")
driver.get("https://letskodeit.teachable.com/pages/practice")


driver.execute_script("window.scrollBy(0,400)")
ele1 = driver.find_element_by_id("openwindow")
ele1.click()

handles = driver.window_handles
parent = driver.current_window_handle

for i in handles:
    if i not in parent:
        driver.switch_to.window(i)

driver.find_element(By.ID, "search-courses").send_keys("Python")

#time.sleep(10)
#driver.quit()




