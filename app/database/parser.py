from datetime import datetime
from time import sleep
from fake_headers import Headers
from selenium import webdriver
from selenium.webdriver.common.by import By
from tqdm import tqdm

from config import path_logger


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

        __options = webdriver.ChromeOptions()
        __headers = Headers(os="win", headers=True).generate()
        __options.add_argument(f'user-agent={__headers}')
        # Отключение режима драйвера.
        __options.add_argument('--disable-blink-features=AutomationControlled')
        # Работа в фоновом режиме.
        __options.add_argument('headless')
        self.content = dict()

        # Инициализация драйвера Chrome.
        self.__driver = webdriver.Chrome(options=__options)
        self.__driver.set_window_size(1920, 1080)

    def load_content(self):
        """ Загружает контент с сайта. """
        try:
            for title, url in tqdm(self.__urls.items()):
                list_content = []
                self.__driver.get(url=url)
                sleep(3)
                block = self.__driver.find_element(By.XPATH,
                                                   '//div[contains(@class,"page")]')
                res = block.find_elements(By.TAG_NAME, 'p')
                for el in res[3:]:
                    if el.text == '*****' or el.text == '':
                        continue
                    list_content.append(el.text)
                self.content[title] = [list_content][0]

            print('БД загружена!')

        except Exception as e:
            with open(path_logger, 'a', encoding='utf-8') as file_log:
                file_log.write(f'{datetime.now()}\nError: {e}')
            print(e)
        finally:
            self.__driver.close()
            self.__driver.quit()

    def get_content(self) -> dict:
        """ Возвращает загруженный контент. """
        return self.content
