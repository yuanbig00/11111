#coding:utf8
from django.apps import AppConfig
import os#新增。修改app名为中文

default_app_config='front.FrontConfig'
def get_current_app_name(_file):
    return os.path.split(os.path.dirname(_file))[-1]

class FrontConfig(AppConfig):
    name=get_current_app_name(__file__)
    verbose_name="事件管理和用户管理"