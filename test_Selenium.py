from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
import math

url="http://suninjuly.github.io/explicit_wait2.html"


browser=webdriver.Chrome()
browser.get(url)
text=WebDriverWait(browser,15).until(expected_conditions.text_to_be_present_in_element((By.ID, "price"), "100"))
browser.find_element_by_css_selector("button").click()



x=int(browser.find_element_by_css_selector("#input_value").text)
ans=math.log(abs (12 * math.sin(x)))
browser.find_element_by_css_selector("input").send_keys(str(ans))
browser.find_element_by_css_selector("#solve").click()