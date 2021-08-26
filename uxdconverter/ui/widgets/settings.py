# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'settings.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Settings(object):
    def setupUi(self, Settings):
        Settings.setObjectName("Settings")
        Settings.resize(640, 480)
        Settings.setWindowTitle("")
        self.gridLayout = QtWidgets.QGridLayout(Settings)
        self.gridLayout.setObjectName("gridLayout")
        self.gridLayout_5 = QtWidgets.QGridLayout()
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.groupBox = QtWidgets.QGroupBox(Settings)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setFieldGrowthPolicy(QtWidgets.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setObjectName("formLayout")
        self.label_wavelength = QtWidgets.QLabel(self.groupBox)
        self.label_wavelength.setObjectName("label_wavelength")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_wavelength)
        self.wavelength = QtWidgets.QLineEdit(self.groupBox)
        self.wavelength.setObjectName("wavelength")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.wavelength)
        self.label_beam_width = QtWidgets.QLabel(self.groupBox)
        self.label_beam_width.setObjectName("label_beam_width")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_beam_width)
        self.beam_width = QtWidgets.QLineEdit(self.groupBox)
        self.beam_width.setObjectName("beam_width")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.beam_width)
        self.label_sample_length = QtWidgets.QLabel(self.groupBox)
        self.label_sample_length.setObjectName("label_sample_length")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_sample_length)
        self.sample_length = QtWidgets.QLineEdit(self.groupBox)
        self.sample_length.setObjectName("sample_length")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.sample_length)
        self.label_knife_edge = QtWidgets.QLabel(self.groupBox)
        self.label_knife_edge.setObjectName("label_knife_edge")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_knife_edge)
        self.knige_edge = QtWidgets.QCheckBox(self.groupBox)
        self.knige_edge.setChecked(True)
        self.knige_edge.setObjectName("knige_edge")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.knige_edge)
        self.label_average_data = QtWidgets.QLabel(self.groupBox)
        self.label_average_data.setObjectName("label_average_data")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_average_data)
        self.average_data = QtWidgets.QCheckBox(self.groupBox)
        self.average_data.setObjectName("average_data")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.average_data)
        self.label_convert_qz = QtWidgets.QLabel(self.groupBox)
        self.label_convert_qz.setObjectName("label_convert_qz")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.label_convert_qz)
        self.convert_qz = QtWidgets.QCheckBox(self.groupBox)
        self.convert_qz.setChecked(True)
        self.convert_qz.setObjectName("convert_qz")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.convert_qz)
        self.label_cropping = QtWidgets.QLabel(self.groupBox)
        self.label_cropping.setObjectName("label_cropping")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.label_cropping)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.data_range_min = QtWidgets.QLineEdit(self.groupBox)
        self.data_range_min.setObjectName("data_range_min")
        self.horizontalLayout_4.addWidget(self.data_range_min)
        self.data_range_max = QtWidgets.QLineEdit(self.groupBox)
        self.data_range_max.setObjectName("data_range_max")
        self.horizontalLayout_4.addWidget(self.data_range_max)
        self.formLayout.setLayout(7, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout_4)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.formLayout.setItem(8, QtWidgets.QFormLayout.FieldRole, spacerItem)
        self.gridLayout_7.addLayout(self.formLayout, 0, 0, 1, 1)
        self.gridLayout_5.addWidget(self.groupBox, 0, 0, 1, 1)
        self.groupBox_8 = QtWidgets.QGroupBox(Settings)
        self.groupBox_8.setObjectName("groupBox_8")
        self.gridLayout_20 = QtWidgets.QGridLayout(self.groupBox_8)
        self.gridLayout_20.setObjectName("gridLayout_20")
        self.gridLayout_18 = QtWidgets.QGridLayout()
        self.gridLayout_18.setObjectName("gridLayout_18")
        self.label_wavelength_error = QtWidgets.QLabel(self.groupBox_8)
        self.label_wavelength_error.setObjectName("label_wavelength_error")
        self.gridLayout_18.addWidget(self.label_wavelength_error, 0, 1, 1, 1)
        self.wavelength_error = QtWidgets.QLineEdit(self.groupBox_8)
        self.wavelength_error.setObjectName("wavelength_error")
        self.gridLayout_18.addWidget(self.wavelength_error, 0, 2, 1, 1)
        self.label_theta_error = QtWidgets.QLabel(self.groupBox_8)
        self.label_theta_error.setObjectName("label_theta_error")
        self.gridLayout_18.addWidget(self.label_theta_error, 1, 1, 1, 1)
        self.theta_error = QtWidgets.QLineEdit(self.groupBox_8)
        self.theta_error.setObjectName("theta_error")
        self.gridLayout_18.addWidget(self.theta_error, 1, 2, 1, 1)
        self.gridLayout_20.addLayout(self.gridLayout_18, 0, 0, 1, 1)
        self.gridLayout_5.addWidget(self.groupBox_8, 2, 0, 1, 1)
        self.groupBox_2 = QtWidgets.QGroupBox(Settings)
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.normalization_max = QtWidgets.QRadioButton(self.groupBox_2)
        self.normalization_max.setObjectName("normalization_max")
        self.verticalLayout_3.addWidget(self.normalization_max)
        self.normalization_flank = QtWidgets.QRadioButton(self.groupBox_2)
        self.normalization_flank.setChecked(True)
        self.normalization_flank.setObjectName("normalization_flank")
        self.verticalLayout_3.addWidget(self.normalization_flank)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.normalization_manual = QtWidgets.QRadioButton(self.groupBox_2)
        self.normalization_manual.setObjectName("normalization_manual")
        self.horizontalLayout_3.addWidget(self.normalization_manual)
        self.normalization_factor = QtWidgets.QLineEdit(self.groupBox_2)
        self.normalization_factor.setObjectName("normalization_factor")
        self.horizontalLayout_3.addWidget(self.normalization_factor)
        self.verticalLayout_4.addLayout(self.horizontalLayout_3)
        self.pushbutton_select_graph = QtWidgets.QPushButton(self.groupBox_2)
        self.pushbutton_select_graph.setObjectName("pushbutton_select_graph")
        self.verticalLayout_4.addWidget(self.pushbutton_select_graph)
        self.verticalLayout_3.addLayout(self.verticalLayout_4)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem1)
        self.gridLayout_5.addWidget(self.groupBox_2, 0, 1, 1, 1)
        self.groupBox_7 = QtWidgets.QGroupBox(Settings)
        self.groupBox_7.setObjectName("groupBox_7")
        self.gridLayout_23 = QtWidgets.QGridLayout(self.groupBox_7)
        self.gridLayout_23.setObjectName("gridLayout_23")
        self.gridLayout_22 = QtWidgets.QGridLayout()
        self.gridLayout_22.setObjectName("gridLayout_22")
        self.label_plot_yaxis = QtWidgets.QLabel(self.groupBox_7)
        self.label_plot_yaxis.setObjectName("label_plot_yaxis")
        self.gridLayout_22.addWidget(self.label_plot_yaxis, 0, 0, 1, 1)
        self.plot_log_scale = QtWidgets.QCheckBox(self.groupBox_7)
        self.plot_log_scale.setChecked(True)
        self.plot_log_scale.setObjectName("plot_log_scale")
        self.gridLayout_22.addWidget(self.plot_log_scale, 0, 1, 1, 1)
        self.gridLayout_23.addLayout(self.gridLayout_22, 0, 0, 1, 1)
        self.gridLayout_5.addWidget(self.groupBox_7, 2, 1, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_5, 0, 0, 1, 1)

        self.retranslateUi(Settings)
        QtCore.QMetaObject.connectSlotsByName(Settings)

    def retranslateUi(self, Settings):
        _translate = QtCore.QCoreApplication.translate
        self.groupBox.setTitle(_translate("Settings", "Measurement Context"))
        self.label_wavelength.setText(_translate("Settings", "<html><head/><body><p>X-Ray wavelength [&#8491;]</p></body></html>"))
        self.wavelength.setText(_translate("Settings", "1.54186"))
        self.label_beam_width.setText(_translate("Settings", "X-Ray beam width [mm]"))
        self.beam_width.setText(_translate("Settings", "0,1"))
        self.label_sample_length.setText(_translate("Settings", "Sample length [mm]"))
        self.sample_length.setText(_translate("Settings", "20,0"))
        self.label_knife_edge.setText(_translate("Settings", "Knife Edge"))
        self.knige_edge.setToolTip(_translate("Settings", "Was the measurement carried out with a knife edge?"))
        self.knige_edge.setText(_translate("Settings", "Enabled"))
        self.label_average_data.setText(_translate("Settings", "Average overlapping data"))
        self.average_data.setToolTip(_translate("Settings", "Average data on overlapping regions"))
        self.average_data.setText(_translate("Settings", "Enabled"))
        self.label_convert_qz.setText(_translate("Settings", "Convert to Qz"))
        self.convert_qz.setText(_translate("Settings", "Enabled"))
        self.label_cropping.setText(_translate("Settings", "<html><head/><body><p>Qz range [&#8491;⁻1]</p></body></html>"))
        self.data_range_min.setText(_translate("Settings", "0,01"))
        self.data_range_max.setText(_translate("Settings", "0,5"))
        self.groupBox_8.setTitle(_translate("Settings", "Errors"))
        self.label_wavelength_error.setText(_translate("Settings", "<html><head/><body><p>Error wavelength [&#8491;]</p></body></html>"))
        self.wavelength_error.setText(_translate("Settings", "1,0e-3"))
        self.label_theta_error.setText(_translate("Settings", "<html><head/><body><p>Error theta [deg]</p></body></html>"))
        self.theta_error.setText(_translate("Settings", "1.379388e-2"))
        self.groupBox_2.setTitle(_translate("Settings", "Normalization"))
        self.normalization_max.setToolTip(_translate("Settings", "Normalize the maximal counts per second to 1"))
        self.normalization_max.setText(_translate("Settings", "maximum"))
        self.normalization_flank.setToolTip(_translate("Settings", "Normalize the point with the lowest absolute slope to one. Only points left to the first flank are considered"))
        self.normalization_flank.setText(_translate("Settings", "first flank and derivative"))
        self.normalization_manual.setToolTip(_translate("Settings", "Normalize all points using the given scaling factor"))
        self.normalization_manual.setText(_translate("Settings", "manual"))
        self.normalization_factor.setText(_translate("Settings", "1,0"))
        self.pushbutton_select_graph.setToolTip(_translate("Settings", "Select a scaling factor from graph. Click on graph and press \'x\' button or double click"))
        self.pushbutton_select_graph.setText(_translate("Settings", "Select from graph"))
        self.groupBox_7.setTitle(_translate("Settings", "Plotting settings"))
        self.label_plot_yaxis.setText(_translate("Settings", "log y - Axis"))
        self.plot_log_scale.setText(_translate("Settings", "Enabled"))