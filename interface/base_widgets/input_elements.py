from PySide2.QtCore import Qt
from PySide2.QtWidgets import QCheckBox, QVBoxLayout

from interface.base_widgets.main_widget import BaseWidget


class CheckBoxWidget(BaseWidget):
    CONTENT_MARGINS = (0, 0, 0, 0)

    def __init__(self, object_name: str or int):
        super().__init__()
        self.object_name = str(object_name)
        self.layout = QVBoxLayout()
        self.layout.setContentsMargins(*self.CONTENT_MARGINS)
        self.setLayout(self.layout)
        self.check_box = QCheckBox()
        self.check_box.setObjectName(self.object_name)
        self.layout.addWidget(self.check_box)
        self.layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

    def get_object_name(self):
        return self.object_name
