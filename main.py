import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QFileDialog)
import MainWindow


if __name__ == '__main__':

    app = QApplication(sys.argv)
   
    w = MainWindow.MainWindow()
    w.resize(400, 300)
    # w.move(300, 300)
    w.setWindowTitle('Шенкер by dimansf')
    w.show()
    
    sys.exit(app.exec_())
     