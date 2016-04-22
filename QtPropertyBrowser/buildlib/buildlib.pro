TEMPLATE=lib
CONFIG += qt dll qtpropertybrowser-buildlib static
mac:CONFIG += absolute_library_soname
win32|mac:!wince*:!win32-msvc:!macx-xcode:CONFIG += debug_and_release build_all
include(../src/qtpropertybrowser.pri)
TARGET = $${QTPROPERTYBROWSER_LIBNAME}4
DESTDIR = $$QTPROPERTYBROWSER_LIBDIR
win32 {
    DLLDESTDIR = $$[QT_INSTALL_BINS]
    QMAKE_DISTCLEAN += $$[QT_INSTALL_BINS]\\$${QTPROPERTYBROWSER_LIBNAME}.dll
}
target.path = $$DESTDIR
INSTALLS += target

# Sip build command
sip.commands += python \"$${SIP_CONFIGURE}\" --module-name=\"$${QTPROPERTYBROWSER_LIBNAME}\" --sip-file=\"$${SIP_PATH}/$${SIP_MAIN_FILE}\" --lib=\"$${TARGET}\" --lib-path=\"$${QTPROPERTYBROWSER_LIBDIR}\" --include-path=\"$${SIP_INCLUDE_PATH}\" --build-path=\"$${SIP_BUILD_PATH}\" &&
sip.commands += cd /d \"$${SIP_BUILD_PATH}\" &&
sip.commands += \"%VS90COMNTOOLS%/../../VC/vcvarsall.bat\" &&
sip.commands += nmake &&
sip.commands += nmake install
#message($${sip.commands})
QMAKE_EXTRA_TARGETS += sip

