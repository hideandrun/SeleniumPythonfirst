#coding=utf-8
from PIL import Image
import time
from util.ShowapiRequest import ShowapiRequest
class GetCode:
    def __init__(self,driver):
        self.driver = driver
     #获取图片
    def get_code_image(self,file_name):
        self.driver.save_screenshot(file_name)
        code_element = self.driver.find_element_by_id("getcode_num") 
    #code_element拿到的是元素左上角的坐标，计算元素的宽高
        #print(code_element.location)
        left = code_element.location['x']
        top = code_element.location['y']
        right = code_element.size['width']+left
        height = code_element.size['height']+top
        im = Image.open(file_name)
        img = im.crop((left,top,right,height))
        #img_size = img.resize((1920,1080)) #重置图片的分辨率
        img.save(file_name)
        time.sleep(2)

    #解析图片，获取验证码
    def code_online(self,file_name):
        self.get_code_image(file_name)
        r = ShowapiRequest("http://route.showapi.com/184-4","103592","3388e72a386041dd85f8eb604914bcbd" )
        r.addBodyPara("typeId", "35")
        r.addBodyPara("convert_to_jpg", "0")
        r.addFilePara("image", file_name)#文件上传时设置
        r.addBodyPara("needMorePrecise", "0")
        res = r.post()
        text = res.json()['showapi_res_body']['Result']
        time.sleep(2)
        return text 
