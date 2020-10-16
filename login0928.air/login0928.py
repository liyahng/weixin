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
    
#账户配置		
accoutConf = {'commonUser':{'account':'19011111122', 'pwd':'pptv123456'}, 'vipUser':{'account':'19011111167', 'pwd':'pptv123456'}}
vipVideoName = '寒战'
login = Login('weixin')
longVideo = LongVideo()

#断言统一处理
def  checkResult(data, msg = ''):
    if isinstance(data, dict):
        for key in data:
            try:
                assert_equal(data[key], True, msg + '--【' + key + '】')
            except:
                print('------')
                pass
    else:
        try:
            assert_equal(data, True, msg)
        except:
            print('------')
            pass

#我的--微信登录-退出        
try:
    thirdLoginRes = login.ThirdAuthLogin(1)
    log('res;',thirdLoginRes)
    if (thirdLoginRes):
        logoutRes = login.logOut()
        log('退出结果', logoutRes)
except:
    print('微信登录--我的--失败')
    pass
checkResult(thirdLoginRes, '微信登录--我的')


#会员--微信登录--退出
try:
    thirdLoginRes = login.ThirdAuthLogin(2)
    if (thirdLoginRes):
        print('登录结果：',  thirdLoginRes)
        login.logOut(2)
except:
    print('微信登录--会员--失败')
    pass
checkResult(thirdLoginRes, '微信登录--会员')


# #长视频--微信登录--退出
try:
    SearchToLongvideo(vipVideoName)
    thirdLoginRes = login.ThirdAuthLogin(3)
    print('登录结果:', thirdLoginRes)
    if (thirdLoginRes and quit()):
        print('退出登录----')
        logoutRes = login.logOut(2)
        if (logoutRes == False):
            print('退出失败~~~~')
except:
    print('微信--长视频--失败')
    pass
checkResult(thirdLoginRes, '微信--长视频')

# #个人--PP账号登录--退出
try:
    ppLoginRes = login.ppLogin(accoutConf['commonUser'],1)
    if (ppLoginRes):
        login.logOut(1)
except:
    print('PP账号--我的--失败')
    pass
checkResult(ppLoginRes, 'PP账号--我的')

# #长视频--PP账号登录--退出
try:
    SearchToLongvideo(vipVideoName)
    ppLoginRes = login.ppLogin(accoutConf['commonUser'], 3)
    print('登录结果:', ppLoginRes)
    if (ppLoginRes and quit()):
        print('退出登录----')
        logoutRes = login.logOut(2)
        if (logoutRes == False):
            print('退出失败~~~~')
except:
    print('PP账号--长视频--失败')
    pass
checkResult(ppLoginRes, 'PP账号--长视频')