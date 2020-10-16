# -*- encoding=utf8 -*-
__author__ = "lyh"
from airtest.core.api import *
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
import random

poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)

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
def quit(type = 1, num = 1, isIndex = True):    
    if type == 1:
        print('位置：', poco(text = "PP视频").get_position()[0])
        # 只适用于以【PP视频】未标题的返回到首页 (首页 【PP视频】标题位置X=0.11  其他页面是0.17)
        while (poco(text = "PP视频").get_position()[0] >= 0.13):
            keyevent("back")
            sleep(2)
    else:
        for index in range(num):
            keyevent("back")
            sleep(2)
    if (isIndex):
        poco(text = "首页").click()
    return True

# N元购买、用券观看、续费会员用券看、邀请好友拼团、开通会员免费看、开通会员特价看、开通会员用券看
# 【'观看整片，请 ', '登录'】、【'观看整片，请 ', '开通会员'】、【'观看整片，请 ', '购买单片'】、【'观看整片，请 ', '用券'】、【'观看整片，请 ', '续费会员用券'】

class LongVideo():
    
    #视频配置（VIP免费、用券、付费）
    def __init__(self, config = {}):
        ##安卓端
        #视频配置
        self.freeTv = ['球王', '雾非雾', '财神有道']
        self.freeMovie = ['千局百计', '好想吃拉面', '青春派', '最终玩家']
        self.vipFreeTv = ['从将军到士兵']
        self.vipFreeMovie =['寒战', '灭绝', '毒战']
        self.vipTicket = ['速度与激情8（英文原版）','至暗时刻', '掠食城市(普通话)', '谍影重重5']
        self.vipTicket = ['速度与激情8（英文原版）']
        self.vipPay = ['爱玛', '王者天下']
        #a = random.choice(self.VipTicket)

        #时长
        self.freeMovieDuration = {'千局百计':'110:37', '好想吃拉面':'102:03', '青春派':'83:36', '最终玩家':'86:15'}
        
        #长视频播放器--按钮场景值
        self.videoRightBtns = {'commonFront':'观看整片，请', 'login':'登录', 'buyMember':'开通会员', 'buySingleChip':'购买单片', 'ticket': '用券', 'renewMemberTicket':'续费会员用券', 'buyMemberTicket':'开通会员用券'}
        #type 1、登录  2、N元购买   3、用券观看  4、跳转开通会员页面 5、邀请好友拼团
        self.videoCenterBtns = {'login': {'text':'观看整片，请登录', 'type':1},'buy':{'text':'5.0元购买', 'type':2},'vipbuy':{'text':'2.0元购买','type':2}, 'useTicket':{'text':'用券观看', 'type':3}, 'renewTicket': {'text':'续费会员用券看', 'type':4},'pintuan':{'text':'邀请好友拼团', 'type':5}, 'buyMemberFree':{'text':'开通会员免费看', 'type':4}, 'buyMemberPay': {'text':'开通会员特价看', 'type':4}, 'buyMemberTicket':{'text':'开通会员用券看', 'type':4}}
        
        #数据格式处理
        self.btnType = {}
        for index in self.videoCenterBtns:
            print(index)
            self.btnType[self.videoCenterBtns[index]['text']] = self.videoCenterBtns[index]['type']
            #self.btnType[self.videoCenterBtns[index]['text']] = self.btnType[self.videoCenterBtns[index]['type']]
        
        print(self.btnType)
        ##未登录播放器-右上角||中心位置--展示场景
        self.noLoginRightBtnShow = [self.videoRightBtns['commonFront'], self.videoRightBtns['login']]
        self.noLoginCenterBtnShow = [self.videoCenterBtns['login']]
        
         ##普通用户播放器-右上角--展示场景
        self.normalUserVideoRightBtnShow = {'vipFreeTv':[self.videoRightBtns['commonFront'], self.videoRightBtns['buyMember']], 'vipFreeMovie':[self.videoRightBtns['commonFront'], self.videoRightBtns['buyMember']], 'vipTicket':[self.videoRightBtns['commonFront'], self.videoRightBtns['ticket'], self.videoRightBtns['buyMemberTicket']], 'vipPay':[self.videoRightBtns['commonFront'], self.videoRightBtns['buySingleChip']]}
        
        ##普通用户播放器--中心位置-展示场景
        self.normalUserVideoCenterBtnShow = {'vipFreeTv':[self.videoCenterBtns['buyMemberFree']['text'], self.videoCenterBtns['pintuan']['text']], 'vipFreeMovie':[self.videoCenterBtns['buyMemberFree']['text'], self.videoCenterBtns['pintuan']['text'], self.videoCenterBtns['buy']['text']], 'vipTicket':[self.videoCenterBtns['useTicket']['text'], self.videoCenterBtns['buyMemberTicket']['text'], self.videoCenterBtns['buy']['text']], 'vipPay':[self.videoCenterBtns['buy']['text'], self.videoCenterBtns['buyMemberPay']['text']]}

        ##VIP用户播放器-右上角--展示场景
        self.vipUserVideoRightBtnShow = { 'vipTicket':[self.videoRightBtns['commonFront'], self.videoRightBtns['ticket'],self.videoRightBtns['renewMemberTicket']], 'vipPay':[self.videoRightBtns['commonFront'], self.videoRightBtns['buySingleChip']]}
        
        ##VIP用户播放器-中心位置--展示场景
        self.vipUserVideoCenterBtnShow = {'vipTicket':[self.videoCenterBtns['useTicket']['text'], self.videoCenterBtns['renewTicket']['text'], self.videoCenterBtns['vipbuy']['text']], 'vipPay':[self.videoCenterBtns['vipbuy']['text']]}
        
        #按钮展示规则  |||  视频类型
        self.btnShow = {'noLoginRightBtnShow' : self.noLoginRightBtnShow, 'noLoginCenterBtnShow': self.noLoginCenterBtnShow, 'normalUserVideoRightBtnShow':self.normalUserVideoRightBtnShow, 'vipUserVideoRightBtnShow':self.vipUserVideoRightBtnShow, 'normalUserVideoCenterBtnShow':self.normalUserVideoCenterBtnShow, 'vipUserVideoCenterBtnShow':self.vipUserVideoCenterBtnShow}
        self.videoType = {'vipFreeTv' : self.vipFreeTv, 'vipFreeMovie' : self.vipFreeMovie, 'vipTicket': self.vipTicket, 'vipPay':self.vipPay, 'freeMovie':self.freeMovie}
    
    #登录播放器展示文案  loginType;videoType:1、VIP免费电视剧（vipFreeTv）、2、VIP免费电影（vipFreeMovie）3、VIP用券（vipTicket）  4、VIP付费（vipPay）
    def videoRightShow(self, loginType = 'noLoginRightBtnShow', videoType = 'vipTicket'):
        #随机选择某种类型的视频--从搜索进入
        videoName = random.choice(self.videoType[videoType])
        SearchToLongvideo(videoName)

        #电视剧类型--需要切换到VIP选集
        if (videoType == 'vipFreeTv'):
            poco(text = 'VIP').click()
        else:
            #点击暂停
            sleep(20) #广告时长
            
        if (poco(text = "暂停").exists()):
            poco.click([0.5,0.2])
            poco(text = "暂停").click()
        if (loginType == 'noLoginRightBtnShow'):
            arr = self.btnShow[loginType]
        else:
            arr = self.btnShow[loginType][videoType]
        
        sleep(2)
        resIsExists = {}
        for index in arr:
            print('index---', index)
            if (poco(text = index).exists()):
                resIsExists[index] = True
            else:
                resIsExists[index] = False
        
        print('resIsExists', resIsExists)
        return resIsExists
    
    #播放器中心位置
    def videoCenterShow(self, loginType = 'noLoginCenterBtnShow', videoType = 'vipTicket'):
        videoName = random.choice(self.videoType[videoType])
        SearchToLongvideo(videoName)
        
        #电视剧类型--需要切换到VIP选集
        if (videoType == 'vipFreeTv'):
            poco(text = 'VIP').click()
        else:
            sleep(20) #广告时长
        
        #播放至视频结束位置
        isEnd = self.slideVideo(10)
        print('isEnd----', isEnd)
        if (isEnd == False):
            isEnd = self.slideVideo(2)
        print('isEnd----', isEnd)
        
        if (loginType == 'noLoginCenterBtnShow'):
            arr = self.btnShow[loginType]
        else:
            arr = self.btnShow[loginType][videoType]
        
        print('arr', arr)
        resIsExists = {}
        for index in arr:
            print('index---', index)
            if (poco(text = index).exists()):
                resIsExists[index] = True
            else:
                resIsExists[index] = False
        
        print('videoName--', videoName, 'resIsExists', resIsExists)        
        return resIsExists
    
    #观看有权益的视频
    def watchRightsVideo(self, loginType = 'normalUserVideoCenterBtnShow', videoType = 'freeMovie'):
        #随机选择一个免费视频进入
        videoName = random.choice(self.videoType[videoType])
        SearchToLongvideo(videoName)
        sleep(20) #广告时长

        #总时长---有观看整片的权益  --滑动到最后暂时无法实现---
        duration = self.freeMovieDuration[videoName]
        if (poco(text = duration).exists()):
            return True
        else:
            return False
    
    #开通会员 {'login': '观看整片，请登录','buy':'5.0元购买','vipbuy':'2.0元购买', 'useTicket':'用券观看', 'renewTicket': '续费会员用券看','pintuan':'邀请好友拼团', 'buyMemberFree':'开通会员免费看', 'buyMemberPay': '开通会员特价看', 'buyMemberTicket':'开通会员用券看'}
    #点击播放器----button
    def clickBtn(self, loginType = 'normalUserVideoCenterBtnShow', videoType = 'vipFreeMovie'):
        videoName = random.choice(self.videoType[videoType])
        SearchToLongvideo(videoName)
        
        #电视剧类型--需要切换到VIP选集
        if (videoType == 'vipFreeTv'):
            poco(text = 'VIP').click()
        else:
            sleep(20) #广告时长

        #播放至视频结束位置
        isEnd = self.slideVideo(10)
        print('isEnd----', isEnd)
        if (isEnd == False):
            isEnd = self.slideVideo(2)
        print('isEnd----', isEnd)
        
        if (loginType == 'noLoginCenterBtnShow'):
            arr = self.btnShow[loginType]
        else:
            arr = self.btnShow[loginType][videoType]        
        
        res = {}
        for index in arr:
            print('index---', index)
            if (poco(text = index).exists()):
                print(index, poco(text = index).exists())
                res[index] = self.checkAfterShow(index, videoName)
                
        return res
                
    #检测点击按钮后--页面响应是否符合预期  [续费会员用券看||开通会员免费看|| 开通会员特价看||开通会员用券看]、 【2.0元购买 || 5.0元购买】、【用券观看】【邀请好友拼团】----1、登录  2、N元购买   3、用券观看  4、跳转开通会员页面 5、邀请好友拼团
    def checkAfterShow(self, textBtn, videoName):
        #---退到前一个页面---todo
        print('点击' + textBtn)
        poco(text = textBtn).click()
        if (self.btnType[textBtn] == 1):
            print(1)
            #弹框 ==获取不到元素---todo
        elif(self.btnType[textBtn] == 2):
            print(2)
            if (poco(text = '有效天数：7天').exists() and poco(text = '确认').exists()):
                poco(text = '确认').click() #跳转--支付
                print('支付---', poco(text = '支付').exists())
                print('价格---', poco(text = '价格').exists())
                print('商品名称---', poco(text = '商品名称').exists())
                print('确认支付---', poco(text = '确认支付').exists())
                sleep(2)
                if (poco(text = '支付').exists() and poco(text = '价格').exists() and poco(text = '商品名称').exists() and poco(text = '确认支付').exists()):
                    print('点击--确认支付--按钮')
                    poco(text = '确认支付').click() #调起键盘支付
                    print('上海聚力传媒技术有限公司', poco(text = '上海聚力传媒技术有限公司').exists())
                    sleep(3)
                    if (poco(text = '上海聚力传媒技术有限公司').exists()):
                        #--5----540 , 1966----0.50,0.90  ; 4----173 1953----0.16,0.89  6----900.1961---0.83,0.90;  1-----181,1800--0.16,0.82; 5-----540 , 1966--0.50,0.90    zhengping 1080 , 2174--todo
