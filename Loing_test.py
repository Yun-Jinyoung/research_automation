from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

from openpyxl import load_workbook  #excel lib load

import time
import os
import subprocess

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()
driver.get('http://192.168.50.39:5000/')



time.sleep(2)

driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div/a[2]').click()
time.sleep(1)

driver.find_element(By.XPATH, '/html/body/div[2]/div/div/form/button').click()
time.sleep(1)

# excel load
load_wb = load_workbook("Login_info_v2021_0514.xlsx", data_only=True)
load_ws = load_wb['Login_info']


all_values = []
excel_init_count=0
for row in load_ws.rows:
    if excel_init_count == 0 : 
        excel_init_count = 1
        continue
    row_value = []
    for cell in row:
        if cell.column ==2 : continue
        if str(cell.value) == 'None' : cell.value = ''
        row_value.append(cell.value)
    all_values.append(row_value)

#excel_data_set
for excel_data in all_values:
    print(excel_data)



for login_info in all_values:
    driver.find_element_by_id("email").clear()
    driver.find_element_by_id("password").clear()
    driver.find_element_by_id("confirm-password").clear()
    driver.find_element_by_id("secret-key").clear()

    driver.find_element_by_id("email").send_keys(str(login_info[1]))
    driver.find_element_by_id("password").send_keys(str(login_info[2]))
    driver.find_element_by_id("confirm-password").send_keys(str(login_info[3]))
    driver.find_element_by_id("secret-key").send_keys(str(login_info[4]))
    time.sleep(2)


