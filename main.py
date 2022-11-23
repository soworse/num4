import sqlite3
import sys
from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtWidgets import *
from PyQt5.QtSql import QSqlDatabase, QSqlQuery, QSqlTableModel, QSqlQueryModel
from PyQt5.QtCore import *
from PyQt5.QtGui import *


class chukupuka(QMainWindow):
    def __init__(self):
        super(chukupuka, self).__init__()
        uic.loadUi('main.ui', self)
        db = QSqlDatabase.addDatabase('QSQLITE')
        db.setDatabaseName('coffee.sqlite')
        db.open()
        model = QSqlTableModel(self, db)
        model.setTable('coffee')
        model.select()
        self.tableView.setModel(model)
        self.tableView.show()


if __name__ == '__main__':
    report_app = QApplication(sys.argv)
    ex1 = chukupuka()
    ex1.show()
    sys.exit(report_app.exec_())
