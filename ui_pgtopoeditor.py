# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_pgtopoeditor.ui'
#
# Created by: PyQt4 UI code generator 4.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


def _translate(context, text, disambig):
    return QtGui.QGuiApplication.translate(context, text, disambig)


class Ui_PgTopoEditor(object):
    def setupUi(self, PgTopoEditor):
        PgTopoEditor.setObjectName("PgTopoEditor")
        PgTopoEditor.resize(400, 300)
        self.buttonBox = QtWidgets.QDialogButtonBox(PgTopoEditor)
        self.buttonBox.setGeometry(QtCore.QRect(30, 240, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")

        self.retranslateUi(PgTopoEditor)
        # QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), PgTopoEditor.accept)
        # QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), PgTopoEditor.reject)

        self.buttonBox.accepted.connect(PgTopoEditor.accept)
        self.buttonBox.rejected.connect(PgTopoEditor.reject)

        QtCore.QMetaObject.connectSlotsByName(PgTopoEditor)

    def retranslateUi(self, PgTopoEditor):
        PgTopoEditor.setWindowTitle(_translate("PgTopoEditor", "PgTopoEditor", None))

