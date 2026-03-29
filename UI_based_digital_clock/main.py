import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
from PyQt5.QtCore import QTimer, QTime, Qt
from PyQt5.QtGui import QFont, QFontDatabase
import os


class digitalclock(QWidget):
    def __init__(self):
        super().__init__()
        self.timer_label = QLabel(self)
        self.timer = QTimer(self)
        self.base_dir = os.path.dirname(os.path.abspath(__file__))
        self.font_path = os.path.join(self.base_dir, "DS-DIGIT.TTF")

        self.initUI()

    def initUI(self):
        self.setWindowTitle("Digital clock")
        self.setGeometry(700, 300, 500, 200)

        vbox = QVBoxLayout()
        vbox.addWidget(self.timer_label)
        self.setLayout(vbox)
        self.timer_label.setAlignment(Qt.AlignCenter)
        self.timer_label.setStyleSheet("font-size : 150px;"
                                       "color : hsl(128, 44%, 60%);")
        self.setStyleSheet("background-color : black;")
        self.font_id = QFontDatabase.addApplicationFont(self.font_path)
        font_family = QFontDatabase.applicationFontFamilies(self.font_id)[0]
        my_font = QFont(font_family, 150)
        self.timer_label.setFont(my_font)
        self.timer.timeout.connect(self.update_time)
        self.timer.start(1000)
        self.update_time()

    def update_time(self):
        current_time = QTime.currentTime().toString("hh:mm:ss AP")
        self.timer_label.setText(current_time)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    clock = digitalclock()
    clock.show()
    sys.exit(app.exec_())
