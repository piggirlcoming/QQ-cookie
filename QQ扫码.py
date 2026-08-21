import requests, random, time

def ptqrlogin(qrsig, pt_login_sig):
    def hash33(s):
        h = 0
        for c in s:
            h += (h << 5) + ord(c)
            h &= 0x7fffffff
        return h

    ptqrtoken = hash33(qrsig)
    action = f"0-0-{int(time.time() * 1000)}"

    url = "https://xui.ptlogin2.qq.com/ssl/ptqrlogin?"
    param = f"u1=https://qun.qq.com/&ptqrtoken={ptqrtoken}&ptredirect=1&h=1&t=1&g=1&from_ui=1&ptlang=2052&action={action}&js_ver=26071711&js_type=1&login_sig={pt_login_sig}&pt_uistyle=40&aid=715030901&daid=73&has_onekey=1&&o1vId=7a8119f0a721c0bcec39385f586d6a4e&pt_js_version=c1987b96"

    headers = {
        'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/151.0.0.0 Safari/537.36 Edg/151.0.0.0",
    }

    return requests.get(url + param, headers=headers).text


session = requests.Session()
session.headers.update({'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/151.0.0.0 Safari/537.36 Edg/151.0.0.0"})

# 取回pt_login_sig(这个是新加的) 可以选择固定, 应该吧
session.get("https://xui.ptlogin2.qq.com/cgi-bin/xlogin?appid=715030901&target=self&style=40&s_url=https://qun.qq.com/")
pt_login_sig = session.cookies.get('pt_login_sig')

t = random.random()
url = "https://xui.ptlogin2.qq.com/ssl/ptqrshow?"
param = f"appid=715030901&e=2&l=M&s=3&d=72&v=4&t={t}&daid=73&pt_3rd_aid=0&u1=https://qun.qq.com/"
data = session.get(url + param)

qrsig = session.cookies.get('qrsig')

while True:
    print(ptqrlogin(session, qrsig, pt_login_sig))
    time.sleep(2)