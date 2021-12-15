from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

class DefaultTest:
    def __init__(self, address: str):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.address = address


    def teardown(self):
        self.driver.quit()

    def change_window(self, target: str):
        if target == 'parent':
            # child window close
            self.driver.close()
            self.driver.switch_to.window(self.driver.window_handles[0])
        elif target == 'child':
            self.driver.switch_to.window(self.driver.window_handles[1])
        else:
            print("Wrong target!")

    def auto_test(self):
        self.driver.get(self.address)
        self.driver.set_window_size(974, 1040)
        self.driver.find_element(By.XPATH, "/html/body/p/a").click()
        self.change_window("child")
        self.driver.find_element(By.XPATH, '/html/body/form/table/tbody/tr[6]/td[2]/input').click()
        # 결과를 보기 위해 5초간 sleep
        sleep(5)
        self.change_window("parent")


if __name__ == '__main__':
    test_address = "http://demo.guru99.com/popup.php"
    test = DefaultTest(test_address)
    test.auto_test()
    test.teardown()