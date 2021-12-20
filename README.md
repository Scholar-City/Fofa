# Fofa批量URL

Fofa_Query.py

使用环境：python3
Fofa高级会员 获取10000 条 把 size设置成1w即可，默认100条



配置文件 config.ini

[fofa_config]

email = 20200606@163.com

api = da123dwcdaeb96c922c9da539fb93597

keyword = aG9zdD0nYmFpZHUuY29tJw==

page = 2

size = 10000




把关键字用base64编码后，再放上去。这里这样做是为了防止中文编码的时候出错。
例如 百度，直接把百度base64编码即可 55m+5bqm
生成出来的文件名是当前时间戳



