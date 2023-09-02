import sys
from typing import Optional
from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QApplication, QWidget, QLineEdit, 
    QVBoxLayout, QHBoxLayout, QTextEdit, 
    QPushButton
)


class RegistrationForm(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Registration Form")
        self.create_window_content()

    def create_window_content(self):
        # Create Vertical Box Layout and assigne a parent widget to it
        main_layout = QVBoxLayout(self)

        # create text inputs
        self.first_name_field = QLineEdit()
        self.last_name_field = QLineEdit()
        self.address_field = QLineEdit()
        self.phone_field = QLineEdit()
        self.email_field = QLineEdit()

        # create a multiline text input
        self.about_field = QTextEdit()

        self.save_button = QPushButton("Save Data")

        # add text inputs do main_layout
        main_layout.addWidget(self.first_name_field)
        main_layout.addWidget(self.last_name_field)
        main_layout.addWidget(self.address_field)
        main_layout.addWidget(self.phone_field)
        main_layout.addWidget(self.email_field)
        main_layout.addWidget(self.about_field)
        main_layout.addWidget(self.save_button)


if __name__ == "__main__":
    # create a new QApplication
    app = QApplication(sys.argv)

    # create an instance of our window
    win = RegistrationForm()
    win.show()

    # wait for window close
    sys.exit(app.exec())