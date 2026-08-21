import requests
import re
import time
from urllib.parse import quote
import json
def SunnyNetCreateRequest1():
    """ 
    [ /cgi-bin/qun_mgr/set_group_card ]
    本函数由SunnyNet网络中间件生成   
    """
    url = "https://qun.qq.com/cgi-bin/qun_mgr/set_group_card?bkn=778368430&ts=1752848535303"
    payload = "gc=651541849&u=468668346&name=o&bkn=778368430"
    headers = {
        'Content-Type': "application/x-www-form-urlencoded",
        'Cookie': "uin=o3596407014; skey=@uoebILbRU; p_uin=o3596407014; p_skey=PcIg11oZlOvMTo9cEhWhybx9gpMY*waLVrBEm3vlaDw_;",
    }
    response = requests.request("POST", url, data=payload, headers=headers)

    print(response.text)

# SunnyNetCreateRequest1()

def SunnyNetCreateRequest2():
    """ 
    [ /cgi-bin/qun_mgr/delete_group_member ]
    本函数由SunnyNet网络中间件生成   
    """
    url = "https://qun.qq.com/cgi-bin/qun_mgr/delete_group_member?bkn=1015492084&ts=1754400853000"
    payload = "gc=917892661&ul=2649172213&flag=0&bkn=1015492084"
    headers = {
        'Accept': "application/json, text/plain, */*",
        'Cookie': "uin=o3596407014; skey=@7iabb9H3V; p_uin=o3596407014; p_skey=yGuTXjk3-hBBGRvvf-NWfEf6C3qOPtzHYgIyBxXqNZw_;",

    }
    response = requests.request("POST", url, data=payload, headers=headers)

    print(response.text)

SunnyNetCreateRequest2()

def SunnyNetCreateRequest3():
    """ 
    [ /cgi-bin/qun_mgr/set_group_admin ]
    本函数由SunnyNet网络中间件生成   
    """
    url = "https://qun.qq.com/cgi-bin/qun_mgr/set_group_admin?bkn=1598622672&ts=1754385891012"
    payload = "gc=651541849&ul=468668346&op=0&bkn=1598622672"
    headers = {
        'Accept': "application/json, text/plain, */*",
        'Cookie': "uin=o3596407014; skey=@Z5KO70DJm; p_uin=o3596407014; p_skey=b29PyE1WK0zz1hV3yxk8oj7b87jDz9N0d*VhXJTxyyU_;",

    }
    response = requests.request("POST", url, data=payload, headers=headers)

    print(response.text)

#SunnyNetCreateRequest3()

def skey_to_bkn(skey: str) -> str:
    base = 5381
    count = 0
    length = len(skey)
    while count < length:
        base += (base << 5) + ord(skey[count])
        count += 1
    result = base & 2147483647
    return str(result)

