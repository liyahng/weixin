# -*- encoding=utf8 -*-
__author__ = "lyh"

from airtest.core.api import *
#from airtest.cli.parser import cli_setup
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)

accoutConf = {'commonUser':{'account':'19011111122', 'pwd':'pptv123456'}, 'vipUser':{'account':'19011111167', 'pwd':'pptv123456'}}