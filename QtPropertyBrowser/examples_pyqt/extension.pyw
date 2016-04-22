__author__ = 'Po'

"""
Python conversion of the QtPropertyBrowser "extension" example.

"""

from PyQt4 import QtCore, QtGui
from PyQt4.QtPropertyBrowser import *
import sys


class VariantManager(QtVariantPropertyManager):
	class Data(object):
		value = None
		x = None
		y = None


	def __init__(self, parent=None):
		super(VariantManager, self).__init__(parent)

		self.propertyToData = dict()
		self.xToProperty = dict()
		self.yToProperty = dict()

		self.valueChanged.connect(self.slotValueChanged)
		self.propertyDestroyed.connect(self.slotPropertyDestroyed)

	def value(self, property):
		if property in self.propertyToData:
			return self.propertyToData[property].value
		return super(VariantManager, self).value(property)

	def valueType(self, propertyType):
		if propertyType == QtCore.QVariant.PointF:
			return QtCore.QVariant.PointF
		return super(VariantManager, self).valueType(propertyType)

	def isPropertyTypeSupported(self, propertyType):
		if propertyType == QtCore.QVariant.PointF:
			return True
		return super(VariantManager, self).isPropertyTypeSupported(propertyType)

	def valueText(self, property):
		if property in self.propertyToData:
			p = self.propertyToData[property].value
			return '(%s, %s)' % (p.x(), p.y())
		return super(VariantManager, self).valueText(property)

	def setValue(self, property, val):
		assert isinstance(val, QtCore.QVariant)
		if property in self.propertyToData:
			if val.type() != QtCore.QVariant.PointF and not val.canConvert(QtCore.QVariant.PointF):
				return
			p = val.toPointF()
			d = self.propertyToData[property]
			d.value = p
			if d.x:
				d.x.setValue(p.x())
			if d.y:
				d.y.setValue(p.y())
			self.propertyToData[property] = d
			self.propertyChanged.emit(property)
			self.valueChanged.emit(property, val)
			return
		super(VariantManager, self).setValue(property, val)

	def initializeProperty(self, property):
		if self.propertyType(property) == QtCore.QVariant.PointF:
			d = VariantManager.Data()
			d.value = QtCore.QPointF(0, 0)

			d.x = self.addProperty(QtCore.QVariant.Double)
			d.x.setPropertyName('Position X')
			property.addSubProperty(d.x)
			self.xToProperty[d.x] = property

			d.y = self.addProperty(QtCore.QVariant.Double)
			d.y.setPropertyName('Position Y')
			property.addSubProperty(d.y)
			self.yToProperty[d.y] = property

			self.propertyToData[property] = d
		super(VariantManager, self).initializeProperty(property)

	def uninitializeProperty(self, property):
		if property in self.propertyToData:
			d = self.propertyToData[property]
			if d.x:
				del self.xToProperty[d.x]
			if d.y:
				del self.yToProperty[d.y]
			del self.propertyToData[property]
		super(VariantManager, self).uninitializeProperty(property)

	def slotValueChanged(self, property, value):
		assert isinstance(value, QtCore.QVariant)
		if property in self.xToProperty:
			pointProperty = self.xToProperty[property]
			p = self.value(pointProperty)
			v, _ = value.toDouble()
			p.setX(v)
			self.setValue(pointProperty, QtCore.QVariant(p))
		elif property in self.yToProperty:
			pointProperty = self.yToProperty[property]
			p = self.value(pointProperty)
			v, _ = value.toDouble()
			p.setY(v)
			self.setValue(pointProperty, QtCore.QVariant(p))

	def slotPropertyDestroyed(self, property):
		if property in self.xToProperty:
			pointProperty = self.xToProperty[property]
			self.propertyToData[pointProperty].x = 0
			del self.xToProperty[property]
		elif property in self.yToProperty:
			pointProperty = self.yToProperty[property]
			self.propertyToData[pointProperty].y = 0
			del self.yToProperty[property]


if __name__ == '__main__':
	app = QtGui.QApplication(sys.argv)

	variantManager = VariantManager()

	item = variantManager.addProperty(QtCore.QVariant.PointF, 'PointF Property')
	item.setValue(QtCore.QPointF(2.5, 13.13))

	variantFactory = QtVariantEditorFactory()

	ed1 = QtTreePropertyBrowser()
	ed1.setFactoryForManager(variantManager, variantFactory)
	ed1.addProperty(item)

	ed1.show()

	app.exec_()
	app.deleteLater()
	sys.exit()