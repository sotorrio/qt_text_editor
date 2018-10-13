import sys, os
from PyQt5.QtWidgets import QTextEdit, QPushButton, QVBoxLayout, QHBoxLayout, QWidget
from PyQt5.QtWidgets import QApplication, QFileDialog, qApp, QAction, QMainWindow


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


class Writer(QMainWindow):
    def __init__(self):
        super().__init__()

        self.form_widget = Editor()
        self.setCentralWidget(self.form_widget)

        self.init_ui()

    def init_ui(self):
        bar = self.menuBar()
        file = bar.addMenu('File')

        new_action = QAction('&New', self)
        new_action.setShortcut('Ctrl+N')

        save_action = QAction('&Save', self)
        save_action.setShortcut('Ctrl+S')

        open_action = QAction('&Open', self)
        open_action.setShortcut('Ctrl+O')

        quit_action = QAction('&Quit', self)
        quit_action.setShortcut('ESC')

        file.addAction(new_action)
        file.addAction(open_action)
        file.addAction(save_action)
        file.addAction(quit_action)

        quit_action.triggered.connect(self.quit_trigger)

        file.triggered.connect(self.respond)

        self.show()

    def quit_trigger(self):
        qApp.quit()

    def respond(self, q):
        signal = q.text()

        if signal == '&New':
            self.form_widget.clear_text()
        elif signal == '&Open':
            self.form_widget.open_text()
        elif signal == '&Save':
            self.form_widget.save_text()



app = QApplication(sys.argv)
ed_window = Writer()
sys.exit(app.exec_())