# -*- coding: utf-8 -*-
"""
Created on Wed Jan 20 14:54:00 2021

@author: chunxia
"""

def fun_bmi (person,height,weight):
    '''
    function: 根据身高，体重计算BMI指数
    person: name
    height: 身高，单位：米
    weight: 体重，单位：千克
    '''
    
    print(person+"的身高:"+str(height)+"米\t体重："+str(weight)+"千克")
    bmi = weight/(height**2)
    print(person + "的BMI指数："+str(bmi))


def fun_bmi_upgrade (*person):
    '''
    function: 根据身高，体重计算BMI指数(升级版)
    person: 可变参数需要传输3个元素的列表 分别为：
        - person： 名字
        - height: 身高，单位：米
        - weight: 体重，单位：千克
    '''
    for list_person in person:
        for item in list_person:
            name = item[0]
            height = item[1]
            weight = item[2]
            fun_bmi(name,height,weight)


if __name__ == "__main__":
    person = ("Jaky", 1.7,60)
    fun_bmi("Jaky",1.7,60)
    #fun_bmi_upgrade([("jacky",1.7,60),('Mary', 1.5, 50)])