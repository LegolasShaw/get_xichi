# -*- coding: utf-8 -*-


from urllib import request
import urllib
from bs4 import BeautifulSoup

from datetime import datetime

if __name__ == "__main__":
    headers =  {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
                'Accept-Language': 'zh-CN,zh;q=0.9',
                'Connection': 'keep-alive',
                'Cookie': 'td_cookie=536784898; _free_proxy_session=BAh7B0kiD3Nlc3Npb25faWQGOgZFVEkiJWZjNDkwNTBhYmJlMDViNTBhYjQyOWNkYmNlMDIxYzIzBjsAVEkiEF9jc3JmX3Rva2VuBjsARkkiMUhqVExyT3oxRzNjdDN3bXBKdnVPNFc1NEpLUWxTYi9BUlM5aWMzVHFJRlU9BjsARg%3D%3D--b65e914271867805de4451a498ae20dc1dbe9c8e; Hm_lvt_0cf76c77469e965d2957f0553e6ecf59=1539237106,1539579344; Hm_lpvt_0cf76c77469e965d2957f0553e6ecf59=1539581275',
                'Host': 'www.xicidaili.com',
                'Referer': 'http://www.xicidaili.com/',
                'Upgrade-Insecure-Requests': 1,
                'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.75 Safari/537.36'}

    # for i in range(1, 100):
    #     url = 'http://www.xicidaili.com/nn/' + str(i)
    #     req = request.Request(url=url, headers=headers)
    #     res = urllib.request.urlopen(req)
    #     bs_obj = BeautifulSoup(res.read().decode('utf-8'), 'html5lib')
    #
    #     with open("ip_prox.txt", 'ab') as fr:
    #         target_obj = bs_obj.find_all('tr', class_='odd')
    #         for obj in target_obj:
    #             result = obj.contents[3].text + ':' + obj.contents[5].text + '\n'
    #             b_re = result.encode('utf-8')
    #             fr.write(b_re)
    #             print("get a free prox " + datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    with open("ip_prox.txt", 'r') as fr:
        for row in fr.readlines():
            print(row)