%ModuleHeaderCode
#include <qteditorfactory.h>
typedef QtAbstractEditorFactory<QtIntPropertyManager> QtAbstractEditorFactoryQtIntPropertyManager;
typedef QtAbstractEditorFactory<QtDoublePropertyManager> QtAbstractEditorFactoryQtDoublePropertyManager;
typedef QtAbstractEditorFactory<QtBoolPropertyManager> QtAbstractEditorFactoryQtBoolPropertyManager;
typedef QtAbstractEditorFactory<QtStringPropertyManager> QtAbstractEditorFactoryQtStringPropertyManager;
typedef QtAbstractEditorFactory<QtDatePropertyManager> QtAbstractEditorFactoryQtDatePropertyManager;
typedef QtAbstractEditorFactory<QtTimePropertyManager> QtAbstractEditorFactoryQtTimePropertyManager;
typedef QtAbstractEditorFactory<QtDateTimePropertyManager> QtAbstractEditorFactoryQtDateTimePropertyManager;
typedef QtAbstractEditorFactory<QtKeySequencePropertyManager> QtAbstractEditorFactoryQtKeySequencePropertyManager;
typedef QtAbstractEditorFactory<QtCharPropertyManager> QtAbstractEditorFactoryQtCharPropertyManager;
typedef QtAbstractEditorFactory<QtEnumPropertyManager> QtAbstractEditorFactoryQtEnumPropertyManager;
typedef QtAbstractEditorFactory<QtCursorPropertyManager> QtAbstractEditorFactoryQtCursorPropertyManager;
typedef QtAbstractEditorFactory<QtColorPropertyManager> QtAbstractEditorFactoryQtColorPropertyManager;
typedef QtAbstractEditorFactory<QtFontPropertyManager> QtAbstractEditorFactoryQtFontPropertyManager;
%End

typedef QtAbstractEditorFactory<QtIntPropertyManager> QtAbstractEditorFactoryQtIntPropertyManager /NoTypeName/;
typedef QtAbstractEditorFactory<QtDoublePropertyManager> QtAbstractEditorFactoryQtDoublePropertyManager /NoTypeName/;
typedef QtAbstractEditorFactory<QtBoolPropertyManager> QtAbstractEditorFactoryQtBoolPropertyManager /NoTypeName/;
typedef QtAbstractEditorFactory<QtStringPropertyManager> QtAbstractEditorFactoryQtStringPropertyManager /NoTypeName/;
typedef QtAbstractEditorFactory<QtDatePropertyManager> QtAbstractEditorFactoryQtDatePropertyManager /NoTypeName/;
typedef QtAbstractEditorFactory<QtTimePropertyManager> QtAbstractEditorFactoryQtTimePropertyManager /NoTypeName/;
typedef QtAbstractEditorFactory<QtDateTimePropertyManager> QtAbstractEditorFactoryQtDateTimePropertyManager /NoTypeName/;
typedef QtAbstractEditorFactory<QtKeySequencePropertyManager> QtAbstractEditorFactoryQtKeySequencePropertyManager /NoTypeName/;
typedef QtAbstractEditorFactory<QtCharPropertyManager> QtAbstractEditorFactoryQtCharPropertyManager /NoTypeName/;
typedef QtAbstractEditorFactory<QtEnumPropertyManager> QtAbstractEditorFactoryQtEnumPropertyManager /NoTypeName/;
typedef QtAbstractEditorFactory<QtCursorPropertyManager> QtAbstractEditorFactoryQtCursorPropertyManager /NoTypeName/;
typedef QtAbstractEditorFactory<QtColorPropertyManager> QtAbstractEditorFactoryQtColorPropertyManager /NoTypeName/;
typedef QtAbstractEditorFactory<QtFontPropertyManager> QtAbstractEditorFactoryQtFontPropertyManager /NoTypeName/;
class QtSpinBoxFactory : QtAbstractEditorFactoryQtIntPropertyManager
{

%TypeHeaderCode
#include <qteditorfactory.h>
%End

public:
    QtSpinBoxFactory(QObject *parent /TransferThis/ = 0);

protected:
    void connectPropertyManager(QtIntPropertyManager *manager);
    QWidget *createEditorFromManager(QtIntPropertyManager *manager, QtProperty *property, QWidget *parent /TransferThis/);
    void disconnectPropertyManager(QtIntPropertyManager *manager);
};

