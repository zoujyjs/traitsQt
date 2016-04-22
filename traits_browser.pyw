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


class TraitWrapper(object):
    PRIMITIVE_TYPE = {
        Bool: QVariant.Bool,
        Int: QVariant.Int,
        Float: QVariant.Double,
        String: QVariant.String,
        Enum: QtVariantPropertyManager.enumTypeId(),
        Instance: QtVariantPropertyManager.groupTypeId(),
        List: QtVariantPropertyManager.groupTypeId(),
    }

    def __init__(self, obj, attr):
        super(TraitWrapper, self).__init__()
        self.obj = obj
        self.attr = attr

    def _ctrait(self):
        return self.obj.trait(self.attr)

    def name(self):
        return self._ctrait().label or ''

    def value(self):
        val = getattr(self.obj, self.attr)
        if isinstance(val, bytes):
            val = val.decode('utf8')
        return val

    def qttype(self):
        return TraitWrapper.PRIMITIVE_TYPE.get(type(self._ctrait().handler))

    def childrens(self):
        return []

    def update_property(self, prop):
        '''Update the assosiated property created by QtVariantPropertyManager'''
        prop.setValue(self.value())


class EnumTraitWrapper(TraitWrapper):
    def update_property(self, prop):
        '''Update the assosiated property created by QtVariantPropertyManager'''
        val = self.value()
        values = self._ctrait().handler.values
        prop.setAttribute('enumNames', list(values))  # must be a list
        prop.setValue(values.index(val))


class InstanceTraitWrapper(TraitWrapper):
    def childrens(self):
        inst = self.value()
        if isinstance(inst, HasTraits):
            return sorted(inst.traits().keys())

    def update_property(self, prop):
        pass


class ListTraitWrapper(TraitWrapper):
    def value(self):
        return self.obj  # list need to return it's host obj for list item

    def _list_value(self):
        return getattr(self.obj, self.attr)

    def childrens(self):
        lst = self._list_value()
        print '======list childrens======', [(self.attr, i) for i in xrange(len(lst))]
        return [(self.attr, i) for i in xrange(len(lst))]

    def update_property(self, prop):
        pass


class TupleTraitWrapper(ListTraitWrapper):
    pass


class DictTraitWrapper(TraitWrapper):
    def value(self):
        return self.obj  # list need to return it's host obj for list item

    def _dict_value(self):
        return getattr(self.obj, self.attr)

    def childrens(self):
        dikt = self._dict_value()
        return [(self.attr, k) for k in sorted(dikt.keys())]

    def update_property(self, prop):
        pass


class ListItemTraitWrapper(TraitWrapper):
    def __init__(self, obj, attr, key):
        super(ListItemTraitWrapper, self).__init__(obj, attr)
        self.key = key

    def qttype(self):
        lsttrait = self._ctrait()
        ctrait = lsttrait.inner_traits[0]
        return TraitWrapper.PRIMITIVE_TYPE.get(type(ctrait.handler))

    def _sequence_value(self):
        return getattr(self.obj, self.attr)

    def value(self):
        val = self._sequence_value()[self.key]
        if isinstance(val, bytes):
            val = val.decode('utf8')
        return val

    def name(self):
        return unicode(self.key)


class DictItemTraitWrapper(ListItemTraitWrapper):
    pass


class TupleItemTraitWrapper(ListItemTraitWrapper):
    pass


class WrapperFactory(object):
    WRAPPER_CLS = {
        List: ListTraitWrapper,
        Tuple: TupleTraitWrapper,
        Dict: DictTraitWrapper,
        Enum: EnumTraitWrapper,
        Instance: InstanceTraitWrapper,
    }
    ITEM_CLS = {
        List: ListItemTraitWrapper,
        Tuple: TupleItemTraitWrapper,
        Dict: DictItemTraitWrapper,
    }

    @classmethod
    def get_wrapper(cls, hastraits, attr, key=None):
        ctraits = hastraits.trait(attr)
        if key is None:
            return cls.WRAPPER_CLS.get(type(ctraits.handler), TraitWrapper)(hastraits, attr)
        else:
            return cls.ITEM_CLS.get(type(ctraits.handler), TraitWrapper)(hastraits, attr, key)


class TraitManager(QtVariantPropertyManager):
    def __init__(self, parent=None):
        super(TraitManager, self).__init__()

    def addProperty(self, obj, attr, key=None):
        wrapper = WrapperFactory.get_wrapper(obj, attr, key)  # obj.attr
        if wrapper.qttype():
            qtprop = super(TraitManager, self).addProperty(wrapper.qttype(), self.trUtf8(wrapper.name()))
            print '========add property======', wrapper.qttype(), wrapper.name()
            wrapper.update_property(qtprop)
            for childname in wrapper.childrens():
                if isinstance(childname, tuple):
                    prop = self.addProperty(wrapper.value(), *childname)  # contains a key
                else:
                    prop = self.addProperty(wrapper.value(), childname)
                qtprop.addSubProperty(prop)
            return qtprop

    # def setValue(self):
    #     # @TODO add event trigger adaptor and enable value changed
    #     pass


class Person(HasTraits):
    age = Int(20, label='年龄')
    name = String('邹俊洋', label='名字')
    degree = Enum(['B.S.', 'M.S.'], label='学位')
    awards = List(trait=String(), value=['s', 's', 's+'], label='奖励')


class Group(HasTraits):
    leader = Instance(klass=Person, args=(), label='leader')
    groupname = String('', label='group name')


class TraitBrowser(QWidget):
    def __init__(self, parent=None):
        super(TraitBrowser, self).__init__(parent)

        self.__obj = None

        self.browser = QtTreePropertyBrowser(self)
        self.browser.setRootIsDecorated(False)
        self.browser.setPropertyColumnTitle(self.trUtf8('属性'))
        self.browser.setValueColumnTitle(self.trUtf8('值'))
        # self.browser.setResizeMode(QtTreePropertyBrowser.Interactive)

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
    group = Group()
    editor.setObject(group)
    editor.show()

    app.exec_()
    app.deleteLater()
    sys.exit()
