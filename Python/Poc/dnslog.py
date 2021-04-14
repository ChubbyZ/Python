import requests
import time
def dnslog_get():
    headers = {
        "Cookie": "UM_distinctid=178ce6e908a0-0e56e69bac7299-c3f3568-1ecde4-178ce6e908b7b9; CNZZDATA1278305074=903547381-1618366436-null%7C1618366436; PHPSESSID=9l7erjviikjo7r3fsfjvo1p016"
    }
    req = requests.get("http://www.dnslog.cn/getdomain.php", headers=headers, timeout=6)
    # req = requests.get("http://www.dnslog.cn/getdomain.php",  timeout=6)
    return req.text
def dnslog_refresh():
    headers = {
        "Cookie": "UM_distinctid=178ce6e908a0-0e56e69bac7299-c3f3568-1ecde4-178ce6e908b7b9; CNZZDATA1278305074=903547381-1618366436-null%7C1618366436; PHPSESSID=9l7erjviikjo7r3fsfjvo1p016"
    }
    req_rf = requests.get("http://www.dnslog.cn/getrecords.php", headers=headers, timeout=6)
    print(req_rf.text)


domain = dnslog_get()
print(domain)
time.sleep(20)
dnslog_refresh()
