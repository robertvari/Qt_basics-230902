from PySide6.QtQml import QQmlApplicationEngine
from PySide6.QtGui import QGuiApplication
import sys, os

APP_ROOT = os.path.dirname(__file__)
MAIN_QML = os.path.join(APP_ROOT, "main.qml")

class RegistrationForm:
    def __init__(self) -> None:
        self.app = QGuiApplication(sys.argv)
        self.engine = QQmlApplicationEngine()

        self.engine.load(MAIN_QML)

        if not self.engine.rootObjects():
            sys.exit(-1)

        sys.exit(self.app.exec())


if __name__ == "__main__":
    RegistrationForm()