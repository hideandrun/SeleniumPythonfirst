#coding=utf-8
import pytesseract
from PIL import Image
from ShowapiRequest import ShowapiRequest
# image = Image.open("E:/imooc1.png")
# text = pytesseract.image_to_string(image)
# print(image)
# python3.6.5
# 需要引入requests包 ：运行终端->进入python/Scripts ->输入：pip install requests


r = ShowapiRequest("http://route.showapi.com/184-4","103592","3388e72a386041dd85f8eb604914bcbd" )
r.addBodyPara("typeId", "35")
r.addBodyPara("convert_to_jpg", "0")
r.addFilePara("image", r"E:/imooc1.png")#文件上传时设置
r.addBodyPara("needMorePrecise", "0")
res = r.post()
print(res.json())
text = res.json()['showapi_res_body']['Result']
print(text) # 返回信息