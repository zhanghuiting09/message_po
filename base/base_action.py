from selenium.webdriver.support.wait import WebDriverWait


class BaseAction():

    # 初始化设置driver对象
    def __init__(self, driver):
        self.driver = driver

    # 查找一个元素封装(使用显式等待)
    def find_element(self, feature, timeout=10, poll=1):
        # feayure元组类型,进行拆包
        by, value = feature
        return WebDriverWait(self.driver, timeout, poll).until(lambda x:x.find_element(by, value))

    # 查找一个元素封装(使用显式等待)
    def find_elements(self, feature, timeout=10, poll= 1):
        by, value = feature
        return WebDriverWait(self.driver, timeout, poll).until(lambda x:x.find_elements(by, value))

    # 封装点击元素方法
    def click(self, feature):
        self.find_element(feature).click()

    # 封装输入方法
    def input(self, feature, content):
        # 输入前先清空操作
        self.clear(feature)
        self.find_element(feature).send_keys(content)

    # 封装清空方法
    def clear(self, feature):
        self.find_element(feature).clear()













