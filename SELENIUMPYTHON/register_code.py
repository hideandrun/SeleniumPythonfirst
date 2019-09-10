#coding=utf-8
from selenium import webdriver
import time
import random
from PIL import Image
from ShowapiRequest import ShowapiRequest
driver =webdriver.Chrome()
#浏览器初始化
def driver_init():
    driver.get("http://www.5itest.cn/register?goto=/course/explore")
    driver.maximize_window()
    time.sleep(5)

#获取element元素信息
def get_element(id):
    element = driver.find_element_by_id(id)
    return element

#获取随机数
def get_range_user():
    user_info = ''.join(random.sample('1234567890abcdefghijklm',8))
    return user_info

#获取图片
def get_code_image(file_name):
    driver.save_screenshot(file_name)
    code_element = driver.find_element_by_id("getcode_num") 
    print(code_element.location) #code_element拿到的是元素左上角的坐标，计算元素的宽高
    left = code_element.location['x']
    top = code_element.location['y']
    right = code_element.size['width']+left
    height = code_element.size['height']+top
    im = Image.open(file_name)
    img = im.crop((left,top,right,height))
    #img_size = img.resize((1920,1080)) #重置图片的分辨率
    img.save(file_name)

#解析图片，获取验证码
def code_online(file_name):
    r = ShowapiRequest("http://route.showapi.com/184-4","103592","3388e72a386041dd85f8eb604914bcbd" )
    r.addBodyPara("typeId", "35")
    r.addBodyPara("convert_to_jpg", "0")
    r.addFilePara("image", file_name)#文件上传时设置
    r.addBodyPara("needMorePrecise", "0")
    res = r.post()
    text = res.json()['showapi_res_body']['Result']
    return text 

#运行主程序
def run_mian():
    user_name_info = get_range_user()
    user_email = user_name_info+"@163.com"
    file_name = "E:/imooc/image/test01.png"
    driver_init()
    get_element("register_email").send_keys(user_email)
    get_element("register_nickname").send_keys(user_name_info)
    get_element("register_password").send_keys("111111")
    get_code_image(file_name)
    text = code_online(file_name)
    get_element("captcha_code").send_keys(text)
    get_element("register-btn").click()
    time.sleep(5)
    driver.close()

run_mian()

