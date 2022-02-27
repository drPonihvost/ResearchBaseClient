import json
from typing import List, Dict

from PySide2.QtGui import QIcon, QFont, QFontDatabase

from interface.base_widgets.input_elements import CheckBoxWidget
from interface.base_widgets.main_widget import BaseWidget
from interface.resources import rc_resources

import requests
from PySide2.QtWidgets import QTableWidget, QAbstractItemView, QTableWidgetItem, QButtonGroup, QCheckBox, QWidget, \
    QVBoxLayout


class ResearchTable(QTableWidget, BaseWidget):
    FIELDS = [
        'Выбрать',
        'Номер',
        'Дата записи',
        'Номер материала',
        'Дата формирования',
        'Событие',
        'Дата происшествия',
        'Адрес места происшествия',
        'Статья УК РФ',
        'Родственный поиск',
        'Дата регистрации',
    ]

    def __init__(self):
        super(ResearchTable, self).__init__()
        self.set_window_config()
        self.setColumnCount(len(self.FIELDS))
        self.setHorizontalHeaderLabels(self.FIELDS)
        self.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.resize_to_content()

        self.itemSelectionChanged.connect(self.get_id_list)

    def resize_to_content(self):
        column_width = 300
        self.resizeColumnsToContents()
        self.setColumnWidth(self.FIELDS.index('Событие'), column_width)
        self.setColumnWidth(self.FIELDS.index('Адрес места происшествия'), column_width)
        self.setColumnWidth(self.FIELDS.index('Статья УК РФ'), column_width)
        self.resizeRowsToContents()

    def set_data(self, research_list: List[Dict]):
        self.setRowCount(0)
        for research in research_list:
            row = self.rowCount()
            self.insertRow(row)
            check_box = CheckBoxWidget(research['id'])
            check_box.check_box.toggled.connect(self.check_box_clicked)
            self.setCellWidget(row, self.FIELDS.index('Выбрать'), check_box)
            self.setItem(row, self.FIELDS.index('Номер'), QTableWidgetItem(str(research['reg_number'])))
            self.setItem(row, self.FIELDS.index('Дата записи'), QTableWidgetItem(research['date_of_record']))
            self.setItem(row, self.FIELDS.index('Номер материала'), QTableWidgetItem(research['event_number']))
            self.setItem(row, self.FIELDS.index('Дата формирования'), QTableWidgetItem(research['formation_date']))
            self.setItem(row, self.FIELDS.index('Событие'), QTableWidgetItem(research['plot']))
            self.setItem(row, self.FIELDS.index('Дата происшествия'), QTableWidgetItem(research['incident_date']))
            self.setItem(row, self.FIELDS.index('Адрес места происшествия'), QTableWidgetItem(research['address']))
            self.setItem(row, self.FIELDS.index('Статья УК РФ'), QTableWidgetItem(research['article']))
            self.setItem(row, self.FIELDS.index('Родственный поиск'), QTableWidgetItem(research['relative_search']))
            self.setItem(row, self.FIELDS.index('Дата регистрации'), QTableWidgetItem(research['reg_date']))
        self.resize_to_content()

    def check_box_clicked(self):
        if self.sender().isChecked():
            print(self.sender().objectName())
            return self.sender().objectName()

    def get_id_list(self):
        checked_list = []
        for i in range(self.rowCount()):
            if self.cellWidget(i, 0).check_box.isChecked():
                checked_list.append(self.cellWidget(i, 0).object_name)
        return checked_list


if __name__ == '__main__':
    import sys
    from PySide2.QtWidgets import QApplication
    app = QApplication(sys.argv)
    w = ResearchTable()
    researches = requests.get('http://127.0.0.1:8000/researches/')
    w.set_data(researches.json())
    w.show()
    sys.exit(app.exec_())