class QtSliderFactory : QtAbstractEditorFactoryQtIntPropertyManager
{

%TypeHeaderCode
#include <qteditorfactory.h>
%End

public:
    QtSliderFactory(QObject *parent /TransferThis/ = 0);

protected:
    void connectPropertyManager(QtIntPropertyManager *manager);
    QWidget *createEditorFromManager(QtIntPropertyManager *manager, QtProperty *property, QWidget *parent /TransferThis/);
    void disconnectPropertyManager(QtIntPropertyManager *manager);
};

class QtScrollBarFactory : QtAbstractEditorFactoryQtIntPropertyManager
{

%TypeHeaderCode
#include <qteditorfactory.h>
%End

public:
    QtScrollBarFactory(QObject *parent /TransferThis/ = 0);

protected:
    void connectPropertyManager(QtIntPropertyManager *manager);
    QWidget *createEditorFromManager(QtIntPropertyManager *manager, QtProperty *property, QWidget *parent /TransferThis/);
    void disconnectPropertyManager(QtIntPropertyManager *manager);
};

class QtCheckBoxFactory : QtAbstractEditorFactoryQtBoolPropertyManager
{

%TypeHeaderCode
#include <qteditorfactory.h>
%End

public:
    QtCheckBoxFactory(QObject *parent /TransferThis/ = 0);

protected:
    void connectPropertyManager(QtBoolPropertyManager *manager);
    QWidget *createEditorFromManager(QtBoolPropertyManager *manager, QtProperty *property, QWidget *parent /TransferThis/);
    void disconnectPropertyManager(QtBoolPropertyManager *manager);
};

class QtDoubleSpinBoxFactory : QtAbstractEditorFactoryQtDoublePropertyManager
{

%TypeHeaderCode
#include <qteditorfactory.h>
%End
public:
    QtDoubleSpinBoxFactory(QObject *parent /TransferThis/ = 0);

protected:
    void connectPropertyManager(QtDoublePropertyManager *manager);
    QWidget *createEditorFromManager(QtDoublePropertyManager *manager, QtProperty *property,
                QWidget *parent /TransferThis/);
    void disconnectPropertyManager(QtDoublePropertyManager *manager);
};

class QtLineEditFactory : QtAbstractEditorFactoryQtStringPropertyManager
{

%TypeHeaderCode
#include <qteditorfactory.h>
%End

public:
    QtLineEditFactory(QObject *parent /TransferThis/ = 0);

protected:
    void connectPropertyManager(QtStringPropertyManager *manager);
    QWidget *createEditorFromManager(QtStringPropertyManager *manager, QtProperty *property, QWidget *parent /TransferThis/);
    void disconnectPropertyManager(QtStringPropertyManager *manager);
};

class QtDateEditFactory : QtAbstractEditorFactoryQtDatePropertyManager
{

%TypeHeaderCode
#include <qteditorfactory.h>
%End

public:
    QtDateEditFactory(QObject *parent /TransferThis/ = 0);

protected:
    void connectPropertyManager(QtDatePropertyManager *manager);
    QWidget *createEditorFromManager(QtDatePropertyManager *manager, QtProperty *property, QWidget *parent /TransferThis/);
    void disconnectPropertyManager(QtDatePropertyManager *manager);
};

class QtTimeEditFactory : QtAbstractEditorFactoryQtTimePropertyManager
{

%TypeHeaderCode
#include <qteditorfactory.h>
%End

public:
    QtTimeEditFactory(QObject *parent /TransferThis/ = 0);

protected:
    void connectPropertyManager(QtTimePropertyManager *manager);
    QWidget *createEditorFromManager(QtTimePropertyManager *manager, QtProperty *property, QWidget *parent /TransferThis/);
    void disconnectPropertyManager(QtTimePropertyManager *manager);
};

