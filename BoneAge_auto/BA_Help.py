from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import BA_CONST as BAC
import time
import pyautogui

def Help_Menu_Click(driver, logger):
    try:
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="nav-item-file"]')))
        driver.find_element(By.XPATH, '//*[@id="nav-item-file"]').click()

        WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="service-info-btn"]')))
        driver.find_element(By.XPATH, '//*[@id="service-info-btn"]').click()
    except Exception as inst:
            logger.error("[ Failed ] (Help_Menu_Click) Click Fail  : " + str(inst))


def Help_load_text_check(driver, logger, function_name, get_text_type,click_xpath, show_text_xpath, l_filename):
    try:
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, click_xpath)))
        driver.find_element(By.XPATH, click_xpath).click()

        logger.info( ' ----- ('+function_name + ')   Check [ start ]' )
        if get_text_type == 'get_attribute' : Current_Label = (driver.find_element(By.XPATH, show_text_xpath).get_attribute("value")).split('\n')
        if get_text_type == 'text' : Current_Label = (driver.find_element(By.XPATH, show_text_xpath).text).split('\n')

        f = open( "C:\\Users\\dell\\Documents\\GitHub\\Login_test\\BoneAge_auto\\"+l_filename, mode='rt', encoding='utf-8')

        if len(Current_Label) != len(f.readlines()) : logger.error("[ Failed ] (Help_load_text_check)  Label Text line Count is not samed " )
        f.seek(0)

        for row_text in Current_Label:
            Lasted_Label = f.readline()
            if row_text != (Lasted_Label).strip('\n') :
                logger.error("[ Failed ] (HELP_Label_Check) Label Text not Matched " )
                logger.info( row_text )
                logger.info((Lasted_Label).strip('\n'))
        f.close()

        logger.info( ' ----- ('+function_name + ')   Check [ End ]' )
        logger.info('')
        print(Lasted_Label)

    except Exception as inst:
        logger.error("[ Failed ] (Help_load_text_check) Click Data Collect Fail  : " + str(inst))




def HELP_InstructionForUse_Check(driver, logger):
    try:
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="service-info"]/div[2]/table/tbody/tr[2]/td')))
        driver.find_element(By.XPATH, '//*[@id="service-info"]/div[2]/table/tbody/tr[2]/td').click()

        WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="service-info"]/div[2]/div/div[2]/div/a')))
        driver.find_element(By.XPATH, '//*[@id="service-info"]/div[2]/div/div[2]/div/a').click()

        # driver.switch_to_window(driver.window_handles[1]) <== Call by value로 처리되어 본체의 탭에 접근이 안된다.
        # BAC.Driver 즉 Driver를 Python의 Call by reference로 동작하도록 List에 담아 전달하여 switch_to_window 동작을 처리 하도록 한다.
        (BAC.Driver_List[0]).switch_to_window(driver.window_handles[1])
        time.sleep(2)
        screenshot_time = time.strftime('%Y_%m%d_%H_%M', time.localtime(time.time()))
        pyautogui.screenshot(BAC.SCREENSHOT_FILE_PATH + "\\" + str(screenshot_time) + '_DeepBrain_Menual.png')
        logger.info("Load page : " + driver.current_url)
        (BAC.Driver_List[0]).switch_to_window(driver.window_handles[0])
    except Exception as inst:
        logger.error("[ Failed ] (HELP_InstructionForUse_Check) Click Data Collect Fail  : " + str(inst))


def Help_Close(driver, logger):
    try:
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="service-info"]/div[1]/div[2]')))
        driver.find_element(By.XPATH, '//*[@id="service-info"]/div[1]/div[2]').click()
    except Exception as inst:
        logger.error("[ Failed ] (Help_Close) Click Data Collect Fail  : " + str(inst))



