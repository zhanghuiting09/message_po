from time import sleep
import pytest
from base.base_driver import init_driver
from page.page import Page


class TestMessage():

    def setup(self):
        self.driver = init_driver()
        self.page = Page(self.driver)

    def teardown(self):
        sleep(5)
        self.driver.quit()

    @pytest.mark.parametrize(("recive", "message"),
                             [("185", "123"), ("999", "123"), ("888", "123")])
    def test_send_new_message(self, recive, message):
        self.page.message.click_new_message_button()
        self.page.new_message.receive_person(recive)
        self.page.new_message.send_message(message)
        self.page.new_message.click_send_button()
		
	def test_new(self):
		print("新增")
	def test_02(self):
		print("第二次新增")
		
