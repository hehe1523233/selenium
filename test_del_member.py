from appium.webdriver.common.mobileby import MobileBy
from po.page.app import App
import pytest
import time

driver = App().start().main().goto_address_book()
elems = driver._driver.find_elements(MobileBy.XPATH, "//*[contains(@text, 'name')]")


class TestDelMember:

    # def setup(self):
    # self.main = App().start().main().goto_address_book()

    @pytest.mark.parametrize("elem", elems)
    def test_del_member(self, elem):
        elem.click()
        driver._driver.find_element(MobileBy.ID, 'com.tencent.wework:id/hvd').click()
        time.sleep(1)
        driver._driver.find_element(MobileBy.ID, 'com.tencent.wework:id/b87').click()
        time.sleep(1)
        driver._driver.swipe(712, 1695, 570, 837, 5000)
        driver._driver.find_element(MobileBy.ID, 'com.tencent.wework:id/efq').click()
        driver._driver.find_element(MobileBy.ID, 'com.tencent.wework:id/bit').click()
        time.sleep(5)
        assert True
