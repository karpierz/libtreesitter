# flake8-in-file-ignores: noqa: E402

# Copyright (c) 2026 Adam Karpierz
# SPDX-License-Identifier: MIT

import ctypes
import sysconfig
from pathlib import Path
from functools import partial

__all__ = ('DLL_PATH', 'DLL', 'dlclose', 'CFUNC')

here = Path(__file__).resolve().parent
dll_suff = sysconfig.get_config_var("EXT_SUFFIX") or ".pyd"

DLL_PATH = here/("tree_sitter" + dll_suff)

from ctypes  import CDLL as _DLL
from _ctypes import dlclose  # type: ignore[attr-defined]
from ctypes  import CFUNCTYPE as CFUNC

DLL = partial(_DLL, mode=ctypes.RTLD_GLOBAL)
