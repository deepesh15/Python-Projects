import requests
import wget
for i in range(27,53):
    url = "https://goethemp4s.akamaized.net/resources/files/mp34/radiod_englisch_teil2_lektion{}1.mp3".format(i)
    reponse = requests.get(url)
    print("File :{},Status: ".format(i),reponse)
    wget.download(url,'D:/Deutsch/A2')






''''

<video class="jw-video jw-reset" x-webkit-airplay="allow" webkit-playsinline="" preload="none" jw-loaded="started" src="//goethemp4s.akamaized.net/resources/files/mp34/radiod_englisch_teil2_lektion271.mp3"></video>

import wget

for i in range(1,1000):
    print("\nStarting download: {}".format(i))
    url = "https://goethemp4s.akamaized.net/resources/files/mp34/radiod_englisch_teil1_lektion{}.mp3".format(i)
    wget.download(url,'D:/Deutsch/A2')
'''