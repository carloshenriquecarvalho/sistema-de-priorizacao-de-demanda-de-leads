# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'janela_principal.ui'
##
## Created by: Qt User Interface Compiler version 6.12.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QFormLayout, QGroupBox,
    QLabel, QLineEdit, QListView, QMainWindow,
    QMenuBar, QPushButton, QSizePolicy, QStatusBar,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(745, 409)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(0, 10, 741, 341))
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(150)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox_2 = QGroupBox(self.groupBox)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(10, 10, 711, 121))
        self.formLayoutWidget = QWidget(self.groupBox_2)
        self.formLayoutWidget.setObjectName(u"formLayoutWidget")
        self.formLayoutWidget.setGeometry(QRect(10, 20, 331, 71))
        self.formLayout = QFormLayout(self.formLayoutWidget)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.input_vendedor = QLineEdit(self.formLayoutWidget)
        self.input_vendedor.setObjectName(u"input_vendedor")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(150)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.input_vendedor.sizePolicy().hasHeightForWidth())
        self.input_vendedor.setSizePolicy(sizePolicy1)
        self.input_vendedor.setMinimumSize(QSize(200, 0))

        self.formLayout.setWidget(0, QFormLayout.ItemRole.FieldRole, self.input_vendedor)

        self.label = QLabel(self.formLayoutWidget)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.label)

        self.input_etapa_vazia = QCheckBox(self.formLayoutWidget)
        self.input_etapa_vazia.setObjectName(u"input_etapa_vazia")
        self.input_etapa_vazia.setEnabled(True)
        self.input_etapa_vazia.setMouseTracking(True)
        self.input_etapa_vazia.setChecked(True)

        self.formLayout.setWidget(1, QFormLayout.ItemRole.LabelRole, self.input_etapa_vazia)

        self.formLayoutWidget_2 = QWidget(self.groupBox_2)
        self.formLayoutWidget_2.setObjectName(u"formLayoutWidget_2")
        self.formLayoutWidget_2.setGeometry(QRect(350, 20, 341, 71))
        self.formLayout_2 = QFormLayout(self.formLayoutWidget_2)
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.formLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.formLayoutWidget_2)
        self.label_2.setObjectName(u"label_2")

        self.formLayout_2.setWidget(0, QFormLayout.ItemRole.LabelRole, self.label_2)

        self.input_quantidade_de_leads = QLineEdit(self.formLayoutWidget_2)
        self.input_quantidade_de_leads.setObjectName(u"input_quantidade_de_leads")
        sizePolicy1.setHeightForWidth(self.input_quantidade_de_leads.sizePolicy().hasHeightForWidth())
        self.input_quantidade_de_leads.setSizePolicy(sizePolicy1)
        self.input_quantidade_de_leads.setMinimumSize(QSize(200, 0))

        self.formLayout_2.setWidget(0, QFormLayout.ItemRole.FieldRole, self.input_quantidade_de_leads)

        self.input_conversao = QLineEdit(self.formLayoutWidget_2)
        self.input_conversao.setObjectName(u"input_conversao")
        sizePolicy1.setHeightForWidth(self.input_conversao.sizePolicy().hasHeightForWidth())
        self.input_conversao.setSizePolicy(sizePolicy1)
        self.input_conversao.setMinimumSize(QSize(200, 0))

        self.formLayout_2.setWidget(1, QFormLayout.ItemRole.FieldRole, self.input_conversao)

        self.label_4 = QLabel(self.formLayoutWidget_2)
        self.label_4.setObjectName(u"label_4")

        self.formLayout_2.setWidget(1, QFormLayout.ItemRole.LabelRole, self.label_4)

        self.botao_calcular = QPushButton(self.groupBox_2)
        self.botao_calcular.setObjectName(u"botao_calcular")
        self.botao_calcular.setEnabled(True)
        self.botao_calcular.setGeometry(QRect(10, 90, 81, 26))
        self.listView = QListView(self.groupBox)
        self.listView.setObjectName(u"listView")
        self.listView.setGeometry(QRect(10, 140, 711, 191))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 745, 33))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.groupBox.setTitle("")
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"Dados", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Vendedor", None))
        self.input_etapa_vazia.setText(QCoreApplication.translate("MainWindow", u"1\u00aa Etapa Vazia?", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Quantidade de Leads", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Taxa de Convers\u00e3o", None))
        self.botao_calcular.setText(QCoreApplication.translate("MainWindow", u"Calcular", None))
    # retranslateUi

