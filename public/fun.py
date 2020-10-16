# -*- encoding=utf8 -*-
__author__ = "lyh"

from airtest.core.api import *
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
from poco.exceptions import PocoTargetTimeout
import sys

poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)

def SearchToLongvideo(name):
    poco(text = "首页").click()
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

#滑动回到页面初始位置
def swipeStartIndex(num = 1, type = 'up'):
    for index in range(num):
        print('index-', index)
        if (type == 'down'):
            poco.swipe([0.5, 0.2], [0.5, 0.9])
        else:
            poco.swipe([0.5, 0.9], [0.5, 0.2]) 
