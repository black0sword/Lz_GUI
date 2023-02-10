### `Lz_gui`收集器 

#### 信息收集大保健(整合网站)

1.子域名查询模块

* 在线子域名爆破    https://phpinfo.me/domain/

- 基于`SSL`证书查询  `censys.io`  `crt.sh`

- 基于第三方网站接口查询  `1.riskiq `  `2.shodan`   `3.findsubdomains`      `4.fofa` 

>  shadon永久会员      salvador_mccoy   testforall@123

2.`cdn`检测识别

* 历史`DNS`记录  http://viewdns.info/

3.目录爆破

* `ffuf  `

  优雅美观的输出

  ```shell
  ffuf -w phpdict.txt -u http://baidu/FUZZ -recursion  -s
  ```

  

4.端口扫描

http://duankou.wlphp.com/

5.`whois`查询



6.目标`C`段与旁注  

* 收集`ip`所在网段信息     http://IPwhois.cnnic.net.cn

* 域名搜索网站，还会自动归纳同一个`IP`的多个域名    http://dnsdumpster.com  !!!
* 旁站查询  https://site.ip138.com/ 

7.`md5`解密



8.批量`url`去重   ok



9.批量 `js`文件寻找



10.谷歌/Bing/百度  爬虫  ok



11.公众号/小程序收集  

* 搜狗搜索引擎

* python脚本

  

12.敏感信息收集 -->

* `github`，`Gitee`

* 网盘信息 ---> 可能有些源码中会存在账号信息

  盘多多：http://www.panduoduo.net/
  盘搜搜：http://www.pansoso.com/
  盘搜：http://www.pansou.com/
  凌云风搜索：https://www.lingfengyun.com/    这个还行

  直接输入厂商名字然后搜索，可以看看是否泄露了源码，或者什么账号密码之类的

13. 社工,查q绑,手机号查q号 
    * 社工库接口        https://sgk66.cc/        https://zy.xywlapi.cc/home.html
    *  查注册过的网站   https://www.reg007.com
    
    *  q绑接口
    
    * http://hack.lovejm.fun/verify.php?name=&id=
    
    * https://zy.xywlapi.cc/qqcx2023?qq=67375794  
    
    *  社工字典生成
    

14.邮箱手机   

- 爱企查等批量查询
- https://hunter.io

15.杀毒识别

* tasklist /svc

16.常用安全论坛与网站整理

* 火线  https://zone.huoxian.cn/

* `90sec` https://forum.90sec.com/
* 社工密码生成网  https://www.shentoushi.top/tools/dict/index.php
* 动漫岛  http://www.dmd85.com/

* `md5`解密网  https://www.somd5.com/

* 油猴官网  https://greasyfork.org/zh-CN
* 某社工库 https://sgk66.cc/

* 好用的翻译网  http://www.iciba.com

* 找邮箱的网站 https://phonebook.cz/

* 天眼查,企查查,







### 2023.1.29

1.增加`whois`查询  `icp`备案

2.实时`cmd`

3.`py`增加社工字典接口

### 2023.1.30

1.文件合并模块
