import time
import execjs
import requests

Config = {
    "ROUTER_IP": "http://192.168.0.1",  # 路由器地址
    "ROUTER_PWD": "123456",  # 路由器密码
    "JS_FILE_PATH": "tplink.js",  # 路由器加密文件
}


# 定义路由器操作类
class RouterController:
    def __init__(self):
        self.ip_flag = 0
        self.router_ip = Config['ROUTER_IP']
        self.password = Config['ROUTER_PWD']
        self.token = None
        self.get_token()

    # 返回登录后tptoken
    def get_token(self):
        headers = {
            'Accept': 'application/json, text/javascript, */*; q=0.01',
            'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
            'Connection': 'keep-alive',
            'Content-Type': 'application/json; charset=UTF-8',
            'Origin': self.router_ip,
            'Referer': self.router_ip,
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
            'X-Requested-With': 'XMLHttpRequest',
        }

        # 调用外部js 加密返回
        with open('tplink.js', 'r', encoding='utf8') as f:
            js_file = f.read()

        result = execjs.compile(js_file).call('orgAuthPwd', '123456')

        json_data = {
            'method': 'do',
            'login': {
                'password': result,
            },
        }

        response = requests.post('http://192.168.0.1/', headers=headers, json=json_data, verify=False).json()
        self.token = response['stok']
        print('token:', self.token)

    # 重新拨号, 更换外网IP地址
    def change_ip(self):
        if self.ip_flag == 0:  # 确保每次仅可调用一次
            self.ip_flag = 1
            print('ip:', self.get_public_ip())
            # 断开链接
            requests.post('http://192.168.0.1/stok=' + self.token,
                                data='{"network":{"change_wan_status":{"proto":"pppoe","operate":"disconnect"}},"method":"do"}')
            # 连接网络
            requests.post('http://192.168.0.1/stok=' + self.token,
                                data='{"network":{"change_wan_status":{"proto":"pppoe","operate":"connect"}},"method":"do"}')

            time.sleep(2)  # 休眠2秒

            print("切换路由器IP")
            print('ip:', self.get_public_ip())

            self.ip_flag = 0
        else:
            time.sleep(1)

    def get_public_ip(self):
        try:
            res = requests.get("https://httpbin.org/ip")
            return res.json()["origin"]
        except:
            print("无法获取外网IP")
            return None


if __name__ == '__main__':
    router = RouterController()
    router.change_ip()
