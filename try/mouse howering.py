from selenium import webdriver
from selenium.webdriver import ActionChains

driver = webdriver.Chrome(executable_path=r"C:\Users\bhavy\PycharmProjects\amazon\drivers\chromedriver.exe")
driver.get("https://letskodeit.teachable.com/pages/practice")

driver.execute_script("window.scrollBy(0,1000);")
print("scrolled down")
driver.implicitly_wait(10)

obj = ActionChains(driver)
ele1 = driver.find_element_by_id("mousehover")
obj.move_to_element(ele1).click().perform()
print("Mouse Hovered on element")

top = driver.find_element_by_xpath(".//div[@class='mouse-hover-content']//a[text()='Top']")
obj.move_to_element(top).click().perform()
print("Click success")

#driver.close()