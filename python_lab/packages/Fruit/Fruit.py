# -*- coding: utf-8 -*-
"""
Created on Thu Jan 21 16:59:28 2021
@module: Fruit
@description: lab of class as module
@author: chunxia
"""

class Fruit:
    """
    @class: Fruit
    """
    def __init__(self,color="绿色"):
        Fruit._color = color
        
    def harvest(self,color):
        print("水果是："+self._color +"的!")
        print("水果已经收获......")
        print("水果原来是："+Fruit._color+"的")


class Apple(Fruit):
    '''
    @class Apple,
    '''
    __color = '红色'
    _color = 'Red'
    
    def __init__(self):
        print("我是苹果")
        print("__color",Apple.__color,"_color =",Apple._color)
        print("__init__, _color =", Apple._color)
        super().__init__()
        

class Sapodilla(Fruit):
    def __init__(self,color):
        print("\n我是人参果")
        super().__init__(color)
    #重写harvest()方法
    def harvest(self,color):
        print("人参果是"+self._color +"的！")
        print("人参果已经收获......")
        print("人参果是原来是："+Fruit._color+"的")


if __name__ == "__main__":
    apple = Apple()
    apple.harvest(apple._color)
    sapodilla = Sapodilla("白色")
    sapodilla.harvest("金黄色带紫色条纹")