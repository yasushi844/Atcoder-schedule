import requests
from bs4 import BeautifulSoup

url = "https://atcoder.jp/home"
link = "https://atcoder.jp"
select_tag = "#contest-table-upcoming a"

target = '"'
start_index = 0
end_index = 0

contest_set = []
contests = []


#データの取り出し
res = requests.get(url)
soup = BeautifulSoup(res.content,"html.parser")
elems = soup.select(select_tag)
for index, element in enumerate(elems):
    element_text = str(element.getText())
    contest_set.append(element_text)

    if index % 2 == 1:
        element_link = str(element)
        start_index = element_link.find(target) + 1
        end_index = element_link[start_index:].find(target) + start_index
        contest_set.append(link + element_link[start_index : end_index])

        contests.append(contest_set)
        contest_set = []

#出力
for contest in contests:
    print(*contest)