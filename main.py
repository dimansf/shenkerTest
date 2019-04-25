import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QFileDialog)
import MainWindow
import Task


if __name__ == '__main__':

    app = QApplication(sys.argv)
    if '-d' in sys.argv:
        import config
        task = Task.Task(config.config)
    else:
        task = Task.Task(None)
    w = MainWindow.MainWindow(task)
    w.resize(400, 300)
    w.setWindowTitle('Шенкер by dimansf')
    w.show()
    
    sys.exit(app.exec_())
     