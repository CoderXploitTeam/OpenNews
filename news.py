import os
import time
import requests
import json
link='https://opennewsapi.herokuapp.com/api/news/'
os.system('clear')
print('''
┏━━━┓        ┏━┓ ┏┓
┃┏━┓┃        ┃┃┗┓┃┃
┃┃ ┃┣━━┳━━┳━┓┃┏┓┗┛┣━━┳┓┏┓┏┳━━┓
┃┃ ┃┃┏┓┃┃━┫┏┓┫┃┗┓┃┃┃━┫┗┛┗┛┃━━┫
┃┗━┛┃┗┛┃┃━┫┃┃┃┃ ┃┃┃┃━╋┓┏┓┏╋━━┃
┗━━━┫┏━┻━━┻┛┗┻┛ ┗━┻━━┛┗┛┗┛┗━━┛
    ┃┃
    ┗┛
''')
try:
    req=requests.get(link)
    jeson=json.loads(req.text)
except requests.ConnectionError:
    print('koneksi tidak ada')
for data in jeson['results']:
    print(60*'=')
    print('sumber  :', data['source'])
    print('tag     :', data['tag'])
    print('tanggal :', data['created_at'])
    print('judul   :', data['title'])
    print('link    :', data['link'])
    print('gambar  :', data['image'])
    time.sleep(0.09)