__author__ = 'Po'

"""
Python conversion of the QtPropertyBrowser "decoration" example.

"""

from PyQt4 import QtCore, QtGui
from PyQt4.QtPropertyBrowser import *
import sys


class DecoratedDoublePropertyManager(QtDoublePropertyManager):
	prefixChanged = QtCore.pyqtSignal(QtProperty, QtCore.QString)
	suffixChanged = QtCore.pyqtSignal(QtProperty, QtCore.QString)


	class Data(object):
		prefix = ''
		suffix = ''


	def __init__(self, parent=None):
		super(DecoratedDoublePropertyManager, self).__init__(parent)
		self.propertyToData = dict()

	def prefix(self, property):
		if property not in self.propertyToData:
			return ''
		return self.propertyToData[property].prefix

	def suffix(self, property):
		if property not in self.propertyToData:
			return ''
		return self.propertyToData[property].suffix

	def setPrefix(self, property, prefix):
		if property not in self.propertyToData:
			return

		data = self.propertyToData[property]
		if data.prefix == prefix:
			return

		data.prefix = prefix
		self.propertyToData[property] = data

		self.propertyChanged.emit(property)
		self.prefixChanged.emit(property, prefix)

	def setSuffix(self, property, suffix):
		if property not in self.propertyToData:
			return

		data = self.propertyToData[property]
		if data.suffix == suffix:
			return

		data.suffix = suffix
		self.propertyToData[property] = data

		self.propertyChanged.emit(property)
		self.suffixChanged.emit(property, suffix)

	def valueText(self, property):
		text = super(DecoratedDoublePropertyManager, self).valueText(property)
		if property not in self.propertyToData:
			return text

		data = self.propertyToData[property]
		text = data.prefix + text + data.suffix

		return text

	def initializeProperty(self, property):
		self.propertyToData[property] = DecoratedDoublePropertyManager.Data()
		super(DecoratedDoublePropertyManager, self).initializeProperty(property)

	def uninitializeProperty(self, property):
		if property in self.propertyToData:
			del self.propertyToData[property]
		super(DecoratedDoublePropertyManager, self).uninitializeProperty(property)


class DecoratedDoubleSpinBoxFactory(QtAbstractEditorFactoryQtAbstractPropertyManager):
	def __init__(self, parent=None):
		super(DecoratedDoubleSpinBoxFactory, self).__init__(parent)
		self.originalFactory = QtDoubleSpinBoxFactory(self)
		self.createdEditors = dict()
		self.editorToProperty = dict()

	def connectPropertyManager(self, manager):
		self.originalFactory.addPropertyManager(manager)
		manager.prefixChanged.connect(self.slotPrefixChanged)
		manager.suffixChanged.connect(self.slotSuffixChanged)

	def createEditorFromManager(self, manager, property, parent):
		w = self.originalFactory.createEditor(property, parent)
		if not w:
			return 0

		if not isinstance(w, QtGui.QDoubleSpinBox):
			return 0

		spinBox = w
		spinBox.setPrefix(manager.prefix(property))
		spinBox.setSuffix(manager.suffix(property))

		manager.setPrefix(property, 'what: ')

		self.createdEditors.setdefault(property, []).append(spinBox)
		self.editorToProperty[spinBox] = property

		return spinBox

	def disconnectPropertyManager(self, manager):
		self.originalFactory.removePropertyManager(manager)
		manager.prefixChanged.disconnect(self.slotPrefixChanged)
		manager.suffixChanged.disconnect(self.slotSuffixChanged)

	def slotPrefixChanged(self, property, prefix):
		if property not in self.createdEditors:
			return

		manager = self.propertyManager(property)
		if not manager:
			return

		editors = self.createdEditors[property]
		for editor in editors:
			editor.setPrefix(prefix)

	def slotSuffixChanged(self, property, suffix):
		if property not in self.createdEditors:
			return

		manager = self.propertyManager(property)
		if not manager:
			return

		editors = self.createdEditors[property]
		for editor in editors:
			editor.setSuffix(suffix)

	def slotEditorDestroyed(self, object):
		if object in self.editorToProperty:
			editor = object
			property = self.editorToProperty[object]
			del self.editorToProperty[editor]
			del self.createdEditors[property]


if __name__ == '__main__':
	app = QtGui.QApplication(sys.argv)

	undecoratedManager = QtDoublePropertyManager()
	undecoratedProperty = undecoratedManager.addProperty('Undecorated')
	undecoratedManager.setValue(undecoratedProperty, 123.45)

	decoratedManager = DecoratedDoublePropertyManager()
	decoratedProperty = decoratedManager.addProperty('Decorated')
	decoratedManager.setPrefix(decoratedProperty, 'speed: ')
	decoratedManager.setSuffix(decoratedProperty, ' km/h')
	decoratedManager.setValue(decoratedProperty, 123.45)

	undecoratedFactory = QtDoubleSpinBoxFactory()
	decoratedFactory = DecoratedDoubleSpinBoxFactory()

	editor = QtTreePropertyBrowser()
	editor.setFactoryForManager(undecoratedManager, undecoratedFactory)
	editor.setFactoryForManager(decoratedManager, decoratedFactory)
	editor.addProperty(undecoratedProperty)
	editor.addProperty(decoratedProperty)

	editor.show()

	app.exec_()
	app.deleteLater()
	sys.exit()
