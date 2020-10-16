__author__ = "lyh"
from airtest.core.api import *
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
from poco.exceptions import PocoTargetTimeout
from poco.exceptions import PocoNoSuchNodeException

poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)


#搜索
class Search():
    #搜索
    def __init__(self, config = {}):
        self.moduleConf = []

    #搜索功能
    def moduleShow(self):
        #等待首页加载完毕
        zbys = poco(text="重磅影视")
        zzk = poco(text="正在看")
        try:
            poco.wait_for_any([zbys, zzk],4)
        except PocoTargetTimeout:
            print('等待超时')
            pass

        #获取搜索点击元素
        searchButton = poco("android.widget.FrameLayout").offspring("android.webkit.WebView").offspring("android.widget.Image")

        try:
            searchButton.wait_for_appearance()
        except PocoNoSuchNodeException:
            print('终止')
            log('搜索框未找到--终止操作')
            raise
        assert_equal(searchButton.exists(), True, "首页搜索框存在")

        #点击搜索框进入搜索页面
        searchButton.click()

        #搜索页面广告检测
        sleep(3)
        adExists = poco(text="广告").exists()
        if adExists:
            assert_equal(adExists, True, "搜索页面广告存在")
        else:
            log('搜索页面广告未展示')
            assert_equal(adExists, False, "搜索页面广告不存在")
        #输入【许嵩】点击搜索按钮
        text("许嵩")
        poco(text="搜索").wait_for_appearance()
        poco(text="搜索").click()


        #搜索结果页面展示【立即播放按钮】
        poco(text="立即播放").wait_for_appearance()
        nowPlayButtonExists = poco(text="立即播放").exists()
        assert_equal(nowPlayButtonExists, True, "搜索结果页面展示ok--立即播放按钮存在")


        #搜索结果页面展示【广告】
        adExists2 = poco(text="广告").exists()
        if adExists2:
            assert_equal(adExists2, True, "搜索结果页面广告2存在")
        else:
            assert_equal(adExists2, False, "搜索结果页面广告2不存在")
        return res













