import os
import requests
import time

print('''
88""Yb 88  88     88   88 88""Yb 88         88 88b 88 888888  dP"Yb  
88__dP 88  88     88   88 88__dP 88         88 88Yb88 88__   dP   Yb 
88"Yb  888888     Y8   8P 88"Yb  88  .o     88 88 Y88 88""   Yb   dP 
88  Yb 88  88     `YbodP' 88  Yb 88ood8     88 88  Y8 88      YbodP  

A TOOL FOR GETTING INFO OF A LINK''')

url = str(input('Enter URL : '))
print('''
1. url status code
2. url headers
3. url html scraper (Not Displayed using bs4)
4. url encoding
5. all info''')
a = int(input('Enter the choices : '))


goturl = requests.get(url)

if(a == 1):
            print("Status code : ")
            print(goturl.status_code)
elif (a == 2):
            print("Headers : ")
            print(goturl.headers)
elif (a == 3):
            print("Scraped HTML : ")
            print(goturl.content)

elif (a == 4):
            print("URL ENCODE TYPE : ")
            print(goturl.apparent_encoding)

elif    (a == 5):
     print("Status code : ")
     print(goturl.status_code)
     print('----------------------------')
     print("Scraped HTML : ")
     print(goturl.content)
     print('----------------------------')
     print("Headers : ")
     print(goturl.headers)
     print('----------------------------')
     print("URL ENCODE TYPE : ")
     print(goturl.elapsed)
     print('----------------------------')
     print("URL : ")
     print(goturl.url)
     print('----------------------------')


else:
    print ('link is invalid try again')


exit = input('press enter to exit, have a nice day!' )


