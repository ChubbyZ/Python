#批量提取文件中的ip地址，并计算IP在此文件中出现的总次数并写入excel
import re
from collections import Counter
import xlwt

path = "文件地址"
f = open(path, "r", encoding="utf-8")
contents = f.read()
# print(contents)
result_ip = re.findall(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', contents)
print(result_ip[0])
print(len(result_ip))

result = re.findall(r"\b(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\b",
                    contents)
if result:
    tmp = list(set(result))
    tmp.sort(key=result.index)
    print(tmp)
    print(result)
    workbook = xlwt.Workbook(encoding='utf-8')
    worksheet = workbook.add_sheet('sheet1')

    # 设置表头
    worksheet.write(0, 0, label='ip')
    worksheet.write(0, 1, label='count')
    # 将json字典写入excel
    # 变量用来循环时控制写入单元格，感觉有更好的表达方式
    val1 = 1
    val2 = 1
    val3 = 1
    val4 = 1
    for key, value in Counter(result).items():
        if key != '127.0.0.1' and key != '0.0.0.0' and key not in result_ip:
            print(key, ":\t", value)
            worksheet.write(val1, 0, key)
            worksheet.write(val1, 1, value)
            val1 += 1
        else:
            pass
    # 保存
    workbook.save('result.xls')
else:
    print("re cannot find ipNo.2 IPv6")
string_IPv6 = "1050:0:0:0:5:600:300c:326b"
# 匹配是否满足IPv6格式要求,请注意例子里大小写不敏感
if re.match(r"^(?:[A-F0-9]{1,4}:){7}[A-F0-9]{1,4}$", string_IPv6, re.I):
    print("IPv6 vaild")
else:
    print("IPv6 invaild")
# 提取IPv6，例子里大小写不敏感
result = re.findall(r"(?<![:.\w])(?:[A-F0-9]{1,4}:){7}[A-F0-9]{1,4}(?![:.\w])", string_IPv6, re.I)
# 打印提取结果
print(result)
