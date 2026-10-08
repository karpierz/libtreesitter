# Copyright (c) 2026 Adam Karpierz
# SPDX-License-Identifier: MIT

import unittest
from unittest import mock
import sys

import libtreesitter
import libtreesitter as ts
from utlx.platform import is_windows


class MainTestCase(unittest.TestCase):

    def setUp(self):
        pass

    @unittest.skipUnless(is_windows, "Windows-only test")
    def test_dll_nonexistent(self):
        with mock.patch("sysconfig.get_config_var",
                        return_value=".nonexistent"), \
             self.assertRaises(ImportError) as exc:
            sys.modules.pop("libtreesitter._platform.windows", None)
            sys.modules.pop("libtreesitter._platform", None)
            import libtreesitter._platform
        sys.modules.pop("libtreesitter._platform.windows", None)
        sys.modules.pop("libtreesitter._platform", None)
        import libtreesitter._platform
        self.assertIn("Shared library not found: ", str(exc.exception))

    def test_main(self):
        pass
