import QtQuick
import QtQuick.Controls
import QtQuick.Layouts


ApplicationWindow{
    width: 400
    height: 400
    visible: true
    title: "Registration Form"

    ColumnLayout{
        anchors.fill: parent
        anchors.margins: 10

        Label{
            text: MyName
        }

        TextField{id: name_field; placeholderText: "Name"; Layout.fillWidth: true}
        TextField{id: email_field; placeholderText: "Email"; Layout.fillWidth: true}
        TextField{id: phone_field; placeholderText: "Phone"; Layout.fillWidth: true}
        TextField{id: address_field; placeholderText: "Address"; Layout.fillWidth: true}
        TextArea{id: about_field; placeholderText: "About"; Layout.fillWidth: true; Layout.fillHeight: true}

        Button{
            text: "Save User Data"
            Layout.fillWidth: true

            onClicked: {
                UserDataSaver.save_data(
                    name_field.text,
                    email_field.text,
                    phone_field.text,
                    address_field.text,
                    about_field.text
                )

                name_field.clear()
                email_field.clear()
                phone_field.clear()
                address_field.clear()
                about_field.clear()
            }
        }
    }
}