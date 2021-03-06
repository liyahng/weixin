# -*- encoding=utf8 -*-
__author__ = "lyh"

from airtest.core.api import *
#from airtest.cli.parser import cli_setup

from poco.drivers.android.uiautomation import AndroidUiautomationPoco
using("F:/aritest/ppWx/class")
from Ad import Ad
from Search import Search
from ShortVideo import ShortVideo
from Member import Member
from LongVideo import LongVideo
from Login import Login
from VipList import Vip
using("F:/aritest/ppWx/public")
from fun import SearchToLongvideo,quit,swipeStartIndex
using("F:/aritest/ppWx/conf")
from Conf  import accoutConf

poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)

if(poco(text = "首页").exists() == False):
    poco(text = "微信").click()
    poco.swipe([0.5, 0.4], [0.5, 0.8], duration = 1)
    poco(text = "PP视频").click()
    

vip = Vip()
login = Login('weixin')



#会员--微信登录--退出
thirdLoginRes = login.ThirdAuthLogin(2)
try:
    if(thirdLoginRes):
        print('登录结果：',  thirdLoginRes)	
        poco(text="开通会员").click()
        res = vip.clickBuy("1个月16元原价20元")
        assert_equal(res, True, '1个月16元原价20元-调起支付-展示金额正确16元')
except:
    print('error')
    pass

try:
    vipRes = vip.Bydesc()
    swipeStartIndex(2, 'down')
    print('连续包月说明：', vipRes)
    assert_equal(vipRes,True,'协议连接正确')
    #退出登录--todo
    quit(2,1)
    login.logOut(2)   
except:
    print('error')
    pass    




    


