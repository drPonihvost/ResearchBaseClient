from PySide2.QtGui import QFont, QGuiApplication, QIcon, QPixmap, QFontDatabase
from PySide2.QtWidgets import QWidget
from interface.resources import rc_resources

class BaseWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setContentsMargins(3, 3, 3, 3)

    def set_window_config(self):
        self.setWindowIcon(QIcon(':dna_icon.svg'))
        QFontDatabase.addApplicationFont(':ubuntu_regular.ttf')
        font = QFont(':ubuntu_regular', 10)
        font.setFamily('Ubuntu')
        self.setFont(font)
        self.setWindowTitle('Направления на исследования')

    def center_and_set_the_size(self, x_ratio: float = 1, y_ratio: float = 1) -> None:
        desktop = QGuiApplication.screens()[0].geometry()
        desktop_width = desktop.width()
        desktop_height = desktop.height()
        self.resize(desktop.width() * x_ratio, desktop.height() * y_ratio)

        x = (desktop_width - desktop.width() * x_ratio) // 2
        y = (desktop_height - desktop.height() * y_ratio) // 2
        self.move(x, y)