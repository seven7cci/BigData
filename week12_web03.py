from bs4 import BeautifulSoup

html = """
<html>
<head>
<title>스크레이핑 실습</title>
</head>
<body>
<a href="http://www.daelim.ac.kr">대림대학교</a><br>
<a href="http://www.harvard.edu">하버드대학교</a><br>
</body>
</html>
"""
soup = BeautifulSoup(html, 'html.parser')
urls = soup.find_all("a")  # return list
print(urls)
# 하버드대학교의 url주소는 http://www.harvard.edu입니다.
for url in urls:
    print("{0}의 주소는 {1}입니다.".format(url.string, url.attrs['href']))