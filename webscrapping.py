import bs4 as bs
import sys
import urllib.request 
from PyQt5.QtWebEngineWidgets import QWebEnginePage
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QUrl
from pandas import DataFrame

class Page(QWebEnginePage):
    def __init__(self, url):
        self.app = QApplication(sys.argv)
        QWebEnginePage.__init__(self)
        self.html = ''
        self.loadFinished.connect(self._on_load_finished)
        self.load(QUrl(url))
        self.app.exec_()

    def _on_load_finished(self):
        self.html = self.toHtml(self.Callable)
        print('Load finished')

    def Callable(self, html_str):
        self.html = html_str
        self.app.quit()


def main():
    page = Page('http://qsstechnosoft.com/')
    soup = bs.BeautifulSoup(page.html, 'html.parser')
    print(soup.find_all('blockquote'))    
    #df = DataFrame({'Stimulus Time': soup.find('blockquote')})
    #aList = []
    #for link in soup.find_all('a'): aList.insert(len(aList),link.get('href'))
    #df = DataFrame({'Stimulus Time': aList})
    #df.to_excel('test.xlsx', sheet_name='sheet1', index=False)
    
if __name__ == '__main__': main()