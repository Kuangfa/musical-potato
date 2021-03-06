# -*- coding: utf-8 -*-
"""
Created on Sat Aug 17 16:44:02 2019


@author: Administrator
"""
from datetime import datetime, timedelta, date
import re
#Errors=['验证通过!','身份证号码位数不对!','身份证号码出生日期超出范围或含有非法字符!','身份证号码校验错误!','身份证地区非法!']
def checkIdcard(idcard):
    Errors=['验证通过,身份证号正确!','身份证号码位数不对!','身份证号码出生日期超出范围或含有非法字符!','身份证号码校验错误!','身份证地区非法!']
    area={"11":"北京","12":"天津","13":"河北","14":"山西","15":"内蒙古","21":"辽宁","22":"吉林","23":"黑龙江","31":"上海","32":"江苏","33":"浙江","34":"安徽","35":"福建","36":"江西","37":"山东","41":"河南","42":"湖北","43":"湖南","44":"广东","45":"广西","46":"海南","50":"重庆","51":"四川","52":"贵州","53":"云南","54":"西藏","61":"陕西","62":"甘肃","63":"青海","64":"宁夏","65":"新疆","71":"台湾","81":"香港","82":"澳门","91":"国外"}
    idcard=str(idcard)
    idcard=idcard.strip()
    idcard_list=list(idcard)
    #地区校验
    if(not area[(idcard)[0:2]]):
        print ((Errors[4]))
    #15位身份号码检测
    if(len(idcard)==15):
        if((int(idcard[6:8])+1900) % 4 == 0 or((int(idcard[6:8])+1900) % 100 == 0 and (int(idcard[6:8])+1900) % 4 == 0 )):
            erg=re.compile('[1-9][0-9]{5}[0-9]{2}((01|03|05|07|08|10|12)(0[1-9]|[1-2][0-9]|3[0-1])|(04|06|09|11)(0[1-9]|[1-2][0-9]|30)|02(0[1-9]|[1-2][0-9]))[0-9]{3}$')#//测试出生日期的合法性
        else:
            ereg=re.compile('[1-9][0-9]{5}[0-9]{2}((01|03|05|07|08|10|12)(0[1-9]|[1-2][0-9]|3[0-1])|(04|06|09|11)(0[1-9]|[1-2][0-9]|30)|02(0[1-9]|1[0-9]|2[0-8]))[0-9]{3}$')#//测试出生日期的合法性
        if(re.match(ereg,idcard)):
            print (Errors[0])
        else:
            print (Errors[2])
    #18位身份号码检测
    elif(len(idcard)==18):
        #出生日期的合法性检查
        #闰年月日:((01|03|05|07|08|10|12)(0[1-9]|[1-2][0-9]|3[0-1])|(04|06|09|11)(0[1-9]|[1-2][0-9]|30)|02(0[1-9]|[1-2][0-9]))
        #平年月日:((01|03|05|07|08|10|12)(0[1-9]|[1-2][0-9]|3[0-1])|(04|06|09|11)(0[1-9]|[1-2][0-9]|30)|02(0[1-9]|1[0-9]|2[0-8]))
        if(int(idcard[6:10]) % 4 == 0 or (int(idcard[6:10]) % 100 == 0 and int(idcard[6:10])%4 == 0 )):
            ereg=re.compile('[1-9][0-9]{5}(19[0-9]{2}|20[0-9]{2})((01|03|05|07|08|10|12)(0[1-9]|[1-2][0-9]|3[0-1])|(04|06|09|11)(0[1-9]|[1-2][0-9]|30)|02(0[1-9]|[1-2][0-9]))[0-9]{3}[0-9Xx]$')#//闰年出生日期的合法性正则表达式
        else:
            ereg=re.compile('[1-9][0-9]{5}(19[0-9]{2}|20[0-9]{2})((01|03|05|07|08|10|12)(0[1-9]|[1-2][0-9]|3[0-1])|(04|06|09|11)(0[1-9]|[1-2][0-9]|30)|02(0[1-9]|1[0-9]|2[0-8]))[0-9]{3}[0-9Xx]$')#//平年出生日期的合法性正则表达式
        #//测试出生日期的合法性
        if(re.match(ereg,idcard)):
            #//计算校验位
            S = (int(idcard_list[0]) + int(idcard_list[10])) * 7 + (int(idcard_list[1]) + int(idcard_list[11])) * 9 + (int(idcard_list[2]) + int(idcard_list[12])) * 10 + (int(idcard_list[3]) + int(idcard_list[13])) * 5 + (int(idcard_list[4]) + int(idcard_list[14])) * 8 + (int(idcard_list[5]) + int(idcard_list[15])) * 4 + (int(idcard_list[6]) + int(idcard_list[16])) * 2 + int(idcard_list[7]) * 1 + int(idcard_list[8]) * 6 + int(idcard_list[9]) * 3
            Y = S % 11
            M = "F"
            JYM = "10X98765432"
            M = JYM[Y]#判断校验位
            if(M == idcard_list[17]):#检测ID的校验位
                print (Errors[0])
                return 1
            else:
                print (Errors[3])
                return 0
        else:
            print (Errors[2])
            return 0
    else:
        print (Errors[1])
        return 0
class GetInformation(object):


     def __init__(self,id):
         self.id = id
         self.birth_year = int(self.id[6:10])
         self.birth_month = int(self.id[10:12])
         self.birth_day = int(self.id[12:14])


     def get_birthday(self):
         """通过身份证号获取出生日期"""
         birthday = "{0}-{1}-{2}".format(self.birth_year, self.birth_month, self.birth_day)
         return birthday
     def get_address(self):
         area_dict = {}
         with open('dict_copy.txt', 'r') as dict_file:
            for line in dict_file:
                (key, value) = line.strip().split(':')
                area_dict[key] = value
         return "{}省 {}市 {}".format(area_dict[self.id[0:2] + "0000"].rstrip("省"),
                                     area_dict[self.id[0:4] + "00"].rstrip("市"),
                                     area_dict[self.id[0:6]])  
     def get_sex(self):
         """男生：1 女生：2"""
         num = int(self.id[16:17])
         if num % 2 == 0:
             return "女生"
         else:
             return "男生"


     def get_age(self):
         """通过身份证号获取年龄"""
         now = (datetime.now() + timedelta(days=1))
         year = now.year
         month = now.month
         day = now.day


         if year == self.birth_year:
             return 0
         else:
             if self.birth_month > month or (self.birth_month == month and self.birth_day > day):
                 return year - self.birth_year - 1
             else:
                 return year - self.birth_year


id = '110000199611103268'
x=checkIdcard(id)
#print(x)
if x==1:
    birthday = GetInformation(id).get_birthday() # 1995-09-25
    age = GetInformation(id).get_age() # 23
    sex=GetInformation(id).get_sex()
    address=str(GetInformation(id).get_address())
    print("birthday"+"="+birthday)
    print("age"+"="+str(age))
    print("sex"+"="+str(sex))
    print("address"+"="+str(address))
else:
    print("身份证号错误")
