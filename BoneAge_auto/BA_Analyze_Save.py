from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.common.keys import Keys

from openpyxl import load_workbook
import BA_CONST as BAC
import time
import pywinauto
import pyautogui


def AnalyzeSave_Excel_Patient_Info(logger):
    try:
        # excel load
        load_wb = load_workbook(BAC.EXCEL_Analyze_Save_Edit_Patient_Info_FILE_NAME , data_only=True)
        load_ws = load_wb['Sheet1']

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
            BAC.Analyze_Save_data_Patient.append(row_value)

        #excel_data_set
        for excel_data in BAC.Analyze_Save_data_Patient:
            print(excel_data)

    except Exception as inst:
                logger.error("[ Failed ]  - (Negative_Login_test) Excel load Fail : " + str(inst))



def AnalyzeSave_Load_DCM(driver, logger):
    try:
        ix = 0
        for Upload_file_name in BAC.DCM_FILE_NAME:

            try:
                WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="nav-item-file"]')))
                driver.find_element(By.XPATH, '//*[@id="nav-item-file"]').click()
                WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.ID, "open-filebutton")))
                driver.find_element(By.ID, 'open-filebutton').click()
                time.sleep(1)

                app=pywinauto.Application().connect(title_re="열기")
                logger.info(" -Openfile- : "+ Upload_file_name )
                app["Dialog"]["Edit1"].set_text(Upload_file_name)
                app["Dialog"]["Edit1"].type_keys('{ENTER}')
                print(Upload_file_name)
                time.sleep(1)
            except Exception as inst:
                logger.error("[ Failed ] AnalyzeSave_Load_DCM  : Load To DCM File " + str(inst))

            try:
                driver.find_element_by_name("patient-id").clear()
                WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.NAME, "patient-id")))
                driver.find_element_by_name("patient-id").send_keys(BAC.Analyze_Save_data_Patient[ix][1])

                driver.find_element_by_name("patient-name").clear()
                WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.NAME, "patient-name")))
                driver.find_element_by_name("patient-name").send_keys(BAC.Analyze_Save_data_Patient[ix][2])

                WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="modal-patient-information"]/div[3]/div[2]')))
                driver.find_element(By.XPATH, '//*[@id="modal-patient-information"]/div[3]/div[2]').click()
                time.sleep(2)
            except Exception as inst:
                logger.error("[ Failed ] AnalyzeSave_Load_DCM  : Patient Information Click " + str(inst))


            # WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div[1]/div[2]/div[1]/div[3]/canvas')))
            # driver.find_element(By.XPATH, '/html/body/div[2]/div[1]/div[2]/div[1]/div[3]/canvas').size['height']
            # driver.find_element(By.XPATH, '/html/body/div[2]/div[1]/div[2]/div[1]/div[3]/canvas').size['width']

            # driver.find_element(By.XPATH, '/html/body/div[2]/div[1]/div[2]/div[1]/div[3]/canvas').size['width'] = 200
            # WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div[1]/div[2]/div[1]/div[1]/p[2]')))
            # if (driver.find_element(By.XPATH, '/html/body/div[2]/div[1]/div[2]/div[1]/div[1]/p[2]').text)[13:] != BAC.Analyze_Save_data_Patient[ix][1] : time.sleep(2)

            try:
                WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, 'analyze-button')))
                time.sleep(5)
                driver.find_element(By.ID, 'analyze-button').click()
            except Exception as inst:
                logger.error("[ Failed ] AnalyzeSave_Load_DCM  : analyze-button Click " + str(inst))

            try:
                WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="Female-23"]/div[1]/div[1]')))
                WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, 'save-button')))
                driver.find_element(By.ID, 'save-button').click()
                time.sleep(2)

                WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, 's-patient-height-input')))
                WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, 's-patient-m-height-input')))
                WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, 's-patient-f-height-input')))

                driver.find_element(By.ID, 's-patient-height-input').send_keys(BAC.Analyze_Save_data_Patient[ix][3])
                driver.find_element(By.ID, 's-patient-m-height-input').send_keys(BAC.Analyze_Save_data_Patient[ix][4])
                driver.find_element(By.ID, 's-patient-f-height-input').send_keys(BAC.Analyze_Save_data_Patient[ix][5])

                WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, 'confirm-button')))
                driver.find_element(By.ID, 'confirm-button').click()
                time.sleep(1)

                # driver.find_element(By.CLASS_NAME, 'ui.cancel.button.core-button').click()
                #driver.find_element(By.CLASS_NAME, 'ui.small.modal.transition.visible.active').text  # 이거 텍스트 따서 PASS FAIL 평가 해야 함

                pyautogui.click((BAC.ResolutionX // 2), (BAC.ResolutionY // 4) )
                time.sleep(1)
            except Exception as inst:
                logger.error("[ Failed ] AnalyzeSave_Load_DCM  : Save, Confirm, Modal Form " + str(inst))

            ix += 1  # for문 End에 이거 있어야 함

    except Exception as inst:
        logger.error("[ Failed ] AnalyzeSave_Load_DCM  : " + str(inst))
#--------------------------------------- ( 파일 로드에 대한 체크 어떻게 할 것인지? ) - 환자정보로 하면 될듯?