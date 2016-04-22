%ModuleHeaderCode
#include <qtpropertybrowser.h>
typedef QLineEdit::EchoMode EchoMode;
%End
typedef QLineEdit::EchoMode EchoMode;

class QtProperty
{
  
%TypeHeaderCode
#include <qtpropertybrowser.h>
%End

%ConvertToSubClassCode
    // Auto cast to subclass type according to rtti.
    if (typeid(*sipCpp) == typeid(QtProperty)){
        sipType = sipType_QtProperty;
    } else if (typeid(*sipCpp) == typeid(QtVariantProperty)) {
        sipType = sipType_QtVariantProperty;
    } else {
        // We don't recognise the type.
        sipType = NULL;
    }
%End

public:
    QList<QtProperty *> subProperties() const;

    QtAbstractPropertyManager *propertyManager() const;

    QString toolTip() const;
    QString statusTip() const;
    QString whatsThis() const;
    QString propertyName() const;
    bool isEnabled() const;
    bool isModified() const;

    bool hasValue() const;
    QIcon valueIcon() const;
    QString valueText() const;
    QString displayText() const;

    void setToolTip(const QString &text);
    void setStatusTip(const QString &text);
    void setWhatsThis(const QString &text);
    void setPropertyName(const QString &text);
    void setEnabled(bool enable);
    void setModified(bool modified);

    void addSubProperty(QtProperty *property);
    void insertSubProperty(QtProperty *property, QtProperty *afterProperty);
    void removeSubProperty(QtProperty *property);
    
protected:
    explicit QtProperty(QtAbstractPropertyManager *manager);
    void propertyChanged();
};

class QtAbstractPropertyManager : QObject
{

%TypeHeaderCode
#include <qtpropertybrowser.h>
%End  

public:

    explicit QtAbstractPropertyManager(QObject *parent /TransferThis/ = 0);

    QSet<QtProperty *> properties() const;
    void clear() const;

    QtProperty *addProperty(const QString &name = QString());
signals:
    void propertyInserted(QtProperty *property, QtProperty *parent /TransferThis/, QtProperty *after);
    void propertyChanged(QtProperty *property);
    void propertyRemoved(QtProperty *property, QtProperty *parent /TransferThis/);
    void propertyDestroyed(QtProperty *property);
protected:
    virtual bool hasValue(const QtProperty *property) const;
    virtual QIcon valueIcon(const QtProperty *property) const;
    virtual QString valueText(const QtProperty *property) const;
    virtual QString displayText(const QtProperty *property) const;
    virtual EchoMode echoMode(const QtProperty *) const;
    virtual void initializeProperty(QtProperty *property) = 0;
    virtual void uninitializeProperty(QtProperty *property);
    virtual QtProperty *createProperty();
};

class QtAbstractEditorFactoryBase : QObject
{

%TypeHeaderCode
#include <qtpropertybrowser.h>
%End

public:
    virtual QWidget *createEditor(QtProperty *property, QWidget *parent /TransferThis/) = 0;
    
protected:
    explicit QtAbstractEditorFactoryBase(QObject *parent /TransferThis/ = 0);

    virtual void breakConnection(QtAbstractPropertyManager *manager) = 0;

protected slots:
    virtual void managerDestroyed(QObject *manager) = 0;
};

template <PropertyManager>
class QtAbstractEditorFactory : QtAbstractEditorFactoryBase
{
  
%TypeHeaderCode
#include <qtpropertybrowser.h>
%End
  
public:
    explicit QtAbstractEditorFactory(QObject *parent /TransferThis/);
    QWidget *createEditor(QtProperty *property, QWidget *parent /TransferThis/);
    void addPropertyManager(PropertyManager *manager);
    void removePropertyManager(PropertyManager *manager);
    QSet<PropertyManager *> propertyManagers() const;

    PropertyManager *propertyManager(QtProperty *property) const;
    
protected:
    virtual void connectPropertyManager(PropertyManager *manager) = 0;
    virtual QWidget *createEditorFromManager(PropertyManager *manager, QtProperty *property, QWidget *parent /TransferThis/) = 0;
    virtual void disconnectPropertyManager(PropertyManager *manager) = 0;
    void managerDestroyed(QObject *manager);
private:
    void breakConnection(QtAbstractPropertyManager *manager);
};

