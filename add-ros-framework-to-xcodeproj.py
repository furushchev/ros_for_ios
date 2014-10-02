#!/usr/bin/env python
# -*- coding: utf-8 -*-

from mod_pbxproj.mod_pbxproj import XcodeProject as XP
import sys
from os import path as P

argv = sys.argv
argc = len(argv)

DIR=P.dirname(P.abspath(__file__))

def main():
    appname = argv[1]
    pbxproj_path = P.realpath(P.join(DIR, appname, appname + '.xcodeproj', 'project.pbxproj'))
    proj = XP.Load(pbxproj_path)
    framework_group = proj.get_or_create_group('Frameworks')

    # add ios framework
    for f in ['UIKit', 'Foundation', 'AudioToolbox', 'CoreGraphics']:
        path = 'System/Library/Frameworks/%s.framework' % f
        proj.add_file(path, tree='SDKROOT', parent=framework_group)
    proj.add_file('usr/lib/libiconv.2.4.0.dylib', tree='SDKROOT', parent=framework_group)

    # add ros framework
    path = P.realpath(P.join(DIR, 'ros', 'frameworks'))
    proj.add_folder(path, parent=framework_group)
    if proj.modified:
        proj.backup()
        proj.save()


if __name__ == '__main__':
    main()
