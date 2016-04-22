class QtButtonPropertyBrowser : QtAbstractPropertyBrowser
{

%TypeHeaderCode
#include <qtbuttonpropertybrowser.h>
%End

public:

    QtButtonPropertyBrowser(QWidget *parent /TransferThis/ = 0);

    void setExpanded(QtBrowserItem *item, bool expanded);
    bool isExpanded(QtBrowserItem *item) const;

signals:

    void collapsed(QtBrowserItem *item);
    void expanded(QtBrowserItem *item);

protected:
    virtual void itemInserted(QtBrowserItem *item, QtBrowserItem *afterItem);
    virtual void itemRemoved(QtBrowserItem *item);
    virtual void itemChanged(QtBrowserItem *item);
};
