from time import sleep

import requests
from fake_headers import Headers
from bs4 import BeautifulSoup


class Parser:
    """ Парсит тосты с сайта https://alcofan.com/ """

    def __init__(self):
        self.__urls = {
            'short': 'https://alcofan.com/luchshie-korotkie-tosty.html',
            'humor': 'https://alcofan.com/sbornik-smeshnyx-i-veselyx-tostov.html',
            'birthday': 'https://alcofan.com/tosty-pozdravleniya-na-den-rozhdeniya.html',
            'anniversary': 'https://alcofan.com/sbornik-yubilejnyx-tostov.html',
            'wedding': 'https://alcofan.com/luchshie-svadebnye-tosty.html',
            'parents': 'https://alcofan.com/sbornik-tostov-dlya-roditelej.html',
            'woman': 'https://alcofan.com/tosty-vypit-za-zhenshhin.html',
            'love': 'https://alcofan.com/sbornik-tostov-za-lyubov.html',
            'caucasus': 'https://alcofan.com/sbornik-gruzinskix-i-kavkazskix-tostov.html',
            'parable': 'https://alcofan.com/sbornik-tostov-pritchami.html'}

    def __attempt_get(self):
        """ Пытается получить контент с сайта. """
        for title, url_ in self.__urls.items():
            url = self.__urls['wedding']
            __headers = Headers(os="win", headers=True).generate()
            response = requests.get(url, headers=__headers)
            sleep(1)
            if response.status_code == 200:
                response.encoding = 'utf-8'
                soup = BeautifulSoup(response.text, 'lxml')
                block = soup.find('div', attrs={'class': 'page'})
                res = block.find_all('p')[3:]
                for el in res:
                    if el.text == '*****':
                        continue
                    print(el.text + '\n')
            print(title + '\n')

    def load_content(self):
        """ Загружает контент с сайта. """
        try:
            self.__attempt_get()
        except AttributeError:
            self.__attempt_get()


parser = Parser()
parser.load_content()
