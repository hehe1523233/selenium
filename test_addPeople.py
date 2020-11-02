from basePage.base import BasePage


class Test_wx:
    driver = BasePage.init_driver()

    def teardown(self):
        self.driver.quit()

    def test_add(self):
        self.driver.find_element_by_xpath("//span[contains(text(),'添加成员')]").click()
