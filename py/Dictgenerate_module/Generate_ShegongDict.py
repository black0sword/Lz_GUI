import itertools
import os

def ReadInformationList():
   try:
       # 读取个人信息文件，并按行存入lines
       informationFile = open(str(current_dir)  + '/xiaobai.txt', 'r',encoding='gbk') #打开xiaobai.txt并读取内容
       lines = informationFile.readlines()                         #文件中的每一行存入到lines列表
       for line in lines:                                          #对lines列表进行遍历
           if(line.strip().split(':')[1].strip() == ""):
             continue
           infolist.append(line.strip().split(':')[1])             #取出line每一项的数字段，去除'\n'，并存入infolist列表中
   except Exception as e:
       print(e)
       print("xiaobai.txt文件读取错误！")

def CreateNumberList():
   # 数字元素
   words = "0123456789"
   # 利用itertools来产生不同数字排列,数字组合长度为3
   itertoolsNumberList = itertools.product(words, repeat=3)
   for number in itertoolsNumberList:                         #对itertoolsNumberList遍历
       numberList.append("".join(number))                     #把每一项存入numberList表中

def common():
   try:
       # 读取common.txt文件，并先存入password字典文件
       informationFile = open( str(current_dir) +'./common.txt', 'r')
       lines = informationFile.readlines()
       for line in lines:
           dictionaryFile.write(line)
   except Exception as e:
       print(e + "\n")
       print("common.txt文件读取错误！")

def CreateSpecialList():
   specialWords = "`~!@#$%^&*()?|/><,."     #特殊字符
   for i in specialWords:                   #遍历特殊字符
       specialList.append("".join(i))       #把特殊字符每一项存入specialList表中

def Combination():
   for a in range(len(infolist)):
       # 把个人信息大于等于8为的直接输出到字典
       if (len(infolist[a]) >= 8):
           dictionaryFile.write(infolist[a] + '\n')
       # 对于小于8位的个人信息利用数字进行补全到8位输出
       else:
           needWords = 8 - len(infolist[a])     #获取需要补全的位数
           for b in itertools.permutations("1234567890", needWords):
               dictionaryFile.write(infolist[a] + ''.join(b) + '\n')
       # 把个人信息元素两两进行相互拼接，大于等于8位的输出到字典
       for c in range(0, len(infolist)):
           if (len(infolist[a] + infolist[c]) >= 8):
               dictionaryFile.write(infolist[a] + infolist[c] + '\n')
               # 在2个个人信息元素加入特殊字符组合起来，大于等于8位就输出到字典
       for d in range(0, len(infolist)):
           for e in range(0, len(specialList)):
               if (len(infolist[a] + specialList[e] + infolist[d]) >= 8):
                   # 特殊字符加尾部
                   dictionaryFile.write(infolist[a] + infolist[d] + specialList[e] + '\n')
                   # 特殊字符加中间
                   dictionaryFile.write(infolist[a] + specialList[e] + infolist[d] + '\n')
                   # 特殊字符加首部
                   dictionaryFile.write(specialList[e] + infolist[a] + infolist[d] + '\n')
   # 关闭字典文件对象
   dictionaryFile.close()

if __name__ == '__main__':
   current_dir = os.path.dirname(os.path.abspath(__file__))
   

   # 创建社工字典文件
   # dictionaryFile = open('passwordyy.txt', 'w')
   dictionaryFile = open(str(current_dir) + './shegongdict.txt','w')
   # 用户信息列表
   infolist = []
   # 数字列表
   numberList = []
   # 特殊字符列表
   specialList = []
   # 读取个人信息文件dictionaryFile
   ReadInformationList()
   # 创建数字列表
   CreateNumberList()
   # 创建特殊字符列表
   
   #CreateSpecialList()
   # 把常见密码先写入字典文件
   common()
   # 字典生成主体，将个人信息+数字列表+特殊字符列表，进行组合加入字典
   Combination()
   print("字典生成成功！" +'\n'+"字典路径=>"+current_dir+"/shegongdict.txt")
