import requests
from bs4 import BeautifulSoup

# scholar = 'https://scholar.google.co.kr/'
search_scholar = 'https://scholar.google.co.kr/scholar?start='
prefix = '&q='
postfix = '&hl=ko&as_sdt=0,5'
sos_paper_list = []
failure_paper_list = []

for i in range(10):
    search_word = 'failure+scenarios'
    req = requests.get(search_scholar + str(i * 10) + prefix + search_word + postfix)
    print(search_scholar + str(i * 10) + prefix + search_word + postfix)
    html = req.text
    # print(html)
    soup = BeautifulSoup(html, 'html.parser')
    # papers = soup.select('#gs_res_ccl_mid > div:nth-child(1) > div.gs_ri > h3')
    # papers = soup.select('#gs_res_ccl_mid > * > div.gs_ri > h3 > a')
    papers = soup.select('#gs_res_ccl_mid > * > div.gs_ri > h3')
    print('1')
    print(papers)
    for paper in papers:
        print('2')
        print(paper.text)
        failure_paper_list.append(paper.text)
        
for i in range(10):
    search_word = 'system+of+systems'
    req = requests.get(search_scholar + str(i * 10) + prefix + search_word + postfix)
    html = req.text
    soup = BeautifulSoup(html, 'html.parser')
    # papers = soup.select('#gs_res_ccl_mid > div:nth-child(1) > div.gs_ri > h3')
    papers = soup.select('#gs_res_ccl_mid > * > div.gs_ri > h3 > a')

    for paper in papers:
        print(paper.text)
        sos_paper_list.append(paper.text)
        
print(failure_paper_list)
print(sos_paper_list)