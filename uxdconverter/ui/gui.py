# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_UXDConverter(object):
    def setupUi(self, UXDConverter):
        UXDConverter.setObjectName("UXDConverter")
        UXDConverter.resize(640, 476)
        UXDConverter.setMinimumSize(QtCore.QSize(640, 476))
        self.centralwidget = QtWidgets.QWidget(UXDConverter)
        self.centralwidget.setMinimumSize(QtCore.QSize(640, 476))
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout_2.addLayout(self.gridLayout)
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setEnabled(True)
        self.tabWidget.setTabPosition(QtWidgets.QTabWidget.North)
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tabWidget.setObjectName("tabWidget")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.gridLayout_9 = QtWidgets.QGridLayout(self.tab_3)
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_2 = QtWidgets.QLabel(self.tab_3)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_5.addWidget(self.label_2)
        self.lineEdit_output = QtWidgets.QLineEdit(self.tab_3)
        self.lineEdit_output.setObjectName("lineEdit_output")
        self.horizontalLayout_5.addWidget(self.lineEdit_output)
        self.pushButton_output = QtWidgets.QPushButton(self.tab_3)
        self.pushButton_output.setObjectName("pushButton_output")
        self.horizontalLayout_5.addWidget(self.pushButton_output)
        self.gridLayout_9.addLayout(self.horizontalLayout_5, 7, 0, 1, 1)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label = QtWidgets.QLabel(self.tab_3)
        self.label.setObjectName("label")
        self.horizontalLayout_6.addWidget(self.label)
        self.lineEdit_input = QtWidgets.QLineEdit(self.tab_3)
        self.lineEdit_input.setDragEnabled(False)
        self.lineEdit_input.setObjectName("lineEdit_input")
        self.horizontalLayout_6.addWidget(self.lineEdit_input)
        self.pushButton_input = QtWidgets.QPushButton(self.tab_3)
        self.pushButton_input.setCheckable(False)
        self.pushButton_input.setFlat(False)
        self.pushButton_input.setObjectName("pushButton_input")
        self.horizontalLayout_6.addWidget(self.pushButton_input)
        self.pushButton_addfile = QtWidgets.QPushButton(self.tab_3)
        self.pushButton_addfile.setObjectName("pushButton_addfile")
        self.horizontalLayout_6.addWidget(self.pushButton_addfile)
        self.gridLayout_9.addLayout(self.horizontalLayout_6, 0, 0, 1, 1)
        self.gridLayout_8 = QtWidgets.QGridLayout()
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.treeWidget_file = QtWidgets.QTreeWidget(self.tab_3)
        self.treeWidget_file.setToolTip("")
        self.treeWidget_file.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.treeWidget_file.setObjectName("treeWidget_file")
        self.treeWidget_file.headerItem().setText(0, "1")
        self.treeWidget_file.header().setVisible(False)
        self.gridLayout_8.addWidget(self.treeWidget_file, 0, 0, 1, 1)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.pushButton_deletefile = QtWidgets.QPushButton(self.tab_3)
        self.pushButton_deletefile.setObjectName("pushButton_deletefile")
        self.horizontalLayout_7.addWidget(self.pushButton_deletefile)
        self.pushButton_resetfile = QtWidgets.QPushButton(self.tab_3)
        self.pushButton_resetfile.setObjectName("pushButton_resetfile")
        self.horizontalLayout_7.addWidget(self.pushButton_resetfile)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem)
        self.gridLayout_8.addLayout(self.horizontalLayout_7, 2, 0, 1, 1)
        self.gridLayout_9.addLayout(self.gridLayout_8, 6, 0, 1, 1)
        self.tabWidget.addTab(self.tab_3, "")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.tab)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.measurements = QtWidgets.QTreeWidget(self.tab)
        self.measurements.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.measurements.setRootIsDecorated(True)
        self.measurements.setColumnCount(2)
        self.measurements.setObjectName("measurements")
        self.measurements.header().setVisible(False)
        self.measurements.header().setCascadingSectionResizes(True)
        self.measurements.header().setHighlightSections(False)
        self.measurements.header().setMinimumSectionSize(100)
        self.measurements.header().setSortIndicatorShown(True)
        self.measurements.header().setStretchLastSection(False)
        self.gridLayout_3.addWidget(self.measurements, 0, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.pushButton_plot = QtWidgets.QPushButton(self.tab)
        self.pushButton_plot.setObjectName("pushButton_plot")
        self.horizontalLayout.addWidget(self.pushButton_plot)
        self.gridLayout_3.addLayout(self.horizontalLayout, 1, 0, 1, 1)
        self.gridLayout_4.addLayout(self.gridLayout_3, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setEnabled(True)
        self.tab_2.setObjectName("tab_2")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.tab_2)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.gridLayout_5 = QtWidgets.QGridLayout()
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.groupBox = QtWidgets.QGroupBox(self.tab_2)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.label_5 = QtWidgets.QLabel(self.groupBox)
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.label_6 = QtWidgets.QLabel(self.groupBox)
        self.label_6.setObjectName("label_6")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_6)
        self.lineEdit_wavelength = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_wavelength.setObjectName("lineEdit_wavelength")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lineEdit_wavelength)
        self.lineEdit_beam_width = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_beam_width.setObjectName("lineEdit_beam_width")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.lineEdit_beam_width)
        self.checkBox_knifeedge = QtWidgets.QCheckBox(self.groupBox)
        self.checkBox_knifeedge.setChecked(True)
        self.checkBox_knifeedge.setObjectName("checkBox_knifeedge")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.checkBox_knifeedge)
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.lineEdit_sample_length = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_sample_length.setObjectName("lineEdit_sample_length")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.lineEdit_sample_length)
        self.label_7 = QtWidgets.QLabel(self.groupBox)
        self.label_7.setObjectName("label_7")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_7)
        self.checkbox_average = QtWidgets.QCheckBox(self.groupBox)
        self.checkbox_average.setObjectName("checkbox_average")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.checkbox_average)
        self.label_cropping = QtWidgets.QLabel(self.groupBox)
        self.label_cropping.setObjectName("label_cropping")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.label_cropping)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.lineEdit_qz_range_min = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_qz_range_min.setObjectName("lineEdit_qz_range_min")
        self.horizontalLayout_4.addWidget(self.lineEdit_qz_range_min)
        self.lineEdit_qz_range_max = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_qz_range_max.setObjectName("lineEdit_qz_range_max")
        self.horizontalLayout_4.addWidget(self.lineEdit_qz_range_max)
        self.formLayout.setLayout(7, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout_4)
        self.label_9 = QtWidgets.QLabel(self.groupBox)
        self.label_9.setObjectName("label_9")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.label_9)
        self.checkBox_convert_qz = QtWidgets.QCheckBox(self.groupBox)
        self.checkBox_convert_qz.setChecked(True)
        self.checkBox_convert_qz.setObjectName("checkBox_convert_qz")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.checkBox_convert_qz)
        self.gridLayout_7.addLayout(self.formLayout, 0, 0, 1, 1)
        self.gridLayout_5.addWidget(self.groupBox, 0, 0, 1, 1)
        self.groupBox_2 = QtWidgets.QGroupBox(self.tab_2)
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.radioButton_maximum = QtWidgets.QRadioButton(self.groupBox_2)
        self.radioButton_maximum.setObjectName("radioButton_maximum")
        self.verticalLayout_3.addWidget(self.radioButton_maximum)
        self.radioButton_flank = QtWidgets.QRadioButton(self.groupBox_2)
        self.radioButton_flank.setChecked(True)
        self.radioButton_flank.setObjectName("radioButton_flank")
        self.verticalLayout_3.addWidget(self.radioButton_flank)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.radioButton_manual = QtWidgets.QRadioButton(self.groupBox_2)
        self.radioButton_manual.setObjectName("radioButton_manual")
        self.horizontalLayout_3.addWidget(self.radioButton_manual)
        self.lineEdit_normalization_factor = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_normalization_factor.setObjectName("lineEdit_normalization_factor")
        self.horizontalLayout_3.addWidget(self.lineEdit_normalization_factor)
        self.verticalLayout_4.addLayout(self.horizontalLayout_3)
        self.pushbutton_select_graph = QtWidgets.QPushButton(self.groupBox_2)
        self.pushbutton_select_graph.setObjectName("pushbutton_select_graph")
        self.verticalLayout_4.addWidget(self.pushbutton_select_graph)
        self.verticalLayout_3.addLayout(self.verticalLayout_4)
        self.gridLayout_5.addWidget(self.groupBox_2, 0, 1, 1, 1)
        self.gridLayout_6.addLayout(self.gridLayout_5, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.gridLayout_13 = QtWidgets.QGridLayout(self.tab_4)
        self.gridLayout_13.setObjectName("gridLayout_13")
        self.gridLayout_12 = QtWidgets.QGridLayout()
        self.gridLayout_12.setObjectName("gridLayout_12")
        self.groupBox_3 = QtWidgets.QGroupBox(self.tab_4)
        self.groupBox_3.setObjectName("groupBox_3")
        self.gridLayout_11 = QtWidgets.QGridLayout(self.groupBox_3)
        self.gridLayout_11.setObjectName("gridLayout_11")
        self.gridLayout_10 = QtWidgets.QGridLayout()
        self.gridLayout_10.setObjectName("gridLayout_10")
        self.conversion_to_qz = QtWidgets.QRadioButton(self.groupBox_3)
        self.conversion_to_qz.setObjectName("conversion_to_qz")
        self.gridLayout_10.addWidget(self.conversion_to_qz, 0, 0, 1, 1)
        self.conversion_input_qz = QtWidgets.QLineEdit(self.groupBox_3)
        self.conversion_input_qz.setMaximumSize(QtCore.QSize(150, 16777215))
        self.conversion_input_qz.setMaxLength(10)
        self.conversion_input_qz.setObjectName("conversion_input_qz")
        self.gridLayout_10.addWidget(self.conversion_input_qz, 0, 2, 1, 1)
        self.conversion_to_theta = QtWidgets.QRadioButton(self.groupBox_3)
        self.conversion_to_theta.setObjectName("conversion_to_theta")
        self.gridLayout_10.addWidget(self.conversion_to_theta, 1, 0, 1, 1)
        self.conversion_input_theta = QtWidgets.QLineEdit(self.groupBox_3)
        self.conversion_input_theta.setMaximumSize(QtCore.QSize(150, 16777215))
        self.conversion_input_theta.setMaxLength(10)
        self.conversion_input_theta.setObjectName("conversion_input_theta")
        self.gridLayout_10.addWidget(self.conversion_input_theta, 1, 2, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_10.addItem(spacerItem2, 1, 3, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_10.addItem(spacerItem3, 0, 3, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(30, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_10.addItem(spacerItem4, 1, 1, 1, 1)
        self.gridLayout_11.addLayout(self.gridLayout_10, 0, 0, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_11.addItem(spacerItem5, 1, 0, 1, 1)
        self.gridLayout_12.addWidget(self.groupBox_3, 0, 0, 1, 1)
        self.gridLayout_13.addLayout(self.gridLayout_12, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab_4, "")
        self.tab_xrd = QtWidgets.QWidget()
        self.tab_xrd.setObjectName("tab_xrd")
        self.gridLayout_15 = QtWidgets.QGridLayout(self.tab_xrd)
        self.gridLayout_15.setObjectName("gridLayout_15")
        self.groupBox_5 = QtWidgets.QGroupBox(self.tab_xrd)
        self.groupBox_5.setObjectName("groupBox_5")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout(self.groupBox_5)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.label_10 = QtWidgets.QLabel(self.groupBox_5)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_10.addWidget(self.label_10)
        self.cif_file = QtWidgets.QLineEdit(self.groupBox_5)
        self.cif_file.setObjectName("cif_file")
        self.horizontalLayout_10.addWidget(self.cif_file)
        self.cif_browse = QtWidgets.QPushButton(self.groupBox_5)
        self.cif_browse.setObjectName("cif_browse")
        self.horizontalLayout_10.addWidget(self.cif_browse)
        self.cif_import = QtWidgets.QPushButton(self.groupBox_5)
        self.cif_import.setObjectName("cif_import")
        self.horizontalLayout_10.addWidget(self.cif_import)
        self.horizontalLayout_11.addLayout(self.horizontalLayout_10)
        self.gridLayout_15.addWidget(self.groupBox_5, 0, 0, 1, 1)
        self.gridLayout_14 = QtWidgets.QGridLayout()
        self.gridLayout_14.setObjectName("gridLayout_14")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_8 = QtWidgets.QLabel(self.tab_xrd)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_8.addWidget(self.label_8)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem6)
        self.combobox_crystalfamily = QtWidgets.QComboBox(self.tab_xrd)
        self.combobox_crystalfamily.setEditable(False)
        self.combobox_crystalfamily.setObjectName("combobox_crystalfamily")
        self.combobox_crystalfamily.addItem("")
        self.combobox_crystalfamily.addItem("")
        self.combobox_crystalfamily.addItem("")
        self.combobox_crystalfamily.addItem("")
        self.combobox_crystalfamily.addItem("")
        self.combobox_crystalfamily.addItem("")
        self.combobox_crystalfamily.addItem("")
        self.horizontalLayout_8.addWidget(self.combobox_crystalfamily)
        self.button_calculate_bragg = QtWidgets.QPushButton(self.tab_xrd)
        self.button_calculate_bragg.setObjectName("button_calculate_bragg")
        self.horizontalLayout_8.addWidget(self.button_calculate_bragg)
        self.gridLayout_14.addLayout(self.horizontalLayout_8, 7, 0, 1, 1)
        self.gridLayout_15.addLayout(self.gridLayout_14, 1, 0, 1, 1)
        self.groupBox_4 = QtWidgets.QGroupBox(self.tab_xrd)
        self.groupBox_4.setObjectName("groupBox_4")
        self.gridLayout_17 = QtWidgets.QGridLayout(self.groupBox_4)
        self.gridLayout_17.setObjectName("gridLayout_17")
        self.gridLayout_16 = QtWidgets.QGridLayout()
        self.gridLayout_16.setObjectName("gridLayout_16")
        self.lattice_b = QtWidgets.QLineEdit(self.groupBox_4)
        self.lattice_b.setMaximumSize(QtCore.QSize(100, 16777215))
        self.lattice_b.setMaxLength(8)
        self.lattice_b.setReadOnly(True)
        self.lattice_b.setObjectName("lattice_b")
        self.gridLayout_16.addWidget(self.lattice_b, 0, 3, 1, 1)
        self.lattice_param_a = QtWidgets.QLabel(self.groupBox_4)
        self.lattice_param_a.setAlignment(QtCore.Qt.AlignCenter)
        self.lattice_param_a.setObjectName("lattice_param_a")
        self.gridLayout_16.addWidget(self.lattice_param_a, 0, 0, 1, 1)
        self.lattice_param_b = QtWidgets.QLabel(self.groupBox_4)
        self.lattice_param_b.setAlignment(QtCore.Qt.AlignCenter)
        self.lattice_param_b.setObjectName("lattice_param_b")
        self.gridLayout_16.addWidget(self.lattice_param_b, 0, 2, 1, 1)
        self.lattice_c = QtWidgets.QLineEdit(self.groupBox_4)
        self.lattice_c.setMaximumSize(QtCore.QSize(100, 16777215))
        self.lattice_c.setMaxLength(8)
        self.lattice_c.setReadOnly(True)
        self.lattice_c.setObjectName("lattice_c")
        self.gridLayout_16.addWidget(self.lattice_c, 0, 5, 1, 1)
        self.lattice_param_c = QtWidgets.QLabel(self.groupBox_4)
        self.lattice_param_c.setAlignment(QtCore.Qt.AlignCenter)
        self.lattice_param_c.setObjectName("lattice_param_c")
        self.gridLayout_16.addWidget(self.lattice_param_c, 0, 4, 1, 1)
        self.lattice_a = QtWidgets.QLineEdit(self.groupBox_4)
        self.lattice_a.setMaximumSize(QtCore.QSize(100, 16777215))
        self.lattice_a.setMaxLength(8)
        self.lattice_a.setObjectName("lattice_a")
        self.gridLayout_16.addWidget(self.lattice_a, 0, 1, 1, 1)
        self.lattice_param_alpha = QtWidgets.QLabel(self.groupBox_4)
        self.lattice_param_alpha.setAlignment(QtCore.Qt.AlignCenter)
        self.lattice_param_alpha.setObjectName("lattice_param_alpha")
        self.gridLayout_16.addWidget(self.lattice_param_alpha, 1, 0, 1, 1)
        self.lattice_alpha = QtWidgets.QLineEdit(self.groupBox_4)
        self.lattice_alpha.setMaximumSize(QtCore.QSize(100, 16777215))
        self.lattice_alpha.setMaxLength(8)
        self.lattice_alpha.setReadOnly(True)
        self.lattice_alpha.setObjectName("lattice_alpha")
        self.gridLayout_16.addWidget(self.lattice_alpha, 1, 1, 1, 1)
        self.lattice_beta = QtWidgets.QLineEdit(self.groupBox_4)
        self.lattice_beta.setMaximumSize(QtCore.QSize(100, 16777215))
        self.lattice_beta.setMaxLength(8)
        self.lattice_beta.setReadOnly(True)
        self.lattice_beta.setObjectName("lattice_beta")
        self.gridLayout_16.addWidget(self.lattice_beta, 1, 3, 1, 1)
        self.lattice_gamma = QtWidgets.QLineEdit(self.groupBox_4)
        self.lattice_gamma.setMaximumSize(QtCore.QSize(100, 16777215))
        self.lattice_gamma.setMaxLength(8)
        self.lattice_gamma.setReadOnly(True)
        self.lattice_gamma.setObjectName("lattice_gamma")
        self.gridLayout_16.addWidget(self.lattice_gamma, 1, 5, 1, 1)
        self.lattice_param_beta = QtWidgets.QLabel(self.groupBox_4)
        self.lattice_param_beta.setAlignment(QtCore.Qt.AlignCenter)
        self.lattice_param_beta.setObjectName("lattice_param_beta")
        self.gridLayout_16.addWidget(self.lattice_param_beta, 1, 2, 1, 1)
        self.lattice_param_gamma = QtWidgets.QLabel(self.groupBox_4)
        self.lattice_param_gamma.setAlignment(QtCore.Qt.AlignCenter)
        self.lattice_param_gamma.setObjectName("lattice_param_gamma")
        self.gridLayout_16.addWidget(self.lattice_param_gamma, 1, 4, 1, 1)
        self.gridLayout_17.addLayout(self.gridLayout_16, 0, 0, 1, 1)
        self.gridLayout_15.addWidget(self.groupBox_4, 3, 0, 1, 1)
        self.groupBox_6 = QtWidgets.QGroupBox(self.tab_xrd)
        self.groupBox_6.setObjectName("groupBox_6")
        self.gridLayout_19 = QtWidgets.QGridLayout(self.groupBox_6)
        self.gridLayout_19.setObjectName("gridLayout_19")
        self.bragg_table = QtWidgets.QTableWidget(self.groupBox_6)
        self.bragg_table.setCornerButtonEnabled(True)
        self.bragg_table.setObjectName("bragg_table")
        self.bragg_table.setColumnCount(3)
        self.bragg_table.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.bragg_table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.bragg_table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.bragg_table.setHorizontalHeaderItem(2, item)
        self.bragg_table.horizontalHeader().setVisible(False)
        self.bragg_table.horizontalHeader().setDefaultSectionSize(85)
        self.bragg_table.verticalHeader().setVisible(False)
        self.gridLayout_19.addWidget(self.bragg_table, 1, 0, 1, 1)
        self.bragg_table_2 = QtWidgets.QTableWidget(self.groupBox_6)
        self.bragg_table_2.setCornerButtonEnabled(True)
        self.bragg_table_2.setObjectName("bragg_table_2")
        self.bragg_table_2.setColumnCount(3)
        self.bragg_table_2.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.bragg_table_2.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.bragg_table_2.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.bragg_table_2.setHorizontalHeaderItem(2, item)
        self.bragg_table_2.horizontalHeader().setVisible(False)
        self.bragg_table_2.horizontalHeader().setDefaultSectionSize(85)
        self.bragg_table_2.verticalHeader().setVisible(False)
        self.gridLayout_19.addWidget(self.bragg_table_2, 1, 1, 1, 1)
        self.gridLayout_15.addWidget(self.groupBox_6, 10, 0, 1, 1)
        self.tabWidget.addTab(self.tab_xrd, "")
        self.verticalLayout_2.addWidget(self.tabWidget, 0, QtCore.Qt.AlignLeft)
        self.verticalLayout.addLayout(self.verticalLayout_2)
        self.gridLayout_2.addLayout(self.verticalLayout, 0, 0, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pushButton_convert = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_convert.setObjectName("pushButton_convert")
        self.horizontalLayout_2.addWidget(self.pushButton_convert)
        self.checkBox_view_plot = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_view_plot.setChecked(True)
        self.checkBox_view_plot.setObjectName("checkBox_view_plot")
        self.horizontalLayout_2.addWidget(self.checkBox_view_plot)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem7)
        self.pushButton_preview = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_preview.setObjectName("pushButton_preview")
        self.horizontalLayout_2.addWidget(self.pushButton_preview)
        self.gridLayout_2.addLayout(self.horizontalLayout_2, 1, 0, 1, 1)
        UXDConverter.setCentralWidget(self.centralwidget)

        self.retranslateUi(UXDConverter)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(UXDConverter)

    def retranslateUi(self, UXDConverter):
        _translate = QtCore.QCoreApplication.translate
        UXDConverter.setWindowTitle(_translate("UXDConverter", "UXDConverter"))
        self.label_2.setText(_translate("UXDConverter", "Output file"))
        self.pushButton_output.setText(_translate("UXDConverter", "Browse"))
        self.label.setText(_translate("UXDConverter", "Add file"))
        self.pushButton_input.setText(_translate("UXDConverter", "Browse"))
        self.pushButton_addfile.setToolTip(_translate("UXDConverter", "Add a file to the file list"))
        self.pushButton_addfile.setText(_translate("UXDConverter", "Add file"))
        self.pushButton_deletefile.setToolTip(_translate("UXDConverter", "Delete the selected files from file list"))
        self.pushButton_deletefile.setText(_translate("UXDConverter", "Delete selected file"))
        self.pushButton_resetfile.setToolTip(_translate("UXDConverter", "Reset the file list"))
        self.pushButton_resetfile.setText(_translate("UXDConverter", "Reset files"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("UXDConverter", "File"))
        self.measurements.headerItem().setText(0, _translate("UXDConverter", "asd"))
        self.measurements.headerItem().setText(1, _translate("UXDConverter", "2"))
        self.pushButton_plot.setToolTip(_translate("UXDConverter", "Plot the selected measurements in a theta-intensity graph"))
        self.pushButton_plot.setText(_translate("UXDConverter", "Plot selected measurements"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("UXDConverter", "Measurement"))
        self.groupBox.setTitle(_translate("UXDConverter", "Measurement Context"))
        self.label_4.setText(_translate("UXDConverter", "<html><head/><body><p>X-Ray wavelength [&#8491;]</p></body></html>"))
        self.label_5.setText(_translate("UXDConverter", "X-Ray beam width [mm]"))
        self.label_6.setText(_translate("UXDConverter", "Knife Edge"))
        self.lineEdit_wavelength.setText(_translate("UXDConverter", "1,5418"))
        self.lineEdit_beam_width.setText(_translate("UXDConverter", "0,1"))
        self.checkBox_knifeedge.setToolTip(_translate("UXDConverter", "Was the measurement carried out with a knife edge?"))
        self.checkBox_knifeedge.setText(_translate("UXDConverter", "Enabled"))
        self.label_3.setText(_translate("UXDConverter", "Sample length [mm]"))
        self.lineEdit_sample_length.setText(_translate("UXDConverter", "20,0"))
        self.label_7.setText(_translate("UXDConverter", "Average overlapping data"))
        self.checkbox_average.setToolTip(_translate("UXDConverter", "Average data on overlapping regions"))
        self.checkbox_average.setText(_translate("UXDConverter", "Enabled"))
        self.label_cropping.setText(_translate("UXDConverter", "<html><head/><body><p>Qz range [&#8491;⁻1]</p></body></html>"))
        self.lineEdit_qz_range_min.setText(_translate("UXDConverter", "0,01"))
        self.lineEdit_qz_range_max.setText(_translate("UXDConverter", "0,5"))
        self.label_9.setText(_translate("UXDConverter", "Convert to Qz"))
        self.checkBox_convert_qz.setText(_translate("UXDConverter", "Enabled"))
        self.groupBox_2.setTitle(_translate("UXDConverter", "Normalization"))
        self.radioButton_maximum.setToolTip(_translate("UXDConverter", "Normalize the maximal counts per second to 1"))
        self.radioButton_maximum.setText(_translate("UXDConverter", "maximum"))
        self.radioButton_flank.setToolTip(_translate("UXDConverter", "Normalize the point with the lowest absolute slope to one. Only points left to the first flank are considered"))
        self.radioButton_flank.setText(_translate("UXDConverter", "first flank and derivative"))
        self.radioButton_manual.setToolTip(_translate("UXDConverter", "Normalize all points using the given scaling factor"))
        self.radioButton_manual.setText(_translate("UXDConverter", "manual"))
        self.lineEdit_normalization_factor.setText(_translate("UXDConverter", "1,0"))
        self.pushbutton_select_graph.setToolTip(_translate("UXDConverter", "Select a scaling factor from graph. Click on graph and press \'x\' button or double click"))
        self.pushbutton_select_graph.setText(_translate("UXDConverter", "Select from graph"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("UXDConverter", "Settings"))
        self.groupBox_3.setTitle(_translate("UXDConverter", "Scattering vector conversions"))
        self.conversion_to_qz.setText(_translate("UXDConverter", "Qz [A⁻1]"))
        self.conversion_input_qz.setText(_translate("UXDConverter", "0.1"))
        self.conversion_to_theta.setText(_translate("UXDConverter", "Theta [deg]"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("UXDConverter", "Conversions"))
        self.groupBox_5.setTitle(_translate("UXDConverter", "Import from .cif"))
        self.label_10.setText(_translate("UXDConverter", "File"))
        self.cif_file.setToolTip(_translate("UXDConverter", ".cif file to import lattice parameters from"))
        self.cif_browse.setToolTip(_translate("UXDConverter", "Browse for a .cif file"))
        self.cif_browse.setText(_translate("UXDConverter", "Browse"))
        self.cif_import.setToolTip(_translate("UXDConverter", "Import the selected file"))
        self.cif_import.setText(_translate("UXDConverter", "Import"))
        self.label_8.setText(_translate("UXDConverter", "Crystal family"))
        self.combobox_crystalfamily.setToolTip(_translate("UXDConverter", "Crystal family of the compound"))
        self.combobox_crystalfamily.setItemText(0, _translate("UXDConverter", "cubic"))
        self.combobox_crystalfamily.setItemText(1, _translate("UXDConverter", "hexagonal"))
        self.combobox_crystalfamily.setItemText(2, _translate("UXDConverter", "rhombohedral"))
        self.combobox_crystalfamily.setItemText(3, _translate("UXDConverter", "tetragonal"))
        self.combobox_crystalfamily.setItemText(4, _translate("UXDConverter", "orthorhombic"))
        self.combobox_crystalfamily.setItemText(5, _translate("UXDConverter", "monoclinic"))
        self.combobox_crystalfamily.setItemText(6, _translate("UXDConverter", "triclinic"))
        self.button_calculate_bragg.setToolTip(_translate("UXDConverter", "Calculate the Bragg peaks from the crystal family and the lattice parameters"))
        self.button_calculate_bragg.setText(_translate("UXDConverter", "Calculate Bragg Peaks"))
        self.groupBox_4.setTitle(_translate("UXDConverter", "Lattice parameter"))
        self.lattice_b.setToolTip(_translate("UXDConverter", "lattice parameter b in angstrom"))
        self.lattice_param_a.setText(_translate("UXDConverter", "<html><head/><body>a [&#8491;]</body></html>"))
        self.lattice_param_b.setText(_translate("UXDConverter", "<html><head/><body>b [&#8491;]</body></html>"))
        self.lattice_c.setToolTip(_translate("UXDConverter", "lattice parameter c in angstrom"))
        self.lattice_param_c.setText(_translate("UXDConverter", "<html><head/><body>c [&#8491;]</body></html>"))
        self.lattice_a.setToolTip(_translate("UXDConverter", "lattice parameter a in angstrom"))
        self.lattice_a.setText(_translate("UXDConverter", "5,431"))
        self.lattice_param_alpha.setText(_translate("UXDConverter", "<html><head/><body><p>&alpha; [deg]</p></body></html>"))
        self.lattice_alpha.setToolTip(_translate("UXDConverter", "lattice parameter alpha in degrees"))
        self.lattice_alpha.setText(_translate("UXDConverter", "90"))
        self.lattice_beta.setToolTip(_translate("UXDConverter", "lattice parameter beta in degrees"))
        self.lattice_gamma.setToolTip(_translate("UXDConverter", "lattice parameter gamma in degrees"))
        self.lattice_param_beta.setText(_translate("UXDConverter", "<html><head/><body><p>&beta; [deg]</p></body></html>"))
        self.lattice_param_gamma.setText(_translate("UXDConverter", "<html><head/><body><p>&gamma; [deg]</p></body></html>"))
        self.groupBox_6.setTitle(_translate("UXDConverter", "Bragg Condition"))
        item = self.bragg_table.horizontalHeaderItem(0)
        item.setText(_translate("UXDConverter", "hkl"))
        item = self.bragg_table.horizontalHeaderItem(1)
        item.setText(_translate("UXDConverter", "theta"))
        item = self.bragg_table.horizontalHeaderItem(2)
        item.setText(_translate("UXDConverter", "2 theta"))
        item = self.bragg_table_2.horizontalHeaderItem(0)
        item.setText(_translate("UXDConverter", "hkl"))
        item = self.bragg_table_2.horizontalHeaderItem(1)
        item.setText(_translate("UXDConverter", "theta"))
        item = self.bragg_table_2.horizontalHeaderItem(2)
        item.setText(_translate("UXDConverter", "2 theta"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_xrd), _translate("UXDConverter", "XRD"))
        self.pushButton_convert.setToolTip(_translate("UXDConverter", "Convert the measurements and save into output file"))
        self.pushButton_convert.setText(_translate("UXDConverter", "Convert"))
        self.checkBox_view_plot.setText(_translate("UXDConverter", "Plot after Conversion"))
        self.pushButton_preview.setToolTip(_translate("UXDConverter", "Preview the conversion"))
        self.pushButton_preview.setText(_translate("UXDConverter", "Preview"))
