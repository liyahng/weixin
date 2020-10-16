# -*- encoding=utf8 -*-
__author__ = "lyh"
from airtest.core.api import *
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)
#1、微信登录
#2、PP账户登陆
#3、退出登录
#登录path

def SearchToLongvideo(name):
    print('搜索进入长视频', name)
    #获取搜索点击元素
    searchButton = poco("android.widget.FrameLayout").offspring("android.webkit.WebView").offspring("android.widget.Image")
    searchButton.click()
    text(name)
    poco(text="搜索").wait_for_appearance()
    poco(text="搜索").click()

    #搜索结果页面展示【立即播放按钮】
    poco(text="立即播放").wait_for_appearance()
    if(poco(text="立即播放").exists()):
        poco(text="立即播放").click()
        return 1
    return 0

#type: 1、以【PP视频】为标题的返回到首页 2、其它方式   num：返回次数
def quit(type = 1, num = 1):
    print('8888888888888888888888888')
    print('位置：', poco(text = "PP视频").get_position()[0])
    if type == 1:
        # 只适用于以【PP视频】未标题的返回到首页 (首页 【PP视频】标题位置X=0.11  其他页面是0.17)
        while (poco(text = "PP视频").get_position()[0] >= 0.13):
            keyevent("back")
            sleep(2)
    else:
        for index in range(num):
            keyevent("back")
            sleep(2)
    poco(text = "首页").click()
    return True
    
class Login(object):
    #页面元素初始化
    def __init__(self, applet, config = {}):
        self.indexTabs = {'indextab':'首页', 'Sports':'体育', 'channel': '体育', 'member':'会员', 'mine': '我的'}
        self.set = {'accountCancel':'注销', 'logoutButton': '退出登录', 'confirm':'确定', 'cancel':'取消'}
        self.login = {'accountPwdButton':'账号密码登录', 'pplogintab':'PP账号登录', 'ppAccount': 'PP视频账号', 'pwd':'密码','loginButton':'登录'}
        self.tabMember = {'loginButton':'登录', 'renew':'续费会员','open':'开通会员'}
        self.longVideo = {'rightLoginTip1':'登录', 'centerLoginBtn': ' 观看整片，请登录'}
        self.tabMine = {'loginButton':'点我登录', 'set':'设置'}
        if applet == 'baidu':
            self.tabMine['loginButton'] = '点击登录'
        self.loginPopup = {'thirdLoginButton':'微信登录', 'ppLoginButton':'PP视频账号登录','authAllow' :'允许', 'longVideoTitle': '观看整片请登录'} 
        if applet == 'baidu':
            self.loginPopup['thirdLoginButton'] = '手机号码一键登录'

        print('self',self.indexTabs)
        
    #第三方授权登录
    def ThirdAuthLogin(self, path = 1):
        self.loginPopupF(path, self.loginPopup['thirdLoginButton'])
        sleep(3)
        return self.checkLogin(path)
    
    #PP账户登录
    def ppLogin(self, accountConf, path = 1):
        #切换到PP账号登录面板
        self.loginPopupF(path, self.loginPopup['ppLoginButton'])
        poco(text = self.login['accountPwdButton']).wait(2).click()

        #切换到PP账号登录----存在则点击，不存在则定位点击
        if (poco(text = self.login['pplogintab']).exists()):
            poco(text = self.login['pplogintab']).wait(2).click()
        else:
            print('PP账号登录tab---位置点击')
            poco(text = "登录").click([5, 3.5])
            
        sleep(2)
        print('PP视频账号--输入框--数量',len(poco(text = self.login['ppAccount'])))
        poco(text = self.login['ppAccount']).click()
        text(accoutConf['commonUser']['account'])
        print('密码--输入框--数量', len(poco(text = self.login['pwd'])))
        
        #头条光标选中问题--多试几次
        for index in range(3):
            poco(text = self.login['pwd']).click()
        sleep(1)
        text(accoutConf['commonUser']['pwd'])
        sleep(1)
        #我的页面===【登录】关键词2个===需要取第二个
        print('【登录】按钮--数量', len(poco(text = self.login['loginButton'])))
        poco(text = self.login['loginButton'])[1].wait(2).click()
        sleep(2)
        return self.checkLogin(path)
    
    #登录弹框组件
    def loginPopupF(self, path, loginType):
        #path--1、个人  2、会员 3、长视频页-右上角登录 4、长视频--播放结束展示
        #loginType---1、微信账号登录  2、PP视频账号登录 
        #poco(text = loginType).wait(2).click()
        if path == 1:
            #首次进入关闭弹框
            poco(text = self.indexTabs['mine']).click()
            poco(text = self.indexTabs['mine']).click([0.5, 2])
            print('请登录---按钮',  poco(text = self.tabMine['loginButton']).exists())
            poco(text = self.tabMine['loginButton']).click()
        elif path == 2:
            poco(text = self.indexTabs['member']).click()
            poco(text = self.tabMember['loginButton']).click()
        elif path == 3:
            #前贴广告播放完---还是傻傻的等10秒吧---其它方式不靠谱
            sleep(20)
            if  (poco(text = self.longVideo['rightLoginTip1']).exists()):
                poco(text = self.longVideo['rightLoginTip1']).click()
            else:
                print('登录--按钮找不到元素')
                return False
        else:
            return False
        # -#:0.55--0.62---PP 都是PP账号登录   0.48-0.50是微信账号登录---新版UI
        popupPositionWx = [0.5, 0.55] if (path == 3) else [0.5, 0.49]
        popupPositionPP = [0.5, 0.66] if (path == 3) else [0.5, 0.6]

        if (loginType == self.loginPopup['ppLoginButton']):
            print('登录弹框----PP视频账号登录')
            poco.click(popupPositionPP)
        else:
            print('登录弹框----第三方登录')
            poco.click(popupPositionWx) 
        #poco(text = loginType).wait(2).click()
        if (poco(text = self.loginPopup['authAllow']).exists()):
            poco(text = self.loginPopup['authAllow']).click()
        return True
    
    #退出登录
    def logOut(self, path = 1):
        #根据不同路径返回到--底部tab【我的】页面
        if path == 1:
            print('我的----登录')
        elif path == 2:
            poco(text = self.indexTabs['mine']).click()
        elif path == 3:#返回到首页--todo
            self.quit()
        else:
            print('退出登录--路径不存在~~~')
        #页面刷新需要点time--否则容易点击进入播放记录
        sleep(3)
        poco(text = self.tabMine['set']).wait_for_appearance()
        if (poco(text = self.tabMine['set']).exists()):
            poco(text = self.tabMine['set']).click()
        else: 
            return False
        #等待时间不够可能会点击进入其他地方
        if (poco(text = self.set['logoutButton']).exists()):
            poco(text = self.set['logoutButton']).click()
            poco(text = self.set['confirm']).click()
        else:
            return False
        return poco(text = self.tabMine['loginButton']).exists()
    
    #检测登录是否成功
    def checkLogin(self, path):
        if path == 1:
            res = poco(text = self.tabMine['set']).exists()
            print('设置---', poco(text = self.tabMine['set']).exists())
        elif path == 2:
            res = (poco(text = self.tabMember['open']).exists() or poco(text = self.tabMember['renew']).exists())
        elif path == 3:
            res = poco(text = self.longVideo['rightLoginTip1']).exists() == False
            print('购买单片--展示', poco(text = '购买单片').exists())
        else:
            res = False
        return res
    def quit(self):
        return 555
