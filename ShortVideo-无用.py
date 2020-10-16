# -*- encoding=utf8 -*-
__author__ = "lyh"
from airtest.core.api import *
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
import random
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)

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

#滑动回到页面初始位置
def swipeStartIndex(num = 1):
    for index in range(num):
        print('index-', index)
        poco.swipe([0.5, 0.2], [0.5, 0.9])    

#1、首页-feed--播放、分享、跳转、滑动
#2、体育tab--播放、分享、跳转、滑动
#3、短视频详情--播放、分享、跳转、滑动
class ShortVideo():
    #视频播放正确
    def play(self, type = 1):
        self.joinShortVideo(type)
        for index in range(10):
            print('out-', index)
            poco.swipe([0.5, 0.8], [0.5, 0.3])
            if exists(Template(r"tpl1596440995706.png", threshold=0.4, record_pos=(0.003, 0.409), resolution=(1080, 2340))):
                print('in--', index)
                touch(Template(r"tpl1596440995706.png", threshold=0.4, record_pos=(0.003, 0.409), resolution=(1080, 2340)))
                sleep(2)
                if (poco(text = "暂停").exists() and poco(text = "全屏").exists()):
                    print('播放成功')
                    return True
        return False
    
    #微信分享
    def wxPlay(self, type = 1):
        #self.joinShortVideo(type)
        for index in range(10):
            print('out-', index)
            poco.swipe([0.5, 0.8], [0.5, 0.3])
            if exists(Template(r"tpl1596440728879.png", record_pos=(0.391, -0.03), resolution=(1080, 2340))):
                print('in--', index)
                touch(Template(r"tpl1596440728879.png", record_pos=(0.391, -0.03), resolution=(1080, 2340)))
                sleep(2)
                if (poco(text = "选择").exists()):
                    print('分享--弹框展示')
                    poco(desc = "返回").click()
                    return True
        return False
                              
    #type:1、进入短视频详情页 || 2、进入到首页feed位置 || 3、进入到体育feed
    def joinShortVideo(self, type = 1):
        if (type == 1):
            poco(text = '体育').click()
            touch(Template(r"tpl1596444154700.png", threshold=0.5, record_pos=(0.273, 0.246), resolution=(1080, 2340)))
            sleep(3)
            if (poco(text = "相关推荐").exists()):
                return True
        elif (type == 2):
            #滑动至首页猜你喜欢位置--大概
            for index in range(4):
                poco.swipe([0.5, 0.7], [0.5, 0.4], duration = 1)
        elif (type == 3):
            if (poco(text = "体育").exists()):
                poco(text = "体育").click()
            else:
                print('体育--tab--不存在')
                return False
        else:
            print('type参数不存在')
            return False   
        
    
#首页播放
shortVideo = ShortVideo()
playRes = shortVideo.play(3)
wxRes = shortVideo.wxPlay(3)
quit()
print('视频播放结果-详情--', playRes)
print('微信分享弹框--详情-', playRes)


shortVideo = ShortVideo()
playRes = shortVideo.play(2)
wxRes = shortVideo.wxPlay(2)
swipeStartIndex(4)
print('视频播放结果-首页--', playRes)
print('微信分享弹框--首页-', playRes)

playRes = shortVideo.play(1)
wxRes = shortVideo.wxPlay(1)
print('视频播放结果--体育tab-', playRes)
print('微信分享弹框--体育tab-', playRes)
quit(2, 0)