__author__ = 'Po'

"""
Python conversion of the QtPropertyBrowser "demo" example.

"""

if __name__ == '__main__':
	from PyQt4 import QtCore, QtGui, Qt
	from PyQt4.QtPropertyBrowser import *
	import sys

	app = QtGui.QApplication(sys.argv)

	w = QtGui.QWidget()

	boolManager = QtBoolPropertyManager(w)
	intManager = QtIntPropertyManager(w)
	stringManager = QtStringPropertyManager(w)
	sizeManager = QtSizePropertyManager(w)
	rectManager = QtRectPropertyManager(w)
	sizePolicyManager = QtSizePolicyPropertyManager(w)
	enumManager = QtEnumPropertyManager(w)
	groupManager = QtGroupPropertyManager(w)

	item0 = groupManager.addProperty('QObject')

	item1 = stringManager.addProperty('objectName')
	item0.addSubProperty(item1)

	item2 = boolManager.addProperty('enabled')
	item0.addSubProperty(item2)

	item3 = rectManager.addProperty('geometry')
	item0.addSubProperty(item3)

	item4 = sizePolicyManager.addProperty('sizePolicy')
	item0.addSubProperty(item4)

	item5 = sizeManager.addProperty('sizeIncrement')
	item0.addSubProperty(item5)

	item7 = boolManager.addProperty('mouseTracking')
	item0.addSubProperty(item7)

	item8 = enumManager.addProperty('direction')
	enumNames = QtCore.QStringList()
	enumNames << 'Up' << 'Right' << 'Down' << 'Left'
	enumManager.setEnumNames(item8, enumNames)

	enumIcons = dict()
	enumIcons[0] = QtGui.QIcon(':/demo/images/up.png')
	enumIcons[1] = QtGui.QIcon(':/demo/images/right.png')
	enumIcons[2] = QtGui.QIcon(':/demo/images/down.png')
	enumIcons[3] = QtGui.QIcon(':/demo/images/left.png')
	enumManager.setEnumIcons(item8, enumIcons)
	item2.addSubProperty(item8)

	item9 = intManager.addProperty('value')
	intManager.setRange(item9, -100, 100)
	item0.addSubProperty(item9)

	checkBoxFactory = QtCheckBoxFactory(w)
	spinBoxFactory = QtSpinBoxFactory(w)
	sliderFactory = QtSliderFactory(w)
	scrollBarFactory = QtScrollBarFactory(w)
	lineEditFactory = QtLineEditFactory(w)
	comboBoxFactory = QtEnumEditorFactory(w)

	editor1 = QtTreePropertyBrowser()
	editor1.setFactoryForManager(boolManager, checkBoxFactory)
	editor1.setFactoryForManager(intManager, spinBoxFactory)
	editor1.setFactoryForManager(stringManager, lineEditFactory)
	editor1.setFactoryForManager(sizeManager.subIntPropertyManager(), spinBoxFactory)
	editor1.setFactoryForManager(rectManager.subIntPropertyManager(), spinBoxFactory)
	editor1.setFactoryForManager(sizePolicyManager.subIntPropertyManager(), spinBoxFactory)
	editor1.setFactoryForManager(sizePolicyManager.subEnumPropertyManager(), comboBoxFactory)
	editor1.setFactoryForManager(enumManager, comboBoxFactory)

	editor1.addProperty(item0)

	# editor2 = QtTreePropertyBrowser()
	# editor2.addProperty(item0)

	# editor3 = QtGroupBoxPropertyBrowser()
	# editor3.setFactoryForManager(boolManager, checkBoxFactory)
	# editor3.setFactoryForManager(intManager, spinBoxFactory)
	# editor3.setFactoryForManager(stringManager, lineEditFactory)
	# editor3.setFactoryForManager(sizeManager.subIntPropertyManager(), spinBoxFactory)
	# editor3.setFactoryForManager(rectManager.subIntPropertyManager(), spinBoxFactory)
	# editor3.setFactoryForManager(sizePolicyManager.subIntPropertyManager(), spinBoxFactory)
	# editor3.setFactoryForManager(sizePolicyManager.subEnumPropertyManager(), comboBoxFactory)
	# editor3.setFactoryForManager(enumManager, comboBoxFactory)

	# editor3.addProperty(item0)

	# scroll3 = QtGui.QScrollArea()
	# scroll3.setWidgetResizable(True)
	# scroll3.setWidget(editor3)

	# editor4 = QtGroupBoxPropertyBrowser()
	# editor4.setFactoryForManager(boolManager, checkBoxFactory)
	# editor4.setFactoryForManager(intManager, scrollBarFactory)
	# editor4.setFactoryForManager(stringManager, lineEditFactory)
	# editor4.setFactoryForManager(sizeManager.subIntPropertyManager(), spinBoxFactory)
	# editor4.setFactoryForManager(rectManager.subIntPropertyManager(), spinBoxFactory)
	# editor4.setFactoryForManager(sizePolicyManager.subIntPropertyManager(), sliderFactory)
	# editor4.setFactoryForManager(sizePolicyManager.subEnumPropertyManager(), comboBoxFactory)
	# editor4.setFactoryForManager(enumManager, comboBoxFactory)

	# editor4.addProperty(item0)

	# scroll4 = QtGui.QScrollArea()
	# scroll4.setWidgetResizable(True)
	# scroll4.setWidget(editor4)

	# editor5 = QtButtonPropertyBrowser()
	# editor5.setFactoryForManager(boolManager, checkBoxFactory)
	# editor5.setFactoryForManager(intManager, scrollBarFactory)
	# editor5.setFactoryForManager(stringManager, lineEditFactory)
	# editor5.setFactoryForManager(sizeManager.subIntPropertyManager(), spinBoxFactory)
	# editor5.setFactoryForManager(rectManager.subIntPropertyManager(), spinBoxFactory)
	# editor5.setFactoryForManager(sizePolicyManager.subIntPropertyManager(), sliderFactory)
	# editor5.setFactoryForManager(sizePolicyManager.subEnumPropertyManager(), comboBoxFactory)
	# editor5.setFactoryForManager(enumManager, comboBoxFactory)

	# editor5.addProperty(item0)

	# scroll5 = QtGui.QScrollArea()
	# scroll5.setWidgetResizable(True)
	# scroll5.setWidget(editor5)

	layout = QtGui.QGridLayout(w)
	label1 = QtGui.QLabel("Editable Tree Property Browser")
	# label2 = QtGui.QLabel("Read Only Tree Property Browser, editor factories are not set")
	# label3 = QtGui.QLabel("Group Box Property Browser")
	# label4 = QtGui.QLabel("Group Box Property Browser with different editor factories")
	# label5 = QtGui.QLabel("Button Property Browser")
	label1.setWordWrap(True)
	# label2.setWordWrap(True)
	# label3.setWordWrap(True)
	# label4.setWordWrap(True)
	# label5.setWordWrap(True)
	label1.setFrameShadow(QtGui.QFrame.Sunken)
	# label2.setFrameShadow(QtGui.QFrame.Sunken)
	# label3.setFrameShadow(QtGui.QFrame.Sunken)
	# label4.setFrameShadow(QtGui.QFrame.Sunken)
	# label5.setFrameShadow(QtGui.QFrame.Sunken)
	label1.setFrameShape(QtGui.QFrame.Panel)
	# label2.setFrameShape(QtGui.QFrame.Panel)
	# label3.setFrameShape(QtGui.QFrame.Panel)
	# label4.setFrameShape(QtGui.QFrame.Panel)
	# label5.setFrameShape(QtGui.QFrame.Panel)
	label1.setAlignment(Qt.Qt.AlignCenter)
	# label2.setAlignment(Qt.Qt.AlignCenter)
	# label3.setAlignment(Qt.Qt.AlignCenter)
	# label4.setAlignment(Qt.Qt.AlignCenter)
	# label5.setAlignment(Qt.Qt.AlignCenter)

	layout.addWidget(label1, 0, 0)
	# layout.addWidget(label2, 0, 1)
	# layout.addWidget(label3, 0, 2)
	# layout.addWidget(label4, 0, 3)
	# layout.addWidget(label5, 0, 4)
	layout.addWidget(editor1, 1, 0)
	# layout.addWidget(editor2, 1, 1)
	# layout.addWidget(scroll3, 1, 2)
	# layout.addWidget(scroll4, 1, 3)
	# layout.addWidget(scroll5, 1, 4)

	w.show()

	app.exec_()
	app.deleteLater()
	sys.exit()

