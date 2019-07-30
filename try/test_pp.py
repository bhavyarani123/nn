from selenium import webdriver
import pytest

class TestA():
    @pytest.yield_fixture()
    def test_setup(self):
        self.driver = webdriver.Chrome(executable_path=r"C:\Users\bhavy\PycharmProjects\amazon\drivers\chromedriver.exe")
        self.driver.get("https://letskodeit.teachable.com/pages/practice")
        yield
        self.driver.close()
        print('Test completed')

    def test_login(self,test_setup):
        print("Login success")

