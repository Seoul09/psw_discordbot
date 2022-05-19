import requests # 파이썬으로 HTTP 통신이 필요한 프로그램을 작성할때 쓰는 라이브러리
from bs4 import BeautifulSoup # HTML 문서을 탐색해서 원하는 부분만 쉽게 뽑아낼 수 있는 파이썬 라이브러리
from datetime import datetime


# 추출할 사이트 주소
url = 'http://gnubs-h.gne.go.kr/gnubs-h/na/ntt/selectNttList.do?mi=529980&bbsId=5038685'

# URL에서 HTML을 추출한다.
response = requests.get(url)

if response.status_code == 200:
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
    title = soup.select_one('#subContent > div > div:nth-child(7) > div.board-text > table > tbody > tr:nth-child(1)')
    title = title.get_text()
    title = title.split()
    print(title)
else :
    print(response.status_code)