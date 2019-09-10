#coidng=utf-8
from selenium import webdriver
import time
import random
from PIL import Image
from ShowapiRequest import ShowapiRequest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.get("http://www.5itest.cn/register?goto=/course/explore")
driver.maximize_window()
time.sleep(5)
print(EC.title_contains("注册"))
email_element = driver.find_element_by_id("register_email")
driver.save_screenshot("E:/imooc.png")
code_element = driver.find_element_by_id("getcode_num") 
print(code_element.location) #code_element拿到的是元素左上角的坐标，计算元素的宽高
left = code_element.location['x']
top = code_element.location['y']
right = code_element.size['width']+left
height = code_element.size['height']+top
im = Image.open("E:/imooc.png")
img = im.crop((left,top,right,height))
#img_size = img.resize((1920,1080)) #重置图片的分辨率
img.save("E:/imooc1.png")

r = ShowapiRequest("http://route.showapi.com/184-4","103592","3388e72a386041dd85f8eb604914bcbd" )
r.addBodyPara("typeId", "35")
r.addBodyPara("convert_to_jpg", "0")
r.addFilePara("image", r"E:/imooc1.png")#文件上传时设置
r.addBodyPara("needMorePrecise", "0")
res = r.post()
text = res.json()['showapi_res_body']['Result']
print(text) # 返回信息
time.sleep(2)
driver.find_element_by_id("captcha_code").send_keys(text)
time.sleep(5)
# element = driver.find_element_by_class_name("controls")
# locator = (By.CLASS_NAME,"controls")
# WebDriverWait(driver,2).until(EC.visibility_of_element_located(locator))
# email_element = driver.find_element_by_id("register_email")
# print(email_element.get_attribute("placeholder"))
# email_element.send_keys("2233152210@qq.com")
# print(email_element.get_attribute("value"))
# for i in range(5):
#     user_email = ''.join(random.sample('1234567890abcdefg',8))+"@163.com"
#     print(user_email)


# driver.find_element_by_id("register_email").send_keys("2233152210@qq.com")
# user_name_element_node = driver.find_elements_by_class_name("controls")[1]
# user_element = user_name_element_node.find_element_by_class_name("form-control")
# user_element.send_keys("Hideandrun")
# driver.find_element_by_name("password").send_keys("zbh19631101")
# driver.find_element_by_xpath("//*[@id='captcha_code']").send_keys(111111)
# driver.find_element_by_id("register-btn").click()
time.sleep(3)
driver.close()