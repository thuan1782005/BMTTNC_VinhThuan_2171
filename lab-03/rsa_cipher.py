import sys
import requests
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from ui.rsa import Ui_MainWindow


class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.pushButton.clicked.connect(self.call_api_gen_keys)
        self.ui.pushButton_2.clicked.connect(self.call_api_encrypt)
        self.ui.pushButton_3.clicked.connect(self.call_api_decrypt)
        self.ui.pushButton_4.clicked.connect(self.call_api_sign)
        self.ui.pushButton_5.clicked.connect(self.call_api_verify)

    def call_api_gen_keys(self):
        url = "http://127.0.0.1:5000/api/rsa/generate_keys"

        try:
            response = requests.get(url)

            if response.status_code == 200:
                data = response.json()

                QMessageBox.information(
                    self,
                    "Success",
                    data["message"]
                )
            else:
                print("Error while calling API")

        except requests.exceptions.RequestException as e:
            print(f"Error: {e}")

    def call_api_encrypt(self):
        url = "http://127.0.0.1:5000/api/rsa/encrypt"

        payload = {
            "message": self.ui.txt_plain_text.toPlainText(),
            "key_type": "public"
        }

        try:
            response = requests.post(url, json=payload)

            if response.status_code == 200:
                data = response.json()

                self.ui.txt_cipher_text.setPlainText(
                    data["encrypted_message"]
                )

                QMessageBox.information(
                    self,
                    "Success",
                    "Encrypted Successfully"
                )
            else:
                print("Error while calling API")

        except requests.exceptions.RequestException as e:
            print(f"Error: {e}")

    def call_api_decrypt(self):
        url = "http://127.0.0.1:5000/api/rsa/decrypt"

        payload = {
            "ciphertext": self.ui.txt_cipher_text.toPlainText(),
            "key_type": "private"
        }

        try:
            response = requests.post(url, json=payload)

            if response.status_code == 200:
                data = response.json()

                self.ui.txt_plain_text.setPlainText(
                    str(data["decrypted_message"])
                )

                QMessageBox.information(
                    self,
                    "Success",
                    "Decrypted Successfully"
                )
            else:
                print("Error while calling API")

        except requests.exceptions.RequestException as e:
            print(f"Error: {e}")

    def call_api_sign(self):
        url = "http://127.0.0.1:5000/api/rsa/sign"

        payload = {
            "message": self.ui.txt_information.toPlainText()
        }

        try:
            response = requests.post(url, json=payload)

            if response.status_code == 200:
                data = response.json()

                self.ui.txt_signature.setPlainText(
                    data["signature"]
                )

                QMessageBox.information(
                    self,
                    "Success",
                    "Signed Successfully"
                )
            else:
                print("Error while calling API")

        except requests.exceptions.RequestException as e:
            print(f"Error: {e}")

    def call_api_verify(self):
        url = "http://127.0.0.1:5000/api/rsa/verify"

        payload = {
            "message": self.ui.txt_information.toPlainText(),
            "signature": self.ui.txt_signature.toPlainText()
        }

        try:
            response = requests.post(url, json=payload)

            if response.status_code == 200:
                data = response.json()

                if data["is_verified"]:
                    QMessageBox.information(
                        self,
                        "Verify",
                        "Verified Successfully"
                    )
                else:
                    QMessageBox.warning(
                        self,
                        "Verify",
                        "Verified Fail"
                    )
            else:
                print("Error while calling API")

        except requests.exceptions.RequestException as e:
            print(f"Error: {e}")


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MyApp()
    window.show()

    sys.exit(app.exec_())