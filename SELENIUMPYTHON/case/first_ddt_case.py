#coding=utf-8
#邮箱、用户名、密码、验证码、错误信息定位元素、错误提示信息
import ddt
import unittest
import sys
sys.path.append('C:\\Users\\15927\\Documents\\SELENIUMPYTHONBASE')
import os
import time
from selenium import webdriver
from business.register_business import RegisterBusiness
#from log.user_log import UserLog
import HTMLTestRunner
from util.excel_util import ExcelUtil
ex = ExcelUtil()
data = ex.get_data()
file_name = "E:/case/image/test02.png"
@ddt.ddt
class FirstDdtCase(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://www.5itest.cn/register?goto=/course/explore")
        self.driver.maximize_window()
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
    '''
    @ddt.data(
            ['234','test0007','111111','code','user_email_error','请输入有效的电子邮件地址'],
            ['@qq.com','test0007','111111','code','user_email_error','请输入有效的电子邮件地址'],
            ['2343@qq.com','test0007','111','code','user_email_error','请输入有效的电子邮件地址']
        )

    @ddt.unpack
    '''
    @ddt.data(*data)
    def test_register_case(self,data):
        email,username,password,self.file_name,assertCode,assertText = data     
        email_error = self.login.register_function(email,username,password,self.file_name,assertCode,assertText)
        self.assertFalse(email_error,"测试失败")

if __name__ == "__main__":
    #unittest.main()
    file_path = os.path.join(os.getcwd()+"/report/"+"first_case1.html")
    f = open(file_path,'wb')
    suite = unittest.TestLoader().loadTestsFromTestCase(FirstDdtCase)
    runner = HTMLTestRunner.HTMLTestRunner(stream=f,title="this is first report11",description=u"这个是我的第一次测试报告1",verbosity=2)
    runner.run(suite)
