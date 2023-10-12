# # import urllib.request
# #
# # url = 'https://www.daelim.ac.kr/type/KOR_A/img/intro/logo.png'
# # urllib.request.urlretrieve(url,'daelim.png')  # 웹에서 가져온 이미지를 보조기억장치에 저장
# # print('저장완료')
#
# import urllib.request
#
# url = 'https://www.daelim.ac.kr/type/KOR_A/img/intro/logo.png'
# logo = urllib.request.urlopen(url).read()  # 이미지를 다운받아서 메모리에 저장
#
# with open('daelim.png', 'wb') as file:  # 원본 이미지가 png 포맷이므로 쓰기모드를 텍스트가 아닌 바이너리 형식으로 설정
#     file.write(logo)  # 실제 보조기억장치에 쓰기
#     print('저장 완료')


import urllib.request
import urllib.parse

api = 'https://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp'

station_id = input('지역코드 : ')  # 전국 108, 수도권 109, 강원 105, 제주 184 .....
values = {'stnId': station_id}
parameters = urllib.parse.urlencode(values)
url = api + "?" + parameters  # api string + ? + stnId=station_id
print(url)

urls = urllib.request.urlopen(url).read()
texts = urls.decode('utf-8')
print(texts)
