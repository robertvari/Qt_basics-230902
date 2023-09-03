from PySide6.QtQml import QQmlApplicationEngine
from PySide6.QtGui import QGuiApplication
from PySide6.QtCore import QObject, Slot
import json

import sys, os

APP_ROOT = os.path.dirname(__file__)
MAIN_QML = os.path.join(APP_ROOT, "main.qml")


class UserDataSaver(QObject):
    @Slot(str, str, str, str, str)
    def save_data(self, name, email, phone, address, about):
        user_data = {
            "name": name, 
            "email": email, 
            "phone": phone, 
            "address": address, 
            "about": about
        }

        with open("user_data.json", "w") as f:
            json.dump(user_data, f)

        print("Data saved!")


class RegistrationForm:
    def __init__(self) -> None:
        self.app = QGuiApplication(sys.argv)
        self.engine = QQmlApplicationEngine()
        self.root_context = self.engine.rootContext()

        self.user_data_save = UserDataSaver()
        self.root_context.setContextProperty("UserDataSaver", self.user_data_save)

        self.engine.load(MAIN_QML)

        if not self.engine.rootObjects():
            sys.exit(-1)

        sys.exit(self.app.exec())


if __name__ == "__main__":
    RegistrationForm()