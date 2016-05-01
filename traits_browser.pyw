# -*- coding: utf-8 -*-
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4.QtPropertyBrowser import *
import sys
import operator
from traits.api import HasTraits
from traits.api import Int, String, Enum, Instance, Bool, Float, List, Dict, Tuple


class TraitEditorFactory(QtVariantEditorFactory):
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
            val = val.decode('utf8')  # decode the str to unicode with given codec (utf8)
        return val

    def set_value(self, value):
        if isinstance(value, QString):
            value = unicode(value.toUtf8(), 'utf8', 'ignore')
        setattr(self.obj, self.attr, value)

    def qttype(self):
        return TraitWrapper.PRIMITIVE_TYPE.get(type(self._ctrait().handler))

    def childrens(self):
        return []

    def update_property(self, prop):
        '''Update the assosiated property created by QtVariantPropertyManager'''
        prop.setValue(self.value())
        # fetch some metas and adapt to qt attributes basically for numeric
        # values.
        low = self._ctrait().low
        high = self._ctrait().high
        step = self._ctrait().step
        if low is not None:
            prop.setAttribute('minimum', low)
        if high is not None:
            prop.setAttribute('maximum', high)
        if step is not None:
            prop.setAttribute('singleStep', step)


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

    def set_value(self, value):
        if isinstance(value, QString):
            value = unicode(value.toUtf8(), 'utf8', 'ignore')
        lst = self._list_value()
        lst[self.key] = value

    def name(self):
        return unicode(self.key)


class DictItemTraitWrapper(ListItemTraitWrapper):
    pass


class TupleItemTraitWrapper(ListItemTraitWrapper):
    pass


class WrapperFactory(object):
    '''Get the wrapper according to the traits type. Default wrapper is
    TraitsWrapper.
    '''
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
        self.valueChanged.connect(self.slotValueChanged)
        # you need to keep a ref to the sip wrapped object since it is like a
        # weak ref wrapped the c++ instance. Or it will be garbage collected
        # when addProperty returns. Hence you will get a different sip wrapped
        # object emitted in valueChanged signal.
        self.refs = []

    def addProperty(self, obj, attr, key=None):
        wrapper = WrapperFactory.get_wrapper(obj, attr, key)  # obj.attr
        if wrapper.qttype():
            qtprop = super(TraitManager, self).addProperty(wrapper.qttype(), self.trUtf8(wrapper.name()))
            wrapper.update_property(qtprop)
            qtprop.traits_wrapper = wrapper
            self.refs.append(qtprop)  # inc count to keep the sip wrapped object alive
            for childname in wrapper.childrens():
                if isinstance(childname, tuple):
                    prop = self.addProperty(wrapper.value(), *childname)  # contains a key
                else:
                    prop = self.addProperty(wrapper.value(), childname)
                qtprop.addSubProperty(prop)
            return qtprop

    #def initializeProperty(self, prop):
        #if self.wrapper_adding is not None:
            #prop.traits_wrapper = self.wrapper_adding
            #print '=====initialize prop===', prop, prop.traits_wrapper
            ##self.propertyToTraitWrapper[property] = self.newTraitWrapper
            ##self.traitSenderToProperty[self.newTraitWrapper.sender()] = property
            ## connect traits changed to update logic (either value or meta)
            ##TraitValueChangedSignal.connect(self.traitValueChanged, self.newTraitWrapper.sender())
            ##TraitMetaChangedSignal.connect(self.traitMetaChanged, self.newTraitWrapper.sender())
            #super(TraitManager, self).initializeProperty(prop)
            #self.wrapper_adding = None
            #print '=====initialize prop2===', prop, prop.traits_wrapper

    #def uninitializeProperty(self, prop):
            ##traitWrapper = self.propertyToTraitWrapper[property]
            ##TraitValueChangedSignal.disconnect(self.traitValueChanged, traitWrapper.sender())
            ##TraitMetaChangedSignal.disconnect(self.traitMetaChanged, traitWrapper.sender())
        #super(TraitManager, self).uninitializeProperty(prop)

    def slotValueChanged(self, prop, value):
        assert isinstance(value, QVariant)
        wrapper = getattr(prop, 'traits_wrapper', None)
        if wrapper is not None:
            try:
                wrapper.set_value(value.toPyObject())
            except Exception as ex:
                pass

    #def traitValueChanged(self, sender, new, **kwargs):
        #if sender in self.traitSenderToProperty:
            #property = self.traitSenderToProperty[sender]
            #self.setValue(property, new)

    #def traitMetaChanged(self, sender, key, new, **kwargs):
        #if sender in self.traitSenderToProperty:
            #property = self.traitSenderToProperty[sender]
            #if key == KEY_DESC:
                #property.setPropertyName(new)


class Person(HasTraits):
    age = Int(20, low=0, high=150, label=u'年龄')
    name = String(u'邹俊洋', label=u'姓名')
    degree = Enum(['B.S.', 'M.S.'], label=u'学历')
    awards = List(trait=String(), value=['s', 's', 's+'], label='奖励')


class Group(HasTraits):
    leader = Instance(klass=Person, args=(), label='LEADER')
    income = Float(low=0, high=100, label=u'收入')
    groupname = String('', label='GROUP NAME')


def dump_dict(hastraits, dikt):
    traits_list = hastraits.traits()
    for trait in traits_list:
        _dump(hastraits, trait, dikt)


def _dump(obj, attr, dikt):
    ctrait = obj.trait(attr)
    if not ctrait.label:
        return
    if isinstance(ctrait.handler, Instance):
        new_dikt = dikt.setdefault(ctrait.label, {})
        dump_dict(getattr(obj, attr), new_dikt)
    else:
        dikt[ctrait.label] = getattr(obj, attr)


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
        self.factory = TraitEditorFactory(self)
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
        global prop
        for name, trait in traits:
            prop = self.manager.addProperty(obj, name)
            self.browser.addProperty(prop)

        self.__obj = obj

    def object(self):
        return self.__obj

    def slotValueChanged(self, prop, variant):
        pass

prop = None
if __name__ == '__main__':
    app = QApplication(sys.argv)

    editor = TraitBrowser()
    group = Group()
    editor.setObject(group)
    editor.show()

    app.exec_()
    app.deleteLater()

    dikt = {}
    dump_dict(group, dikt)
    print '==========', dikt
    sys.exit()