#print(skey_to_bkn("@7iabb9H3V"))
def SunnyNetCreateRequest4():
    """ 
    [ /note/7360323126909095219 ]
    本函数由SunnyNet网络中间件生成   
    """
    url = "https://www.douyin.com/note/7360323126909095219"
    payload = ""
    headers = {
        'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36 Edg/138.0.0.0",
        'Cookie': "n_mh=Jwkk2k_pB7o9GglfgboeGMNnyekRAeWbIMJVBLEmdpU; uid_tt=df6f9157b29027089e5b613f2e1f8186; uid_tt_ss=df6f9157b29027089e5b613f2e1f8186; sid_tt=218dc7a44d93b913607eae1fca381cb5; sessionid=218dc7a44d93b913607eae1fca381cb5; sessionid_ss=218dc7a44d93b913607eae1fca381cb5; session_tlb_tag=sttt%7C20%7CIY3HpE2TuRNgfq4fyjgctf________-4iAsNl5iJjnP_vhJxbPyoJZ_XWpoxf6f1bJ2VTl04XdQ%3D; is_staff_user=false; login_time=1750556546490; UIFID=8f584679f13361d7674396b25a46f1c75dd7736730eef2bca7f1b3cfea8b216dc639644da9b4f74d37caa9e376774c9da962f36a63b76918141f56b05f862340cd2a71095cc055833c66d14adb7835ec524ea43d9d6df5d53593c137cf3d5c173f281c31a3e4fdfd4dc51f49e9a81479a2a094d345fad86b3c328484931c2a6558cf086f519d9a4898072162753bf0e9dee94041fc1b57eeaf78fd938fb48105; SelfTabRedDotControl=%5B%5D; _bd_ticket_crypt_cookie=90fbc171891013427fcc3d005384ac47; __security_mc_1_s_sdk_sign_data_key_web_protect=d15da0ac-4b37-99cb; __security_mc_1_s_sdk_cert_key=878fda64-4465-8bb6; __security_server_data_status=1; douyin.com; device_web_cpu_core=4; device_web_memory_size=4; architecture=amd64; dy_swidth=1920; dy_sheight=1080; strategyABtestKey=%221752850117.686%22; is_dash_user=1; xg_device_score=6.905294117647059; volume_info=%7B%22volume%22%3A0.822%2C%22isMute%22%3Atrue%2C%22isUserMute%22%3Atrue%7D; sid_guard=218dc7a44d93b913607eae1fca381cb5%7C1752850154%7C5184000%7CTue%2C+16-Sep-2025+14%3A49%3A14+GMT; sid_ucp_v1=1.0.0-KGE5NTY2YmNkMjc4ZjcyMjY3MzM4NmNkMDc1MjIyYzdjNDQ1YTIzODEKHwj42OHP6AIQ6r3pwwYY7zEgDDD3uazWBTgHQPQHSAQaAmhsIiAyMThkYzdhNDRkOTNiOTEzNjA3ZWFlMWZjYTM4MWNiNQ; ssid_ucp_v1=1.0.0-KGE5NTY2YmNkMjc4ZjcyMjY3MzM4NmNkMDc1MjIyYzdjNDQ1YTIzODEKHwj42OHP6AIQ6r3pwwYY7zEgDDD3uazWBTgHQPQHSAQaAmhsIiAyMThkYzdhNDRkOTNiOTEzNjA3ZWFlMWZjYTM4MWNiNQ; WallpaperGuide=%7B%22showTime%22%3A1752850240858%2C%22closeTime%22%3A0%2C%22showCount%22%3A1%2C%22cursor1%22%3A10%2C%22cursor2%22%3A2%7D; download_guide=%223%2F20250718%2F0%22; stream_recommend_feed_params=%22%7B%5C%22cookie_enabled%5C%22%3Atrue%2C%5C%22screen_width%5C%22%3A1920%2C%5C%22screen_height%5C%22%3A1080%2C%5C%22browser_online%5C%22%3Atrue%2C%5C%22cpu_core_num%5C%22%3A4%2C%5C%22device_memory%5C%22%3A4%2C%5C%22downlink%5C%22%3A10%2C%5C%22effective_type%5C%22%3A%5C%224g%5C%22%2C%5C%22round_trip_time%5C%22%3A50%7D%22; __ac_nonce=0687a660800964552ef24; __ac_signature=_02B4Z6wo00f01TvLYNAAAIDAiQb7mcVtKaE762RAACaL55; stream_player_status_params=%22%7B%5C%22is_auto_play%5C%22%3A0%2C%5C%22is_full_screen%5C%22%3A0%2C%5C%22is_full_webscreen%5C%22%3A0%2C%5C%22is_mute%5C%22%3A1%2C%5C%22is_speed%5C%22%3A1%2C%5C%22is_visible%5C%22%3A0%7D%22; FOLLOW_LIVE_POINT_INFO=%22MS4wLjABAAAAaP7QwyVgCW0dz5VEDyzyselSoOdiVXWHEVLnP1vnExU%2F1752854400000%2F0%2F0%2F1752852617035%22; FOLLOW_NUMBER_YELLOW_POINT_INFO=%22MS4wLjABAAAAaP7QwyVgCW0dz5VEDyzyselSoOdiVXWHEVLnP1vnExU%2F1752854400000%2F0%2F0%2F1752853217037%22; bd_ticket_guard_client_data=eyJiZC10aWNrZXQtZ3VhcmQtdmVyc2lvbiI6MiwiYmQtdGlja2V0LWd1YXJkLWl0ZXJhdGlvbi12ZXJzaW9uIjoxLCJiZC10aWNrZXQtZ3VhcmQtcmVlLXB1YmxpYy1rZXkiOiJCRHJQdjlCNlVrWUxrbDlKZjZvcVZVMG5reW5XNnRFd1JtLzJOaXo4dzEzL2RON3RETkJ4UU5kVjFNRUtxM0RIbWZ4UzYvWG1ORHdsR1BqdzM0L0ZrTVE9IiwiYmQtdGlja2V0LWd1YXJkLXdlYi12ZXJzaW9uIjoyfQ%3D%3D; home_can_add_dy_2_desktop=%221%22; publish_badge_show_info=%220%2C0%2C0%2C1752852020982%22; ttwid=1%7Cx448bZitSqfujdaTwgo3nhyXjRVHU80Hsgi31s17NmQ%7C1752852048%7C0762f35db13cae54b08552cf746048fc5ceda16ccecb9565a116fd68ad788704; biz_trace_id=b8a9445f; sdk_source_info=7e276470716a68645a606960273f276364697660272927676c715a6d6069756077273f276364697660272927666d776a68605a607d71606b766c6a6b5a7666776c7571273f275e58272927666a6b766a69605a696c6061273f27636469766027292762696a6764695a7364776c6467696076273f275e582729277672715a646971273f2763646976602729277f6b5a666475273f2763646976602729276d6a6e5a6b6a716c273f2763646976602729276c6b6f5a7f6367273f27636469766027292771273f2733363431373537303d37303234272927676c715a75776a716a666a69273f2763646976602778; bit_env=84X-fuIuj8C6oy_Q5c_aTRj8GcFbE6O1QZ30zh6rHXjUYvbdCiMQPsQhv-U8iLagKrDg3QyY4i_x2yQj5G0NgpVj0D5Ecs_9F_l42EUyUK1MBZurKORFJoNqhZHNE--fTSEjd4KYPKJU-hHNDmQis3N0_3i7bWr5Ss23dPpndS4yE98fhPjVE8Ga6e73m9UCcZ9HQlh9ptDFxFnzlxUNRy_JxlI5mRe4ZmYmfiDw4KTo2kiuFEj-e-uZEgQZD0H2SIR-GJ3ee082J-CEHV9Z7jyqU3LImSdhOeqmwsJhcA8DdBA1V84DEEbp5YWr-u3jtJOUPuAddntBlpr-HLDnRTbFD9W61yJTD--ST-AdxutqmGgBLOMMFfx3oXY2k-OuGWrhIM3CqGr2oAm42fj39kda6LRbm-L7yTN9FsM3E7PUH3m-Y5bbNyj2p644ttdZi0UWMnykHtVQ3L-tsH03mvJ7qNzV_cqEOYYCNN6QI61M-1AZYic4o5tgp1DSKvI-2GYOzCS_Pq0sWUIe2mktr6uz0GEamYaoymcieBAh_fo%3D; gulu_source_res=eyJwX2luIjoiNzU0M2ZjOGQ1M2I0ODllM2QzNDA1NDBmYmViY2VhOTQ5YjdkNmE0NmQyY2RiODQzN2RiNDY4OTdiNDkzN2RlZiJ9; passport_auth_mix_state=hur2k8alw8cu0e85f674enisx8483o2a2l853p0tb2oxfyx6; odin_tt=2f50e93dc99cbac9935096e4b99261bf2c37789ace90f8f5d3050fd4f996841c3790e718fc0ed8bae2ec531af4498160; IsDouyinActive=false; passport_fe_beating_status=false",

    }
    response = requests.request("GET", url, data=payload, headers=headers).text
    file_path = "D:/phpstudy_pro/WWW/mangyu.aaa/python-bot/output.txt"
    with open(file_path, "w", encoding="utf-8") as file:
        file.write(response)
    pattern = r'https?://p3-pc-sign\.douyinpic\.com/tos-cn-i-0813/[^\s"\']+'
    matches = re.findall(pattern, response)

    if matches:
        print("找到匹配的 URL:")
        for url in matches:
            print(url)
    else:
        print("未找到匹配的 URL")


