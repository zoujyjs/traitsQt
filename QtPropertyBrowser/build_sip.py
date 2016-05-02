# -*- coding: utf-8 -*-

__author__ = 'zoujyjs'

import os
import sys
import argparse
import subprocess


devbat = None
make = None


def OnWindows():
  return platform.system() == 'Windows'


def ParseArguments():
    parser = argparse.ArgumentParser()
    parser.add_argument( '--msvc', type=int, choices=[11, 12, 14], default=14,
        help='Choose the Microsoft Visual Studio version '
        '(default: %(default)s).' )
    args = parser.parse_args()
    return args


def CheckDeps(args):
    environ_var = 'VS%d0COMNTOOLS' % args.msvc
    toolpath = os.environ.get(environ_var)
    if not toolpath:
        sys.exit('%s is not set in the environment. Please check the '
                'installation of the coresponding Microsoft Visual Studio.')
    global devbat, make
    devbat = toolpath + 'VsDevCmd.bat'
    binpath = devbat.split(os.sep)[:-3] + ['VC', 'bin', 'nmake.exe']  # ../../vs
    make = os.path.sep.join(binpath)


def Main():
    args = ParseArguments()
    CheckDeps(args)
    os.chdir('buildlib')
    subprocess.check_call([devbat, '&&', make])
    os.chdir('..')
    subprocess.check_call(['python', 'configure-sip.py',
        '--module-name', 'QtPropertybrowser',
        '--sip-file', 'sip\qtpropertybrowser_module.sip',
        '--lib-path', 'lib',
        '--include-path', 'src',
        '--build-path', 'lib',
        '--lib', 'QtPropertyBrowser4'])
    os.chdir('lib')
    subprocess.check_call([devbat, '&&', make])

if __name__ == '__main__':
    Main()
