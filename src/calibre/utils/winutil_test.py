#!/usr/bin/env python2
# vim:fileencoding=utf-8
# License: GPL v3 Copyright: 2019, Kovid Goyal <kovid at kovidgoyal.net>

from __future__ import absolute_import, division, print_function, unicode_literals

import os
import unittest


class TestWinutil(unittest.TestCase):

    def setUp(self):
        from calibre.constants import plugins
        self.winutil = plugins['winutil'][0]

    def tearDown(self):
        del self.winutil

    def test_add_to_recent_docs(self):
        self.winutil.add_to_recent_docs(os.path.abspath(__file__), None)
        self.winutil.add_to_recent_docs(os.path.abspath(__file__), 'some-app-uid')


def find_tests():
    return unittest.defaultTestLoader.loadTestsFromTestCase(TestWinutil)
