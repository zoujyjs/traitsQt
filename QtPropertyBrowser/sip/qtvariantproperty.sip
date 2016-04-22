/*
maybe needs to be wrapped
typedef QMap<int, QIcon> QtIconMap;
*/

%ModuleHeaderCode
#include <qtvariantproperty.h>

typedef QtAbstractEditorFactory<QtVariantPropertyManager> QtAbstractEditorFactoryQtVariantPropertyManager;
%End

typedef QtAbstractEditorFactory<QtVariantPropertyManager> QtAbstractEditorFactoryQtVariantPropertyManager /NoTypeName/;
class QtVariantProperty : QtProperty
{

%TypeHeaderCode
#include <qtvariantproperty.h>
%End

public:
    QVariant value() const;
    QVariant attributeValue(const QString &attribute) const;
    int valueType() const;
    int propertyType() const;

    void setValue(const QVariant &value);
    void setAttribute(const QString &attribute, const QVariant &value);

protected:
    QtVariantProperty(QtVariantPropertyManager *manager);
};


class QtVariantPropertyManager : QtAbstractPropertyManager
{

%TypeHeaderCode
#include <qtvariantproperty.h>
%End
  
public:
    QtVariantPropertyManager(QObject *parent /TransferThis/ = 0);

    virtual QtVariantProperty *addProperty(int propertyType, const QString &name = QString());

    int propertyType(const QtProperty *property) const;
    int valueType(const QtProperty *property /Constrained/) const;
    QtVariantProperty *variantProperty(const QtProperty *property) const;

    virtual bool isPropertyTypeSupported(int propertyType) const;
    virtual int valueType(int propertyType) const;
    virtual QStringList attributes(int propertyType) const;
    virtual int attributeType(int propertyType, const QString &attribute) const;

    virtual QVariant value(const QtProperty *property) const;
    virtual QVariant attributeValue(const QtProperty *property, const QString &attribute) const;

    static int enumTypeId();
    static int flagTypeId();
    static int groupTypeId();
    static int iconMapTypeId();
public slots:
    virtual void setValue(QtProperty *property, const QVariant &val);
    virtual void setAttribute(QtProperty *property, const QString &attribute, const QVariant &value);
signals:
    void valueChanged(QtProperty *property, const QVariant &val);
    void attributeChanged(QtProperty *property, const QString &attribute, const QVariant &val);
    
protected:
    virtual bool hasValue(const QtProperty *property) const;
    QString valueText(const QtProperty *property) const;
    QIcon valueIcon(const QtProperty *property) const;
    virtual void initializeProperty(QtProperty *property);
    virtual void uninitializeProperty(QtProperty *property);
    virtual QtProperty *createProperty();
};

class QtVariantEditorFactory : QtAbstractEditorFactoryQtVariantPropertyManager
{

%TypeHeaderCode
#include <qtvariantproperty.h>
%End

public:
    QtVariantEditorFactory(QObject *parent /TransferThis/ = 0);

protected:
    void connectPropertyManager(QtVariantPropertyManager *manager);
    QWidget *createEditorFromManager(QtVariantPropertyManager *manager, QtProperty *property, QWidget *parent /TransferThis/);
    void disconnectPropertyManager(QtVariantPropertyManager *manager);
};

/* maybe needs to be wrapped
Q_DECLARE_METATYPE(QIcon)
Q_DECLARE_METATYPE(QtIconMap)
*/
