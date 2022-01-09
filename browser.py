import sys
from pyqt5.qtcore import *
from pyqt5.qtcore import *
from pyqt5.qtwebenginewidgets import *

class MainWindow (QMainWindow):
    def__init__(self).__init__()
    self.browser = QWebEngineView()
    self.browser.seturl(QUrl('http://www.google.com'))
    self.setCentralWidget(self.browser)
    self.showMaximized()

    #navbar
    navbar = qtool()
    self.addToolBar(navbar)

    back_btn = qaction('Back', self)
    back_btn.triggered.connect(self.browser.back)
    navbar.addaction(back_btn)

    back_btn = qaction('Forward', self)
    back_btn.triggered.connect(self.browser.back)
    navbar.addaction(forward_btn)

    back_btn = qaction('Reload', self)
    back_btn.triggered.connect(self.browser.back)
    navbar.addaction(reload_btn)

    back_btn = qaction('Home', self)
    back_btn.triggered.connect(self.browser.back)
    navbar.addaction(home_btn)

    self.url_bar = qlinedit()
    self.url_bar.returnPressed.connect(self.navigate_to_url)
    navbar.addWidget(self.url_bar)

    self.browser.urlChanged.connect(self.update_url)

    def navigate_home(self):
        self.brower.seturl(qurl('http://programming-hero.com'))

    def navigate_to_url(self):
        url = self.url_bar.text()
        self.browser.setUrl(qurl(url))

    def update_url(self, q):
        self.url_bar.setText(q.toString())
    
    app = QApplication(sys.argv)
    qapplication.setapplicationname('My Cool Browser')
    window = MainWindow()
    app.exec_()
        












