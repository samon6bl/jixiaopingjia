# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './绩效目标审核.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1444, 757)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 0, 601, 111))
        self.layoutWidget.setBaseSize(QtCore.QSize(0, 11))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setHorizontalSpacing(2)
        self.gridLayout.setObjectName("gridLayout")
        self.label_7 = QtWidgets.QLabel(self.layoutWidget)
        self.label_7.setBaseSize(QtCore.QSize(0, 11))
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 1, 3, 1, 1)
        self.item_catagory = QtWidgets.QTextBrowser(self.layoutWidget)
        self.item_catagory.setBaseSize(QtCore.QSize(0, 1))
        self.item_catagory.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.item_catagory.setObjectName("item_catagory")
        self.gridLayout.addWidget(self.item_catagory, 2, 3, 1, 1, QtCore.Qt.AlignVCenter)
        self.label_6 = QtWidgets.QLabel(self.layoutWidget)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 1, 2, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.layoutWidget)
        self.label_8.setBaseSize(QtCore.QSize(0, 11))
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 1, 4, 1, 1)
        self.bianma_box = QtWidgets.QComboBox(self.layoutWidget)
        self.bianma_box.setObjectName("bianma_box")
        self.gridLayout.addWidget(self.bianma_box, 2, 2, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 2, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.layoutWidget)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 1, 1, 1, 1)
        self.bennianjine = QtWidgets.QTextBrowser(self.layoutWidget)
        self.bennianjine.setBaseSize(QtCore.QSize(0, 1))
        self.bennianjine.setObjectName("bennianjine")
        self.gridLayout.addWidget(self.bennianjine, 2, 4, 1, 1, QtCore.Qt.AlignVCenter)
        self.layoutWidget1 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget1.setGeometry(QtCore.QRect(10, 130, 601, 291))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.layoutWidget1)
        self.gridLayout_2.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.niandumubiao = QtWidgets.QTextBrowser(self.layoutWidget1)
        self.niandumubiao.setObjectName("niandumubiao")
        self.gridLayout_2.addWidget(self.niandumubiao, 2, 2, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_2.setWordWrap(True)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 1, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_3.setWordWrap(True)
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 2, 0, 1, 1)
        self.cesuanyiju = QtWidgets.QTextBrowser(self.layoutWidget1)
        self.cesuanyiju.setObjectName("cesuanyiju")
        self.gridLayout_2.addWidget(self.cesuanyiju, 1, 2, 1, 1)
        self.label = QtWidgets.QLabel(self.layoutWidget1)
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setScaledContents(False)
        self.label.setWordWrap(True)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)
        self.zhengceyiju = QtWidgets.QTextBrowser(self.layoutWidget1)
        self.zhengceyiju.setObjectName("zhengceyiju")
        self.gridLayout_2.addWidget(self.zhengceyiju, 0, 2, 1, 1)
        self.jixiaozhibiao_tableview = QtWidgets.QTableView(self.centralwidget)
        self.jixiaozhibiao_tableview.setGeometry(QtCore.QRect(750, 0, 681, 461))
        self.jixiaozhibiao_tableview.setLineWidth(1)
        self.jixiaozhibiao_tableview.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.jixiaozhibiao_tableview.setObjectName("jixiaozhibiao_tableview")
        self.jixiaozhibiao_tableview.horizontalHeader().setVisible(True)
        self.jixiaozhibiao_tableview.horizontalHeader().setCascadingSectionResizes(False)
        self.jixiaozhibiao_tableview.horizontalHeader().setDefaultSectionSize(100)
        self.jixiaozhibiao_tableview.horizontalHeader().setMinimumSectionSize(5)
        self.jixiaozhibiao_tableview.horizontalHeader().setStretchLastSection(True)
        self.jixiaozhibiao_tableview.verticalHeader().setCascadingSectionResizes(False)
        self.jixiaozhibiao_tableview.verticalHeader().setDefaultSectionSize(5)
        self.jixiaozhibiao_tableview.verticalHeader().setMinimumSectionSize(5)
        self.jixiaozhibiao_tableview.verticalHeader().setStretchLastSection(False)
        self.summary_view = QtWidgets.QListView(self.centralwidget)
        self.summary_view.setGeometry(QtCore.QRect(620, 220, 111, 201))
        self.summary_view.setObjectName("summary_view")
        self.wanzheng_listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.wanzheng_listWidget.setGeometry(QtCore.QRect(70, 430, 541, 261))
        self.wanzheng_listWidget.setObjectName("wanzheng_listWidget")
        self.checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox.setGeometry(QtCore.QRect(630, 130, 101, 21))
        self.checkBox.setObjectName("checkBox")
        self.checkBox_2 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_2.setGeometry(QtCore.QRect(630, 160, 101, 21))
        self.checkBox_2.setObjectName("checkBox_2")
        self.checkBox_3 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_3.setGeometry(QtCore.QRect(630, 190, 101, 21))
        self.checkBox_3.setObjectName("checkBox_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(0, 510, 71, 31))
        self.label_4.setObjectName("label_4")
        self.kecexing_listwidget = QtWidgets.QListWidget(self.centralwidget)
        self.kecexing_listwidget.setGeometry(QtCore.QRect(790, 490, 281, 201))
        self.kecexing_listwidget.setObjectName("kecexing_listwidget")
        self.comboBox_2 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_2.setGeometry(QtCore.QRect(640, 570, 101, 21))
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_3 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_3.setGeometry(QtCore.QRect(640, 610, 101, 21))
        self.comboBox_3.setObjectName("comboBox_3")
        self.kexingxing_listwidget = QtWidgets.QListWidget(self.centralwidget)
        self.kexingxing_listwidget.setGeometry(QtCore.QRect(1100, 490, 321, 201))
        self.kexingxing_listwidget.setObjectName("kexingxing_listwidget")
        self.comboBox_4 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_4.setGeometry(QtCore.QRect(640, 530, 101, 21))
        self.comboBox_4.setObjectName("comboBox_4")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(630, 70, 101, 41))
        self.pushButton.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 1444, 22))
        self.menuBar.setObjectName("menuBar")
        self.menu = QtWidgets.QMenu(self.menuBar)
        self.menu.setObjectName("menu")
        MainWindow.setMenuBar(self.menuBar)
        self.actionOpen_project_directory = QtWidgets.QAction(MainWindow)
        self.actionOpen_project_directory.setCheckable(False)
        self.actionOpen_project_directory.setObjectName("actionOpen_project_directory")
        self.menu.addAction(self.actionOpen_project_directory)
        self.menuBar.addAction(self.menu.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_7.setText(_translate("MainWindow", "项目类型"))
        self.label_6.setText(_translate("MainWindow", "项目编码"))
        self.label_8.setText(_translate("MainWindow", "本年金额"))
        self.label_5.setText(_translate("MainWindow", "审核人"))
        self.label_2.setText(_translate("MainWindow", "测算依据"))
        self.label_3.setText(_translate("MainWindow", "年度目标"))
        self.label.setText(_translate("MainWindow", "政策依据"))
        self.zhengceyiju.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'.AppleSystemUIFont\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.checkBox.setText(_translate("MainWindow", "政策依据审核"))
        self.checkBox_2.setText(_translate("MainWindow", "测算依据审核"))
        self.checkBox_3.setText(_translate("MainWindow", "年度目标审核"))
        self.label_4.setText(_translate("MainWindow", "完整性审核"))
        self.pushButton.setText(_translate("MainWindow", "项目文件夹"))
        self.menu.setTitle(_translate("MainWindow", "文件"))
        self.actionOpen_project_directory.setText(_translate("MainWindow", "Open project directory"))
