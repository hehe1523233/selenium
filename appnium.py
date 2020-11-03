import time
from appium import webdriver


class Test:
    desired_caps = {
        "platformName": "Android",
        "deviceName": "emulator-5554",
        "platformVersion": "7.1.2",
        "appPackage": "com.tencent.wework",
        "appActivity": ".launch.WwMainActivity",
        "noReset": "true",
        "resetKeyboard": "true",
        "unicodeKeyboard": "true"
    }
    driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

    def test(self):
        self.driver.find_element_by_xpath("//*[@text='通讯录']").click()
        self.driver.implicitly_wait(5)
        self.driver.find_element_by_id('com.tencent.wework:id/hvn').click()
        self.driver.implicitly_wait(5)
        self.driver.find_element_by_id('com.tencent.wework:id/gfs').send_keys('tester')
        time.sleep(2)
        self.driver.find_element_by_xpath("//*[@text='tester(test_selenium)']").click()
        time.sleep(2)
        self.driver.find_element_by_xpath("//*[@text='发消息']").click()
        time.sleep(1)
        self.driver.find_element_by_id('com.tencent.wework:id/ei_').send_keys("测试code")
        self.driver.find_element_by_xpath("//*[@text='发送']").click()

    def tearDown(self):
        self.driver.quit()
