import sys
from PyQt5.QtWidgets import QTextEdit, QPushButton, QVBoxLayout, QWidget, QApplication


class Editor(QWidget):

    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.text = QTextEdit()
        self.btn_clr = QPushButton('Clear')
        
        layout = QVBoxLayout()
        layout.addWidget(self.text)
        layout.addWidget(self.btn_clr)

        self.btn_clr.clicked.connect(lambda: self.clear())

        self.setLayout(layout)

        self.show()

    def clear(self):
        self.text.clear()


app = QApplication(sys.argv)
ed_window = Editor()
sys.exit(app.exec_())