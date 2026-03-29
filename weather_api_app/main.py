import sys
from PyQt5.QtWidgets import (QApplication, QWidget,
                             QLabel, QLineEdit, QVBoxLayout, QPushButton)
from PyQt5.QtCore import Qt
import requests


class weatherapp(QWidget):
    def __init__(self):
        super().__init__()
        self.city_label = QLabel("Enter the city name", self)
        self.city_input = QLineEdit(self)
        self.get_weather_button = QPushButton("Click weather here", self)
        self.temperature_label = QLabel(self)
        self.emoji_label = QLabel(self)
        self.description_label = QLabel(self)
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Weather app")

        vbox = QVBoxLayout()
        vbox.addWidget(self.city_label)
        vbox.addWidget(self.city_input)
        vbox.addWidget(self.get_weather_button)
        vbox.addWidget(self.temperature_label)
        vbox.addWidget(self.emoji_label)
        vbox.addWidget(self.description_label)
        self.setLayout(vbox)

        self.city_label.setAlignment(Qt.AlignCenter)
        self.city_input.setAlignment(Qt.AlignCenter)
        self.temperature_label.setAlignment(Qt.AlignCenter)
        self.emoji_label.setAlignment(Qt.AlignCenter)
        self.description_label.setAlignment(Qt.AlignCenter)

        self.city_label.setObjectName("city_label")
        self.city_input.setObjectName("city_input")
        self.get_weather_button.setObjectName("get_weather_button")
        self.temperature_label.setObjectName("temperature_label")
        self.emoji_label.setObjectName("emoji_label")
        self.description_label.setObjectName("description_label")

        self.setStyleSheet("""
                            QLabel, QPushButton{
                            font-family : calibri;
                           }     
                            QLabel#city_label{
                           font-size : 40px;
                           font-style : italic;
                           }
                           QLineEdit#city_input{
                           font-size : 40px;
                           }
                           QPushButton#get_weather_button{
                           font-size : 30px;
                           font-weight : bold;
                           }
                           QLabel#temperature_label{
                           font-size : 70px;
                           }
                           QLabel#emoji_label{
                           font-size : 100px;
                           font-family : Segoe UI emoji;
                           }
                           QLabel#description_label{
                           font-size : 50px;
                           }

                            """)
        self.get_weather_button.clicked.connect(self.get_weather)

    def get_weather(self):
        api_key = "621c8871e68b48387136be63c3b7549c"
        city = self.city_input.text()
        url = f"={city}&appid={api_key}"
        try:
            response = requests.get(url)
            data = response.json()
            response.raise_for_status()
            print(data)
            if data["cod"] == 200:
                self.display_weather(data)
        except requests.exceptions.HTTPError as http_error:
            match response.status_code:
                case 400:
                    self.display_error("Bad request\nPlease check your input")
                case 401:
                    self.display_error("Unauthorised\nInvalid api key")
                case 403:
                    self.display_error("Forbidden\nAccess denied")
                case 404:
                    self.display_error("Not found\nCity not found")
                case 500:
                    self.display_error(
                        "Internal server error\nPlease try again later")
                case 502:
                    self.display_error(
                        "Bad gateway\nInvalid response from the server")
                case 503:
                    self.display_error("Service unavailable\nServer is down")
                case 504:
                    self.display_error(
                        "Gateway timeout\nNo response from the server")
                case _:
                    self.display_error(f"HTTP error occured\n {http_error}")
        except requests.exceptions.ConnectionError:
            self.display_error(
                "Connection error\nCheck your internet connection")
        except requests.exceptions.Timeout:
            self.display_error("Timeout error/nThe request has timed out")
        except requests.exceptions.TooManyRedirects:
            self.display_error("Too many requests\nCheck the URL")
        except requests.exceptions.RequestException as req_error:
            self.display_error(f"Request error\n{req_error}")

    def display_error(self, message):
        self.temperature_label.setStyleSheet("font-size : 30px;")
        self.temperature_label.setText(message)
        self.emoji_label.clear()
        self.description_label.clear()

    def display_weather(self, data):
        self.temperature_label.setStyleSheet("font-size : 70px;")
        temperature_k = data["main"]["temp"]
        temperature_c = (temperature_k - 273.15)
        temperature_f = ((temperature_c * (9/5)) + 32)
        weather_id = data["weather"][0]["id"]
        print(weather_id)
        self.temperature_label.setText(f"{temperature_c:.2f}°C")
        weather_description = data["weather"][0]["description"]
        self.description_label.setText(weather_description)
        self.emoji_label.setText(self.display_emoji(weather_id))

    @staticmethod
    def display_emoji(weather_id):
        if 200 <= weather_id <= 230:
            return "⛈️"
        elif 300 <= weather_id <= 321:
            return "🌦️"
        elif 500 <= weather_id <= 531:
            return "🌧️"
        elif 600 <= weather_id <= 622:
            return "🌨️"
        elif 700 <= weather_id <= 741:
            return "🌫️"
        elif weather_id == 762:
            return "🌋"
        elif weather_id == 771:
            return "💨"
        elif weather_id == 781:
            return "🌪️"
        elif weather_id == 800:
            return "☀️"
        elif 801 <= weather_id <= 804:
            return "☁️"
        else:
            return ""


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = weatherapp()
    window.show()
    sys.exit(app.exec_())
