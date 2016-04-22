# -*- coding: utf-8 -*-
__author__ = 'Po'


import operator
from xtraits import *
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4.QtPropertyBrowser import *


class TraitWrapper(object):
	def __init__(self, obj, attr):
		self.obj = obj
		self.attr = attr

	def trait(self):
		return self.obj.trait(self.attr)

	def sender(self):
		return self.obj.trait_sender(self.attr)

	def name(self):
		return self.trait().get_metadata(KEY_DESC) or ''

	def value(self):
		v = getattr(self.obj, self.attr)
		if isinstance(v, bytes):
			return unicode(v, 'gbk')
		else:
			return v

	def setValue(self, value):
		if isinstance(value, QString):
			value = unicode(value.toUtf8(),'utf8','ignore').encode('gbk')
		setattr(self.obj, self.attr, value)


class TupleTraitItemWrapper(TraitWrapper):
	def __init__(self, obj, attr, idx):
		super(TupleTraitItemWrapper, self).__init__(obj, attr)
		self.idx = idx

	def trait(self):
		tupleTrait = super(TupleTraitItemWrapper, self).trait()
		return tupleTrait.inner_traits()[self.idx]

	def name(self):
		return self.trait().get_metadata(KEY_DESC)

	def value(self):
		t = getattr(self.obj, self.attr)
		if isinstance(t, tuple):
			if 0 <= self.idx < len(t):
				v = t[self.idx]
				if isinstance(v, bytes):
					return unicode(v, 'gbk')
				else:
					return v
		return None

	def setValue(self, value):
		t = getattr(self.obj, self.attr)
		if isinstance(t, tuple):
			if 0 <= self.idx < len(t):
				l = list(t)
				if isinstance(value, QString):
					value = unicode(value.toUtf8(),'utf8','ignore').encode('gbk')
				l[self.idx] = value
				setattr(self.obj, self.attr, tuple(l))


class ListTraitItemWrapper(TraitWrapper):
	def __init__(self, obj, attr, idx):
		super(ListTraitItemWrapper, self).__init__(obj, attr)
		self.idx = idx

	def trait(self):
		listTrait = super(ListTraitItemWrapper, self).trait()
		return listTrait.inner_traits()[0]

	def name(self):
		return unicode(str(self.idx), 'gbk')

	def value(self):
		l = getattr(self.obj, self.attr)
		if isinstance(l, TraitListObject):
			if 0 <= self.idx < len(l):
				v = l[self.idx]
				if isinstance(v, bytes):
					return unicode(v, 'gbk')
				else:
					return v
		return None

	def setValue(self, value):
		l = getattr(self.obj, self.attr)
		if isinstance(l, TraitListObject):
			if 0 <= self.idx < len(l):
				if isinstance(value, QString):
					value = unicode(value.toUtf8(),'utf8','ignore').encode('gbk')
				l[self.idx] = value


class DictTraitItemWrapper(TraitWrapper):
	def __init__(self, obj, attr, key):
		super(DictTraitItemWrapper, self).__init__(obj, attr)
		self.key = key

	def trait(self):
		dictTrait = super(DictTraitItemWrapper, self).trait()
		return dictTrait.get_metadata(KEY_VALUE_TRAIT)

	def name(self):
		return unicode(str(self.key), 'gbk')

	def value(self):
		d = getattr(self.obj, self.attr)
		if isinstance(d, TraitDictObject):
			if self.key in d:
				v = d[self.key]
				if isinstance(v, bytes):
					return unicode(v, 'gbk')
				else:
					return v
		return None

	def setValue(self, value):
		d = getattr(self.obj, self.attr)
		if isinstance(d, TraitDictObject):
			if isinstance(value, QString):
				value = unicode(value.toUtf8(),'utf8','ignore').encode('gbk')
			d[self.key] = value

