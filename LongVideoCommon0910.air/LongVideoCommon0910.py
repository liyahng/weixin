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

# 2、普通用户-不同类型视频-播放器展示场景
ppLoginRes = login.ppLogin(accoutConf['commonUser'], 1)
# #退到--首页
quit(2, 0)
if (ppLoginRes):
    try:
        res = longVideo.videoRightShow('normalUserVideoRightBtnShow', 'vipFreeTv')
    except:
        print('普通用户--右--VIP电视剧')
        pass
    quit()
    checkResult(res, '普通用户--右--VIP电视剧')

    try:
        res = longVideo.videoRightShow('normalUserVideoRightBtnShow', 'vipFreeMovie')
    except:
        print('普通用户--右--VIP电影')
    quit()
    checkResult(res, '普通用户--右--VIP电影')

    try:
        res = longVideo.videoRightShow('normalUserVideoRightBtnShow', 'vipTicket')
    except:
        print('普通用户--右--用券电影')
        pass
    quit()
    checkResult(res, '普通用户--右--用券电影')

    try:
        res = longVideo.videoRightShow('normalUserVideoRightBtnShow', 'vipPay')
    except:
        print('普通用户--右--付费')
        pass
    quit()
    checkResult(res, '普通用户--右--付费')

    try:
        res = longVideo.videoCenterShow('normalUserVideoCenterBtnShow', 'vipFreeTv')
    except:
        print('普通用户--中心--VIP电视剧')
        pass
    quit()
    checkResult(res, '普通用户--中心--VIP电视剧')

    try:
        res = longVideo.videoCenterShow('normalUserVideoCenterBtnShow', 'vipFreeMovie')
    except:
        print('普通用户--中心--VIP电影')
        pass
    quit()
    checkResult(res, '普通用户--中心--VIP电影')

    try:
        res = longVideo.videoCenterShow('normalUserVideoCenterBtnShow', 'vipTicket')
    except:
        print('普通用户--中心--用券')
        pass
    quit()
    checkResult(res, '普通用户--中心--用券')

    try:
        res = longVideo.videoCenterShow('normalUserVideoCenterBtnShow', 'vipPay')
    except:
        print('普通用户--中心--付费')
        pass
    quit()
    checkResult(res, '普通用户--中心--付费')
    
    #退出登录
    logoutRes = login.logOut(2)
    log('退出结果：', logoutRes)
else:
    log('登录失败~~~~')
 