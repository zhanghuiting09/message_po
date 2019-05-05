from page.message_page import MessagePage
from page.new_message_page import NewMessagePage


class Page():
    def __init__(self, driver):
        self.driver = driver

    @property
    def message(self):
        return MessagePage(self.driver)

    @property
    def new_message(self):
        return NewMessagePage(self.driver)