#                         poco.click([0.5,0.9])  
#                         poco.click([0.16,0.89])
#                         poco.click([0.83,0.90])
#                         poco.click([0.16,0.82])
#                         poco.click([0.5,0.9])
#                         poco.click([0.16,0.82])
                        #返回到长视频页面
                        sleep(3)
                        poco(name = '关闭').click()
                        quit(2, 1, False)
                        return True
        elif(self.btnType[textBtn] == 3): #弹框元素有概率取不到
            print(3)
            sleep(3)
            title = "购买《"+ videoName +"》"
            print('有效天数：7天', poco(text = '有效天数：7天').exists())
            print('确认', poco(text = '确认').exists())
            print(title, poco(text = title).exists())
            if (poco(text = '有效天数：7天').exists() and poco(text = '确认').exists() and poco(text = title).exists()):
                poco(text = '取消').click()
                return True
            
        elif(self.btnType[textBtn] == 4):
            print(4)
            #检查是否跳转页面成功----PP视频会员购买---标题存在--暂定
            if (poco(text = 'PP视频会员购买').exists() and poco(text = '会员套餐').exists()  and poco(text = '购买').exists()):
                quit(2, 1, False)
                return True
            
        elif(self.btnType[textBtn] == 5):
            print(5)
            ##todo
        else :
            print('未知类型--按钮')
        return False
        
    #滑动无权益视频至播放结束~
    def slideVideo(self, num = 10):
        times = 0
        while times < num:
            poco.swipe([0.15, 0.28], [0.95, 0.28], duration = 1.5)
            times = times + 1
            
            #不需要滑动多次（如：从4分钟开始播放 ||   电视剧一般都是10多秒）
            if (times % 3 == 0):
                if (poco(text = "播放").exists() == False and poco(text = "暂停").exists() == False):
                    return True
            print(times)
        print('播放', poco(text = "播放").exists())
        print('暂停', poco(text = "暂停").exists())
        if (poco(text = "播放").exists() or poco(text = "暂停").exists()):
            return False
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
    def ppLogin(self, accountConfig, path = 1):
        #切换到PP账号登录面板
        self.loginPopupF(path, self.loginPopup['ppLoginButton'])
        poco(text = self.login['accountPwdButton']).wait(2).click()

        print('accoutConf', accoutConf)
        #切换到PP账号登录----存在则点击，不存在则定位点击
        if (poco(text = self.login['pplogintab']).exists()):
            poco(text = self.login['pplogintab']).wait(2).click()
        else:
            print('PP账号登录tab---位置点击')
            poco(text = "登录").click([5, 3.5])
            
        sleep(2)
        print('PP视频账号--输入框--数量',len(poco(text = self.login['ppAccount'])))
        poco(text = self.login['ppAccount']).click()
        text(accountConfig['account'])
        print('密码--输入框--数量', len(poco(text = self.login['pwd'])))
        
        #头条光标选中问题--多试几次
        for index in range(3):
            poco(text = self.login['pwd']).click()
        sleep(1)
        text(accountConfig['pwd'])
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