class LongVideo():
    #从搜索进入某个长视频页面
    def joinLongVideo(self, videoName):
        return True
#账户配置		
accoutConf = {'commonUser':{'account':'19011111122', 'pwd':'pptv123456'}, 'vipUser':{'account':'19011111167', 'pwd':'pptv123456'}}
vipVideoName = ' 寒战'
login = Login('weixin')
longVideo = LongVideo()

# for index in range(3):
#     print('第', index, '次')
#     thirdLoginRes = login.ThirdAuthLogin(1)
#     if (thirdLoginRes):
#         logoutRes = login.logOut()
#         print('退出结果', logoutRes)
#         if logoutRes == False:
#             break
#     else :
#         break
#         print('微信登录-----登录失败')

# #个人--PP账号登录--退出
# for index in range(6):    
#     print('第', index, '次')
#     ppLoginRes = login.ppLogin(accoutConf, 1)
#     if (ppLoginRes):
#         logoutRes = login.logOut()
#         print("PP账号----退出结果", logoutRes)
#     else:
#         print('PP账号-----登录失败')

#会员--微信登录--退出
# thirdLoginRes = login.ThirdAuthLogin(2)
# if (thirdLoginRes):
#     print('登录结果：',  thirdLoginRes)
#     login.logOut(2)

# #个人--PP账号登录--退出
# ppLoginRes = login.ppLogin(2)
# if (ppLoginRes):
#     login.logOut(2)

#长视频--微信登录--退出
# SearchToLongvideo(vipVideoName)
# thirdLoginRes = login.ThirdAuthLogin(3)
# print('登录结果:', thirdLoginRes)
# if (thirdLoginRes and quit()):
#     print('退出登录----')
#     logoutRes = login.logOut(2)
#     if (logoutRes == False):
#         print('退出失败~~~~')

# #长视频--PP账号登录--退出
# SearchToLongvideo(vipVideoName)
# ppLoginRes = login.ppLogin(accoutConf, 3)
# print('登录结果:', ppLoginRes)
# if (ppLoginRes and quit()):
#     print('退出登录----')
#     logoutRes = login.logOut(2)
#     if (logoutRes == False):
#         print('退出失败~~~~')