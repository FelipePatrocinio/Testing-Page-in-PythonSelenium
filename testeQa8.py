from gettext import find
from tabnanny import check
from tkinter import PAGES
from selenium import webdriver
from time import sleep, time
from PIL import Image 
from selenium.webdriver.common.by import By

driver = webdriver.Chrome() 

### Test case #002 - Validando pagina de download ###

driver.get("https://www.selenium.dev/")
driver.maximize_window()
sleep(2)
driver.find_element(By.CSS_SELECTOR, 'a[href="/downloads"]').click()


url = driver.current_url
title = driver.title
print(url,"\n", title)
driver.save_screenshot("image.png") 
image = Image.open("image.png") 
image.show() 

  
