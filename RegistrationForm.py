import sys, json
from typing import Optional
from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QApplication, QWidget, QLineEdit, 
    QVBoxLayout, QHBoxLayout, QTextEdit, 
    QPushButton, QLabel, QMessageBox
)


class RegistrationForm(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Registration Form")
        self.create_window_content()
        self.message = QMessageBox()
        self.message.setWindowTitle("Info")

    def create_window_content(self):
        # Create Vertical Box Layout and assigne a parent widget to it
        main_layout = QVBoxLayout(self)

        # first name layout
        first_name_container = QHBoxLayout()
        main_layout.addLayout(first_name_container)
        first_name_label = QLabel("* First Name:")
        self.first_name_field = QLineEdit()
        first_name_container.addWidget(first_name_label)
        first_name_container.addWidget(self.first_name_field)

        # last name layout
        last_name_container = QHBoxLayout()
        main_layout.addLayout(last_name_container)
        last_name_label = QLabel("* Last Name:")
        self.last_name_field = QLineEdit()
        last_name_container.addWidget(last_name_label)
        last_name_container.addWidget(self.last_name_field)


        self.address_field = QLineEdit()
        self.address_field.setPlaceholderText("* Address")

        self.phone_field = QLineEdit()
        self.phone_field.setPlaceholderText("* Phone")

        self.email_field = QLineEdit()
        self.email_field.setPlaceholderText("* Email")

        # create a multiline text input
        self.about_field = QTextEdit()
        self.about_field.setPlaceholderText("About")

        self.save_button = QPushButton("Save Data")

        # add text inputs do main_layout
        main_layout.addWidget(self.address_field)
        main_layout.addWidget(self.phone_field)
        main_layout.addWidget(self.email_field)
        main_layout.addWidget(self.about_field)
        main_layout.addWidget(self.save_button)

        # connect signals
        self.save_button.clicked.connect(self.save_user_data)

    def save_user_data(self):
        user_data = {
            "first_name": self.first_name_field.text(),
            "last_name": self.last_name_field.text(),
            "address": self.address_field.text(),
            "phone": self.phone_field.text(),
            "email": self.email_field.text(),
            "about": self.about_field.toPlainText(),
        }

        if not self.first_name_field.text():
            self.message.setText("First Name is empty")
            self.message.setWindowTitle("Error")
            self.message.exec()
            return
        
        if not self.last_name_field.text():
            self.message.setText("Last Name is empty")
            self.message.exec()
            return
        
        if not self.address_field.text():
            self.message.setText("Address is empty")
            self.message.exec()
            return
        
        if not self.address_field.text():
            self.message.setText("Address is empty")
            self.message.exec()
            return
        
        if not self.phone_field.text():
            self.message.setText("Phone is empty")
            self.message.exec()
            return
        
        if not self.email_field.text():
            self.message.setText("Email is empty")
            self.message.exec()
            return

        with open("user_data.json", "w") as f:
            json.dump(user_data, f)

        # show message about save
        self.message.setText("Data Saved")
        self.message.exec()

        self.first_name_field.clear()
        self.last_name_field.clear()
        self.address_field.clear()
        self.phone_field.clear()
        self.email_field.clear()
        self.about_field.clear()


if __name__ == "__main__":
    # create a new QApplication
    app = QApplication(sys.argv)

    # create an instance of our window
    win = RegistrationForm()
    win.show()

    # wait for window close
    sys.exit(app.exec())