class TraitManager(QtVariantPropertyManager):

	def __init__(self, parent=None):
		super(TraitManager, self).__init__(parent)

		self.typeMap = {
			Bool: QVariant.Bool,
			Int: QVariant.Int,
			Float: QVariant.Double,
			Bytes: QVariant.String,
			Enum: self.enumTypeId()
		}
		self.propertyToTraitWrapper = dict()
		self.traitSenderToProperty = dict()
		self.newTraitWrapper = None

		self.valueChanged.connect(self.slotValueChanged)

	def addProperty(self, obj, attr):
		traitWrapper = TraitWrapper(obj, attr)
		return self._addProperty(traitWrapper)

	def _addProperty(self, traitWrapper):
		mappedType = self.typeMap.get(type(traitWrapper.trait()), None)

		if mappedType:
			self.newTraitWrapper = traitWrapper
			return super(TraitManager, self).addProperty(
				mappedType, self.trUtf8(self.newTraitWrapper.name()))
		elif isinstance(traitWrapper.trait(), Tuple):
			self.newTraitWrapper = None
			property = super(TraitManager, self).addProperty(
				QVariant.String, self.trUtf8(traitWrapper.name()))
			tupleObject = traitWrapper.value()
			if isinstance(tupleObject, tuple):
				for idx in xrange(0, len(tupleObject)):
					itemWrapper = TupleTraitItemWrapper(traitWrapper.obj, traitWrapper.attr, idx)
					subProperty = self._addProperty(itemWrapper)
					property.addSubProperty(subProperty)
			return property
		elif isinstance(traitWrapper.trait(), Dict):
			self.newTraitWrapper = None
			property = super(TraitManager, self).addProperty(
				QVariant.String, self.trUtf8(traitWrapper.name()))
			dictObject = traitWrapper.value()
			if isinstance(dictObject, TraitDictObject):
				dictKeys = dictObject.keys()
				dictKeys.sort()
				for key in dictKeys:
					itemWrapper = DictTraitItemWrapper(traitWrapper.obj, traitWrapper.attr, key)
					subProperty = self._addProperty(itemWrapper)
					property.addSubProperty(subProperty)
			return property
		elif isinstance(traitWrapper.trait(), Set):
			pass
		elif isinstance(traitWrapper.trait(), List):
			self.newTraitWrapper = None
			property = super(TraitManager, self).addProperty(
				QVariant.String, self.trUtf8(traitWrapper.name()))
			listObject = traitWrapper.value()
			if isinstance(listObject, TraitListObject):
				for idx in xrange(0, len(listObject)):
					itemWrapper = ListTraitItemWrapper(traitWrapper.obj, traitWrapper.attr, idx)
					subProperty = self._addProperty(itemWrapper)
					property.addSubProperty(subProperty)
			return property
		elif isinstance(traitWrapper.trait(), Instance):
			self.newTraitWrapper = None
			property = super(TraitManager, self).addProperty(
				QVariant.String, self.trUtf8(traitWrapper.name()))
			hasTraitObject = traitWrapper.value()
			if isinstance(hasTraitObject, HasTraits):
				traits = hasTraitObject.traits().items()
				traits.sort(key=operator.itemgetter(1))
				for attr, trait in traits:
					attrWrapper = TraitWrapper(hasTraitObject, attr)
					subProperty = self._addProperty(attrWrapper)
					property.addSubProperty(subProperty)
			return property
		return None

	def initializeProperty(self, property):
		if self.newTraitWrapper is not None:
			self.propertyToTraitWrapper[property] = self.newTraitWrapper
			self.traitSenderToProperty[self.newTraitWrapper.sender()] = property
			TraitValueChangedSignal.connect(self.traitValueChanged, self.newTraitWrapper.sender())
			TraitMetaChangedSignal.connect(self.traitMetaChanged, self.newTraitWrapper.sender())
			super(TraitManager, self).initializeProperty(property)
			self.setValue(property, QVariant(self.newTraitWrapper.value()))
			self.newTraitWrapper = None

	def uninitializeProperty(self, property):
		if property in self.propertyToTraitWrapper:
			traitWrapper = self.propertyToTraitWrapper[property]
			TraitValueChangedSignal.disconnect(self.traitValueChanged, traitWrapper.sender())
			TraitMetaChangedSignal.disconnect(self.traitMetaChanged, traitWrapper.sender())
			if traitWrapper.sender() in self.traitSenderToProperty:
				del self.traitSenderToProperty[traitWrapper.sender()]
			del self.propertyToTraitWrapper[property]
		super(TraitManager, self).uninitializeProperty(property)

	def slotValueChanged(self, property, value):
		assert isinstance(value, QVariant)
		if property in self.propertyToTraitWrapper:
			trait = self.propertyToTraitWrapper[property]
			try:
				trait.setValue(value.toPyObject())
			except Exception as ex:
				pass
			self.setValue(property, trait.value())

	def traitValueChanged(self, sender, new, **kwargs):
		if sender in self.traitSenderToProperty:
			property = self.traitSenderToProperty[sender]
			self.setValue(property, new)

	def traitMetaChanged(self, sender, key, new, **kwargs):
		if sender in self.traitSenderToProperty:
			property = self.traitSenderToProperty[sender]
			if key == KEY_DESC:
				property.setPropertyName(new)

