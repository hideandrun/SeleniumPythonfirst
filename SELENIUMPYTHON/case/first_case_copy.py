#coding=utf-8
import sys
sys.path.append('C:\\Users\\15927\\Documents\\SELENIUMPYTHONBASE')
import os
import time
from selenium import webdriver
from business.register_business import RegisterBusiness
from log.user_log import UserLog
import unittest
import HTMLTestRunner

class FirstCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.log = UserLog()
        cls.logger = cls.log.get_log()
         
              
    def setUp(self):
        self.file_name = "E:/unittest/image/test01.png"
        self.driver = webdriver.Chrome()
        self.driver.get("http://www.5itest.cn/register?goto=/course/explore")        
        self.driver.maximize_window()
        self.logger.info("this is chrome")
        self.login = RegisterBusiness(self.driver)
        
        

    def tearDown(self):
        time.sleep(2)
        #if sys.exc_info()[0]:
        for method_name,error in self._outcome.errors:
            if error:
                case_name = self._testMethodName
                file_path = os.path.join(os.getcwd()+"/report/"+case_name+".png")
                self.driver.save_screenshot(file_path)
        self.driver.close()

    # @classmethod
    # def tearDownClass(cls): 
    #     cls.driver.close()  
        #print("这个是后置条件")
    @classmethod
    def tearDownClass(cls):
        cls.log.close_handle()

    
    def test_login_email_error(self):
        email_error = self.login.login_email_error('34@qq.com','111','111111',self.file_name)
        return self.assertFalse(email_error,"测试失败")

        # if email_error == True:
        #     print("注册成功了，此条case执行失败")
        #通过assert判断是否为error


    def test_login_username_error(self):
        user_name_error = self.login.login_name_error('7788@qq.com','ss','111111',self.file_name)
        self.assertFalse(user_name_error)
        # if user_name_error  == True:
        #     print("注册成功了，此条case执行失败")
        

    def test_login_password_error(self):
        password_error = self.login.login_password_error('7788@qq.com','ss','111',self.file_name)
        self.assertFalse(password_error)
        # if password_error  == True:
        #     print("注册成功了，此条case执行失败")

    def test_login_code_error(self):
        code_error = self.login.login_code_error('8866@qq.com','ss','111111',self.file_name)
        self.assertFalse(code_error)
        # if code_error  == True:
        #     print("注册成功了，此条case执行失败")

    

    def test_login_success(self):
        success = self.login.register_success('5544@qq.com','ss','111111',self.file_name)
        self.assertTrue(success)
        # if success == True:
        #     print("注册成功")
'''
def main():
    first = FirstCase()
    first.test_login_email_error()
    first.test_login_username_error()
    first.test_login_password_error()
    first.test_login_code_error()
    first.test_login_success()
'''

if __name__ == "__main__":
    file_path = os.path.join(os.getcwd()+"/report/"+"first_case.html")
    f = open(file_path,'wb')
    suite = unittest.TestSuite()
    suite.addTest(FirstCase('test_login_email_error')) 
    suite.addTest(FirstCase('test_login_username_error'))
    suite.addTest(FirstCase('test_login_password_error'))
    suite.addTest(FirstCase('test_login_code_error'))
    suite.addTest(FirstCase('test_login_success'))               
    #unittest.TextTestRunner().run(suite)
    runner = HTMLTestRunner.HTMLTestRunner(stream=f,title="this is first report",description=u"这个是我的第一次测试报告",verbosity=2)
    runner.run(suite)
