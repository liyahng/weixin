# -*- encoding=utf8 -*-
__author__ = "lyh"
from airtest.core.api import *
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
import random
using("F:/aritest/ppWx/public")
from fun import quit,swipeStartIndex,SearchToLongvideo
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)

#会员页
class Member():
    #会员页模块配置
    def __init__(self, config = {}):
        self.moduleConf = ['正在热播', 'VIP院线电影', 'VIP热血正义', 'VIP经典古装', '好莱坞专区', 'VIP精选系列', 'VIP优质好剧', 'VIP好莱坞大片', 'VIP网络电影', 'VIP动漫', 'VIP海外电影']
        poco(text = "会员").click()

    #模块展示
    def moduleShow(self):
        res = {}
        for index in self.moduleConf:
            res1 = self.swipeModule(index)
            if (res1 == False):
                self.swipeModule(index)
            print(index, poco(text = index).exists())
            y =  poco(text = index).get_position()[1]
            shift = y-0.12
            poco.swipe([0.5, 0.8], [0.5, 0.8-shift])
            aa = poco(text = index).exists()
            bb = self.clickJump(index)
            res[index] = {'isExists':aa, 'click':bb}
            print('aa,bb----', aa,bb)
        return res
    
    #滑动到展示的位置
    def swipeModule(self, name):
        sleep(2)
        print(name, poco(text = name).exists())
        if (poco(text = name).exists()):
            print('找到', name)
            return True
        else:
            poco.swipe([0.5, 0.8], [0.5, 0.6]) #滑动五分之一的屏
            print('未找到', name)
            return False
    
    #跳转长视频页面
    def clickJump(self, name):
        poco(text = name).click([0, 2])
        if (poco(text = "播放").exists() or poco(text = "暂停").exists()):
            quit(2, 1, False)
            return True
        elif (poco(text = "电视剧").exists()):
            poco(text = "会员").click()
            return True
        else:
            quit(2, 1, False)
            print('未知----')
        return False
    
    #轮播图点击
    def carousel(self):
        poco(text = "PP视频").click([0, 2])
        if (poco(text = "播放").exists() or poco(text = "暂停").exists()):
            quit(2, 1, False)
            return True
        else:
            quit(2, 1, False)
        return False
    #登录模块
    def loginModule(self):
        if (poco(text  = "开通会员").exists or poco(text = "续费会员").exists() or poco(text = "登录").exists()):
            return True
        return False
