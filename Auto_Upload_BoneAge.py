from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import pywinauto
import time
import os
import subprocess
import logging
import datetime

import pyautogui
from PIL import ImageGrab

import logging
from win32api import GetSystemMetrics


def search(dirname):
    try:
        filenames = os.listdir(dirname)
        search_fname_set = []
        for filename in filenames:
            full_filename = os.path.join(dirname, filename)
            if os.path.isdir(full_filename):
                search(full_filename)
            else:
                ext = os.path.splitext(full_filename)[-1]
                if ext == '.dcm': 
                    print(full_filename)
                    search_fname_set.append(full_filename)
        return search_fname_set
    except PermissionError:
        pass


def Compare_RGB_Point(Pixel_data_set, function_type):
    diff_count = 0
    for ix in range(0,3):
        if Pixel_data_set[ix] == Pixel_data_set[ix+3] : print('same')
        else : diff_count+=1    # diff count세어야 함 Differ count가 2 이상일 때 정상인걸로
    if diff_count >= 2 : logger.info(" [ PASS ] Pixel_data_set " + function_type + ' : ' + str(diff_count))
    else : logger.error("[ Failed ] Pixel_data_set " + function_type + ' : ' + str(diff_count))


def Use_Mouse_function(Pixel_data_set,  DCM_FILE_PATH, screenshot_time, ResolutionX, ResolutionY ,Move_position, shot_image_name, way_to_move):
    if way_to_move == 'STD_origin' : print('None')
    elif way_to_move == 'LB_Go_right' : pyautogui.dragTo((ResolutionX//2) + Move_position,(ResolutionY//2), Mouse_Speed, button='left')
    elif way_to_move == 'LB_Go_left' : pyautogui.dragTo((ResolutionX//2) - Move_position,(ResolutionY//2), Mouse_Speed, button='left')
    elif way_to_move == 'LB_Go_up' : pyautogui.dragTo((ResolutionX//2),(ResolutionY//2) - Move_position, Mouse_Speed, button='left')
    elif way_to_move == 'LB_Go_down' : pyautogui.dragTo((ResolutionX//2),(ResolutionY//2) + Move_position, Mouse_Speed, button='left')

    screen = pyautogui.screenshot(DCM_FILE_PATH+"\\"+str(screenshot_time)+str(shot_image_name))
    pyautogui.moveTo((ResolutionX//2), (ResolutionY//2))
    Temp_pixel = screen.getpixel(pyautogui.position())
    Pixel_data_set.append(Temp_pixel)


def Use_Mouse_function2(Pixel_data_set,  DCM_FILE_PATH, screenshot_time, ResolutionX, ResolutionY ,Move_position, shot_image_name, way_to_move):
    pyautogui.moveTo((ResolutionX//2), (ResolutionY//2))
    if way_to_move == 'RB_Go_down' : pyautogui.dragTo((ResolutionX//2),(ResolutionY//2) - Move_position, Mouse_Speed, button='right')
    elif way_to_move == 'RB_Go_up' : pyautogui.dragTo((ResolutionX//2),(ResolutionY//2) + Move_position, Mouse_Speed, button='right')
    elif way_to_move == 'MB_Go_down' : pyautogui.dragTo((ResolutionX//2),(ResolutionY//2) - Move_position, Mouse_Speed, button='middle')
    elif way_to_move == 'MB_Go_up' : pyautogui.dragTo((ResolutionX//2),(ResolutionY//2) + Move_position, Mouse_Speed, button='middle')


    screen = pyautogui.screenshot(DCM_FILE_PATH+"\\"+str(screenshot_time)+str(shot_image_name))

    # 3 point Screen shot - start
    pyautogui.moveTo((ResolutionX//2), (ResolutionY//2) + Move_position )
    Temp_pixel = screen.getpixel(pyautogui.position())
    Pixel_data_set.append(Temp_pixel)    

    pyautogui.moveTo((ResolutionX//2), (ResolutionY//2))
    Temp_pixel = screen.getpixel(pyautogui.position())
    Pixel_data_set.append(Temp_pixel)    

    pyautogui.moveTo((ResolutionX//2), (ResolutionY//2) - Move_position)
    Temp_pixel = screen.getpixel(pyautogui.position())
    Pixel_data_set.append(Temp_pixel)            
    # 3 point Screen shot - end



DCM_FILE_PATH = "D:\DATA_SET_Original\hand_dump"
DCM_FILE_NAME = search(DCM_FILE_PATH)


logger = logging.getLogger("[ Bone Age ]")
logger.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(name)s - %(asctime)s - %(levelname)s|[%(lineno)d]|:%(message)s')

ErrorHandler = logging.FileHandler(DCM_FILE_PATH+'\\'+"_Test_Result.log", encoding='utf-8')
ErrorHandler.setLevel(logging.DEBUG)
ErrorHandler.setFormatter(formatter)
logger.addHandler(ErrorHandler)

logger.info(" ==========  "+ time.strftime('%Y_%m%d_%H_%M', time.localtime(time.time())) + " TEST START ========== ")

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()

try:
    driver.get('https://192.168.50.39:5000')    # CXR-TC-002      HTTPS
except Exception as inst:
        logger.error("[ Failed ] CXR-TC-002 - Connect HTTPS Fail : " + str(inst))

try:
    driver.get('http://192.168.50.39:5000')    # CXR-TC-001     HTTP
except Exception as inst:
        logger.error("[ Failed ] CXR-TC-001 - Connect HTTP Fail  : " + str(inst))


try:
    WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.NAME, "email")))
    driver.find_element_by_name("email").send_keys("test@vuno.co")
    WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.NAME, "password")))
    driver.find_element_by_name("password").send_keys("Vuno2020!")
    WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, "//html/body/div[2]/div/div/form/button")))
    driver.find_element(By.XPATH, '//html/body/div[2]/div/div/form/button').click()
    aaa = driver.find_elements_by_xpath()

except Exception as inst:
        logger.error("[ Failed ] CXR-TC-003 - Login Fail  : " + str(inst))



try:
    for Upload_file_name in DCM_FILE_NAME:
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
        break  # break 를 제거하면 선택 폴더 하위 폴더 파일 까지 모두 업로드 한다. 
except Exception as inst:
        logger.error("[ Failed ] CXR-TC-004 - File Load Fail  : " + str(inst))


# content = driver.find_element_by_class_name('image')

sizeY = 0
while sizeY == 0:
    content = driver.find_element_by_class_name('image')
    sizeX = content.size['width']
    sizeY = content.size['height']
    print('not yet')
    time.sleep(1)

print("Width =", GetSystemMetrics(0))
print("Height =", GetSystemMetrics(1))


ResolutionX = GetSystemMetrics(0)
ResolutionY = GetSystemMetrics(1)
Move_position = (sizeY/2)
Mouse_Speed = 0.5

screenshot_time = time.strftime('%Y_%m%d_%H_%M', time.localtime(time.time()))


Pixel_data_Brightness = []
Pixel_data_Zoom = []
Pixel_data_Move = []

try:
# brightness
    time.sleep(1)
    print('STD_origin')    
    Use_Mouse_function(Pixel_data_Brightness, DCM_FILE_PATH, screenshot_time, ResolutionX, ResolutionY, Move_position, '_1_origin_.png', 'STD_origin')

    print('LB_Go_right')
    Use_Mouse_function(Pixel_data_Brightness, DCM_FILE_PATH, screenshot_time, ResolutionX, ResolutionY, Move_position, '_2_right.png', 'LB_Go_right')    

    print('LB_Go_left')
    Use_Mouse_function(Pixel_data_Brightness, DCM_FILE_PATH, screenshot_time, ResolutionX, ResolutionY, Move_position, '_3_left.png', 'LB_Go_left')    

    print('LB_Go_up')
    Use_Mouse_function(Pixel_data_Brightness, DCM_FILE_PATH, screenshot_time, ResolutionX, ResolutionY, Move_position, '_4_up.png', 'LB_Go_up')    

    print('LB_Go_down')
    Use_Mouse_function(Pixel_data_Brightness, DCM_FILE_PATH, screenshot_time, ResolutionX, ResolutionY, Move_position, '_5_down.png', 'LB_Go_down')

    logger.info(" Pixel_data_Brightness - 밝기를 조절 했을 경우의 동일 포인트 값 / 5개중 2개의 값은 달라야" )
    logger.info(" Pixel_data_Brightness : "+ str(Pixel_data_Brightness) )

    # Check Start 지정 픽셀 밝기를 비교하여 기능이 동작하는지 대략적으로 체크 함 
    diff_count = 0
    jx = 5
    for Temp_data in Pixel_data_Brightness:
        jx-=1
        for ix in range(len(Pixel_data_Brightness) - jx, len(Pixel_data_Brightness)):
            if Temp_data == Pixel_data_Brightness[ix] : print('same')
            else : diff_count+=1    # diff count세어야 함 Differ count가 2 이상일 때 정상인걸로
    if diff_count >= 2 : logger.info(" [ PASS ] Pixel_data_Brightness check : "  + str(diff_count))
    else : logger.error("[ Failed ] Pixel_data_Brightness  : " + str(diff_count))
    # Check End --------------------------------------------------------------------------------
        
except Exception as inst:
        logger.error("[ Failed ] CXR-TC-005 - Change the brightness using a mouse Fail  : " + str(inst))

try:
# Zoom
    print('RB_Go_down')
    Use_Mouse_function2(Pixel_data_Zoom,  DCM_FILE_PATH, screenshot_time, ResolutionX, ResolutionY ,Move_position, '_6_Zoom_out.png', 'RB_Go_down')

    print('RB_Go_up')
    Use_Mouse_function2(Pixel_data_Zoom,  DCM_FILE_PATH, screenshot_time, ResolutionX, ResolutionY ,Move_position, '_7_Zoom_in.png', 'RB_Go_up')    

    logger.info(" Pixel_data_Zoom - Zoom 하게 되면 3포인트 샘플 RGB를 추출하고 그중 2개는 값이 다를 것이라 예상 해당 경우 " )
    logger.info(" Pixel_data_Zoom       : "+ str(Pixel_data_Zoom) )

    Compare_RGB_Point(Pixel_data_Zoom, 'Zoom')




except Exception as inst:
        logger.error("[ Failed ] CXR-TC-006 - Change Size using mouse Fail  : " + str(inst))    


try:
# Image Move
    print('MB_Go_down') #MB - Middle button
    Use_Mouse_function2(Pixel_data_Move,  DCM_FILE_PATH, screenshot_time, ResolutionX, ResolutionY ,Move_position, '_8_Image_Move.png', 'MB_Go_down')    

    print('MB_Go_up')
    Use_Mouse_function2(Pixel_data_Move,  DCM_FILE_PATH, screenshot_time, ResolutionX, ResolutionY ,Move_position, '_9_Image_Move.png', 'MB_Go_up')        

    logger.info(" Pixel_data_Move - Move 하게 되면 3포인트 샘플 RGB를 추출하고 그중 2개는 값이 다를 것이라 예상 해당 경우 " )
    logger.info(" Pixel_data_Move       : "+ str(Pixel_data_Move) )

    Compare_RGB_Point(Pixel_data_Move, 'Move')

except Exception as inst:
        logger.error("[ Failed ] CXR-TC-006 - Change Size using mouse Fail  : " + str(inst))            


# End Test Message
logger.info("==========  "+ time.strftime('%Y_%m%d_%H_%M', time.localtime(time.time())) + " TEST End ==========")
pyautogui.alert(text='Test Complete!', title='End Test')

