exists(config.pri):infile(config.pri, SOLUTIONS_LIBRARY, yes): CONFIG += qtpropertybrowser-uselib
TEMPLATE += fakelib
QTPROPERTYBROWSER_LIBNAME = $$qtLibraryTarget(QtPropertyBrowser)
TEMPLATE -= fakelib
QTPROPERTYBROWSER_LIBDIR = $$PWD/lib
unix:qtpropertybrowser-uselib:!qtpropertybrowser-buildlib:QMAKE_RPATHDIR += $$QTPROPERTYBROWSER_LIBDIR

# SIP related var
SIP_CONFIGURE = $$PWD/configure-sip.py
SIP_PATH = $$PWD/sip
SIP_MAIN_FILE = qtpropertybrowser_module.sip
SIP_INCLUDE_PATH = $$PWD/src
SIP_BUILD_PATH = $$OUT_PWD/sip
