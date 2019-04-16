# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'resources\ui\gui_tripwire.ui',
# licensing of 'resources\ui\gui_tripwire.ui' applies.
#
# Created: Tue Apr 16 09:13:17 2019
#      by: pyside2-uic  running on PySide2 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_TripwireDialog(object):
    def setupUi(self, TripwireDialog):
        TripwireDialog.setObjectName("TripwireDialog")
        TripwireDialog.resize(400, 300)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(TripwireDialog.sizePolicy().hasHeightForWidth())
        TripwireDialog.setSizePolicy(sizePolicy)
        TripwireDialog.setMinimumSize(QtCore.QSize(400, 300))
        TripwireDialog.setMaximumSize(QtCore.QSize(400, 300))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        TripwireDialog.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/images/app_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        TripwireDialog.setWindowIcon(icon)
        TripwireDialog.setSizeGripEnabled(False)
        self.gridLayout = QtWidgets.QGridLayout(TripwireDialog)
        self.gridLayout.setObjectName("gridLayout")
        self.lineEdit_pass = QtWidgets.QLineEdit(TripwireDialog)
        self.lineEdit_pass.setInputMethodHints(QtCore.Qt.ImhHiddenText|QtCore.Qt.ImhNoAutoUppercase|QtCore.Qt.ImhNoPredictiveText|QtCore.Qt.ImhSensitiveData)
        self.lineEdit_pass.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_pass.setObjectName("lineEdit_pass")
        self.gridLayout.addWidget(self.lineEdit_pass, 3, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(TripwireDialog)
        self.label_5.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_5.setOpenExternalLinks(True)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 6, 1, 1, 1)
        self.lineEdit_url = QtWidgets.QLineEdit(TripwireDialog)
        self.lineEdit_url.setObjectName("lineEdit_url")
        self.gridLayout.addWidget(self.lineEdit_url, 1, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(TripwireDialog)
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap(":/images/tripwire_banner.png"))
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 0, 0, 1, 2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.checkBox_evescout = QtWidgets.QCheckBox(TripwireDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkBox_evescout.sizePolicy().hasHeightForWidth())
        self.checkBox_evescout.setSizePolicy(sizePolicy)
        self.checkBox_evescout.setToolTip("")
        self.checkBox_evescout.setObjectName("checkBox_evescout")
        self.horizontalLayout.addWidget(self.checkBox_evescout)
        self.label_6 = QtWidgets.QLabel(TripwireDialog)
        self.label_6.setOpenExternalLinks(True)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout.addWidget(self.label_6)
        self.gridLayout.addLayout(self.horizontalLayout, 5, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(TripwireDialog)
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(TripwireDialog)
        self.label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 3, 0, 1, 1)
        self.label = QtWidgets.QLabel(TripwireDialog)
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)
        self.buttonBox = QtWidgets.QDialogButtonBox(TripwireDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout.addWidget(self.buttonBox, 10, 0, 1, 2)
        self.lineEdit_user = QtWidgets.QLineEdit(TripwireDialog)
        self.lineEdit_user.setObjectName("lineEdit_user")
        self.gridLayout.addWidget(self.lineEdit_user, 2, 1, 1, 1)
        self.label_evescout_logo = QtWidgets.QLabel(TripwireDialog)
        self.label_evescout_logo.setCursor(QtCore.Qt.PointingHandCursor)
        self.label_evescout_logo.setText("")
        self.label_evescout_logo.setPixmap(QtGui.QPixmap(":/images/evescout.png"))
        self.label_evescout_logo.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_evescout_logo.setObjectName("label_evescout_logo")
        self.gridLayout.addWidget(self.label_evescout_logo, 4, 0, 4, 1)

        self.retranslateUi(TripwireDialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), TripwireDialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), TripwireDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(TripwireDialog)

    def retranslateUi(self, TripwireDialog):
        TripwireDialog.setWindowTitle(QtWidgets.QApplication.translate("TripwireDialog", "Tripwire Configuration", None, -1))
        self.label_5.setText(QtWidgets.QApplication.translate("TripwireDialog", "<html><head/><body><p><a href=\"https://tripwire.eve-apps.com/\"><span style=\" text-decoration: underline; color:#0000ff;\">Don\'t have a Tripwire account, yet?</span></a></p></body></html>", None, -1))
        self.checkBox_evescout.setText(QtWidgets.QApplication.translate("TripwireDialog", "Enable Eve-Scout", None, -1))
        self.label_6.setText(QtWidgets.QApplication.translate("TripwireDialog", "<html><head/><body><p><a href=\"https://github.com/secondfry/shortcircuit/blob/master/README.md#eve-scout\"><span style=\" text-decoration: underline; color:#0000ff;\">[Should I enable this?]</span></a></p></body></html>", None, -1))
        self.label_2.setText(QtWidgets.QApplication.translate("TripwireDialog", "Username:", None, -1))
        self.label_3.setText(QtWidgets.QApplication.translate("TripwireDialog", "Password:", None, -1))
        self.label.setText(QtWidgets.QApplication.translate("TripwireDialog", "URL:", None, -1))

from . import resources_rc
