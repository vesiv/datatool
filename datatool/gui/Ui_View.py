# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/vesi/documents/bin/datatool/datatool/gui/View.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_DataTool(object):
    def setupUi(self, DataTool):
        DataTool.setObjectName("DataTool")
        DataTool.resize(928, 778)
        self.centralwidget = QtWidgets.QWidget(DataTool)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tabWidget.setMovable(True)
        self.tabWidget.setTabBarAutoHide(True)
        self.tabWidget.setObjectName("tabWidget")
        self.verticalLayout.addWidget(self.tabWidget)
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textEdit.sizePolicy().hasHeightForWidth())
        self.textEdit.setSizePolicy(sizePolicy)
        self.textEdit.setObjectName("textEdit")
        self.verticalLayout.addWidget(self.textEdit)
        self.runButton = QtWidgets.QPushButton(self.centralwidget)
        self.runButton.setWhatsThis("")
        self.runButton.setObjectName("runButton")
        self.verticalLayout.addWidget(self.runButton)
        DataTool.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(DataTool)
        self.statusbar.setObjectName("statusbar")
        DataTool.setStatusBar(self.statusbar)
        self.menubar = QtWidgets.QMenuBar(DataTool)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 928, 30))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuOperations = QtWidgets.QMenu(self.menubar)
        self.menuOperations.setObjectName("menuOperations")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        self.menuEdit = QtWidgets.QMenu(self.menubar)
        self.menuEdit.setObjectName("menuEdit")
        DataTool.setMenuBar(self.menubar)
        self.actionExit = QtWidgets.QAction(DataTool)
        self.actionExit.setObjectName("actionExit")
        self.actionLoad = QtWidgets.QAction(DataTool)
        self.actionLoad.setObjectName("actionLoad")
        self.actionSave = QtWidgets.QAction(DataTool)
        self.actionSave.setObjectName("actionSave")
        self.actionClear_Whitespace = QtWidgets.QAction(DataTool)
        self.actionClear_Whitespace.setObjectName("actionClear_Whitespace")
        self.actionRemove_Non_Numberic = QtWidgets.QAction(DataTool)
        self.actionRemove_Non_Numberic.setObjectName("actionRemove_Non_Numberic")
        self.actionSplit_Phones = QtWidgets.QAction(DataTool)
        self.actionSplit_Phones.setObjectName("actionSplit_Phones")
        self.actionSplit_Emails = QtWidgets.QAction(DataTool)
        self.actionSplit_Emails.setObjectName("actionSplit_Emails")
        self.actionDisperse_Ranks_By_Program = QtWidgets.QAction(DataTool)
        self.actionDisperse_Ranks_By_Program.setObjectName("actionDisperse_Ranks_By_Program")
        self.actionNew_Rows_On_Separator = QtWidgets.QAction(DataTool)
        self.actionNew_Rows_On_Separator.setObjectName("actionNew_Rows_On_Separator")
        self.actionRainmaker = QtWidgets.QAction(DataTool)
        self.actionRainmaker.setObjectName("actionRainmaker")
        self.actionMindBody = QtWidgets.QAction(DataTool)
        self.actionMindBody.setObjectName("actionMindBody")
        self.actionCorrect_Date_Format = QtWidgets.QAction(DataTool)
        self.actionCorrect_Date_Format.setObjectName("actionCorrect_Date_Format")
        self.actionDelete = QtWidgets.QAction(DataTool)
        self.actionDelete.setObjectName("actionDelete")
        self.actionAdd_Column = QtWidgets.QAction(DataTool)
        self.actionAdd_Column.setObjectName("actionAdd_Column")
        self.actionAdd_Row = QtWidgets.QAction(DataTool)
        self.actionAdd_Row.setObjectName("actionAdd_Row")
        self.actionDuplicate = QtWidgets.QAction(DataTool)
        self.actionDuplicate.setObjectName("actionDuplicate")
        self.actionOpen = QtWidgets.QAction(DataTool)
        self.actionOpen.setObjectName("actionOpen")
        self.actionFind_and_Replace = QtWidgets.QAction(DataTool)
        self.actionFind_and_Replace.setObjectName("actionFind_and_Replace")
        self.menuFile.addAction(self.actionLoad)
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionExit)
        self.menuOperations.addAction(self.actionClear_Whitespace)
        self.menuOperations.addAction(self.actionRemove_Non_Numberic)
        self.menuOperations.addAction(self.actionCorrect_Date_Format)
        self.menuOperations.addAction(self.actionSplit_Phones)
        self.menuOperations.addAction(self.actionSplit_Emails)
        self.menuOperations.addAction(self.actionFind_and_Replace)
        self.menuOperations.addAction(self.actionDisperse_Ranks_By_Program)
        self.menuOperations.addAction(self.actionNew_Rows_On_Separator)
        self.menuHelp.addAction(self.actionRainmaker)
        self.menuHelp.addAction(self.actionMindBody)
        self.menuEdit.addAction(self.actionAdd_Row)
        self.menuEdit.addAction(self.actionAdd_Column)
        self.menuEdit.addAction(self.actionDelete)
        self.menuEdit.addAction(self.actionDuplicate)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuOperations.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(DataTool)
        self.tabWidget.setCurrentIndex(-1)
        QtCore.QMetaObject.connectSlotsByName(DataTool)

    def retranslateUi(self, DataTool):
        _translate = QtCore.QCoreApplication.translate
        DataTool.setWindowTitle(_translate("DataTool", "DataTool"))
        self.textEdit.setWhatsThis(_translate("DataTool", "Enter Python code here."))
        self.textEdit.setPlaceholderText(_translate("DataTool", "Enter Python code here."))
        self.runButton.setText(_translate("DataTool", "Run"))
        self.menuFile.setTitle(_translate("DataTool", "File"))
        self.menuOperations.setTitle(_translate("DataTool", "Operation"))
        self.menuHelp.setTitle(_translate("DataTool", "Software"))
        self.menuEdit.setTitle(_translate("DataTool", "Edit"))
        self.actionExit.setText(_translate("DataTool", "Exit"))
        self.actionLoad.setText(_translate("DataTool", "Load"))
        self.actionSave.setText(_translate("DataTool", "Save"))
        self.actionClear_Whitespace.setText(_translate("DataTool", "Remove Whitespace"))
        self.actionClear_Whitespace.setToolTip(_translate("DataTool", "Removes leading and trailing whitespace, as well as all line-breaks"))
        self.actionRemove_Non_Numberic.setText(_translate("DataTool", "Remove Non-Numeric"))
        self.actionRemove_Non_Numberic.setToolTip(_translate("DataTool", "Removes everything but numbers from a column."))
        self.actionSplit_Phones.setText(_translate("DataTool", "Split Phones"))
        self.actionSplit_Phones.setToolTip(_translate("DataTool", "Splits a column of phones based on their suffix. E.g. (M), (C), (H)..."))
        self.actionSplit_Emails.setText(_translate("DataTool", "Split Emails"))
        self.actionSplit_Emails.setToolTip(_translate("DataTool", "Splits a column of comma separated emails into a max of 3 Email columns"))
        self.actionDisperse_Ranks_By_Program.setText(_translate("DataTool", "Ranks By Program"))
        self.actionDisperse_Ranks_By_Program.setToolTip(_translate("DataTool", "Creates new columns based on unique entries in a column (programs) and assigns values (ranks) respectively."))
        self.actionNew_Rows_On_Separator.setText(_translate("DataTool", "New Rows On Separator"))
        self.actionNew_Rows_On_Separator.setToolTip(_translate("DataTool", "Splits a column\'s values up over multiple identical rows."))
        self.actionRainmaker.setText(_translate("DataTool", "Rainmaker"))
        self.actionRainmaker.setToolTip(_translate("DataTool", "Handles entire process for Rainmaker. Please check, double-check, re-check."))
        self.actionMindBody.setText(_translate("DataTool", "MindBody"))
        self.actionMindBody.setToolTip(_translate("DataTool", "Handles entire process for MindBody. Please check, double-check, re-check."))
        self.actionCorrect_Date_Format.setText(_translate("DataTool", "Correct Date Format"))
        self.actionDelete.setText(_translate("DataTool", "Delete"))
        self.actionDelete.setToolTip(_translate("DataTool", "Deletes selected Row/Column"))
        self.actionDelete.setShortcut(_translate("DataTool", "Del"))
        self.actionAdd_Column.setText(_translate("DataTool", "Add Column"))
        self.actionAdd_Row.setText(_translate("DataTool", "Add Row"))
        self.actionDuplicate.setText(_translate("DataTool", "Duplicate"))
        self.actionOpen.setText(_translate("DataTool", "Open"))
        self.actionFind_and_Replace.setText(_translate("DataTool", "Find and Replace"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    DataTool = QtWidgets.QMainWindow()
    ui = Ui_DataTool()
    ui.setupUi(DataTool)
    DataTool.show()
    sys.exit(app.exec_())

