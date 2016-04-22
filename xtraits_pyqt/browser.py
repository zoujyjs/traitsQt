# -*- coding: utf-8 -*-
__author__ = 'Po'


import operator
from manager import *
from factory import *
from ..xtraits import *
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4.QtPropertyBrowser import *


class TraitBrowser(QWidget):

	def __init__(self, parent=None):
		super(TraitBrowser, self).__init__(parent)

		self.__obj = None

		self.browser = QtTreePropertyBrowser(self)
		self.browser.setRootIsDecorated(False)
		self.browser.setPropertyColumnTitle(self.trUtf8('属性'))
		self.browser.setValueColumnTitle(self.trUtf8('值'))
		self.browser.setResizeMode(QtTreePropertyBrowser.Interactive)

		self.verticalLayout = QVBoxLayout(self)
		self.verticalLayout.setMargin(0)
		self.verticalLayout.addWidget(self.browser)

		self.manager = TraitManager(self)
		self.factory = TraitFactory(self)
		self.browser.setFactoryForManager(self.manager, self.factory)

		self.manager.valueChanged.connect(self.slotValueChanged)

	def setObject(self, obj):
		if not isinstance(obj, HasTraits):
			return
		if obj == self.__obj:
			return

		self.browser.clear()
		self.manager.clear()

		traits = obj.traits().items()
		traits.sort(key=operator.itemgetter(1))
		for name, trait in traits:
			property = self.manager.addProperty(obj, name)
			self.browser.addProperty(property)

		self.__obj = obj

	def object(self):
		return self.__obj

	def slotValueChanged(self, property, variant):
		pass

