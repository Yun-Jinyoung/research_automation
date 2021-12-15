
from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


import BA_CONST as BAC
import time

import pywinauto

def BA_DCM_File_load(driver, logger):
	try:
		for Upload_file_name in BAC.DCM_FILE_NAME:
			WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="nav-item-file"]')))
			driver.find_element(By.XPATH, '//*[@id="nav-item-file"]').click()
			WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.ID, "open-filebutton")))
			driver.find_element(By.ID, 'open-filebutton').click()
			time.sleep(2)

			app=pywinauto.Application().connect(title_re="열기")
			logger.info(" -Openfile- : "+ Upload_file_name )
			app["Dialog"]["Edit1"].set_text(Upload_file_name)
			app["Dialog"]["Edit1"].type_keys('{ENTER}')
			print(Upload_file_name)
			time.sleep(2)
			WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="modal-patient-information"]/div[3]/div[2]')))
			driver.find_element(By.XPATH, '//*[@id="modal-patient-information"]/div[3]/div[2]').click()
			# break  # break 를 제거하면 선택 폴더 하위 폴더 파일 까지 모두 업로드 한다.
	except Exception as inst:
			logger.error("[ Failed ] ( BA_DCM_File_load )- File Load Fail  : " + str(inst))
#--------------------------------------- ( 파일 로드에 대한 체크 어떻게 할 것인지? ) - 환자정보로 하면 될듯?
















