# TODO
# list tag to array
# \n to array

from lxml import html
import sys
import requests
import json
from bs4 import BeautifulSoup
from urllib.parse import urljoin


def get_table_rows(url):
    res = requests.get(url)

    st = BeautifulSoup(res.content.decode('utf-8','ignore'),features='lxml')

    for target in st.find_all(["script","style"]):
        target.decompose()

    table = st.find('table', attrs={'class':['infobox','vcard']})

    table_body = table.find('tbody')

    rows = table_body.find_all('tr')

    return rows

def format_header(data):
    header_buffer = {}
    header_buffer['header_value'] = data.text.strip()
    if data.find('a'):
        header_buffer['header_link'] = data.find('a')['href']
    header_buffer['data'] = []

    return header_buffer


def format_normal(data,url):
    label = data.find(attrs={'class':'infobox-label'})
    if label is None:
        label = data.find(attrs={'class':'infobox-above'})
    if label is None:
        label = data.find(attrs={'class':'infobox-image'})

    buf = {}
    if label: 
        buf['label'] = ' '.join([r.text.strip() for r in label])

    data_element = data.find(attrs={'class':'infobox-data'})

    if data_element:
        buf['value'] = ' '.join([r.text.strip() for r in data_element])

        if data_element.find('a'):
            buf['link'] = urljoin(url,data_element.find('a')['href'])
    
    if data.find('img'):
        buf['link'] = urljoin(url,data.find('img')['src'])

    return buf

def collect(url):
    rows = get_table_rows(url)
    data = []
    buf = {}
    collect = False

    for row in rows:
        header = row.find('th', attrs={'class':'infobox-header'})
        if header:
            if len(buf) > 0:
                data.append(buf)
            collect = True
            buf = format_header(header)

        res = format_normal(row,url)
        if res:
            if collect:
                buf['data'].append(res)
            else:
                data.append(res)
    data.append(buf) 
    return data

if __name__ == "__main__":
    res = collect(sys.argv[1])
    out = json.dumps(res,indent=4,ensure_ascii=False)
    print(out)