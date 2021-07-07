# 用法：python3 PingIp.py 路径/ip.txt
# 用途：仅用于批量探测存活IP
import os
import sys

fr = open(sys.argv[1], 'r', encoding='utf-8')
for ip in fr:
    cmd = f'ping -n 2 {ip}'
    res = os.popen(cmd)
    output_str = res.read()   # 获得输出字符串
    if "请求超时" not in output_str:
        with open('live.txt','a+') as fb:
                if ip.split():
                    print(f"存活：{ip}")
                    fb.write(ip)

