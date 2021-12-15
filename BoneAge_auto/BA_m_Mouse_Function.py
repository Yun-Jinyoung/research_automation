# from selenium import webdriver
# from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# from openpyxl import load_workbook  #excel lib load
#

import BA_CONST as BAC
import time
import pyautogui





def Compare_RGB_Point(Pixel_data_set, function_type, logger):
    try:
        diff_count = 0
        for ix in range(0,3):
            if Pixel_data_set[ix] == Pixel_data_set[ix+3] : print('same')
            else : diff_count+=1    # diff count세어야 함 Differ count가 2 이상일 때 정상인걸로
        if diff_count >= 2 : logger.info(" [ PASS ] Pixel_data_set " + function_type + ' : ' + str(diff_count))
        else : logger.error("[ Failed ] (Compare_RGB_Point) Pixel_data_set " + function_type + ' : ' + str(diff_count))
    except Exception as inst:
        logger.error("[ Failed ] (Compare_RGB_Point) ")


def Use_Mouse_function(Pixel_data_set,  SCREENSHOT_FILE_PATH, logger, ResolutionX, ResolutionY ,Move_position, shot_image_name, way_to_move):

    try:
        screenshot_time = time.strftime('%Y_%m%d_%H_%M', time.localtime(time.time()))

        if way_to_move == 'STD_origin' : print('None')
        elif way_to_move == 'LB_Go_right' : pyautogui.dragTo((ResolutionX//2) + Move_position,(ResolutionY//2), BAC.Mouse_Speed, button='left')
        elif way_to_move == 'LB_Go_left' : pyautogui.dragTo((ResolutionX//2) - Move_position,(ResolutionY//2), BAC.Mouse_Speed, button='left')
        elif way_to_move == 'LB_Go_up' : pyautogui.dragTo((ResolutionX//2),(ResolutionY//2) - Move_position, BAC.Mouse_Speed, button='left')
        elif way_to_move == 'LB_Go_down' : pyautogui.dragTo((ResolutionX//2),(ResolutionY//2) + Move_position, BAC.Mouse_Speed, button='left')

        screen = pyautogui.screenshot(SCREENSHOT_FILE_PATH+"\\"+str(screenshot_time)+str(shot_image_name))
        pyautogui.moveTo((ResolutionX//2), (ResolutionY//2))
        Temp_pixel = screen.getpixel(pyautogui.position())
        Pixel_data_set.append(Temp_pixel)
    except Exception as inst:
        logger.error("[ Failed ] (Use_Mouse_function) ")


def Use_Mouse_function2(Pixel_data_set,  SCREENSHOT_FILE_PATH, logger, ResolutionX, ResolutionY ,Move_position, shot_image_name, way_to_move):

    try:
        screenshot_time = time.strftime('%Y_%m%d_%H_%M', time.localtime(time.time()))

        pyautogui.moveTo((ResolutionX//2), (ResolutionY//2))
        if way_to_move == 'RB_Go_down' : pyautogui.dragTo((ResolutionX//2),(ResolutionY//2) - Move_position, BAC.Mouse_Speed, button='right')
        elif way_to_move == 'RB_Go_up' : pyautogui.dragTo((ResolutionX//2),(ResolutionY//2) + Move_position, BAC.Mouse_Speed, button='right')
        elif way_to_move == 'MB_Go_down' : pyautogui.dragTo((ResolutionX//2),(ResolutionY//2) - Move_position, BAC.Mouse_Speed, button='middle')
        elif way_to_move == 'MB_Go_up' : pyautogui.dragTo((ResolutionX//2),(ResolutionY//2) + Move_position, BAC.Mouse_Speed, button='middle')


        screen = pyautogui.screenshot(SCREENSHOT_FILE_PATH+"\\"+str(screenshot_time)+str(shot_image_name))

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
    except Exception as inst:
        logger.error("[ Failed ] (Use_Mouse_function 2 ) ")



def Mouse_Image_Brightness(logger):
    try:
        screenshot_time = time.strftime('%Y_%m%d_%H_%M', time.localtime(time.time()))

        # brightness
        time.sleep(1)
        print('STD_origin')
        Use_Mouse_function(BAC.Pixel_data_Brightness, BAC.SCREENSHOT_FILE_PATH, logger, BAC.ResolutionX, BAC.ResolutionY, BAC.Move_position,
                           '_1_origin_.png', 'STD_origin')

        print('LB_Go_right')
        Use_Mouse_function(BAC.Pixel_data_Brightness, BAC.SCREENSHOT_FILE_PATH, logger, BAC.ResolutionX, BAC.ResolutionY, BAC.Move_position,
                           '_2_right.png', 'LB_Go_right')

        print('LB_Go_left')
        Use_Mouse_function(BAC.Pixel_data_Brightness, BAC.SCREENSHOT_FILE_PATH, logger, BAC.ResolutionX, BAC.ResolutionY, BAC.Move_position,
                           '_3_left.png', 'LB_Go_left')

        print('LB_Go_up')
        Use_Mouse_function(BAC.Pixel_data_Brightness, BAC.SCREENSHOT_FILE_PATH, logger, BAC.ResolutionX, BAC.ResolutionY, BAC.Move_position,
                           '_4_up.png', 'LB_Go_up')

        print('LB_Go_down')
        Use_Mouse_function(BAC.Pixel_data_Brightness, BAC.SCREENSHOT_FILE_PATH, logger, BAC.ResolutionX, BAC.ResolutionY, BAC.Move_position,
                           '_5_down.png', 'LB_Go_down')

        logger.info(" Pixel_data_Brightness - 밝기를 조절 했을 경우의 동일 포인트 값 / 5개중 2개의 값은 달라야")
        logger.info(" Pixel_data_Brightness : " + str(BAC.Pixel_data_Brightness))

        # Check Start 지정 픽셀 밝기를 비교하여 기능이 동작하는지 대략적으로 체크 함
        diff_count = 0
        jx = 5
        for Temp_data in BAC.Pixel_data_Brightness:
            jx -= 1
            for ix in range(len(BAC.Pixel_data_Brightness) - jx, len(BAC.Pixel_data_Brightness)):
                if Temp_data == BAC.Pixel_data_Brightness[ix]:
                    print('same')
                else:
                    diff_count += 1  # diff count세어야 함 Differ count가 2 이상일 때 정상인걸로
        if diff_count >= 2:
            logger.info(" [ PASS ] Pixel_data_Brightness check : " + str(diff_count))
        else:
            logger.error("[ Failed ] Pixel_data_Brightness  : " + str(diff_count))
    # Check End --------------------------------------------------------------------------------

    except Exception as inst:
        logger.error("[ Failed ] (Mouse_Image_Brightness) - Change the brightness using a mouse Fail  : " + str(inst))



def Mouse_Image_Zoom(logger):
    try:
        screenshot_time = time.strftime('%Y_%m%d_%H_%M', time.localtime(time.time()))

        # Zoom
        print('RB_Go_down')
        Use_Mouse_function2(BAC.Pixel_data_Zoom, BAC.SCREENSHOT_FILE_PATH, logger, BAC.ResolutionX, BAC.ResolutionY, BAC.Move_position,
                            '_6_Zoom_out.png', 'RB_Go_down')

        print('RB_Go_up')
        Use_Mouse_function2(BAC.Pixel_data_Zoom, BAC.SCREENSHOT_FILE_PATH, logger, BAC.ResolutionX, BAC.ResolutionY, BAC.Move_position,
                            '_7_Zoom_in.png', 'RB_Go_up')

        logger.info(" Pixel_data_Zoom - Zoom 하게 되면 3포인트 샘플 RGB를 추출하고 그중 2개는 값이 다를 것이라 예상 해당 경우 ")
        logger.info(" Pixel_data_Zoom       : " + str(BAC.Pixel_data_Zoom))

        Compare_RGB_Point(BAC.Pixel_data_Zoom, 'Zoom', logger)

    except Exception as inst:
        logger.error("[ Failed ] (Mouse_Image_Zoom) - Change Size using mouse Fail  : " + str(inst))



def Mouse_Image_Move(logger):
    try:
        screenshot_time = time.strftime('%Y_%m%d_%H_%M', time.localtime(time.time()))

        # Image Move
        print('MB_Go_down')  # MB - Middle button
        Use_Mouse_function2(BAC.Pixel_data_Move, BAC.SCREENSHOT_FILE_PATH, logger, BAC.ResolutionX, BAC.ResolutionY, BAC.Move_position,
                            '_8_Image_Move.png', 'MB_Go_down')

        print('MB_Go_up')
        Use_Mouse_function2(BAC.Pixel_data_Move, BAC.SCREENSHOT_FILE_PATH, logger, BAC.ResolutionX, BAC.ResolutionY, BAC.Move_position,
                            '_9_Image_Move.png', 'MB_Go_up')

        logger.info(" Pixel_data_Move - Move 하게 되면 3포인트 샘플 RGB를 추출하고 그중 2개는 값이 다를 것이라 예상 해당 경우 ")
        logger.info(" Pixel_data_Move       : " + str(BAC.Pixel_data_Move))

        Compare_RGB_Point(BAC.Pixel_data_Move, 'Move', logger)

    except Exception as inst:
        logger.error("[ Failed ] (Mouse_Image_Move) - Change Size using mouse Fail  : " + str(inst))


def Mouse_Image_Init(driver, logger):
    WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.CLASS_NAME, 'image')))
    try:
        while BAC.sizeY == 0:
            # print('456')
            content = driver.find_element_by_class_name('image')
            BAC.sizeY = content.size['height']
            print('not yet')
            time.sleep(1)

        BAC.Move_position = (BAC.sizeY/2)
    except Exception as inst:
        logger.error("[ Failed ] Mouse_Image_Init - Change Size using mouse Fail  : " + str(inst))


