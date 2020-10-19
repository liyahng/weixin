# -*- encoding=utf8 -*-
__author__ = "lyh"

from airtest.core.api import *
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
from poco.exceptions import PocoTargetTimeout
using("F:/aritest/ppWx/class")
from Member import Member

poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)

if(poco(text = "首页").exists() == False):
    poco(text = "微信").click()
    poco.swipe([0.5, 0.4], [0.5, 0.8], duration = 1)
    poco(text = "PP视频").click()

member = Member()
#首页广告展示统计
try:
    res = member.loginModule()
    print('--777-----', res)
    if (res == True):
        assert_equal(True, True, '登录模块存在')
    else:
        assert_equal(False, True, '登录模块存在')
except:
    print('登录模块存在--error')
    pass

#用VIP账号--广告不出现--提高成功率~~~~    
# member = Member()
# # res = member.moduleShow()
# # print(res)

# # res = member.carousel()
# # print(res)

# res = member.loginModule()
# print(res)



