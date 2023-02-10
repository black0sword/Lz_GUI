import requests
from lxml import etree
import json
import time
from concurrent.futures import ThreadPoolExecutor
import time
import urllib3
import sys


print(sys.argv)



urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


class get_ip:
    def __init__(self):
        self.ip_Arr = []
        # self.ok_ip_arr = []
        
        
    def check_proxy_isok(self):
        while True:
            proxies_json = requests.get(url="http://demo.spiderpy.cn/get/").text
            proxiess = json.loads(proxies_json)

            proxies = {
                "https": "http://" + proxiess['proxy']
            }
            header = {
                'Host': 'www.yhdmp.cc',
                'sec-ch-ua': '"Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"',
                'User-Agent': "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36 MicroMessenger/7.0.4.501 NetType/WIFI MiniProgramEnv/Windows WindowsWechat/WMPF",
                'Cookie': 'qike123=%u5F26%u97F3%20-%u8054%u7CFB%u7684%u4E00%u7BAD-%20%u7B2C2%u96C6^https%3A//www.yhdmp.cc/vp/23109-1-1.html_$_%u5F26%u97F3%20-%u8054%u7CFB%u7684%u4E00%u7BAD-%20%u7B2C3%u96C6^https%3A//www.yhdmp.cc/vp/23109-1-2.html_$_|; t1=1774060551519; k1=32978960; k2=4101511674152; t2=1774060587302',
                'Referer': 'https://www.yhdmp.cc/vp/22269-1-0.html'
            }

            print(proxiess,end='')

            try:
                isok = requests.get(url="https://www.yhdmp.cc/s_all?kw=1&pageindex=1", timeout=3, proxies=proxies,
                                    verify=False, headers=header)
                print("  | " + str(isok.status_code))
                is_success = re.findall(r'日本动漫', isok.text)

                if (isok.status_code == 200 and is_success[0] == "日本动漫"):
                    print("[+]获取代理ip成功======>" + proxies['https'])
                    return proxies
                else:
                    continue

            except Exception as e:
                print("[-]" + proxies['https'] + "代理ip无效")
                continue

    def request_yh(self,proxie):
        print("正在检测IP=====>" + proxie)
        proxies = {
            'https': proxie,
        }
        header = {
            'Host': 'www.yhdmp.cc',
            'sec-ch-ua': '"Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"',
            'User-Agent': "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36 MicroMessenger/7.0.4.501 NetType/WIFI MiniProgramEnv/Windows WindowsWechat/WMPF",
            'Cookie': 'qike123=%u5F26%u97F3%20-%u8054%u7CFB%u7684%u4E00%u7BAD-%20%u7B2C2%u96C6^https%3A//www.yhdmp.cc/vp/23109-1-1.html_$_%u5F26%u97F3%20-%u8054%u7CFB%u7684%u4E00%u7BAD-%20%u7B2C3%u96C6^https%3A//www.yhdmp.cc/vp/23109-1-2.html_$_|; t1=1774060551519; k1=32978960; k2=4101511674152; t2=1774060587302',
            'Referer': 'https://www.yhdmp.cc/vp/22269-1-0.html'
        }
        try:
            requests.get(url='https://baidu.com',headers=header,verify=False,timeout=5)
            time.sleep(0.1)
            print("ip is ok ======>" + proxie)
            # self.ok_ip_arr.append(proxie)
            # 得到所有存活ip
            with open("./ok_ip.txt", 'a', encoding='utf-8') as f:

                f.write(proxie)

        except Exception as e:
            print(e)
            pass

    def check_ip(self):
        with ThreadPoolExecutor(max_workers=len(self.ip_Arr)+1) as executor:
            executor.map(self.request_yh,self.ip_Arr)
            #等待所有线程结束
            executor.shutdown()



    def get_ip_from_local(self,filename):
        with open("./" + filename) as f:
            for ip in f.readlines():
                ip = "http://" + ip
                # print(ip,end='')
                self.ip_Arr.append(ip)



    def get_html(self, page):
        headers = {
            'Connection': 'keep-alive',
            'sec-ch-ua': '"Google Chrome";v="87", " Not;A Brand";v="99", "Chromium";v="87"',
            'sec-ch-ua-mobile': '?0',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-User': '?1',
            'Sec-Fetch-Dest': 'document',
            'Referer': f'https://www.kuaidaili.com/free/inha/{page}/',
            'Accept-Language': 'zh-CN,zh-TW;q=0.9,zh;q=0.8,en;q=0.7',
        }

        response = requests.get(f'https://www.kuaidaili.com/free/inha/{page}/', headers=headers)
        html = etree.HTML(response.text)
        trs = html.xpath('//div[@id="list"]//table/tbody/tr')
        # print(trs)
        # print(response)
        for tr in trs:
            ip = tr.xpath('td[@data-title="IP"]/text()')[0]
            port = tr.xpath('td[@data-title="PORT"]/text()')[0]
            print(f"{ip}:{port}")


if __name__ == '__main__':
    g = get_ip()

    #  请输入选项[1] 检测代理 [2]更新代理(快代理) [3]
    select = int(input("请输入选项[1] 检测代理 [2]更新代理(快代理) [3],你的选择是:"))
    if(select == 1):
        filename = 'ip.txt'
        #从本地获取ip
        g.get_ip_from_local(filename=filename)
        #验证ip存活并保存ip
        g.check_ip()


        #文本去重
        with open("./ok_ip.txt" , "r") as f:
            lines = f.readlines()

        lines_set = set(lines)

        with open("./distinct_" + filename, "w") as f:
            for line in lines_set:
                f.write(line)



    elif(select == 2):
        for i in range(1, 50):
            g.get_html(i)
            time.sleep(2)


    else:
        g.check_proxy_isok()