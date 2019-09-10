#coding = utf-8
import sys
sys.path.append('C:\\Users\\15927\\Documents\\SELENIUMPYTHONBASE')
from util.excel_util import ExcelUtil
from keywordselenium.actionMethod import ActionMethod
class KeywordCase:
    def run_main(self):
        self.action_method = ActionMethod()
        handle_excel = ExcelUtil('C:/Users/15927/Documents/SELENIUMPYTHONBASE/config/keyword.xls')
        case_lines = handle_excel.get_lines()
        if case_lines:
            for i in range(1,case_lines):
                is_run = handle_excel.get_col_value(i,3)
                #print(is_run)
                if is_run == 'yes':
                    except_result_method = handle_excel.get_col_value(i,7)
                    except_result = handle_excel.get_col_value(i,8)
                    method = handle_excel.get_col_value(i,4)
                    send_value = handle_excel.get_col_value(i,5)
                    handle_value = handle_excel.get_col_value(i,6)
                    
                    #''而不是None
                    #if send_value:
                    self.run_method(method,send_value,handle_value)
                    if except_result != '':
                        except_value = self.get_except_result_value(except_result)
                        if except_value[0] == 'text':
                            result = self.run_method(except_result_method)
                            #print(result)
                            if except_value[1] in result :
                                handle_excel.write_value(i,'pass')
                            else:
                                handle_excel.write_value(i,'fail')
                    
                        elif except_value[0] == 'element':
                            result = self.run_method(except_result_method,except_value[1])
                            if result:
                                handle_excel.write_value(i,'pass')
                            else:
                                handle_excel.write_value(i,'fail')
                        else:
                            print("没有else")
                    else:
                        print("预期结果为空")




    #获取预期结果值
    def get_except_result_value(self,data):
        return data.split("=")

                        

    def run_method(self,method,send_value='',handle_value=''):
        print(send_value,"---->",handle_value)
        method_value = getattr(self.action_method,method)
        if send_value == '' and handle_value != '':
            result = method_value(handle_value)
        elif send_value == '' and handle_value == '':
            result = method_value()
        elif send_value != '' and handle_value == '' :
            result = method_value(send_value)
        else:
            result = method_value(send_value,handle_value)
        return result
            
'''
        #循环行数，去执行每一行case
        #是否执行
            #拿到执行方法
            #拿到操作值
            #拿到输入数据
            #是否有输入数据
                #执行方法(输入数据，操作元素)
            #没有输入数据
                #执行方法(操作元素)
'''

if __name__ == "__main__":
    test = KeywordCase()
    test.run_main()