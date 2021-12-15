
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from openpyxl import load_workbook  #excel lib load

import BA_CONST as BAC
import time



def Positive_Login_Test(driver, logger):
    try:
        WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.NAME, "email")))
        driver.find_element_by_name("email").send_keys("test@vuno.co")
        WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.NAME, "password")))
        driver.find_element_by_name("password").send_keys("Vuno2020!")
        WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, "//html/body/div[2]/div/div/form/button")))
        driver.find_element(By.XPATH, '//html/body/div[2]/div/div/form/button').click()
    except Exception as inst:
            logger.error("[ Failed ] (Positive_Login_test) Login Fail  : " + str(inst))

    try:#----- Logout logic
        time.sleep(2)
        WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.ID, 'user-drop-menu')))
        driver.find_element(By.ID, 'user-drop-menu').click()        
        time.sleep(2)
        WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, '//*[@id="user-drop-menu"]/div/a')))
        driver.find_element(By.XPATH, '//*[@id="user-drop-menu"]/div/a').click()
        #--------------------------------
    except Exception as inst:
            logger.error("[ Failed ] (Positive_Login_test) LogOut Fail  : " + str(inst))


def Negative_Login_Test(driver, logger):
    try:
        # excel load
        load_wb = load_workbook(BAC.EXCEL_Sign_In_FILE_NAME , data_only=True)
        load_ws = load_wb['Sheet1']

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

    except Exception as inst:
                logger.error("[ Failed ]  - (Negative_Login_test) Excel load Fail : " + str(inst))    


    try:
        Excel_Msg_Set = []
        Present_Msg_Set = []

        Excel_Msg_Set.append

        for login_info in all_values:
            driver.find_element_by_id("email").clear()
            driver.find_element_by_id("password").clear()

            driver.find_element_by_id("email").send_keys(str(login_info[1]))
            driver.find_element_by_id("password").send_keys(str(login_info[2]))

            logger.info(" Input [ID/PW] : "+ str(login_info[1]) + "   /   "+ str(login_info[2]))
            WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, "//html/body/div[2]/div/div/form/button")))
            driver.find_element(By.XPATH, '//html/body/div[2]/div/div/form/button').click()

            time.sleep(2)

            Excel_Msg_Set.append( (str(login_info[0]), str(login_info[3]), str(login_info[4])) )

            try:
                Msg1 = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/form/div[1]/div').text
            except:
                Msg1 = ''

            try:
                Msg2 = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/form/div[2]/div').text
            except:
                Msg2 = ''

            print(Msg1)
            print(Msg2)
            Present_Msg_Set.append( (str(login_info[0]), str(Msg1),str(Msg2)) )

            
        # Input value Clear
        driver.find_element_by_id("email").clear()
        driver.find_element_by_id("password").clear()


        Excel_Msg_Set == Present_Msg_Set
        if Excel_Msg_Set == Present_Msg_Set : logger.info(" [ PASS ] : Negative Login Test ")
        else: 
            logger.error(" [ FAILED ] : Negative Login Test ")
            TestNo = 999
            for ix in range(0, len(Excel_Msg_Set)):
                if Excel_Msg_Set[ix] != Present_Msg_Set[ix]: 
                    TestNo = Excel_Msg_Set[ix][0]
                    logger.error(" [ FAILED ] : Negative Login Test - Fail TEST CASE No : [" + str(TestNo) +"]")


    except Exception as inst:
            logger.error("[ FAILED ]  -   : " + str(inst))    