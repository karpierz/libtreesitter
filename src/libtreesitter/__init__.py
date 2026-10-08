# flake8-in-file-ignores: noqa: F401,F403,F821

# Copyright (c) 2026 Adam Karpierz
# SPDX-License-Identifier: MIT

"""Python API of tree-sitter C library."""

from .__about__ import * ; del __about__  # type: ignore[name-defined]

from ._api import * ; del _api  # type: ignore[name-defined]
