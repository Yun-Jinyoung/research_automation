# 본 에이지 DCM 파일 자동으로 올리기
[ Auto_Upload_BoneAge.py ]
pip install pywinauto  설치 

소스에서 아래 라인을 반복 하면서 upload 가 진행 됩니다. 
    app=Application().connect(title_re="열기")
    app["Dialog"]["Edit1"].TypeKeys(Upload_file_name) 
    app["Dialog"]["Button1"].click()

Upload_file_name은 def search(dirname): 함수에서 지정 폴더 아래의 모든 파일을 리스트화 시켜서 가져 옵니다.

[ 테스트시 커스텀 수정은 파일 검색 폴더 경로만 지정 하면 됩니다.]
DCM_FILE_PATH = search("D:\DATA_SET_Original\hand_dump")


[ 마우스 이동에 따른 명도 값 변화 체크 ]
1. 스크린샷
2. RGB값 체크 
origin (0, 0, 0)
right (67, 67, 67)
left (0, 0, 0)        <--   origin (0, 0, 0) 하고 같은 값을 가져야 함
up (255, 255, 255)
down (0, 0, 0)        <--   origin (0, 0, 0) 하고 같은 값을 가져야 함



# 로그인 자동화 테스트 ( 엑셀 파일 로그인 테이터이용 로그인 시도 )
[ Login_test.py ]
인수 테스트 중 Login테스트 자동화를 위한 업무 진행중


[ 진행중 ]
1. 일반적인 로그인 테스를 위해 Element name, id , xpath등을 이용하여 동작을 시키거나 값을 넣는다. 
2. 로그인에 필요한 값을 넣는 동작은 Excel파일 데이터를 이용하여 값을 넣도록 합니다. 


[ 향후 ]
1. 자동화 테스트를 위한 데이터셋을 마련 
2. 입력에 따른 동작을 감지할 방법을 찾는다.
3. 테스트 체크를 위한 로그를 남긴다.
ㅣ

[ 추가 ]
1. 제품에 따라서 아주 조금씩 로그인 방법에 차이가 난다. 이 부분을 어떻게 처리할 지 생각한다. 
   - 표준 스팩 체크 및 확인
   