accoutConf = {'commonUser':{'account':'19011111122', 'pwd':'pptv123456'}, 'vipUser':{'account':'19011111167', 'pwd':'pptv123456'}}
login = Login('weixin')
longVideo = LongVideo()
# 1、未登录-不同类型视频-播放器展示场景
#未登录---观看VIP免费电影
# longVideo.videoCenterShow('noLoginCenterBtnShow', 'vipFreeMovie')
# quit()

# longVideo.videoRightShow('noLoginRightBtnShow', 'vipFreeMovie')
# quit()

# #未登录----观看VIP电视剧
# longVideo.videoCenterShow('noLoginCenterBtnShow', 'vipFreeTv')
# quit()

# longVideo.videoRightShow('noLoginRightBtnShow', 'vipFreeTv')
# quit()


# #未登录---观看用券视频
# longVideo.videoCenterShow('noLoginCenterBtnShow', 'vipTicket')
# quit()

# longVideo.videoRightShow('noLoginRightBtnShow', 'vipTicket')
# quit()

# #未登录---观看付费视频
# longVideo.videoCenterShow('noLoginCenterBtnShow', 'vipPay')
# quit()

# longVideo.videoRightShow('noLoginRightBtnShow', 'vipPay')
# quit()

# #免费视频观看整片
# res = longVideo.watchRightsVideo('freeMovie')
# quit()
# print(res)



