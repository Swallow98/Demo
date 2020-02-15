#自定义过滤器
from django import template
#实例化对象
register = template.Library()
# 前端调用
# 编写过滤器方法
@register.filter()
def myadd(num):
    return num + num




