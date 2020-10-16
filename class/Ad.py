# -*- encoding=utf8 -*-
__author__ = "lyh"

from airtest.core.api import *
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
from poco.exceptions import PocoTargetTimeout
import sys

poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)

#--todo--广告跳转--
#auto_setup(__file__)
class Ad():
    #1--首页广告展示统计  screenNum滑动的屏幕个数
    def IndexFeedAd(self, screenNum):
        #初始化首页位置||滑动N屏
        adDisplayTimes = 0 #广告出现次数--大于实际出现次数
        #poco.swipe([0.5, 0.3], [0.5, 0.5], duration = 1)
        for index in range(screenNum * 2):
            print(index)
            poco.swipe([0.5, 0.8], [0.5, 0.4], duration = 1)
            sleep(1)
            indexAdTipExists = poco(text = "广告").exists()
            print(indexAdTipExists)
            if(indexAdTipExists):
                adDisplayTimes = adDisplayTimes + 1
        #还原位置
        for index in range(screenNum * 2):
            poco.swipe([0.5, 0.4], [0.5, 0.8], duration = 1)
        # if (adDisplayTimes == 0):
        #     return 0
        return adDisplayTimes
    #2--频道页广告
    def ChannelAd(self):    
        pindaoTab = poco(text = "频道")
        if(pindaoTab.exists()):
            pindaoTab.click()
        else:
            print('频道页tab未找到')
        sleep(3)

        pindaoList  = {'电视剧' : 0, '电影' : 0, '动漫' : 0, '少儿' : 0}
        for index in pindaoList:
            print(index)
            sleep(3)
            if (poco(text = index).exists()):
                poco(text = index).click()
                sleep(2)
                if (poco(text = "广告").exists()):
                    pindaoList[index] = 1
            else:
                print(index,'tab不存在')
        poco(text = "首页").click()
        return pindaoList
    
    def SearchToLongvideo(self, name):
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
    
    #3--长视频页--视频下方广告
    def LongVideoLowAd(self, name = ''):
        self.SearchToLongvideo(name)
        sleep(5)
        
        result =  1 if (poco(text = "广告").wait(2).exists()) else 0
        self.quit()
        return result
    
    #4--视频前贴广告（非会员）--todo
    def LongVideoFrontAd(self,  name = ''):
        self.SearchToLongvideo(name)
        sleep(8)
        
        result =  1 if (poco(text = "关闭").wait(2).exists()) else 0
        self.quit()
        return result
    #5--搜索页、搜索结果页
    def SearchAd(self):
        searchAdres = {"searchpro" : False, "searchres" : False}
        #获取搜索点击元素
        searchButton = poco("android.widget.FrameLayout").offspring("android.webkit.WebView").offspring("android.widget.Image")
        searchButton.click()
        
        #搜索过程页面广告展示
        searchAdres['searchpro'] =  1 if (poco(text = "广告").wait(2).exists()) else 0
        poco(text="搜索").wait_for_appearance()
        poco(text="搜索").click()
        
        #搜索结果页面广告展示
        searchAdres['searchres'] =  1 if (poco(text = "广告").wait(2).exists()) else 0
        
        self.quit()
        return searchAdres
    
    #6--短视频详情页--五插一----下载||查看||进入||立即玩||去逛逛||立即领取|| 去快手||查看详情||下载应用
    def ShortAd(self, screenNum):
        self.joinShortVideo()
        adDisplayTimes = 0 #每次滑动半屏尺寸--停顿--检测广告出现次数--大于实际出现次数
        for index in range(screenNum * 2):
            print(index)
            #indexAdTipExists = poco("视频播放器",type = "android.widget.RelativeLayout").wait(2).exists() #默认第一屏会展示广告
            indexAdTipExists = poco(text = "广告").wait(2).exists() #默认第一屏会展示广告
            print(indexAdTipExists)
            if(indexAdTipExists):
                adDisplayTimes = adDisplayTimes + 1
            poco.swipe([0.5, 0.8], [0.5, 0.3], duration = 1)


        #还原位置
        for index in range(screenNum * 2):
            poco.swipe([0.5, 0.3], [0.5, 0.8], duration = 1)

        #返回首页
        self.quit()
        poco(text = "首页").click()

        #广告次数
        return adDisplayTimes
    #进入短视频详情页--todo
    def joinShortVideo(self):
        poco(text = "体育").click()
        #poco("android.webkit.WebView")[0].child("android.view.View").child("android.view.View")[0].click([0.9, 0.5])
        poco(text = "PP视频").click([0.5,2.5])
        
    #点击返回按钮--退回到首页
    def quit(self):
        while (poco("com.tencent.mm:id/dc").exists()):
            poco("com.tencent.mm:id/dc").click()
    
    def __del__(self):
        class_name = self.__class__.__name__
        print (class_name, "销毁")