# 2、普通用户-不同类型视频-播放器展示场景
#ppLoginRes = login.ppLogin(accoutConf['commonUser'], 1)
#退到--首页
#quit(2, 0)
#if (ppLoginRes):
#     longVideo.videoRightShow('normalUserVideoRightBtnShow', 'vipFreeTv')
#     quit()

#     longVideo.videoRightShow('normalUserVideoRightBtnShow', 'vipFreeMovie')
#     quit()

#     longVideo.videoRightShow('normalUserVideoRightBtnShow', 'vipTicket')
#     quit()

#     longVideo.videoRightShow('normalUserVideoRightBtnShow', 'vipPay')
#     quit()

#     longVideo.videoCenterShow('normalUserVideoCenterBtnShow', 'vipFreeTv')
#     quit()

#     longVideo.videoCenterShow('normalUserVideoCenterBtnShow', 'vipFreeMovie')
#     quit()

#     longVideo.videoCenterShow('normalUserVideoCenterBtnShow', 'vipTicket')
#     quit()

#     longVideo.videoCenterShow('normalUserVideoCenterBtnShow', 'vipPay')
#     quit()
#else:
#     print('登录失败~~~~')

# 3、VIP用户-不同类型视频-播放器展示场景
print('accoutConf---888', accoutConf['vipUser'])
# ppLoginRes = login.ppLogin(accoutConf['vipUser'], 1)
# #退到--首页
# quit(2, 0)
# if (ppLoginRes):
#     longVideo.videoRightShow('vipUserVideoRightBtnShow', 'vipTicket')
#     quit()

