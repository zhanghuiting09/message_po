from selenium.webdriver.common.by import By
import pytest
from base.base_action import BaseAction


class NewMessagePage(BaseAction):
    # 页面的元素
    name_input_box = By.XPATH, "//*[@text='接收者']"
    message_input_box = By.XPATH, "//*[@text='键入信息']"
    send_button = By.ID, "com.android.mms:id/send_button_sms"

    # 接收人
    def receive_person(self, content):
       self.input(self.name_input_box, content)

    # 发送信息内容
    def send_message(self, content):
        self.input(self.message_input_box, content)

    # 点击发送按钮
    def click_send_button(self):
        self.click(self.send_button)