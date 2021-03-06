# -*- encoding=utf8 -*-
__author__ = "lyh"
from airtest.core.api import *
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
import random

using("F:/aritest/ppWx/public")
from fun import SearchToLongvideo,quit,swipeStartIndex
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)

#1、用户信息展示(放到登录用户的位置)、商品展示、协议
class Vip():
    #VIP商品配置--暂不考虑变动
    def __init__(self, config = {}):
        self.vipGoodsList = {'首月2元 连续包月15元原价20元':{'price':'￥15.00', 'index': 0}, '6个月70元原价120元':{'price':'￥70.00', 'index':1}, '3个月40元原价60元':{'price':'￥40.00', 'index':2}, '1个月16元原价20元':{'price':'￥16.00', 'index':1}, '12个月130元原价240元': {'price':'￥130.00', 'index':4}, '12个月130元原价240元':{'price':'￥130.00', 'index':5}}
        
    #VIP商品列表展示
    def goodsShow(self):
        res = {}
        for index in self.vipGoodsList:
            print(index, poco(text = index).exists())
            res[index] = poco(text = index).exists()
        return res
    
    #点击购买--是否弹框-暂时未实现---
    def clickBuy(self, goodsName):
        print('goodsName---', goodsName)
        num = self.vipGoodsList[goodsName]['index']
        print(num)
        print('购买数量', len(poco(text = '购买')))
        #return 
        if (poco(text = '购买')[num].exists()):
            sleep(3)
            poco(text = '购买')[num].click()
            sleep(3)
            print('价格', self.vipGoodsList[goodsName]['price'])
            if (poco(text = self.vipGoodsList[goodsName]['price']).exists()):
                poco(desc = "返回").click()
                poco(text = "放弃").click()
                return True
        return False   
    
    #连续包月说明
    def Bydesc(self):
        poco.swipe([0.5, 0.9], [0.5, 0.3])    
        if (poco(text = "视频会员服务条款").exists() and poco(text = "连续包月说明")[1].exists()):
            poco(text = "视频会员服务条款").click()
            if (poco(text = "PP视频会员服务条款").exists()):
                quit(2, 1, False)
            else:
                print('PP视频会员服务条款--不存在')
                return False
            poco(text = "连续包月说明")[1].click()
            sleep(2)
            if (poco(text = "PP视频会员连续包月服务协议").exists()):
                quit(2, 1, False)
            else:
                print('PP视频会员连续包月服务协议--不存在')
                return False
            return True
        else:
            return False

# vip = Vip()
# vipRes = vip.Bydesc()
# swipeStartIndex(2, 'down')
# print(vipRes)

# res = vip.clickBuy('1个月16元原价20元')
# print(res)