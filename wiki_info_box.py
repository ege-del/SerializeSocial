# TODO
# list tag to array
# \n to array
# clean text encoding

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
    
def collect(url):
    header_buffer = {}
    data = []
    collect_header = False

    rows = get_table_rows(url)

    for row in rows:
        # toggle header collection
        header = row.find('th', attrs={'class':'infobox-header'})
        if header:
            collect_header = True

            header_buffer = {}
            header_buffer['header_value'] = header.text.strip()
            print('Collecting Header '+header_buffer['header_value'])
            if header.find('a'):
                header_buffer['header_link'] = header.find('a')['href']
            header_buffer['data'] = []

        # if this row is a header and we were already collecting header data
        # append this current header data and create a new header to append to
        # or
        # we were collecting headers and this is the last row in the loop
        # also append this header
        if header and collect_header or collect_header and row == rows[-1]:
            collect_header = False
            print('appending header buffer')
            data.append(header_buffer)

        
        
        label = row.find(attrs={'class':'infobox-label'})

        buf = {
            'label':'null',
            'value':'null',
            'link':'null',
        }
        if label: 
            buf['label'] = ' '.join([r.text.strip() for r in label])

        data_element = row.find(attrs={'class':'infobox-data'})
        
        if data_element:
            buf['value'] = ' '.join([r.text.strip() for r in data_element])
            if data_element.find('a'):
                buf['link'] = urljoin(url,data_element.find('a')['href'])

        if buf['label'] == buf['value'] == buf['link'] == 'null':
            print('all null skipping')
            continue

        if collect_header:
            print('appendign header')
            header_buffer['data'].append(buf)
        else:
            print('direct append')
            data.append(buf)

    return data

if __name__ == "__main__":
    print(sys.argv)
    res = collect(sys.argv[1])
    print(res)