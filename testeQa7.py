from cgi import print_directory
from cgitb import enable
from email.mime import image
from sqlite3 import enable_shared_cache
from time import sleep, time
from turtle import Screen
from warnings import catch_warnings
import selenium.webdriver as webdriver
from selenium import webdriver
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from PIL import Image
from selenium.webdriver.support.ui import Select
import time

driver = webdriver.Chrome(executable_path=r'./chromedriver.exe')
driver.get('https://www.selenium.dev/')
driver.maximize_window()
sleep(2)
driver.find_element(By.CSS_SELECTOR, "i[class='fas fa-comments']").click()

driver.current_url

driver.switch_to.window(driver.window_handles[1])

validandobtn = driver.find_element(By.XPATH, '//button[@disabled="disabled"]').is_enabled()

driver.current_url
title = driver.title
url = driver.current_url

print(url,"\n", title,"\n", validandobtn)
driver.get(url) 
driver.save_screenshot("image.png") 
image = Image.open("image.png") 
image.show() 
