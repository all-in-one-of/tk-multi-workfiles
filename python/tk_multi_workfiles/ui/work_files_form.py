# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'work_files_form.ui'
#
#      by: pyside-uic 0.2.13 running on PySide 1.1.0
#
# WARNING! All changes made in this file will be lost!

from tank.platform.qt import QtCore, QtGui

class Ui_WorkFilesForm(object):
    def setupUi(self, WorkFilesForm):
        WorkFilesForm.setObjectName("WorkFilesForm")
        WorkFilesForm.resize(818, 685)
        WorkFilesForm.setStyleSheet("")
        self.verticalLayout_8 = QtGui.QVBoxLayout(WorkFilesForm)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_6 = QtGui.QVBoxLayout()
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setContentsMargins(0, 0, -1, 0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.items_title_label_2 = QtGui.QLabel(WorkFilesForm)
        self.items_title_label_2.setMinimumSize(QtCore.QSize(0, 44))
        self.items_title_label_2.setStyleSheet("#items_title_label {\n"
"font-size: 14pt\n"
"}")
        self.items_title_label_2.setMargin(4)
        self.items_title_label_2.setObjectName("items_title_label_2")
        self.verticalLayout_6.addWidget(self.items_title_label_2)
        self.work_area_frame = QtGui.QFrame(WorkFilesForm)
        self.work_area_frame.setMinimumSize(QtCore.QSize(370, 0))
        self.work_area_frame.setMaximumSize(QtCore.QSize(370, 16777215))
        self.work_area_frame.setCursor(QtCore.Qt.PointingHandCursor)
        self.work_area_frame.setStyleSheet("#work_area_frame {\n"
"border-style: solid;\n"
"border-radius: 2px;\n"
"border-width: 1px;\n"
"border-color: rgb(32,32,32);\n"
"}")
        self.work_area_frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.work_area_frame.setFrameShadow(QtGui.QFrame.Raised)
        self.work_area_frame.setObjectName("work_area_frame")
        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.work_area_frame)
        self.horizontalLayout_3.setContentsMargins(6, 6, 6, 6)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.entity_pages = QtGui.QStackedWidget(self.work_area_frame)
        self.entity_pages.setStyleSheet("")
        self.entity_pages.setObjectName("entity_pages")
        self.entity_page = QtGui.QWidget()
        self.entity_page.setObjectName("entity_page")
        self.verticalLayout_5 = QtGui.QVBoxLayout(self.entity_page)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setSpacing(6)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.entity_label = QtGui.QLabel(self.entity_page)
        self.entity_label.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.entity_label.setStyleSheet("#entity_label {\n"
"font-size: 12pt\n"
"}")
        self.entity_label.setObjectName("entity_label")
        self.verticalLayout_3.addWidget(self.entity_label)
        self.entity_line = QtGui.QFrame(self.entity_page)
        self.entity_line.setFrameShape(QtGui.QFrame.HLine)
        self.entity_line.setFrameShadow(QtGui.QFrame.Sunken)
        self.entity_line.setObjectName("entity_line")
        self.verticalLayout_3.addWidget(self.entity_line)
        self.entity_description = QtGui.QLabel(self.entity_page)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.entity_description.sizePolicy().hasHeightForWidth())
        self.entity_description.setSizePolicy(sizePolicy)
        self.entity_description.setMaximumSize(QtCore.QSize(240, 16777215))
        self.entity_description.setStyleSheet("#entity_description {\n"
"font-size: 9pt\n"
"}")
        self.entity_description.setText("")
        self.entity_description.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.entity_description.setWordWrap(True)
        self.entity_description.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.entity_description.setObjectName("entity_description")
        self.verticalLayout_3.addWidget(self.entity_description)
        self.verticalLayout_3.setStretch(2, 1)
        self.horizontalLayout_4.addLayout(self.verticalLayout_3)
        self.verticalLayout_4 = QtGui.QVBoxLayout()
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.entity_thumbnail = QtGui.QLabel(self.entity_page)
        self.entity_thumbnail.setMinimumSize(QtCore.QSize(100, 100))
        self.entity_thumbnail.setMaximumSize(QtCore.QSize(100, 100))
        self.entity_thumbnail.setStyleSheet("#entity_thumbnail {\n"
"background-color: rgb(0,0,0,32);\n"
"border-radius: 2px;\n"
"}")
        self.entity_thumbnail.setText("")
        self.entity_thumbnail.setScaledContents(False)
        self.entity_thumbnail.setAlignment(QtCore.Qt.AlignCenter)
        self.entity_thumbnail.setObjectName("entity_thumbnail")
        self.verticalLayout_4.addWidget(self.entity_thumbnail)
        spacerItem = QtGui.QSpacerItem(20, 0, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem)
        self.horizontalLayout_4.addLayout(self.verticalLayout_4)
        self.horizontalLayout_4.setStretch(0, 1)
        self.verticalLayout_5.addLayout(self.horizontalLayout_4)
        self.task_pages = QtGui.QStackedWidget(self.entity_page)
        self.task_pages.setLineWidth(0)
        self.task_pages.setObjectName("task_pages")
        self.task_page = QtGui.QWidget()
        self.task_page.setObjectName("task_page")
        self.horizontalLayout_5 = QtGui.QHBoxLayout(self.task_page)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setSpacing(6)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.task_label = QtGui.QLabel(self.task_page)
        self.task_label.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.task_label.setStyleSheet("#task_label {\n"
"font-size: 12pt\n"
"}")
        self.task_label.setObjectName("task_label")
        self.verticalLayout_2.addWidget(self.task_label)
        self.task_line = QtGui.QFrame(self.task_page)
        self.task_line.setFrameShape(QtGui.QFrame.HLine)
        self.task_line.setFrameShadow(QtGui.QFrame.Sunken)
        self.task_line.setObjectName("task_line")
        self.verticalLayout_2.addWidget(self.task_line)
        self.task_details = QtGui.QLabel(self.task_page)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.task_details.sizePolicy().hasHeightForWidth())
        self.task_details.setSizePolicy(sizePolicy)
        self.task_details.setMaximumSize(QtCore.QSize(240, 16777215))
        self.task_details.setStyleSheet("#task_details {\n"
"font-size: 9pt\n"
"}")
        self.task_details.setText("")
        self.task_details.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.task_details.setWordWrap(True)
        self.task_details.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.task_details.setObjectName("task_details")
        self.verticalLayout_2.addWidget(self.task_details)
        self.verticalLayout_2.setStretch(2, 1)
        self.horizontalLayout_5.addLayout(self.verticalLayout_2)
        self.verticalLayout_7 = QtGui.QVBoxLayout()
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.task_thumbnail = QtGui.QLabel(self.task_page)
        self.task_thumbnail.setMinimumSize(QtCore.QSize(100, 100))
        self.task_thumbnail.setMaximumSize(QtCore.QSize(100, 100))
        self.task_thumbnail.setStyleSheet("#task_thumbnail {\n"
"background-color: rgb(0,0,0,32);\n"
"border-radius: 2px;\n"
"}")
        self.task_thumbnail.setFrameShape(QtGui.QFrame.NoFrame)
        self.task_thumbnail.setText("")
        self.task_thumbnail.setAlignment(QtCore.Qt.AlignCenter)
        self.task_thumbnail.setMargin(0)
        self.task_thumbnail.setIndent(0)
        self.task_thumbnail.setObjectName("task_thumbnail")
        self.verticalLayout_7.addWidget(self.task_thumbnail)
        spacerItem1 = QtGui.QSpacerItem(20, 0, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_7.addItem(spacerItem1)
        self.horizontalLayout_5.addLayout(self.verticalLayout_7)
        self.horizontalLayout_5.setStretch(0, 1)
        self.task_pages.addWidget(self.task_page)
        self.no_task_page = QtGui.QWidget()
        self.no_task_page.setObjectName("no_task_page")
        self.horizontalLayout_6 = QtGui.QHBoxLayout(self.no_task_page)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.no_task_label = QtGui.QLabel(self.no_task_page)
        self.no_task_label.setStyleSheet("#no_task_label {\n"
"font-size: 14pt;\n"
"border-style: dashed;\n"
"border-width: 2px;\n"
"border-radius: 3px;\n"
"}")
        self.no_task_label.setAlignment(QtCore.Qt.AlignCenter)
        self.no_task_label.setObjectName("no_task_label")
        self.horizontalLayout_6.addWidget(self.no_task_label)
        self.task_pages.addWidget(self.no_task_page)
        self.verticalLayout_5.addWidget(self.task_pages)
        self.entity_pages.addWidget(self.entity_page)
        self.no_entity_page = QtGui.QWidget()
        self.no_entity_page.setObjectName("no_entity_page")
        self.horizontalLayout_7 = QtGui.QHBoxLayout(self.no_entity_page)
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.no_entity_label = QtGui.QLabel(self.no_entity_page)
        self.no_entity_label.setStyleSheet("#no_entity_label {\n"
"font-size: 14pt;\n"
"border-style: dashed;\n"
"border-width: 2px;\n"
"border-radius: 3px;\n"
"}")
        self.no_entity_label.setAlignment(QtCore.Qt.AlignCenter)
        self.no_entity_label.setObjectName("no_entity_label")
        self.horizontalLayout_7.addWidget(self.no_entity_label)
        self.entity_pages.addWidget(self.no_entity_page)
        self.horizontalLayout_3.addWidget(self.entity_pages)
        self.verticalLayout_6.addWidget(self.work_area_frame)
        self.items_title_label_3 = QtGui.QLabel(WorkFilesForm)
        self.items_title_label_3.setMinimumSize(QtCore.QSize(0, 44))
        self.items_title_label_3.setStyleSheet("#items_title_label {\n"
"font-size: 14pt\n"
"}")
        self.items_title_label_3.setMargin(4)
        self.items_title_label_3.setObjectName("items_title_label_3")
        self.verticalLayout_6.addWidget(self.items_title_label_3)
        self.files_filter_frame = QtGui.QFrame(WorkFilesForm)
        self.files_filter_frame.setStyleSheet("#files_filter_frame {\n"
"border-style: solid;\n"
"border-radius: 2px;\n"
"border-width: 1px;\n"
"border-color: rgb(32,32,32);\n"
"}")
        self.files_filter_frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.files_filter_frame.setFrameShadow(QtGui.QFrame.Raised)
        self.files_filter_frame.setObjectName("files_filter_frame")
        self.verticalLayout = QtGui.QVBoxLayout(self.files_filter_frame)
        self.verticalLayout.setContentsMargins(6, 6, 6, 6)
        self.verticalLayout.setObjectName("verticalLayout")
        self.filter_combo = QtGui.QComboBox(self.files_filter_frame)
        self.filter_combo.setMinimumSize(QtCore.QSize(360, 0))
        self.filter_combo.setObjectName("filter_combo")
        self.verticalLayout.addWidget(self.filter_combo)
        self.horizontalLayout_8 = QtGui.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem2)
        self.show_in_fs_label = QtGui.QLabel(self.files_filter_frame)
        self.show_in_fs_label.setCursor(QtCore.Qt.PointingHandCursor)
        self.show_in_fs_label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.show_in_fs_label.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.show_in_fs_label.setObjectName("show_in_fs_label")
        self.horizontalLayout_8.addWidget(self.show_in_fs_label)
        self.verticalLayout.addLayout(self.horizontalLayout_8)
        self.verticalLayout_6.addWidget(self.files_filter_frame)
        spacerItem3 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_6.addItem(spacerItem3)
        self.verticalLayout_6.setStretch(4, 1)
        self.horizontalLayout.addLayout(self.verticalLayout_6)
        self.file_list = FileListView(WorkFilesForm)
        self.file_list.setStyleSheet("#file_list {\n"
"background-color: rgb(255, 128, 0);\n"
"}")
        self.file_list.setObjectName("file_list")
        self.horizontalLayout.addWidget(self.file_list)
        self.horizontalLayout.setStretch(1, 1)
        self.verticalLayout_8.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem4 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem4)
        self.new_file_btn = QtGui.QPushButton(WorkFilesForm)
        self.new_file_btn.setMinimumSize(QtCore.QSize(80, 0))
        self.new_file_btn.setObjectName("new_file_btn")
        self.horizontalLayout_2.addWidget(self.new_file_btn)
        self.open_file_btn = QtGui.QPushButton(WorkFilesForm)
        self.open_file_btn.setMinimumSize(QtCore.QSize(80, 0))
        self.open_file_btn.setObjectName("open_file_btn")
        self.horizontalLayout_2.addWidget(self.open_file_btn)
        self.verticalLayout_8.addLayout(self.horizontalLayout_2)

        self.retranslateUi(WorkFilesForm)
        self.entity_pages.setCurrentIndex(0)
        self.task_pages.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(WorkFilesForm)

    def retranslateUi(self, WorkFilesForm):
        WorkFilesForm.setWindowTitle(QtGui.QApplication.translate("WorkFilesForm", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.items_title_label_2.setText(QtGui.QApplication.translate("WorkFilesForm", "Select a Work Area", None, QtGui.QApplication.UnicodeUTF8))
        self.work_area_frame.setToolTip(QtGui.QApplication.translate("WorkFilesForm", "Click to Change Work Area...", None, QtGui.QApplication.UnicodeUTF8))
        self.entity_label.setText(QtGui.QApplication.translate("WorkFilesForm", "Shot:", None, QtGui.QApplication.UnicodeUTF8))
        self.task_label.setText(QtGui.QApplication.translate("WorkFilesForm", "Task:", None, QtGui.QApplication.UnicodeUTF8))
        self.no_task_label.setText(QtGui.QApplication.translate("WorkFilesForm", "Click to Select a Task", None, QtGui.QApplication.UnicodeUTF8))
        self.no_entity_label.setText(QtGui.QApplication.translate("WorkFilesForm", "Click to Select a Work Area", None, QtGui.QApplication.UnicodeUTF8))
        self.items_title_label_3.setText(QtGui.QApplication.translate("WorkFilesForm", "Choose Which Files to Display", None, QtGui.QApplication.UnicodeUTF8))
        self.show_in_fs_label.setText(QtGui.QApplication.translate("WorkFilesForm", "<html><head/><body><p><span style=\" text-decoration: underline;\">Show in File System</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.new_file_btn.setText(QtGui.QApplication.translate("WorkFilesForm", "New File", None, QtGui.QApplication.UnicodeUTF8))
        self.open_file_btn.setText(QtGui.QApplication.translate("WorkFilesForm", "Open File", None, QtGui.QApplication.UnicodeUTF8))

from ..file_list_view import FileListView
from . import resources_rc
