# -*- coding: UTF-8 -*-

# ------------------------(max to 80 columns)-----------------------------------
# author by : （学员ID)
# created:  2019.7.10

# Description:
#   类的继承
# ------------------------(max to 80 columns)-----------------------------------


# 父类
class Person(object):  # 定义一个父类
    '''父类 - 人 '''

    def talk(self):  # 父类中的方法
        print("person is talking....")
        return


class Chinese(Person):  # 定义一个子类， 继承Person类
    '''子类 - 中国人 '''

    def walk(self):   # 在子类中定义其自身的方法
        print('A Chinese is walking...')
        return
