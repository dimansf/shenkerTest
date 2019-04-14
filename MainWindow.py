from PyQt5.QtWidgets import *

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.btn = None
        # self.handle = handler
        self.vbox = QVBoxLayout()
        self.setLayout(self.vbox)
        self.buildComponents()
        

    def buildComponents(self):
        
        self.vbox.addWidget(self.chapter1())
        self.vbox.addWidget(self.chapter2())
        self.vbox.addWidget(self.chapter3())
        self.vbox.addWidget(self.chapter4())
        #vbox.addLayout(self.chapter3())
        # vbox.addLayout(self.chapter4())
      

    def openFileDialog(self):
        self.path = QFileDialog.getOpenFileName(self, 'Open file')[0]

    def chapter1(self):
        vbox = QVBoxLayout()
        # 1 row
        vbox.addWidget(QLabel('Выберите файл', self))
        
        hbox = QHBoxLayout()
        btn = QPushButton('Выбрать...', self) 
        btn.clicked.connect(self.openFileDialog)
        hbox.addWidget(btn)
        self.lbl = QLabel()
        hbox.addWidget(self.lbl)
        # 2 row
        vbox.addLayout(hbox)
        qw = QWidget()
        qw.setLayout(vbox)
        return qw

    def chapter2(self):
        vbox = QVBoxLayout()
        vbox.addWidget(QLabel('Дата подачи'))
        self.calendar = QCalendarWidget()
        # self.calendar.setMaximumWidth(150)
        vbox.addWidget(self.calendar)
        vbox.addWidget(QLabel('Если выбраны выходные дни, дата автоматически переносится на ближайший рабочий день'))
        vbox.addStretch(1)
        qw = QWidget()
        qw.setLayout(vbox)
        qw.resize(150, 150)
        return qw

    def chapter3(self):
        vbox = QVBoxLayout()
        vbox.addWidget(QLabel('Сгенерировать файлы по бланкам'))
        btn = QPushButton('Сгенерировать')
        btn.clicked.connect(self.formBid)
        vbox.addWidget(btn)
        qw = QWidget()
        qw.setLayout(vbox)
        return qw

    def chapter4(self):
        hbox = QHBoxLayout()
        self.labelDone = QLabel()
        hbox.addWidget(self.labelDone)
        btn = QPushButton('Открыть папку')
        btn.clicked.connect(self.openDir)
        hbox.addWidget(btn)
        qw = QWidget()
        qw.setLayout(hbox)
        return qw

    def formBid(self):
        self.handle(self.path)

    def openDir(self):
        pass

        