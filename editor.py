import sys, os
from PyQt5.QtWidgets import QTextEdit, QPushButton, QVBoxLayout, QHBoxLayout, QWidget, QApplication, QFileDialog


class Editor(QWidget):

    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.text = QTextEdit()
        self.btn_clr = QPushButton('Clear')
        self.btn_sav = QPushButton('Save')
        self.btn_opn = QPushButton('Open')

        h_box = QHBoxLayout()

        h_box.addWidget(self.btn_clr)
        h_box.addWidget(self.btn_sav)
        h_box.addWidget(self.btn_opn)
        
        layout = QVBoxLayout()
        layout.addWidget(self.text)
        layout.addLayout(h_box)


        self.btn_clr.clicked.connect(lambda: self.clear_text())
        self.btn_sav.clicked.connect(lambda: self.save_text())
        self.btn_opn.clicked.connect(lambda: self.open_text())

        self.setLayout(layout)

        self.show()

    def clear_text(self):
        self.text.clear()

    def save_text(self):
        file_name = QFileDialog.getSaveFileName(self, 'Save File', os.getenv('HOME'))
        if len(file_name[0]) > 0:
            with open(file_name[0], 'w') as f:
                f.write(self.text.toPlainText())

    def open_text(self):
        file_name = QFileDialog.getOpenFileName(self, 'Open File', os.getenv('HOME'))
        if len(file_name[0]) > 0:
            with open(file_name[0], 'r') as f:
                self.text.setText(f.read())


app = QApplication(sys.argv)
ed_window = Editor()
sys.exit(app.exec_())