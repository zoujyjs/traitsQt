class QtGroupPropertyManager: QtAbstractPropertyManager {

%TypeHeaderCode
#include <qtpropertymanager.h>
%End
public:
    QtGroupPropertyManager(QObject *parent /TransferThis/ = 0);

protected:
    virtual bool hasValue(const QtProperty *property) const;

    virtual void initializeProperty(QtProperty *property);
    virtual void uninitializeProperty(QtProperty *property);
};

class QtIntPropertyManager : QtAbstractPropertyManager
{

%TypeHeaderCode
#include <qtpropertymanager.h>
%End

public:
    QtIntPropertyManager(QObject *parent /TransferThis/ = 0);

    int value(const QtProperty *property) const;
    int minimum(const QtProperty *property) const;
    int maximum(const QtProperty *property) const;
    int singleStep(const QtProperty *property) const;
    bool isReadOnly(const QtProperty *property) const;

public slots:
    void setValue(QtProperty *property, int val);
    void setMinimum(QtProperty *property, int minVal);
    void setMaximum(QtProperty *property, int maxVal);
    void setRange(QtProperty *property, int minVal, int maxVal);
    void setSingleStep(QtProperty *property, int step);
    void setReadOnly(QtProperty *property, bool readOnly);
Q_SIGNALS:
    void valueChanged(QtProperty *property, int val);
    void rangeChanged(QtProperty *property, int minVal, int maxVal);
    void singleStepChanged(QtProperty *property, int step);
    void readOnlyChanged(QtProperty *property, bool readOnly);
protected:
    QString valueText(const QtProperty *property) const;
    virtual void initializeProperty(QtProperty *property);
    virtual void uninitializeProperty(QtProperty *property);
};


class QtBoolPropertyManager : QtAbstractPropertyManager
{

%TypeHeaderCode
#include <qtpropertymanager.h>
%End

public:
    QtBoolPropertyManager(QObject *parent /TransferThis/ = 0);

    bool value(const QtProperty *property) const;
    bool textVisible(const QtProperty *property) const;

public slots:
    void setValue(QtProperty *property, bool val);
    void setTextVisible(QtProperty *property, bool textVisible);
Q_SIGNALS:
    void valueChanged(QtProperty *property, bool val);
    void textVisibleChanged(QtProperty *property, bool);
protected:
    QString valueText(const QtProperty *property) const;
    QIcon valueIcon(const QtProperty *property) const;
    virtual void initializeProperty(QtProperty *property);
    virtual void uninitializeProperty(QtProperty *property);
};


class QtDoublePropertyManager : QtAbstractPropertyManager
{

%TypeHeaderCode
#include <qtpropertymanager.h>
%End

public:
    QtDoublePropertyManager(QObject *parent /TransferThis/ = 0);

    double value(const QtProperty *property) const;
    double minimum(const QtProperty *property) const;
    double maximum(const QtProperty *property) const;
    double singleStep(const QtProperty *property) const;
    int decimals(const QtProperty *property) const;
    bool isReadOnly(const QtProperty *property) const;

public slots:
    void setValue(QtProperty *property, double val);
    void setMinimum(QtProperty *property, double minVal);
    void setMaximum(QtProperty *property, double maxVal);
    void setRange(QtProperty *property, double minVal, double maxVal);
    void setSingleStep(QtProperty *property, double step);
    void setDecimals(QtProperty *property, int prec);
    void setReadOnly(QtProperty *property, bool readOnly);
Q_SIGNALS:
    void valueChanged(QtProperty *property, double val);
    void rangeChanged(QtProperty *property, double minVal, double maxVal);
    void singleStepChanged(QtProperty *property, double step);
    void decimalsChanged(QtProperty *property, int prec);
    void readOnlyChanged(QtProperty *property, bool readOnly);
protected:
    QString valueText(const QtProperty *property) const;
    virtual void initializeProperty(QtProperty *property);
    virtual void uninitializeProperty(QtProperty *property);
};

