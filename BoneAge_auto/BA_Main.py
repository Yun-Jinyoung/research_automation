from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import logging
import sys
import time
from win32api import GetSystemMetrics

#----- import sub lib call func
import BA_CONST as BAC 
import BA_Sign_In
import BA_Sign_up
import BA_m_Received_Files
import BA_m_Open_File
import BA_m_Mouse_Function
import BA_Help
import BA_History
import BA_Analyze_Save
#-------------------------------

#----- Init Share Dataset 
Received_P_Info_SData = []
#-------------------------

#----- Init Folder
BAC.createFolder(BAC.LOG_FILE_PATH)
BAC.createFolder(BAC.SCREENSHOT_FILE_PATH)
#-----------------------------------------

#----- Init logger 
logger = logging.getLogger("[ Bone Age ]")
logger.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(name)s - %(asctime)s - %(levelname)s|[%(lineno)d]|:%(message)s')

File_time = time.strftime('%Y_%m%d_%H_%M', time.localtime(time.time()))

ErrorHandler = logging.FileHandler(BAC.LOG_FILE_PATH+'\\'+File_time+"_Test_Result.log", encoding='utf-8')
ErrorHandler.setLevel(logging.DEBUG)
ErrorHandler.setFormatter(formatter)
logger.addHandler(ErrorHandler)
#----------------

logger.info("  ")
logger.info(BAC.BA_AUTO_TEST)
logger.info(" ========== -----  TEST START  ----- ========== ")

#----- Chrome Browser Init 
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()

# List에 담아서 사용하지 않으면 이는 단순히 Call by Value로 취급되어
# (BAC.Driver_List[0]).switch_to_window(driver.window_handles[1]) 같은 처리의 경우 복사체의 값만 변경되고
# 정작 컨트롤 하려는 원본은 바뀌지 않아 의도대로 움직이지 않는다.
BAC.Driver_List.append(driver)

BAC.ResolutionX = GetSystemMetrics(0)  #BA_CONST에서 INIT하면 2460으로 잡혀서 여기서 Init한다.
BAC.ResolutionY = GetSystemMetrics(1)  #Python 스크립트 언어라서 선언이나 값 처리 시점에 따라 값이 변하기도 하는 것으로 보인다. 언어 특성 체크
#---------------------------------------


#----- ReConnect -  correct log in
def BA_Login():
	try:
			WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.NAME, "email")))
			driver.find_element_by_name("email").send_keys("test@vuno.co")
			WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.NAME, "password")))
			driver.find_element_by_name("password").send_keys("Vuno2020!")
			WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, "//html/body/div[2]/div/div/form/button")))
			driver.find_element(By.XPATH, '//html/body/div[2]/div/div/form/button').click()
	except Exception as inst:
			logger.error("[ Failed ] CXR-TC-003 - Login Fail  : " + str(inst))
#---------------------------------------        



#----- HTTP / HTTPS CONNECT TEST
try:
	driver.get('https://192.168.50.39:5000')    #  HTTPS
except Exception as inst:
		Init_browse_check = 1
		logger.error("[ Check ] Connect HTTPS Fail : " + str(inst))

try:
	driver.get('http://192.168.50.39:5000')     #  HTTP
except Exception as inst:
		Init_browse_check = 0
		logger.error("[ Check ]  Connect HTTP Fail  : " + str(inst))

if Init_browse_check == 0 : driver.get('https://192.168.50.39:5000')     #  HTTPS
else : driver.get('http://192.168.50.39:5000')    #  HTTP
#---------------------------------------

# 클릭이 빠른경우 정지하거나 내부로직이 충돌나는 경우가 있다. 구간 별로 sleep을 적절하게 줘야한다.
# driver.implicitly_wait(3) 이걸 줘봤는데 이건 UI까지만 커버하는거고 문제 되는건 내부 로직 포함이다.

#----- Sign-In Test Part   (complete)
BA_Sign_In.Positive_Login_Test(driver, logger)
BA_Sign_In.Negative_Login_Test(driver, logger)
#---------------------------------------

#----- Sign-Up Test Part   (complete)  #대소문자 체크
BA_Sign_up.Positive_Sign_Up_Test(driver, logger)
BA_Sign_up.Negative_Sign_Up_Test(driver, logger)
#---------------------------------------

#------------------------ Coding Area -----------------------
BA_Login()
BA_Analyze_Save.AnalyzeSave_Excel_Patient_Info(logger)# Excel Data Init Load - Patient
BA_Analyze_Save.AnalyzeSave_Load_DCM(driver, logger)
#------------------------------------------------------------

#------------------------ Coding Area -----------------------
BA_History.History_Excel_Search_Keyword(logger) # Excel Data Init Load
BA_History.History_Menu_Click(driver, logger)
BA_History.History_Search_Click(driver, logger)
BA_History.History_CLose(driver, logger)
#------------------------------------------------------------

#----- Received Files
BA_m_Received_Files.Received_Menu_Click(driver, logger)
BA_m_Received_Files.Received_List_File_Click(driver, logger)
BA_m_Received_Files.Popup_Patient_Infomation_Ctrl(driver, logger)
#---------------------------------------

#----- Open DCM Files
BA_m_Open_File.BA_DCM_File_load(driver, logger)
#---------------------------------------

#----- HELP
BA_Help.Help_Menu_Click(driver, logger)
BA_Help.Help_load_text_check(driver, logger, 'Label','text', '//*[@id="service-info"]/div[2]/table/tbody/tr[1]/td', '//*[@id="generate-barcode"]/p', 'Label.txt')
BA_Help.HELP_InstructionForUse_Check(driver, logger)
BA_Help.Help_load_text_check(driver, logger, 'Terms and Conditions','get_attribute', '//*[@id="service-info"]/div[2]/table/tbody/tr[3]/td', '//*[@id="service-info"]/div[2]/div/div[3]/div/textarea[1]', 'TermsAndConditions.txt')
BA_Help.Help_load_text_check(driver, logger, 'Opensource License','text', '//*[@id="service-info"]/div[2]/table/tbody/tr[4]/td', '//*[@id="service-info"]/div[2]/div/div[4]/article', 'OpensourceLicense.txt')
BA_Help.Help_Close(driver, logger)
#---------------------------------------

#----- Mouse Image Function Check
BA_m_Mouse_Function.Mouse_Image_Init(driver, logger)
BA_m_Mouse_Function.Mouse_Image_Brightness(logger)
BA_m_Mouse_Function.Mouse_Image_Zoom(logger)
BA_m_Mouse_Function.Mouse_Image_Move(logger)
#---------------------------------------

logger.info(" ========== -----  TEST END  ----- ========== ")
logger.info("  ")
sys.exit("종료")