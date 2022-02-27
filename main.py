import sys

import requests
from PySide2.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QFileDialog

from settings import Settings


class AppWindow(QWidget):
    def __init__(self):
        super().__init__()

        # layout
        self.main_layout = QVBoxLayout()

        # elements
        self.button = QPushButton('Загрузить')
        self.label = QLabel()

        # configuration
        self.main_layout.addWidget(self.label)
        self.main_layout.addWidget(self.button)
        self.setLayout(self.main_layout)

        # signals
        self.button.clicked.connect(self.load_file)

    def load_research(self):
        request = requests.get(f'{Settings.SERVER}/researches/')
        self.label.setText(request.text)

    def load_file(self):
        request = requests.get(f'{Settings.SERVER}/researches/import/', params={'research_list': [1, 2]})
        name, _ = QFileDialog.getSaveFileName(self, "Browse Geometry File", r"C:\Users\kudro\Desktop\PySide2\ResearchBaseClient\interface", "*.txt")
        print(name)
        file = open(name, 'w')
        text = request.content.decode('UTF-8')
        file.write(text)
        file.close()




if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = AppWindow()
    w.show()
    sys.exit(app.exec_())