class QtStringPropertyManager : QtAbstractPropertyManager
{

%TypeHeaderCode
#include <qtpropertymanager.h>
%End

public:
    QtStringPropertyManager(QObject *parent /TransferThis/ = 0);

    QString value(const QtProperty *property) const;
    QRegExp regExp(const QtProperty *property) const;
    EchoMode echoMode(const QtProperty *property) const;
    bool isReadOnly(const QtProperty *property) const;

public slots:
    void setValue(QtProperty *property, const QString &val);
    void setRegExp(QtProperty *property, const QRegExp &regExp);
    void setEchoMode(QtProperty *property, EchoMode echoMode);
    void setReadOnly(QtProperty *property, bool readOnly);

Q_SIGNALS:
    void valueChanged(QtProperty *property, const QString &val);
    void regExpChanged(QtProperty *property, const QRegExp &regExp);
    void echoModeChanged(QtProperty *property, const int);
    void readOnlyChanged(QtProperty *property, bool);

protected:
    QString valueText(const QtProperty *property) const;
    QString displayText(const QtProperty *property) const;
    virtual void initializeProperty(QtProperty *property);
    virtual void uninitializeProperty(QtProperty *property);
};

class QtDatePropertyManager : QtAbstractPropertyManager
{

%TypeHeaderCode
#include <qtpropertymanager.h>
%End

public:
    QtDatePropertyManager(QObject *parent /TransferThis/ = 0);

    QDate value(const QtProperty *property) const;
    QDate minimum(const QtProperty *property) const;
    QDate maximum(const QtProperty *property) const;

public slots:
    void setValue(QtProperty *property, const QDate &val);
    void setMinimum(QtProperty *property, const QDate &minVal);
    void setMaximum(QtProperty *property, const QDate &maxVal);
    void setRange(QtProperty *property, const QDate &minVal, const QDate &maxVal);
signals:
    void valueChanged(QtProperty *property, const QDate &val);
    void rangeChanged(QtProperty *property, const QDate &minVal, const QDate &maxVal);

protected:
    QString valueText(const QtProperty *property) const;
    virtual void initializeProperty(QtProperty *property);
    virtual void uninitializeProperty(QtProperty *property);
};

class QtTimePropertyManager : QtAbstractPropertyManager
{

%TypeHeaderCode
#include <qtpropertymanager.h>
%End

public:
    QtTimePropertyManager(QObject *parent /TransferThis/ = 0);

    QTime value(const QtProperty *property) const;

public slots:
    void setValue(QtProperty *property, const QTime &val);
signals:
    void valueChanged(QtProperty *property, const QTime &val);

protected:
    QString valueText(const QtProperty *property) const;
    virtual void initializeProperty(QtProperty *property);
    virtual void uninitializeProperty(QtProperty *property);
};

class QtDateTimePropertyManager : QtAbstractPropertyManager
{

%TypeHeaderCode
#include <qtpropertymanager.h>
%End

public:
    QtDateTimePropertyManager(QObject *parent /TransferThis/ = 0);

    QDateTime value(const QtProperty *property) const;

public slots:
    void setValue(QtProperty *property, const QDateTime &val);
signals:
    void valueChanged(QtProperty *property, const QDateTime &val);

protected:
    QString valueText(const QtProperty *property) const;
    virtual void initializeProperty(QtProperty *property);
    virtual void uninitializeProperty(QtProperty *property);
};

class QtKeySequencePropertyManager : QtAbstractPropertyManager
{

%TypeHeaderCode
#include <qtpropertymanager.h>
%End

public:
    QtKeySequencePropertyManager(QObject *parent /TransferThis/ = 0);

    QKeySequence value(const QtProperty *property) const;

public slots:
    void setValue(QtProperty *property, const QKeySequence &val);
signals:
    void valueChanged(QtProperty *property, const QKeySequence &val);

protected:
    QString valueText(const QtProperty *property) const;
    virtual void initializeProperty(QtProperty *property);
    virtual void uninitializeProperty(QtProperty *property);
};

