#  正则 ：是一种字符串的处理方式，用于字符串匹配的
# 字符串的匹配分为两种：
#   内容匹配：
#         python 中的re模块，js中的匹配
#         通过要匹配的内容的类型，长度进行匹配的

#   结构匹配：
#       xpath  获取到内容的某个标签进行匹配
    # #       通过获取内容在这个文档中的结构，进行匹配
#   内容匹配的类型：
#      类型匹配：
#         原样匹配 .  \d  \D  \w  \W   []  |  ()
    #     长度匹配
    #         *  +  ?  {}
    #     特殊匹配
    #         ^  $

import re
# re.findall()  以列表的形式，尽可能返回匹配到的结果
str = 'hello world 123'
'''
原样匹配
    . :匹配除了\n的所有内容
res = re.findall('.',str)
print(res)

     \d :匹配数字的
res = re.findall('\d',str)
print(res)

    \D  :匹配的是除了数字以外的
res = re.findall('\D',str)
print(res)

    \w  :匹配数字字母下划线的
res = re.findall('\w',str)
print(res)

    \W   ：匹配非数字字母下划线的
res = re.findall('\W',str)
print(res)

    []  ：匹配符合括号中的内容
res = re.findall('[1-9]',str)
print(res)

    |  :匹配'|'任意一边的内容
res = re.findall(''hello|world'',str)
print(res)

    () :组 ，组匹配 将括号外面的内容，当作条件进行匹配
res = re.findall('\w l',str)
print(res)
'''
# res = re.findall('hello',str)
# print(res)
lst = '123 444 554'


#长度匹配
#   *
# res = re.findall('\d*',str)
# print(res)

#   +
# res = re.findall('\d+',str)
# print(res)

#   ?
# res = re.findall('\d?',str)
# print(res)

#   {}
# res = re.findall('\d{2}',str)
# print(res)

#     特殊匹配
#         ^:匹配以什么开头
# res = re.findall('^hello',str)
# print(res)
#         $ ：匹配以什么结束
# res = re.findall('3$',str)
# print(res)



