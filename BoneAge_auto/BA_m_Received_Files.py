from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time

Click_file_data = []

def Received_Menu_Click(driver, logger):

    try:
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div[2]/div[1]/div[2]')))
        driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[1]/div[2]').click()
    except Exception as inst:
            logger.error("[ Failed ] (Received_Menu_Click) Click Fail  : " + str(inst))


def Received_List_File_Click(driver, logger):


    try:
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div[2]/div[1]/div[3]/div[3]/a[1]/div')))
        #Click_file_data 리스트에 대입하면 함수를 벗어나면 데이터가 날아감  But append 하면 데이터가 유지되어 append 합니다.
        Click_file_data.append((driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[1]/div[3]/div[3]/a[1]/div').text).split())
    except Exception as inst:
        logger.error("[ Failed ] (Received_List_File_Click) Click Data Collect Fail  : " + str(inst))


    try:
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div[2]/div[1]/div[3]/div[3]/a[1]/div')))
        driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[1]/div[3]/div[3]/a[1]/div').click()
    except Exception as inst:
            logger.error("[ Failed ] (Received_List_File_Click) Click Fail  : " + str(inst))


def Popup_Patient_Infomation_Ctrl(driver, logger):

    try:
        # driver.implicitly_wait(3) #임의 로딩 대기 함수 실제 동작에 대해서 확인하고 향후에 전체적으로 time.sleep대신에 쓸지 안쓸지 확인해서 사용

        # Received file 리스트를 리스트에 담는다.
        # 자동화는 어느 데이터를 선택할지 알고 있기 때문에 세팅된 데이터와 함께 처리해라
        # print('File List')
        #<div class=aaa>  abcd   </div>  abcd 추출 코드
        # print(driver.find_element(By.XPATH, '//*[@id="filelist-body"]/div[1]').get_attribute("innerHTML"))
        # print(driver.find_element(By.XPATH, '//*[@id="filelist-body"]/div[2]').get_attribute("innerHTML"))
        # print(driver.find_element(By.XPATH, '//*[@id="filelist-body"]/div[3]').get_attribute("innerHTML"))
        # print(driver.find_element(By.XPATH, '//*[@id="filelist-body"]/div[4]').get_attribute("innerHTML"))
        # print(driver.find_element(By.XPATH, '//*[@id="filelist-body"]/div[5]').get_attribute("innerHTML"))
        # print('File List End')



        #팝업된 창의 데이터  ( 환자ID / 환자이름 / 성별 / 태어난날 / 분석일자 )
        print('Popup Data Start')

        Patient_Id = driver.find_element(By.XPATH, '//*[@id="patient-id"]').get_attribute("value")
        Patient_Name = driver.find_element(By.XPATH, '//*[@id="patient-name"]').get_attribute("value")
        Sex_Value = list(driver.find_element(By.CLASS_NAME, 'ui.button.sex-button.checkbox-button.active').text)
        Birth_date = driver.find_element(By.XPATH, '//*[@id="date-of-birth"]').get_attribute("value")
        Study_date = driver.find_element(By.XPATH, '//*[@id="date-of-study"]').get_attribute("value")

        if Click_file_data[0][0] != Patient_Id : logger.error("[ Failed ] (Popup_Patient_Infomation_Ctrl) Data Mismatched [ Patient_Id ]")
        if Click_file_data[0][1] != Patient_Name : logger.error("[ Failed ] (Popup_Patient_Infomation_Ctrl) Data Mismatched [ Patient_Name ]")
        if Click_file_data[0][2] != Sex_Value[0] : logger.error("[ Failed ] (Popup_Patient_Infomation_Ctrl) Data Mismatched [ Sex_Value ]")
        if Click_file_data[0][3] != Birth_date : logger.error("[ Failed ] (Popup_Patient_Infomation_Ctrl) Data Mismatched [ Birth_date ]")
        if Click_file_data[0][4] != Study_date : logger.error("[ Failed ] (Popup_Patient_Infomation_Ctrl) Data Mismatched [ Study_date ]")

        time.sleep(2)
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="modal-patient-information"]/div[3]/div[2]')))
        driver.find_element(By.XPATH, '//*[@id="modal-patient-information"]/div[3]/div[2]').click()
        time.sleep(5)

    except Exception as inst:
            logger.error("[ Failed ] (Popup_Patient_Infomation_Ctrl) Ctrl Fail  : " + str(inst))