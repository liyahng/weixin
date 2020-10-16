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
using("F:/aritest/ppWx/public")
from fun import SearchToLongvideo,quit,swipeStartIndex
using("F:/aritest/ppWx/conf")
from Conf  import accoutConf

poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)

if(poco(text = "首页").exists() == False):
    poco(text = "微信").click()
    poco.swipe([0.5, 0.4], [0.5, 0.8], duration = 1)
    poco(text = "PP视频").click()

login = Login('weixin')
longVideo = LongVideo()

def  checkResult(data, msg = ''):
    for key in data:
        try:
            assert_equal(data[key], True, msg + '--【' + key + '】')
        except:
            print('------')
            pass
    
#长视频播放器逻辑展示
# 1、未登录-不同类型视频-播放器展示场景
#未登录---观看VIP免费电影
try:
    res = longVideo.videoCenterShow('noLoginCenterBtnShow', 'vipFreeMovie')
except:
    print('未登录--VIP电影--中心')
    pass    
quit()
log(str(res))
checkResult(res, '未登录--VIP电影--中心')

try:
    res = longVideo.videoRightShow('noLoginRightBtnShow', 'vipFreeMovie')
except:
    print('未登录--VIP电影--右')
    pass
quit()
checkResult(res, '未登录--VIP电影--右')

# # #未登录----观看VIP电视剧
try:
    res = longVideo.videoCenterShow('noLoginCenterBtnShow', 'vipFreeTv')
except:
    print('未登录--VIP电视剧--中心')
    pass    
quit()
checkResult(res, '未登录--VIP电视剧--中心')

try:
    res = longVideo.videoRightShow('noLoginRightBtnShow', 'vipFreeTv')
except:
    print('未登录--VIP电视剧--右')
    pass 
quit()
checkResult(res, '未登录--VIP电视剧--右')


# # #未登录---观看用券视频
try:
    res = longVideo.videoCenterShow('noLoginCenterBtnShow', 'vipTicket')
except:
    print('未登录--用券--中心')
    pass 
quit()
checkResult(res, '未登录--用券--中心')

try:
    res = longVideo.videoRightShow('noLoginRightBtnShow', 'vipTicket')
except:
    print('未登录--用券--右')
    pass 
quit()
checkResult(res, '未登录--用券--右')

# # #未登录---观看付费视频
try:
    res = longVideo.videoCenterShow('noLoginCenterBtnShow', 'vipPay')
except:
    print('未登录--付费--中心')
    pass
quit()
checkResult(res, '未登录--付费--中心')

try:
    res = longVideo.videoRightShow('noLoginRightBtnShow', 'vipPay')
except:
    print('未登录--付费--右--失败')
    pass
quit()
checkResult(res, '未登录--付费--右')