class QtDateTimeEditFactory : QtAbstractEditorFactoryQtDateTimePropertyManager
{

%TypeHeaderCode
#include <qteditorfactory.h>
%End

public:
    QtDateTimeEditFactory(QObject *parent /TransferThis/ = 0);

protected:
    void connectPropertyManager(QtDateTimePropertyManager *manager);
    QWidget *createEditorFromManager(QtDateTimePropertyManager *manager, QtProperty *property, QWidget *parent /TransferThis/);
    void disconnectPropertyManager(QtDateTimePropertyManager *manager);
};

class QtKeySequenceEditorFactory : QtAbstractEditorFactoryQtKeySequencePropertyManager
{

%TypeHeaderCode
#include <qteditorfactory.h>
%End

public:
    QtKeySequenceEditorFactory(QObject *parent /TransferThis/ = 0);

protected:
    void connectPropertyManager(QtKeySequencePropertyManager *manager);
    QWidget *createEditorFromManager(QtKeySequencePropertyManager *manager, QtProperty *property, QWidget *parent /TransferThis/);
    void disconnectPropertyManager(QtKeySequencePropertyManager *manager);
};

class QtCharEditorFactory : QtAbstractEditorFactoryQtCharPropertyManager
{

%TypeHeaderCode
#include <qteditorfactory.h>
%End

public:
    QtCharEditorFactory(QObject *parent /TransferThis/ = 0);

protected:
    void connectPropertyManager(QtCharPropertyManager *manager);
    QWidget *createEditorFromManager(QtCharPropertyManager *manager, QtProperty *property, QWidget *parent /TransferThis/);
    void disconnectPropertyManager(QtCharPropertyManager *manager);
};

class QtEnumEditorFactory : QtAbstractEditorFactoryQtEnumPropertyManager
{

%TypeHeaderCode
#include <qteditorfactory.h>
%End

public:
    QtEnumEditorFactory(QObject *parent /TransferThis/ = 0);

protected:
    void connectPropertyManager(QtEnumPropertyManager *manager);
    QWidget *createEditorFromManager(QtEnumPropertyManager *manager, QtProperty *property, QWidget *parent /TransferThis/);
    void disconnectPropertyManager(QtEnumPropertyManager *manager);
};

class QtCursorEditorFactory : QtAbstractEditorFactoryQtCursorPropertyManager
{

%TypeHeaderCode
#include <qteditorfactory.h>
%End

public:
    QtCursorEditorFactory(QObject *parent /TransferThis/ = 0);

protected:
    void connectPropertyManager(QtCursorPropertyManager *manager);
    QWidget *createEditorFromManager(QtCursorPropertyManager *manager, QtProperty *property, QWidget *parent /TransferThis/);
    void disconnectPropertyManager(QtCursorPropertyManager *manager);
};

class QtColorEditorFactory : QtAbstractEditorFactoryQtColorPropertyManager
{

%TypeHeaderCode
#include <qteditorfactory.h>
%End

public:
    QtColorEditorFactory(QObject *parent /TransferThis/ = 0);

protected:
    void connectPropertyManager(QtColorPropertyManager *manager);
    QWidget *createEditorFromManager(QtColorPropertyManager *manager, QtProperty *property, QWidget *parent /TransferThis/);
    void disconnectPropertyManager(QtColorPropertyManager *manager);
};

class QtFontEditorFactory : QtAbstractEditorFactoryQtFontPropertyManager
{

%TypeHeaderCode
#include <qteditorfactory.h>
%End

public:
    QtFontEditorFactory(QObject *parent /TransferThis/ = 0);

protected:
    void connectPropertyManager(QtFontPropertyManager *manager);
    QWidget *createEditorFromManager(QtFontPropertyManager *manager, QtProperty *property, QWidget *parent /TransferThis/);
    void disconnectPropertyManager(QtFontPropertyManager *manager);
};
