from selenium.webdriver.common.by import By

from base.base_action import BaseAction


class MessagePage(BaseAction):
    # 新增消息按钮
    new_message_button = By.ID, "com.android.mms:id/action_compose_new"

    def click_new_message_button(self):
        self.click(self.new_message_button)