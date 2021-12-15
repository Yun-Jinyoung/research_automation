from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from openpyxl import load_workbook  #excel lib load
import time
import BA_CONST as BAC




def History_Menu_Click(driver, logger):
    try:
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.ID, 'report-button')))
        driver.find_element(By.ID, 'report-button').click()
    except Exception as inst:
        logger.error("[ Failed ] (History_Menu_Click) Click Fail  : " + str(inst))


def History_CLose(driver, logger):
    try:
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="modal-reports"]/div[2]/div')))
        driver.find_element(By.XPATH, '//*[@id="modal-reports"]/div[2]/div').click()
        time.sleep(2)
    except Exception as inst:
        logger.error("[ Failed ] (History_CLose) Click Fail  : " + str(inst))


def History_Search_Click(driver, logger):
    try:
        WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.NAME, "search-input")))

        for excel_data in BAC.History_data_Search_keywor:
            Search_Result_cnt = 0
            driver.find_element_by_name("search-input").clear()
            time.sleep(1)
            driver.find_element_by_name("search-input").send_keys(excel_data[1])
            time.sleep(1)
            WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.CLASS_NAME, 'ui.button.search-button')))
            driver.find_element(By.CLASS_NAME, 'ui.button.search-button').click()
            time.sleep(1)

            page_count_obj_count = len(driver.find_element(By.XPATH, '//*[@id="reports-table"]/div/div/ul').text.split('\n'))

            for ix in range (2, page_count_obj_count):
                driver.find_element(By.XPATH, '//*[@id="reports-table"]/div/div/ul/li[' + str(ix) + ']').click()
                time.sleep(1)
                Search_Result_cnt = Search_Result_cnt + len(driver.find_element_by_id("reports-tbody").text.split('\n'))

            if Search_Result_cnt == 1 and driver.find_element_by_id("reports-tbody").text == 'No search reports' :
                Search_Result_cnt = Search_Result_cnt -1
                continue

            if Search_Result_cnt != int(excel_data[2]) :
                logger.error("[ Failed ] (History_Search_Click) Not Matched | Expected Count" + str(Search_Result_cnt) +' : ' +str(excel_data[1])+' | '+ str(excel_data[2]))

    except Exception as inst:
        logger.error("[ Failed ] (History_Search_Click) Click Fail  : " + str(inst))




def History_Excel_Search_Keyword(logger):
    try:
        # excel load
        load_wb = load_workbook(BAC.EXCEL_History_Search_Keyword_FILE_NAME , data_only=True)
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
            BAC.History_data_Search_keywor.append(row_value)

        #excel_data_set
        for excel_data in BAC.History_data_Search_keywor:
            print(excel_data)

    except Exception as inst:
                logger.error("[ Failed ]  - (History_Excel_Search_Keyword) Excel load Fail : " + str(inst))