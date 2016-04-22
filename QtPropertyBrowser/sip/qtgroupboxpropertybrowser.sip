class QtGroupBoxPropertyBrowser : QtAbstractPropertyBrowser
{

%TypeHeaderCode
#include <qtgroupboxpropertybrowser.h>
%End

public:

    QtGroupBoxPropertyBrowser(QWidget *parent /TransferThis/ = 0);

protected:
    virtual void itemInserted(QtBrowserItem *item, QtBrowserItem *afterItem);
    virtual void itemRemoved(QtBrowserItem *item);
    virtual void itemChanged(QtBrowserItem *item);
};