class QtCharPropertyManager : QtAbstractPropertyManager
{

%TypeHeaderCode
#include <qtpropertymanager.h>
%End

public:
    QtCharPropertyManager(QObject *parent /TransferThis/ = 0);

    QChar value(const QtProperty *property) const;

public slots:
    void setValue(QtProperty *property, const QChar &val);
signals:
    void valueChanged(QtProperty *property, const QChar &val);

protected:
    QString valueText(const QtProperty *property) const;
    virtual void initializeProperty(QtProperty *property);
    virtual void uninitializeProperty(QtProperty *property);
};

class QtLocalePropertyManager : QtAbstractPropertyManager
{

%TypeHeaderCode
#include <qtpropertymanager.h>
%End

public:
    QtLocalePropertyManager(QObject *parent /TransferThis/ = 0);

    QtEnumPropertyManager *subEnumPropertyManager() const;

    QLocale value(const QtProperty *property) const;

public slots:
    void setValue(QtProperty *property, const QLocale &val);
signals:
    void valueChanged(QtProperty *property, const QLocale &val);

protected:
    QString valueText(const QtProperty *property) const;
    virtual void initializeProperty(QtProperty *property);
    virtual void uninitializeProperty(QtProperty *property);
};

class QtPointPropertyManager : QtAbstractPropertyManager
{

%TypeHeaderCode
#include <qtpropertymanager.h>
%End

public:
    QtPointPropertyManager(QObject *parent /TransferThis/ = 0);

    QtIntPropertyManager *subIntPropertyManager() const;

    QPoint value(const QtProperty *property) const;

public slots:
    void setValue(QtProperty *property, const QPoint &val);
signals:
    void valueChanged(QtProperty *property, const QPoint &val);

protected:
    QString valueText(const QtProperty *property) const;
    virtual void initializeProperty(QtProperty *property);
    virtual void uninitializeProperty(QtProperty *property);
};

class QtPointFPropertyManager : QtAbstractPropertyManager
{

%TypeHeaderCode
#include <qtpropertymanager.h>
%End

public:
    QtPointFPropertyManager(QObject *parent /TransferThis/ = 0);

    QtDoublePropertyManager *subDoublePropertyManager() const;

    QPointF value(const QtProperty *property) const;
    int decimals(const QtProperty *property) const;

public slots:
    void setValue(QtProperty *property, const QPointF &val);
    void setDecimals(QtProperty *property, int prec);
signals:
    void valueChanged(QtProperty *property, const QPointF &val);
    void decimalsChanged(QtProperty *property, int prec);

protected:
    QString valueText(const QtProperty *property) const;
    virtual void initializeProperty(QtProperty *property);
    virtual void uninitializeProperty(QtProperty *property);
};

class QtSizePropertyManager : QtAbstractPropertyManager
{

%TypeHeaderCode
#include <qtpropertymanager.h>
%End

public:
    QtSizePropertyManager(QObject *parent /TransferThis/ = 0);

    QtIntPropertyManager *subIntPropertyManager() const;

    QSize value(const QtProperty *property) const;
    QSize minimum(const QtProperty *property) const;
    QSize maximum(const QtProperty *property) const;

public slots:
    void setValue(QtProperty *property, const QSize &val);
    void setMinimum(QtProperty *property, const QSize &minVal);
    void setMaximum(QtProperty *property, const QSize &maxVal);
    void setRange(QtProperty *property, const QSize &minVal, const QSize &maxVal);
signals:
    void valueChanged(QtProperty *property, const QSize &val);
    void rangeChanged(QtProperty *property, const QSize &minVal, const QSize &maxVal);

protected:
    QString valueText(const QtProperty *property) const;
    virtual void initializeProperty(QtProperty *property);
    virtual void uninitializeProperty(QtProperty *property);
};

