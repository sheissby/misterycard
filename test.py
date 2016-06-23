import requests
from bs4 import BeautifulSoup

r = requests.get('http://www.wise.xmu.edu.cn/people/faculty')
html = r.content
soup = BeautifulSoup(html,'html.parser')
div_people_list = soup.find('div', attrs={'class': 'people_list'})
a_s = div_people_list.find_all('a', attrs={'target': '_blank'})
for a in a_s:
    url = a['href']
    name = a.get_text()
    # print name
    parent = a.parent.find_next_sibling()
    job = parent.get_text()
    # print  job
    email= parent.find_next_sibling().get_text()
    # print email
    data = {"name":name,"job":job,"email":email}
    print data