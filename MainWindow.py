from PyQt5.QtWidgets import *
from PyQt5.QtCore import QDate

class MainWindow(QWidget):
    def __init__(self, task):
        super().__init__()
        self.task = task
        self.flag = 0
        self.buildComponents()
        

    def buildComponents(self):
        vbox = QVBoxLayout()
        vbox.addWidget(self.chapter1())
        vbox.addWidget(self.chapter2())
        vbox.addWidget(self.chapter3())
        vbox.addWidget(self.chapter4())
        self.setLayout(vbox)
        #vbox.addLayout(self.chapter3())
        # vbox.addLayout(self.chapter4())
      

    def openFileDialog(self):
        path = QFileDialog.getOpenFileName(self, 'Открыть файл...')[0]
        if(self.task.setMainFile(path) == 0):
            self.flag = 0
            self.filePathLabel.setText('Некорректный файл или путь!')
        else:
            self.flag = 1
            self.filePathLabel.setText(path)
            

    def formBid(self):
        if(self.flag == 0):
            self.filePathLabel.setText('Не выбран файл или выбран некорректный файл')
        else:
            curDate = self.calendar.selectedDate().getDate()
            self.calendarLabel.setText(str(curDate))
            self.task.formBid(curDate)
            self.notifyLbl.setText('Готово!')
            self.flag = 2

    def openDir(self):
        if self.flag != 2:
            self.notifyLbl.setText('Файлы еще не сформированы')
            return
        self.task.openDir()
        
    def chapter1(self):
        vbox = QVBoxLayout()
        
        vbox.addWidget(QLabel('Открыть файл'))
        
        hbox = QHBoxLayout()
        btn = QPushButton('Открыть...') 
        btn.clicked.connect(self.openFileDialog)
        hbox.addWidget(btn)
        self.filePathLabel = QLabel()
        hbox.addWidget(self.filePathLabel)
        # 2 row
        vbox.addLayout(hbox)
        qw = QWidget()
        qw.setLayout(vbox)
        return qw

    def chapter2(self):
        vbox = QVBoxLayout()
        vbox.addWidget(QLabel('Задайте дату забора заказа'))
        self.calendar = QCalendarWidget()
        # self.calendar.setMaximumWidth(150)
        vbox.addWidget(self.calendar)
        vbox.addWidget(QLabel('Если выставлен выходной день, дата переносится на ближайщий рабочий день следующей недели'))
        self.calendarLabel = QLabel('')
        vbox.addWidget(self.calendarLabel)
        y, m, d = self.task.getOptimalDate()
        self.calendar.setSelectedDate(QDate(y, m, d))
        vbox.addStretch(1)
        qw = QWidget()
        qw.setLayout(vbox)
        qw.resize(150, 150)
        return qw

    def chapter3(self):
        vbox = QVBoxLayout()
        vbox.addWidget(QLabel('Сгенерировать заявки из шаблонов'))
        btn = QPushButton('Старт')
        btn.clicked.connect(self.formBid)
        vbox.addWidget(btn)
        self.notifyLbl = QLabel()
        vbox.addWidget(self.notifyLbl)
        qw = QWidget()
        qw.setLayout(vbox)
        return qw

    def chapter4(self):
        hbox = QHBoxLayout()
        self.labelDone = QLabel()
        hbox.addWidget(self.labelDone)
        btn = QPushButton('Открыть папку с бланками')
        btn.clicked.connect(self.openDir)
        hbox.addWidget(btn)
        qw = QWidget()
        qw.setLayout(hbox)
        return qw

        