# SunnyNetCreateRequest4()


def SunnyNetCreateRequest5():
    url = "https://v.douyin.com/97jNQ-B7EDM/"
    session = requests.Session()
    response = session.get(url, allow_redirects=False, verify=False)

    # 2. 检查是否返回 302 并提取 Location
    if response.status_code == 302 and 'Location' in response.headers:
        final_url = response.headers['Location']
        print(re.search(r"/video/(\d+)", final_url).group(1))
    else:
        print("未找到跳转 URL，直接输出:", response.text)

# SunnyNetCreateRequest5()

import requests

url = "https://web.qun.qq.com/qunrobot/proxy/domain/qun.qq.com/cgi-bin/qunrobots/remind_set?bkn=108751813"
time1 = int(time.time()) + 100
config = quote(json.dumps({"loop_type":0,"ts":time1,"week_day":[],"remind_before":15,"date":"2025/07/20"}))
payload = f"bkn=108751813&gc=651541849&remind_msg=1&pic_id=&pic_url=&slot=0&remind_setting={config}&remind_type=0"
headers = {
    'Content-Type': "application/x-www-form-urlencoded",
    'qname-service': "1434753:65536",
    'qname-space': "Production",
    'sec-ch-ua-platform': "\"Android\"",
    'Cookie': "uin=o3596407014; skey=mf34hpyROT; traceid=299dfa2c73; p_uin=o3596407014; p_uid=u_t9bwuDRsKvgpb6K9oRwTaQ; p_skey=EGC*5UEUxOFcnCML-bpccZEmgRIw9BuNvf2IRzOH7xY_; tgw_l7_route=7b3b0139c88b9b33a4b3a6dba986b779"
}

response = requests.post(url, data=payload, headers=headers)
# print(response.text)


