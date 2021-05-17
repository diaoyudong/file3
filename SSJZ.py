import re
import json
import requests
import os
'''
基金代码、名称、简拼进行基金搜索

search = '博时黄金'
url = 'http://fundsuggest.eastmoney.com/FundSearch/api/FundSearchAPI.ashx?m=1&key=' + search  #

result = requests.post(url)  # 发送请求
print('##############查询结果##############')
print(result.text)  # 返回数据
'''
'''
通过基金编码获取估值
'''

code = ['000727','160222','001632','660012','000711','001371']
for f_code in code:

    url = 'http://fundgz.1234567.com.cn/js/%s.js' % f_code
    result = requests.get(url)  # 发送请求
    data = json.loads(re.match(".*?({.*}).*", result.text, re.S).group(1))
    print('##############基金详情##############')
    print('基金编码：%s' % data['fundcode'])
    print('基金名称：%s' % data['name'])
    print('单位净值：%s' % data['dwjz'])
    print('净值日期：%s' % data['jzrq'])
    print('净值估算：%s' % data['gsz'])
    print('估算涨幅：%s%%' % data['gszzl'])
    print('估值时间：%s' % data['gztime'])
# 输入任意键退出
os.system('pause')