class QtBrowserItem
{
  
%TypeHeaderCode
#include <qtpropertybrowser.h>
%End
  
public:
    QtProperty *property() const;
    QtBrowserItem *parent() const;
    QList<QtBrowserItem *> children() const;
    QtAbstractPropertyBrowser *browser() const;
private:
    explicit QtBrowserItem(QtAbstractPropertyBrowser *browser, QtProperty *property, QtBrowserItem *parent /TransferThis/);
    ~QtBrowserItem();
};

%ModuleHeaderCode
#include <qtpropertybrowser.h>
typedef QtAbstractEditorFactory<QtAbstractPropertyManager> QtAbstractEditorFactoryQtAbstractPropertyManager;
%End

typedef QtAbstractEditorFactory<QtAbstractPropertyManager> QtAbstractEditorFactoryQtAbstractPropertyManager /NoTypeName/;

class QtAbstractPropertyBrowser : QWidget
{

%TypeHeaderCode
#include <qtpropertybrowser.h>
%End

public:
    explicit QtAbstractPropertyBrowser(QWidget *parent /TransferThis/ = 0);

    QList<QtProperty *> properties() const;
    QList<QtBrowserItem *> items(QtProperty *property) const;
    QtBrowserItem *topLevelItem(QtProperty *property) const;
    QList<QtBrowserItem *> topLevelItems() const;
    void clear();

    void setFactoryForManager(QtAbstractPropertyManager *manager, QtAbstractEditorFactoryQtAbstractPropertyManager *factory);
    void setFactoryForManager(QtVariantPropertyManager *manager, QtAbstractEditorFactoryQtVariantPropertyManager *factory);
    void setFactoryForManager(QtIntPropertyManager *manager, QtAbstractEditorFactoryQtIntPropertyManager *factory);
    void setFactoryForManager(QtDoublePropertyManager *manager, QtAbstractEditorFactoryQtDoublePropertyManager *factory);
    void setFactoryForManager(QtBoolPropertyManager *manager, QtAbstractEditorFactoryQtBoolPropertyManager *factory);
    void setFactoryForManager(QtStringPropertyManager *manager, QtAbstractEditorFactoryQtStringPropertyManager *factory);
    void setFactoryForManager(QtDatePropertyManager *manager, QtAbstractEditorFactoryQtDatePropertyManager *factory);
    void setFactoryForManager(QtTimePropertyManager *manager, QtAbstractEditorFactoryQtTimePropertyManager *factory);
    void setFactoryForManager(QtDateTimePropertyManager *manager, QtAbstractEditorFactoryQtDateTimePropertyManager *factory);
    void setFactoryForManager(QtKeySequencePropertyManager *manager, QtAbstractEditorFactoryQtKeySequencePropertyManager *factory);
    void setFactoryForManager(QtCharPropertyManager *manager, QtAbstractEditorFactoryQtCharPropertyManager *factory);
    void setFactoryForManager(QtEnumPropertyManager *manager, QtAbstractEditorFactoryQtEnumPropertyManager *factory);
    void setFactoryForManager(QtCursorPropertyManager *manager, QtAbstractEditorFactoryQtCursorPropertyManager *factory);
    void setFactoryForManager(QtColorPropertyManager *manager, QtAbstractEditorFactoryQtColorPropertyManager *factory);
    void setFactoryForManager(QtFontPropertyManager *manager, QtAbstractEditorFactoryQtFontPropertyManager *factory);
    void unsetFactoryForManager(QtAbstractPropertyManager *manager);

    QtBrowserItem *currentItem() const;
    void setCurrentItem(QtBrowserItem *);

signals:
    void currentItemChanged(QtBrowserItem *);

public slots:

    QtBrowserItem *addProperty(QtProperty *property);
    QtBrowserItem *insertProperty(QtProperty *property, QtProperty *afterProperty);
    void removeProperty(QtProperty *property);

protected:

    virtual void itemInserted(QtBrowserItem *item, QtBrowserItem *afterItem) = 0;
    virtual void itemRemoved(QtBrowserItem *item) = 0;
    // can be tooltip, statustip, whatsthis, name, icon, text.
    virtual void itemChanged(QtBrowserItem *item) = 0;

    virtual QWidget *createEditor(QtProperty *property, QWidget *parent /TransferThis/);
};
