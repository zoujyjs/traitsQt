# -*- coding: utf-8 -*-
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4.QtPropertyBrowser import *
import sys
import operator
from traits.api import HasTraits
from traits.api import Int, String, Enum, Instance, Bool, Float, List, Dict, Tuple


class TraitFactory(QtVariantEditorFactory):
    pass


class TraitWrapper(QObject):
    PRIMITIVE_TYPE = {
        Bool: QVariant.Bool,
        Int: QVariant.Int,
        Float: QVariant.Double,
        String: QVariant.String,
        Enum: QtVariantPropertyManager.enumTypeId(),
        Instance: QtVariantPropertyManager.groupTypeId(),
        List: QtVariantPropertyManager.groupTypeId(),
    }

    def __init__(self, trait, attr):  # attr may be a int when obj is a list instead of hastraits
        super(TraitWrapper, self).__init__()
        self.obj = obj
        self.attr = attr

    def _trait(self):
        return self.obj.trait(self.attr)

    def name(self):
        return getattr(self._trait(), 'label') or ''

    def value(self):
        v = getattr(self.obj, self.attr)
        if isinstance(v, bytes):
            v = self.trUtf8(v)
        return v

    def qttype(self):
        return TraitWrapper.PRIMITIVE_TYPE.get(type(self._trait().handler))

    def childrens(self):
        return []

    def update_property(self, prop):
        '''Update the assosiated property created by QtVariantPropertyManager'''
        prop.setValue(self.value())


class EnumTraitWrapper(TraitWrapper):
    def update_property(self, prop):
        '''Update the assosiated property created by QtVariantPropertyManager'''
        val = self.value()
        values = self._trait().handler.values
        prop.setAttribute('enumNames', list(values))  # must be a list
        prop.setValue(values.index(val))


class InstanceTraitWrapper(TraitWrapper):
    def childrens(self):
        inst = self.value()
        if isinstance(inst, HasTraits):
            return sorted(inst.traits().keys())


class ListTraitWrapper(TraitWrapper):
    def __init__(self, obj, attr):
        self.obj = obj
        self.attr = attr
        self.iterator = self._generator()
        self.idx = 0

    def name(self):
        return getattr(self._trait().inner_traits[0], 'label') + str(self.idx) or ''

    def value(self):
        self.iterator.next()

    def update_property(self, prop):
        pass

    def _generator(self):
        v = getattr(self.obj, self.attr)
        for i in xrange(len(v)):
            self.idx = i
            yield v[i]

    def childrens(self):
        val = [getattr(trait, 'label') or '' for trait in self._trait().inner_traits]
        print '==============', val
        return val


class TupleTraitWrapper(ListTraitWrapper):
    pass


class DictTraitWrapper(TraitWrapper):
    pass


class WrapperFactory(object):
    WRAPPER_CLS = {
        List: ListTraitWrapper,
        Tuple: TupleTraitWrapper,
        Dict: DictTraitWrapper,
        Enum: EnumTraitWrapper,
        Instance: InstanceTraitWrapper,
    }

    @classmethod
    def get_wrapper(cls, hastraits, attr):
        ctraits = hastraits.trait(attr)
        return cls.WRAPPER_CLS.get(type(ctraits.handler), TraitWrapper)(hastraits, attr)


class TraitManager(QtVariantPropertyManager):
    def __init__(self, parent=None):
        super(TraitManager, self).__init__()

    def addProperty(self, obj, attr):
        wrapper = WrapperFactory.get_wrapper(obj, attr)  # obj.attr
        if wrapper.qttype():
            qtprop = super(TraitManager, self).addProperty(wrapper.qttype(), self.trUtf8(wrapper.name()))
            wrapper.update_property(qtprop)
            for name in wrapper.childrens():
                prop = self.addProperty(wrapper.value(), name)
                qtprop.addSubProperty(prop)
            return qtprop

    # def setValue(self):
    #     # @TODO add event trigger adaptor and enable value changed
    #     pass


class Person(HasTraits):
    age = Int(20, label='年龄')
    name = String('邹俊洋', label='名字')
    degree = Enum(['B.S.', 'M.S.'], label='学位')
    awards = List(trait=String(label='奖励'), value=['s', 's', 's+'])


class Group(HasTraits):
    leader = Instance(klass=Person, args=())
    groupname = String('', label='group name')


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
        self.browser.setPropertiesWithoutValueMarked(True)
        self.browser.setRootIsDecorated(False)

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
            prop = self.manager.addProperty(obj, name)
            self.browser.addProperty(prop)

        self.__obj = obj

    def object(self):
        return self.__obj

    def slotValueChanged(self, property, variant):
        pass

if __name__ == '__main__':
    app = QApplication(sys.argv)

    editor = TraitBrowser()
    editor.setObject(Group())
    editor.show()

    app.exec_()
    app.deleteLater()
    sys.exit()