#     longVideo.videoRightShow('vipUserVideoRightBtnShow', 'vipPay')
#     quit()

#     longVideo.videoCenterShow('vipUserVideoCenterBtnShow', 'vipTicket')
#     quit()

#     longVideo.videoCenterShow('vipUserVideoCenterBtnShow', 'vipPay')
#     quit()
# else:
#     print('登录失败~~~~')
    



# 普通用户-开通会员（电视剧、电影）
# 普通用户-用券
# 普通用户-单片购买
# VIP用户-用券
# VIP用户-单片购买
    
#ppLoginRes = login.ppLogin(accoutConf['commonUser'], 1)
# quit(2, 0)
# longVideo.clickBtn()

# print('7--', poco(text = '有效天数：7天').exists())
# print('5--', poco(text = '购买价格：5.0').exists())
# print('确认--', poco(text = '确认').exists())
# print('商品名称--', poco(text = '商品名称').exists())
# print(' 尼斯大冒险 --', poco(text = '尼斯大冒险').exists())
# print('确认支付--', poco(text = '确认支付').exists())
# print('请输入支付密码--', poco(text = '请输入支付密码').exists())


aaa = longVideo.clickBtn('vipUserVideoCenterBtnShow', 'vipTicket')
print(aaa)


#longVideo.checkAfterShow('开通会员免费看', '僵尸夜魔')
#longVideo.checkAfterShow('开通会员用券看', '僵尸夜魔')
#longVideo.checkAfterShow('续费会员用券看', '僵尸夜魔')
#aa = longVideo.checkAfterShow('用券观看', '掠食城市')
#print('aa---', aa)


# poco.click([0.5,0.85])  
# sleep(5)
#poco.click([0.16,0.89])
# sleep(5)
# poco.click([0.83,0.90])
# sleep(5)
# poco.click([0.16,0.82])
# sleep(5)
# poco.click([0.5,0.9])
# sleep(5)
#poco.click([0.16,0.82])

#print('绝命航班', len(poco(text = "绝命航班")))

#键盘输入的位置  5（0.5，0.8） 4（0.2，0.8） 6（0.8，0.8） 1 （0.2，0.7） 5（0.5，0.8） 1（0.2，0.7） 
# poco.click([0.5,0.8])
# poco.click([0.2,0.8])
# poco.click([0.8,0.8])
# poco.click([0.2,0.75])
# poco.click([0.5,0.8])
# poco.click([0.2,0.75])
#poco.click([0.5,0.2])
# print('播放', len(poco(text = "播放")))
# print('暂停', len(poco(text = "暂停")))
# poco(text = "暂停").click()
# poco(text = "暂停").click()

#--5----540 , 1966----0.50,0.90  ; 4----173 1953----0.16,0.89  6----900.1961---0.83,0.90;  1-----181,1800--0.16,0.82; 5-----540 , 1966--0.50,0.90    zhengping 1080 , 2174
