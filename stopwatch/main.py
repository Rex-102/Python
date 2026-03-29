import sys
from PyQt5.QtWidgets import QApplication, QLabel, QHBoxLayout, QVBoxLayout, QPushButton, QWidget
from PyQt5.QtCore import QTimer, QTime, Qt


class stopwatch(QWidget):
    def __init__(self):
        super().__init__()
        self.time = QTime(0, 0, 0, 0)
        self.time_label = QLabel("00:00:00.00", self)
        self.start_button = QPushButton("Start", self)
        self.stop_button = QPushButton("Stop", self)
        self.reset_button = QPushButton("Reset", self)
        self.timer = QTimer(self)

        self.initUI()

    def initUI(self):
        self.setWindowTitle("Stopwatch")
        self.setGeometry(700, 300, 500, 200)

        vbox = QVBoxLayout()
        vbox.addWidget(self.time_label)

        self.setLayout(vbox)

        hbox = QHBoxLayout()
        hbox.addWidget(self.start_button)
        hbox.addWidget(self.stop_button)
        hbox.addWidget(self.reset_button)

        vbox.addLayout(hbox)

        self.time_label.setAlignment(Qt.AlignCenter)
        self.setStyleSheet("""
                           QPushButton, QLabel{
                           padding : 20 px;
                           font-weight : bold;
                           font-family : calibri;
                           }
                            QPushButton{
                           font-size : 40px;
                           }  
                           QLabel{
                           font-size : 120px;
                           background-color : Green;
                           border-radius : 20px;
                           
                           }  
                            """)
        self.start_button.clicked.connect(self.start)
        self.stop_button.clicked.connect(self.stop)
        self.reset_button.clicked.connect(self.reset)
        self.timer.timeout.connect(self.update_display)

    def start(self):
        self.timer.start(10)

    def stop(self):
        self.timer.stop()

    def reset(self):
        self.timer.stop()
        self.time = QTime(0, 0, 0, 0)
        self.time_label.setText(self.format(self.time))

    def format(self, time):
        hours = time.hour()
        minutes = time.minute()
        seconds = time.second()
        miliseconds = time.msec() // 10
        return f"{hours:02}:{minutes:02}:{seconds:02}.{miliseconds:02}"

    def update_display(self):
        self.time = self.time.addMSecs(10)
        self.time_label.setText(self.format(self.time))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    watch = stopwatch()
    watch.show()
    sys.exit(app.exec_())
