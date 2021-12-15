import os

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
        print(' Error: Search DIR PermissionError ' )


import os


def createFolder(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print('Error: Creating directory. ' + directory)


# For Call by reference
Driver_List = []

# Set Path
DCM_FILE_PATH = "D:\DATA_SET_Original\hand_dump"
DCM_FILE_NAME = search(DCM_FILE_PATH)

LOG_FILE_PATH = DCM_FILE_PATH +"\BA_LOG"
SCREENSHOT_FILE_PATH = DCM_FILE_PATH +"\BA_SCREENSHOT"

EXCEL_Sign_In_FILE_NAME = "Sign_In.xlsx"
EXCEL_Sign_Up_FILE_NAME = "Sign_Up.xlsx"



EXCEL_History_Search_Keyword_FILE_NAME = "History_Search.xlsx"
History_data_Search_keywor= []

EXCEL_Analyze_Save_Edit_Patient_Info_FILE_NAME = "regist_dcm.xlsx"
Analyze_Save_data_Patient= []


# Test Version check
BA_AUTO_TEST = ' ====== BA_AUTO_TEST Ver.2021-06-01-A ====== '

# Mouse function local var
sizeY = 0
ResolutionX = 0
ResolutionY = 0
Move_position = 0
Mouse_Speed = 0.5

Pixel_data_Brightness = []
Pixel_data_Zoom = []
Pixel_data_Move = []