# -*- coding: UTF-8 -*-

# ------------------------(max to 80 columns)-----------------------------------
# author by : （学员ID)
# created:  2019.7.10

# Description:
#   英雄的类
# ------------------------(max to 80 columns)-----------------------------------

import random


class Hero():

    def __init__(self, a, n, p):
        ''' 初始化函数 '''

        if len(a) > 0 and len(n) > 0 and len(p) > 0:
            self.alias = a
            self.name = n
            self.position = p

            self.ab_viability = random.randint(1, 100)
            self.ab_damage = random.randint(1, 100)
            self.ab_effect = random.randint(1, 100)
            self.ab_difficulty = random.randint(1, 100)
        else:
            alias = '英雄的别名'
            name = '英雄的姓名'
            position = '英雄的定位'

            ab_viability = 0
            ab_damage = 0
            ab_effect = 0
            ab_difficulty = 0
        return

    def show_presentation(self):
        print('\n英雄的介绍：')
        print('英雄是 %s - %s ，定位是 %s' % (self.alias, self.name, self.position))
        print('生存能力=[%d]，攻击伤害=[%d]，技能效果=[%d]，上手难度=[%d]' % (
            self.ab_viability, self.ab_damage, self.ab_effect, self.ab_difficulty))
        return

    def show_story(self):
        print('\n英雄的故事：正在编......')
        return

    def show_history(self):
        print('\n史实中的英雄：其实他没那么厉害......')
        return
