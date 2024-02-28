# Router_Pppoe
tplink路由器, pppoe, ADSL重新拨号换IP

#### 适用路由器
```
tplink 最新版本
...
欢迎提交其他路由器版本
```

#### 如何运行
 - python 安装 ExecJS库
 - `pip install PyExecJS2`
 - 运行
 - `python ip_tplink_adsl.py`

#### 原理
 - 抓取路由器登录页面密码加密代码
 - 调用外部js, 加密密码, 利用加密串登录路由器
 - 调用拨号断开, 连接达到重新拨号效果

#### 运行结果
```
token: cD%3EVxiuV0zx%2C%28%7EsUKz%3C%2AL%29%3E%2B7qV%5Dq%7Ehn
ip: 223.150.28.217
切换路由器IP
ip: 223.150.31.86
```
