# 调用fofaapi
# email和key需自行填入
import requests
import base64

urllist=[]
app_name = "DrayTek"  # 要查找的组件的名称
s = 'app="' + app_name + '" && country!="CN" && after="2022-01-01" && before="2022-03-20"'

a = str(base64.b64encode(s.encode('utf-8'))).split("\'")
req = requests.get(
    f"https://fofa.info/api/v1/search/all?email=xxx&key=xxx&qbase64=" + a[
        1] + "&size=10000")
re_json = req.json()
wz = re_json['results']


# 输出保存到文件中

with open("resultFofa.txt", "a") as fh:
    # wz = set(wz)
    for url in wz:
        url = str(url)
        url = url.split("\'")
        if "https" in url[1]:
            if url[1] not in urllist:
                    urllist.append(url[1] + "\n")
                    fh.write(url[1] + "\n")
            else:pass
        else:
            http_url = "http" + ":" + "//" + url[1] + "\n"
            if http_url not in urllist:
                urllist.append(http_url)
                fh.write(http_url)
