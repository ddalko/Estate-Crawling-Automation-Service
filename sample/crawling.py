# --*-- coding: utf-8 --*--
import time
from selenium import webdriver
from bs4 import BeautifulSoup
from datetime import datetime, timedelta
from PyQt5.QtCore import QThread
from PyQt5.QtCore import pyqtSignal
import sys
import os

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)



class Crawler():
    def __init__(self):
        super().__init__()
        self.keyword = '맛집'
        self.driver = webdriver.Chrome(resource_path("../src/driver/chromedriver.exe"))

        self.run()

    def run(self):
        self.driver.get(
            'https://search.naver.com/search.naver?date_from=&date_option=0&date_to=&dup_remove=1&nso=&post_blogurl=&post_blogurl_without=&query=' + self.keyword.replace(
                " ", "+") + '&sm=tab_pge&srchby=all&st=sim&where=view&start=0')
        soup = BeautifulSoup(self.driver.page_source, 'html5lib')
        # my_titles = soup.select('#main_pack > div.blog.section._blogBase._prs_blg > ul > li.bx')
        # sp_blog_11
        my_titles = soup.select('ul.lst_total > li > div.total_wrap')
        print('==================================')
        print(
            my_titles
        )
        print('==================================')
        for title in my_titles:
            print(title.find('a', {"class": 'api_txt_lines total_tit'}).text)


cr = Crawler()