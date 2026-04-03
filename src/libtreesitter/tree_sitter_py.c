/**
 * Filename: \file
 *
 * Copyright (c) 2026 Adam Karpierz
 * SPDX-License-Identifier: MIT
 *
 * Purpose:
 *
 *     Only for creating C dll using Python setup machinery.
 */

#include <Python.h>

#define MODINIT_FUNC(name) PyInit_##name(void)
#define MODINIT_RETURN(v) v

PyMODINIT_FUNC MODINIT_FUNC(tree_sitter)
{
    return MODINIT_RETURN(NULL);
}
