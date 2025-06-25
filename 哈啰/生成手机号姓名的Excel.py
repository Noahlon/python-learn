import datetime

import openpyxl
import random

# 创建数据
def create_test_data(count):
    # 生成随机手机号
    def generate_phone_number():
        return f"11{str(random.randint(100000000, 999999999))}"
    # 生成随机姓名
    def generate_name():
        names = ["张三", "李四", "王五", "赵六", "赵一"]
        return random.choice(names)
    # 生成随机数据标识
    def generate_data_identifier():
        return str(random.randint(1000000000000000, 9000000000000000))
    reslist = []
    for _ in range(count):
        reslist.append({
            "手机号": generate_phone_number(),
            "数据标识": generate_data_identifier(),
            "姓名": generate_name()
        })
    return reslist
# 创建Excel文件
def create_excel_file(filename,nums):
    # 创建一个新的工作簿
    wb = openpyxl.Workbook()
    # 获取活动的工作表
    ws = wb.active
    # 设置工作表标题
    ws.title = "测试数据"
    
    # 添加表头
    headers = ["手机号", "数据标识", "姓名"]
    ws.append(headers)
    # 添加测试数据
    test_data = create_test_data(nums)  # 生成100条测试数据
    for entry in test_data:
        ws.append([entry["手机号"], entry["数据标识"], entry["姓名"]])
    # 保存指定目录
    filename = f"{filename}.xlsx"
    wb.save(filename)
    print(f"Excel文件 '{filename}' 已创建。")


if __name__ == "__main__":
    
    nums = 100  
    nums_str = nums.__str__()
    filename = "测试数据" + nums_str + "条数据" + datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    # 创建Excel文件
    create_excel_file(filename,nums)
