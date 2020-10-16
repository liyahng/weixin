# -*- encoding=utf8 -*-
__author__ = "lyh"

from airtest.core.api import *
from airtest.cli.parser import cli_setup


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
# 3、VIP用户-不同类型视频-播放器展示场景
ppLoginRes = login.ppLogin(accoutConf['vipUser'], 1)
#退到--首页
quit(2, 0)
if (ppLoginRes):
    try:
        res = longVideo.videoRightShow('vipUserVideoRightBtnShow', 'vipTicket')
    except:
        print('VIP用户--右--用券')
        pass
    quit()
    checkResult(res, '11VIP用户--右--用券')

    try:
        res = longVideo.videoRightShow('vipUserVideoRightBtnShow', 'vipPay')
    except:
        print('VIP用户--右--付费')
        pass
    quit()
    checkResult(res, '22VIP用户--右--付费')
    
    try:
        res = longVideo.videoCenterShow('vipUserVideoCenterBtnShow', 'vipTicket')
    except:
        print('VIP用户--中心--用券')
        pass
    quit()
    checkResult(res, '33VIP用户--中心--用券')

    try:
        res = longVideo.videoCenterShow('vipUserVideoCenterBtnShow', 'vipPay')
    except:
        print('VIP用户--中心--付费')
        pass
    quit()
    checkResult(res,'44VIP用户--中心--付费')
    
    #退出登录
        
    logoutRes = login.logOut(2)
    log('退出结果：', logoutRes)
else:
    print('登录失败~~~~')  