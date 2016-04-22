__author__ = 'Po'

"""
Python conversion of the QtPropertyBrowser "simple" example.

"""

if __name__ == '__main__':
    from PyQt4 import QtCore, QtGui
    from PyQt4.QtPropertyBrowser import *
    import sys
    
    app = QtGui.QApplication(sys.argv)

    variantManager = QtVariantPropertyManager()
    
    topItem = variantManager.addProperty(QtVariantPropertyManager.groupTypeId(), str(22) + "Group Property")
    subItem = variantManager.addProperty(QtVariantPropertyManager.groupTypeId(), str(22) + "sub group")
    topItem.addSubProperty(subItem)

    item = variantManager.addProperty(QtCore.QVariant.Bool, str(0) + "Bool Property")
    item.setValue(True)
    topItem.addSubProperty(item)

    item = variantManager.addProperty(QtCore.QVariant.Int, str(1) + " Int Property")
    item.setValue(20)
    item.setAttribute("minimum", 0)
    item.setAttribute("maximum", 100)
    item.setAttribute("singleStep", 10)
    subItem.addSubProperty(item)

    item = variantManager.addProperty(QtCore.QVariant.Double, str(2) + " Double Property")
    item.setValue(1.2345)
    item.setAttribute("singleStep", 0.1)
    item.setAttribute("decimals", 3)
    topItem.addSubProperty(item)

    item = variantManager.addProperty(QtCore.QVariant.String, str(3) + " String Property")
    item.setValue("Value")
    topItem.addSubProperty(item)

    item = variantManager.addProperty(QtCore.QVariant.Date, str(4) + " Date Property")
    item.setValue(QtCore.QDate.currentDate().addDays(2))
    topItem.addSubProperty(item)

    item = variantManager.addProperty(QtCore.QVariant.Time, str(5) + " Time Property")
    item.setValue(QtCore.QTime.currentTime())
    topItem.addSubProperty(item)

    item = variantManager.addProperty(QtCore.QVariant.DateTime, str(6) + " DateTime Property")
    item.setValue(QtCore.QDateTime.currentDateTime())
    topItem.addSubProperty(item)

    item = variantManager.addProperty(QtCore.QVariant.KeySequence, str(7) + " KeySequence Property")
    item.setValue(QtGui.QKeySequence(QtCore.Qt.ControlModifier | QtCore.Qt.Key_Q))
    topItem.addSubProperty(item)

    item = variantManager.addProperty(QtCore.QVariant.Char, str(8) + " Char Property")
    item.setValue(QtCore.QChar(386))
    topItem.addSubProperty(item)

    item = variantManager.addProperty(QtCore.QVariant.Locale, str(9) + " Locale Property")
    item.setValue(QtCore.QLocale(QtCore.QLocale.Polish, QtCore.QLocale.Poland))
    topItem.addSubProperty(item)

    item = variantManager.addProperty(QtCore.QVariant.Point, str(10) + " Point Property")
    item.setValue(QtCore.QPoint(10, 10))
    topItem.addSubProperty(item)

    item = variantManager.addProperty(QtCore.QVariant.PointF, str(11) + " PointF Property")
    item.setValue(QtCore.QPointF(1.2345, -1.23451))
    item.setAttribute("decimals", 3)
    topItem.addSubProperty(item)

    item = variantManager.addProperty(QtCore.QVariant.Size, str(12) + " Size Property")
    item.setValue(QtCore.QSize(20, 20))
    item.setAttribute("minimum", QtCore.QSize(10, 10))
    item.setAttribute("maximum", QtCore.QSize(30, 30))
    topItem.addSubProperty(item)

    item = variantManager.addProperty(QtCore.QVariant.SizeF, str(13) + " SizeF Property")
    item.setValue(QtCore.QSizeF(1.2345, 1.2345))
    item.setAttribute("decimals", 3)
    item.setAttribute("minimum", QtCore.QSizeF(0.12, 0.34))
    item.setAttribute("maximum", QtCore.QSizeF(20.56, 20.78))
    topItem.addSubProperty(item)

    item = variantManager.addProperty(QtCore.QVariant.Rect, str(14) + " Rect Property")
    item.setValue(QtCore.QRect(10, 10, 20, 20))
    topItem.addSubProperty(item)
    item.setAttribute("constraint", QtCore.QRect(0, 0, 50, 50))

    item = variantManager.addProperty(QtCore.QVariant.RectF, str(15) + " RectF Property")
    item.setValue(QtCore.QRectF(1.2345, 1.2345, 1.2345, 1.2345))
    topItem.addSubProperty(item)
    item.setAttribute("constraint", QtCore.QRectF(0, 0, 50, 50))
    item.setAttribute("decimals", 3)

    item = variantManager.addProperty(QtVariantPropertyManager.enumTypeId(), str(16) + " Enum Property")
    enumNames = []
    enumNames.append("Enum0")
    enumNames.append("Enum1")
    enumNames.append("Enum2")
    item.setAttribute("enumNames", enumNames)
    item.setValue(1)
    topItem.addSubProperty(item)

    item = variantManager.addProperty(QtVariantPropertyManager.flagTypeId(), str(17) + " Flag Property")
    flagNames = []
    flagNames.append("Flag0")
    flagNames.append("Flag1")
    flagNames.append("Flag2")
    item.setAttribute("flagNames", flagNames)
    item.setValue(5)
    topItem.addSubProperty(item)

    item = variantManager.addProperty(QtCore.QVariant.SizePolicy, str(18) + " SizePolicy Property")
    topItem.addSubProperty(item)

    item = variantManager.addProperty(QtCore.QVariant.Font, str(19) + " Font Property")
    topItem.addSubProperty(item)

    item = variantManager.addProperty(QtCore.QVariant.Cursor, str(20) + " Cursor Property")
    topItem.addSubProperty(item)

    item = variantManager.addProperty(QtCore.QVariant.Color, str(21) + " Color Property")
    topItem.addSubProperty(item)

    variantFactory = QtVariantEditorFactory()

    variantEditor = QtTreePropertyBrowser()

    variantEditor.setFactoryForManager(variantManager, variantFactory)
    variantEditor.addProperty(topItem)
    # variantEditor.setPropertiesWithoutValueMarked(True)
    # variantEditor.setRootIsDecorated(False)

    variantEditor.show()

    app.exec_()
    app.deleteLater()
    sys.exit()
