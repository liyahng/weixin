# -*- encoding=utf8 -*-
__author__ = "lyh"

from airtest.core.api import *
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
from poco.exceptions import PocoTargetTimeout
using("F:/aritest/ppWx/class")
from Ad import Ad

poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)

if(poco(text = "首页").exists() == False):
    poco(text = "微信").click()
    poco.swipe([0.5, 0.4], [0.5, 0.8], duration = 1)
    poco(text = "PP视频").click()

ad = Ad()
#首页广告展示统计
try:
    res = ad.IndexFeedAd(5)
    print('--777-----', res)
    if (res > 0):
        assert_equal(True, True, '首页feed广告展示统计次数' + '--【' + res + '】')
    else:
        assert_equal(False, True, '首页feed广告展示统计次数' + '--【' + res + '】')
    print('广告展示统计次数', res)
except:
    print('首页广告展示统计--error')
    pass


#频道页广告
try:
    pindaoList = ad.ChannelAd()
    print('频道结果--', pindaoList)
    for index in pindaoList:
        print(pindaoList[index], '---index')
        if (pindaoList[index] > 0):
            assert_equal(True, True, '频道页广告存在'+index)
        else:
            assert_equal(False, True, '频道页广告不存在'+index)
    print('广告展示统计次数', pindaoList)
except:
    print('频道页广告--error')
    pass

#短视频详情页--五插1
try:
    res = ad.ShortAd(5)
    print('次数：', res)
    if (res > 0):
        assert_equal(True, True, '短视频详情页-广告次数')
    else:
        assert_equal(False, True, '短视频详情页广告不存在')
    print('短视频详情页广告展示统计次数', res)
except:
    print('短视频详情页--error')
    pass



# #搜索页、搜索结果页
try:
    sres = ad.SearchAd()
    print('广告展示统计次数', sres)
    for index in sres:
        if (sres[index] > 0):
            assert_equal(True, True, '搜索--存在' + index)
        else:
            assert_equal(False, True, '搜索--不存在' + index)
except:
    print('搜索页、搜索结果页--error')
    pass



#长视频页--视频下方广告
try:
    res = ad.LongVideoLowAd()
    if (res > 0):
        assert_equal(True, True, '长视频页--视频下方广告')
    else:
        assert_equal(False, True, '长视频页--视频下方广告')
    print('广告展示统计次数', res)
except:
    print('长视频页--视频下方广告--error')
    pass

# #视频前贴广告（非会员）
try:
    res = ad.LongVideoFrontAd()
    print('广告展示统计次数', res)
    if (res > 0):
        assert_equal(True, True, '长视频页--视频前贴广告--')
    else:
        assert_equal(False, True, '长视频页--视频前贴广告--失败频率较高')
except:
    print('视频前贴广告（非会员）--error')
    pass





