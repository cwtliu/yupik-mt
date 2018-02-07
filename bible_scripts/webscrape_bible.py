#Author: cwtliu
#Used to webscrape the Yup'ik Bible
import urllib2, sys
import re
from bs4 import BeautifulSoup
current_book = 'GEN'
counter = 1
with open('listofwebsiteURLs.txt','r') as fdata:
    for line in fdata:
        quote_page = line.strip()
        print(quote_page)
        book = re.search(r'/1390/(.*?)\.[0-9]',quote_page).group(1)
        if book != current_book:
            counter += 1
            current_book = book
        name = str(counter)+'_'+str(book)+'.txt'
        with open(name,'a') as fout:
            hdr = {'User-Agent': 'Mozilla/5.0'}
            req = urllib2.Request(quote_page,headers=hdr)
            page = urllib2.urlopen(req)
            soup = BeautifulSoup(page, 'html.parser')
            name_box = soup.find_all('div', {'class': ['q1','q2','m','p','nb','li','pi','s3']})
            for i in name_box:
                name = i.text.strip()
                #print(name)
                fout.write(name.encode('utf-8'))
                fout.write(' ')
