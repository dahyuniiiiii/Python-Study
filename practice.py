import urllib.request
a = urllib.request.urlopen('https://www.naver.com')
print(a.status)