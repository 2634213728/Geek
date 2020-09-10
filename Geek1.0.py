#使用了有道的翻译API，现在已经暂停注册

# from CMD_color import *

from urllib.parse import urlparse, quote, urlencode, unquote
import requests
import time
from playsound import playsound
from aip import AipSpeech

#使用百度语音
def baidu_voice(string):

    """ 你的 APPID AK SK """
    APP_ID = '18599467'
    API_KEY = 'Ug8MKhK4158Ic4H3V0hp0RfC'
    SECRET_KEY = 'VGa1caOxygbW9CshwEiA2nLrMx9cRgG9'

    client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)
    # result = client.synthesis(text = '我是哈哈哈天才', options={'vol':5})
    result = client.synthesis(string, 'zh', 5, {
        'vol': 4, 'per': 3,
    })
    if not isinstance(result, dict):
        with open('audio.mp3', 'wb') as f:
            f.write(result)
            f.close()
    # else:
        # print(result)
    # time.sleep(3)
    playsound('audio.mp3')
    #解除占用方式
    #https://blog.csdn.net/li
    # ang4000/article/details/96766845?depth_1-utm_source=distribute.pc_relevant.none-task&utm_source=distribute.pc_relevant.none-task

def fetch(query_str=''):
    query_str = query_str.strip("'").strip('"').strip()
    if not query_str:
        query_str = '你是憨憨吗？'
    query = {
        'q': query_str
    }
    url = 'http://fanyi.youdao.com/openapi.do?keyfrom=11pegasus11&key=273646050&type=data&doctype=json&version=1.1&' + urlencode(query)
    s = requests.get(url)
    s.encoding = 'utf-8'
    html=s.json()
    # print(html)
    return html

def parse(d):
    # d = json.loads(html)
    try:
        if d.get('errorCode') == 0:
            explains = d.get('basic').get('explains')
            phonetic =d.get('basic').get('phonetic')
            if phonetic!=None:
                print('读音/音标>',end='')
                print(phonetic)
            if explains !=None:
                print(' 释  义 >',end='')
                for i in explains:
                    print(i,end=';  ')
                print('')
        else:
            print('无法翻译')
    except:
        print('模糊翻译：',end='')
        explains = d.get('translation')
        print(explains)
def main():
    while 1:
        try:
            print()
            print('Time : %s' % time.ctime())
            # CMD_color.printBlue(u'printBlue:蓝色文字\n')
            s=input('input:')
            if s.endswith(" v"):
                s = s.strip(" v")
                baidu_voice(s)
        except IndexError:
            s = '？'
        parse(fetch(s))

if __name__ == '__main__':
    main()