class QtSizeFPropertyManager : QtAbstractPropertyManager
{

%TypeHeaderCode
#include <qtpropertymanager.h>
%End

public:
    QtSizeFPropertyManager(QObject *parent /TransferThis/ = 0);

    QtDoublePropertyManager *subDoublePropertyManager() const;

    QSizeF value(const QtProperty *property) const;
    QSizeF minimum(const QtProperty *property) const;
    QSizeF maximum(const QtProperty *property) const;
    int decimals(const QtProperty *property) const;

public slots:
    void setValue(QtProperty *property, const QSizeF &val);
    void setMinimum(QtProperty *property, const QSizeF &minVal);
    void setMaximum(QtProperty *property, const QSizeF &maxVal);
    void setRange(QtProperty *property, const QSizeF &minVal, const QSizeF &maxVal);
    void setDecimals(QtProperty *property, int prec);
signals:
    void valueChanged(QtProperty *property, const QSizeF &val);
    void rangeChanged(QtProperty *property, const QSizeF &minVal, const QSizeF &maxVal);
    void decimalsChanged(QtProperty *property, int prec);

protected:
    QString valueText(const QtProperty *property) const;
    virtual void initializeProperty(QtProperty *property);
    virtual void uninitializeProperty(QtProperty *property);
};

class QtRectPropertyManager : QtAbstractPropertyManager
{

%TypeHeaderCode
#include <qtpropertymanager.h>
%End

public:
    QtRectPropertyManager(QObject *parent /TransferThis/ = 0);

    QtIntPropertyManager *subIntPropertyManager() const;

    QRect value(const QtProperty *property) const;
    QRect constraint(const QtProperty *property) const;

public slots:
    void setValue(QtProperty *property, const QRect &val);
    void setConstraint(QtProperty *property, const QRect &constraint);
signals:
    void valueChanged(QtProperty *property, const QRect &val);
    void constraintChanged(QtProperty *property, const QRect &constraint);

protected:
    QString valueText(const QtProperty *property) const;
    virtual void initializeProperty(QtProperty *property);
    virtual void uninitializeProperty(QtProperty *property);
};

class QtRectFPropertyManager : QtAbstractPropertyManager
{

%TypeHeaderCode
#include <qtpropertymanager.h>
%End

public:
    QtRectFPropertyManager(QObject *parent /TransferThis/ = 0);

    QtDoublePropertyManager *subDoublePropertyManager() const;

    QRectF value(const QtProperty *property) const;
    QRectF constraint(const QtProperty *property) const;
    int decimals(const QtProperty *property) const;

public slots:
    void setValue(QtProperty *property, const QRectF &val);
    void setConstraint(QtProperty *property, const QRectF &constraint);
    void setDecimals(QtProperty *property, int prec);
signals:
    void valueChanged(QtProperty *property, const QRectF &val);
    void constraintChanged(QtProperty *property, const QRectF &constraint);
    void decimalsChanged(QtProperty *property, int prec);

protected:
    QString valueText(const QtProperty *property) const;
    virtual void initializeProperty(QtProperty *property);
    virtual void uninitializeProperty(QtProperty *property);
};

class QtEnumPropertyManager : QtAbstractPropertyManager
{

%TypeHeaderCode
#include <qtpropertymanager.h>
%End

public:
    QtEnumPropertyManager(QObject *parent /TransferThis/ = 0);

    int value(const QtProperty *property) const;
    QStringList enumNames(const QtProperty *property) const;
    QMap<int, QIcon> enumIcons(const QtProperty *property) const;

public slots:
    void setValue(QtProperty *property, int val);
    void setEnumNames(QtProperty *property, const QStringList &names);
    void setEnumIcons(QtProperty *property, const QMap<int, QIcon> &icons);
signals:
    void valueChanged(QtProperty *property, int val);
    void enumNamesChanged(QtProperty *property, const QStringList &names);
    void enumIconsChanged(QtProperty *property, const QMap<int, QIcon> &icons);

protected:
    QString valueText(const QtProperty *property) const;
    QIcon valueIcon(const QtProperty *property) const;
    virtual void initializeProperty(QtProperty *property);
    virtual void uninitializeProperty(QtProperty *property);
};

