from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import sys

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setUI()


    def setUI(self):
        #background color
        self.setAutoFillBackground(True)
        self.p = self.palette()
        self.p.setColor(self.backgroundRole(), Qt.gray)
        self.setPalette(self.p)

        #objects
        bosLabel=QLabel()
        logo=QLabel()
        author=QLabel("author: Cem Akdemir | Deu YBS 2019")
        header= QLabel("<font color= 'Green'><h1>Vergi Hesaplayıcı \t     </h1></font>")
        priceLabel=QLabel("Fiyat TL :")
        self.fiyatEntry=QLineEdit()
        taxLabel=QLabel("Vergi Oranı % :")
        self.tax=QSpinBox()
        self.button=QPushButton("Hesapla")
        self.sonuc=QLineEdit()


        #Widgets

        grid=QGridLayout()
        grid.addWidget(header,0,0)
        grid.addWidget(logo,0,1)
        #grid.addWidget(bosLabel,1,0)
        grid.addWidget(author,5,1)
        grid.addWidget(priceLabel,2,0)
        grid.addWidget(self.fiyatEntry,2,1)
        grid.addWidget(taxLabel,3,0)
        grid.addWidget(self.tax,3,1)
        grid.addWidget(self.button,4,0)
        grid.addWidget(self.sonuc,4,1)

        #logo
        logo.setPixmap(QPixmap("logom1.png"))
        #signal
        self.button.clicked.connect(self.taxCalculate)


        self.resize(150,150)
        self.show()
        self.setLayout(grid)
        self.setWindowTitle("Vergi Hesaplayıcı v.1")

    def taxCalculate(self):
        fiyat=float(self.fiyatEntry.text())
        vergi=float(self.tax.text())
        hesap= (fiyat*(vergi/100))+fiyat
        self.sonuc.setText(str(hesap))


if __name__=='__main__':
    app=QApplication([])
    pencere=MyWindow()
    pencere.show()
    sys.exit(app.exec())