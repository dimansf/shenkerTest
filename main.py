import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QFileDialog)
import MainWindow
import Task


if __name__ == '__main__':

    app = QApplication(sys.argv)
    config = {
        'regions': r"C:\Users\dimansf\Documents\projects\python\dbshenker\files\Regions.xls",
        'bi_base': r"C:\Users\dimansf\Documents\projects\python\dbshenker\files\BI_Base.xls",
        'graph': r"C:\Users\dimansf\Documents\projects\python\dbshenker\files\Graph.xls",
        'cities': r"C:\Users\dimansf\Documents\projects\python\dbshenker\files\Cities.xls",
        'template': r"C:\Users\dimansf\Documents\projects\python\dbshenker\files\Blank.xlt",
        'xmls': r"C:\Users\dimansf\Documents\projects\python\dbshenker\xmls"
    }
    task = Task.Task(config)
    w = MainWindow.MainWindow(task)
    w.resize(400, 300)
    w.setWindowTitle('Шенкер by dimansf')
    w.show()
    
    sys.exit(app.exec_())
     