class QtFlagPropertyManager : QtAbstractPropertyManager
{

%TypeHeaderCode
#include <qtpropertymanager.h>
%End

public:
    QtFlagPropertyManager(QObject *parent /TransferThis/ = 0);

    QtBoolPropertyManager *subBoolPropertyManager() const;

    int value(const QtProperty *property) const;
    QStringList flagNames(const QtProperty *property) const;

public slots:
    void setValue(QtProperty *property, int val);
    void setFlagNames(QtProperty *property, const QStringList &names);
signals:
    void valueChanged(QtProperty *property, int val);
    void flagNamesChanged(QtProperty *property, const QStringList &names);

protected:
    QString valueText(const QtProperty *property) const;
    virtual void initializeProperty(QtProperty *property);
    virtual void uninitializeProperty(QtProperty *property);
};

class QtSizePolicyPropertyManager : QtAbstractPropertyManager
{

%TypeHeaderCode
#include <qtpropertymanager.h>
%End

public:
    QtSizePolicyPropertyManager(QObject *parent /TransferThis/ = 0);

    QtIntPropertyManager *subIntPropertyManager() const;
    QtEnumPropertyManager *subEnumPropertyManager() const;

    QSizePolicy value(const QtProperty *property) const;

public slots:
    void setValue(QtProperty *property, const QSizePolicy &val);
signals:
    void valueChanged(QtProperty *property, const QSizePolicy &val);

protected:
    QString valueText(const QtProperty *property) const;
    virtual void initializeProperty(QtProperty *property);
    virtual void uninitializeProperty(QtProperty *property);
};

class QtFontPropertyManager : QtAbstractPropertyManager
{

%TypeHeaderCode
#include <qtpropertymanager.h>
%End

public:
    QtFontPropertyManager(QObject *parent /TransferThis/ = 0);

    QtIntPropertyManager *subIntPropertyManager() const;
    QtEnumPropertyManager *subEnumPropertyManager() const;
    QtBoolPropertyManager *subBoolPropertyManager() const;

    QFont value(const QtProperty *property) const;

public slots:
    void setValue(QtProperty *property, const QFont &val);
signals:
    void valueChanged(QtProperty *property, const QFont &val);

protected:
    QString valueText(const QtProperty *property) const;
    QIcon valueIcon(const QtProperty *property) const;
    virtual void initializeProperty(QtProperty *property);
    virtual void uninitializeProperty(QtProperty *property);
};

class QtColorPropertyManager : QtAbstractPropertyManager
{

%TypeHeaderCode
#include <qtpropertymanager.h>
%End

public:
    QtColorPropertyManager(QObject *parent /TransferThis/ = 0);

    QtIntPropertyManager *subIntPropertyManager() const;

    QColor value(const QtProperty *property) const;

public slots:
    void setValue(QtProperty *property, const QColor &val);
signals:
    void valueChanged(QtProperty *property, const QColor &val);

protected:
    QString valueText(const QtProperty *property) const;
    QIcon valueIcon(const QtProperty *property) const;
    virtual void initializeProperty(QtProperty *property);
    virtual void uninitializeProperty(QtProperty *property);
};

class QtCursorPropertyManager : QtAbstractPropertyManager
{

%TypeHeaderCode
#include <qtpropertymanager.h>
%End

public:
    QtCursorPropertyManager(QObject *parent /TransferThis/ = 0);

public slots:
    void setValue(QtProperty *property, const QCursor &val);
signals:
    void valueChanged(QtProperty *property, const QCursor &val);

protected:
    QString valueText(const QtProperty *property) const;
    QIcon valueIcon(const QtProperty *property) const;
    virtual void initializeProperty(QtProperty *property);
    virtual void uninitializeProperty(QtProperty *property);
};


