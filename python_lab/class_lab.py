# -*- coding: utf-8 -*-
"""
Created on Wed Jan 20 16:21:11 2021

@author: chunxia

@package: class_lab
@description: 
    lab for class and package
"""

class geese:
    '''
    class geese.
    '''
    def __init__(self,beak,wing,claw):
        print("我是雁类，有以下特征")
        print(beak)
        print(wing)
        print(claw)
 
## example of decorator property in class.       
class TVShow:
    list_film=["战狼 2","红海行动","西游记","城市猎人"]
    def __init__(self,show):
        self.__show = show
        
    @property
    def show(self):
        return self.__show
    
    @show.setter
    def show(self,value):
        if value in TVShow.list_film:
            self.__show ='您选择了《%s》，稍后将播放'%value
        else:
            self.__show = "您点播的电影不存在"


if __name__ == "__main__":
    tvshow = TVShow("战狼 2")
    print("正在播放《",tvshow.show,"》")
    print("您可以从%s中点播要播放的电影"%tvshow.list_film)
    
    tvshow.show = "红海行动"
    print(tvshow.show)


