# -*- encoding=utf8 -*-
__author__ = "lyh"
from airtest.core.api import *
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
import random
using("F:/aritest/ppWx/public")
from fun import SearchToLongvideo,quit,swipeStartIndex
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)
class LongVideo():
    
    #视频配置（VIP免费、用券、付费）
    def __init__(self, config = {}):
        ##安卓端
        #视频配置
        self.freeTv = ['球王', '雾非雾', '财神有道']
        self.freeMovie = ['千局百计', '好想吃拉面', '青春派', '最终玩家']
        self.vipFreeTv = ['从将军到士兵']
        self.vipFreeMovie =['寒战', '灭绝', '毒战']
        self.vipTicket = ['牡丹花下', '变形金刚', '万物理论']
        #self.vipTicket = ['速度与激情8（英文原版）']
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
        self.noLoginCenterBtnShow = [self.videoCenterBtns['login']['text']]
        
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