from gettext import find
from tabnanny import check
from tkinter import PAGES
from selenium import webdriver
from time import sleep, time
from PIL import Image 

driver = webdriver.Chrome() 
driver.get("https://www.selenium.dev/")
driver.maximize_window()
sleep(2)
driver.find_element('xpath', '//*[@id="main_navbar"]/ul/li[3]/a/span').click()


url = driver.current_url
title = driver.title
print(url,"\n", title)
driver.get(url) 
driver.save_screenshot("image.png") 
image = Image.open("image.png") 
image.show() 

  
