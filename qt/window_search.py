import sys
from PyQt5 import QtWidgets
from window2 import Ui_MainWindow
from parser_site import parse_olimp
from bd_site import work_bd


class Search1(QtWidgets.QMainWindow):
    def __init__(self):
        super(Search1, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

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
        self.ui.pushButton_search1.clicked.connect(self.pushButton_search_clicked1)
        self.ui.pushButton_search2.clicked.connect(self.pushButton_search_clicked2)

    def pushButton_search_clicked1(self):
        text1 = self.ui.subject_search.currentText()
        text2 = self.ui.class_search.currentText()
        text3 = self.ui.type_search.currentText()
        text = parse_olimp.parse_text(text1, text2, text3)
        self.ui.textEdit.setText(f'{text}')

    def pushButton_search_clicked2(self):
        text_value = self.ui.lineEdit_search.text()
        work_bd.bd_sive(text_value)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    sear = Search1()
    sear.show()
    sys.exit(app.exec_())
