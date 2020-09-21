import requests
from bs4 import BeautifulSoup

scholar = 'https://scholar.google.co.kr/'
search_scholar = 'https://scholar.google.co.kr/scholar?start='
prefix = '&q='
search_word = 'system+of+systems'
postfix = '&hl=ko&as_sdt=0,5'

for i in range(10):
    req = requests.get(search_scholar + str(i * 10) + prefix + search_word + postfix)
    html = req.text
    soup = BeautifulSoup(html, 'html.parser')
    # papers = soup.select('#gs_res_ccl_mid > div:nth-child(1) > div.gs_ri > h3')
    papers = soup.select('#gs_res_ccl_mid > * > div.gs_ri > h3 > a')

    for paper in papers:
        print(paper.text)
        