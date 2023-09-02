import sys
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QWidget


class RegistrationForm(QWidget):
    pass


if __name__ == "__main__":
    # create a new QApplication
    app = QApplication(sys.argv)

    # create an instance of our window
    win = RegistrationForm()
    win.show()

    # wait for window close
    sys.exit(app.exec())