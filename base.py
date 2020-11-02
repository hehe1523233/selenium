from selenium import webdriver


class BasePage:
    chrome_opts = webdriver.ChromeOptions()
    chrome_opts.debugger_address = '127.0.0.1:9222'
    driver = webdriver.Chrome(options=chrome_opts, executable_path='config/chromedriver.exe')

    @classmethod
    def init_driver(cls):
        cls.driver.get('https://work.weixin.qq.com/wework_admin/frame')
        return cls.driver