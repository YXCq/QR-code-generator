# my_qrcode_app.py

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout, QFileDialog
from PyQt5.QtGui import QFont, QIcon
import qrcode

class QRCodeGeneratorApp(QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('QR Code Generator')
        self.setGeometry(300, 300, 400, 200)
        self.setWindowIcon(QIcon('logo edus.png'))

        font = QFont()
        font.setPointSize(12)

        self.label_data = QLabel('Enter URL:', self)
        self.label_data.setFont(font)
        self.entry_data = QLineEdit(self)

        self.label_filename = QLabel('Enter filename:', self)
        self.label_filename.setFont(font)
        self.entry_filename = QLineEdit(self)

        self.generate_button = QPushButton('Generate QR Code', self)
        self.generate_button.clicked.connect(self.generate_qr_code)

        self.status_label = QLabel('', self)
        self.status_label.setFont(font)

        self.browse_button = QPushButton('Browse', self)
        self.browse_button.clicked.connect(self.browse_save_path)

        layout = QVBoxLayout()
        layout.addWidget(self.label_data)
        layout.addWidget(self.entry_data)
        layout.addWidget(self.label_filename)
        layout.addWidget(self.entry_filename)
        layout.addWidget(self.browse_button)
        layout.addWidget(self.generate_button)
        layout.addWidget(self.status_label)

        hbox = QHBoxLayout()
        hbox.addStretch(1)
        hbox.addLayout(layout)
        hbox.addStretch(1)

        self.setLayout(hbox)

    def generate_qr_code(self):
        data = self.entry_data.text()
        filename = self.entry_filename.text()

        if data:
            # Here Qr code generates :)
            qr = qrcode.QRCode(
                version=1,
                error_correction=qrcode.constants.ERROR_CORRECT_L,
                box_size=10,
                border=4,
            )
            qr.add_data(data)
            qr.make(fit=True)
            img = qr.make_image(fill_color="black", back_color="white")

            # Here Qr code saves :)
            file_path, _ = QFileDialog.getSaveFileName(self, 'Save QR Code', filter='PNG Files (*.png);;All Files (*)')
            if file_path:
                img.save(file_path)
                self.status_label.setText(f'QR Code saved at: {file_path}')
            else:
                self.status_label.setText('QR Code was not saved.')
        else:
            self.status_label.setText('Please enter data!')

    def browse_save_path(self):
        directory = QFileDialog.getExistingDirectory(self, 'Choose save path')
        self.entry_filename.setText(directory)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = QRCodeGeneratorApp()
    window.show()
    sys.exit(app.exec_())
