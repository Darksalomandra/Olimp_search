import sys
from PyQt5 import QtWidgets
from window2 import *
from parser_site import parse_olimp
from window4 import Ui_Dialog
from window5 import Ui_MainWindow3
from window6 import *
from window7 import *
from handler.work_db import *


class Search1(QtWidgets.QMainWindow):
    """класс в котором работет всё"""

    def __init__(self):
        super(Search1, self).__init__()
        self.db_all = db_all()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.base_line_edit1 = self.ui.lineEdit_search1

        self.subject_search_combo_box()
        self.class_search_combo_box()
        self.type_search_combo_box()
        self.pushButton_search_Button()

    def subject_search_combo_box(self):
        subject_search = ([
            'Биология', 'География', 'Информатика', 'Математика', 'Физика', 'Химия', 'Астрономия', 'ИЗО', 'Искусство',
            'История', 'Лингвистика', 'Литература', 'ОБЖ', 'Обществознание', 'Предпринимательсво', 'Право',
            'Психология', 'Робототехника', 'Русский язык', 'Технология', 'Физкультура', 'Черчение', 'Экология',
            'Экономика', 'Ин.языки'
        ])
        self.ui.subject_search.addItems(subject_search)

    def class_search_combo_box(self):
        class_search = ([])
        for item in range(11):
            class_search.append(str(item + 1))
        self.ui.class_search.addItems(class_search)

    def type_search_combo_box(self):
        type_search = ([
            'Командные', 'Личные', 'Дистанционные', 'Все'
        ])
        self.ui.type_search.addItems(type_search)

    def pushButton_search_Button(self):
        """все кнопки"""
        self.ui.pushButton_search1.clicked.connect(self.pushButton_search_clicked1)
        self.ui.pushButton_search2.clicked.connect(self.reg)
        self.ui.pushButton_search3.clicked.connect(self.pushButton_search_clicked5)
        self.ui.pushButton_search4.clicked.connect(self.pushButton_search_clicked4)

    def pushButton_search_clicked1(self):
        """парсинг"""
        text1 = self.ui.subject_search.currentText()
        text2 = self.ui.class_search.currentText()
        text3 = self.ui.type_search.currentText()
        text = parse_olimp.parse_text(text1, text2, text3)
        self.ui.textEdit.setText(f'{text}')

    def pushButton_search_clicked4(self):
        """окно3"""
        self.window3 = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow3()
        self.ui.setupUi(self.window3)
        self.window3.show()
        self.ui.pushButton1.clicked.connect(self.open_window1)

    def pushButton_search_clicked5(self):
        """окно5"""
        self.window5 = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow5()
        self.ui.setupUi(self.window5)
        self.window5.show()
        self.ui.tableWidget.setColumnWidth(0, 200)
        self.ui.tableWidget.setHorizontalHeaderLabels(["name"])
        self.ui.pushButton_search6.clicked.connect(self.auth)
        self.ui.pushButton_search5.clicked.connect(self.close_window5)
        connection = sqlite3.connect('handler/db_site.sqlite')
        cur = connection.cursor()
        sqlstr = 'SELECT * FROM db_search LIMIT 40'

        tablerow = 0
        results = cur.execute(sqlstr).fetchall()
        self.ui.tableWidget.setRowCount(40)
        for row in results:
            self.ui.tableWidget.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(row[0]))
            tablerow += 1

    def close_window5(self):
        """закрыть окно5"""
        self.window5.close()

    def open_window1(self):
        """окно2"""
        self.window2 = QtWidgets.QDialog()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self.window2)
        self.window2.show()
        self.ui.pushButton_1.clicked.connect(self.on_accepted)
        self.ui.pushButton_2.clicked.connect(self.off_accepted)

    def off_accepted(self):
        """закрыть окно2"""
        self.window2.close()

    def on_accepted(self):
        """закрыть окно2"""
        self.window2.close()

    def auth(self):
        pass

    def reg(self):
        self.ui.lineEdit_search1.clear()
        name = self.ui.lineEdit_search1.text()
        self.db_all.register(name)

    def open_window2(self):
        """окно4"""
        self.window4 = QtWidgets.QDialog()
        self.ui = Ui_Form2()
        self.ui.setupUi(self.window4)
        self.window4.show()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    sear = Search1()
    sear.show()
    sys.exit(app.exec_())
