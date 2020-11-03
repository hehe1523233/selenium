from basePage.base import BasePage
import time
import random

timestamp = int(time.time() * 1000)
moblie = random.randint(10000000, 99999999)


class Test_wx(BasePage):

    def teardown(self):
        self.driver.quit()

    def test_add(self):
        self.driver.find_element_by_xpath("//span[contains(text(),'添加成员')]").click()
        self.driver.implicitly_wait(5)
        self.driver.find_element_by_xpath("//input[@id='username']").send_keys(f'张三{timestamp}')
        self.driver.find_element_by_xpath("//input[@name='acctid']").send_keys(f'{timestamp}')
        self.driver.find_element_by_xpath("//input[@name='mobile']").send_keys(f'123{moblie}')
        # 点【保存】
        self.driver.find_element_by_css_selector("form > div:nth-child(3) > a:nth-child(2)").click()
        self.driver.implicitly_wait(5)
        elems = self.driver.find_elements_by_css_selector("tbody > tr > td:nth-child(2) > span")
        nameList = []
        for elem in elems:
            nameList.append(elem.text)
        assert f'张三{timestamp}' in nameList

