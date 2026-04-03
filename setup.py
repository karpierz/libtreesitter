# Copyright (c) 2026 Adam Karpierz
# SPDX-License-Identifier: MIT

from platform import machine
from setuptools import setup, Extension
from setuptools.command.build_ext import build_ext

class BuildExt(build_ext):

    cc_args_map = {
        "msvc": ["/O2", "/WX", "/std:c11", "/wd4244", "/wd4996", "/wd4018"],
        "unix": ["-O3", "-g0", "-ffast-math",
            "-std=c11",
            "-fvisibility=hidden",
            "-Wno-cast-function-type",
            "-Werror=implicit-function-declaration",
        ],
    }
    ld_args_map = {
        "msvc": ["/DEF:src/libtreesitter/tree_sitter.def"],
        "unix": [],
    }

    def build_extension(self, ext: Extension):
        cc_type = self.compiler.compiler_type
        cc_args = self.cc_args_map.get(cc_type,
                                       self.cc_args_map["unix"])
        ld_args = self.ld_args_map.get(cc_type,
                                       self.ld_args_map["unix"])
        if cc_type == "msvc":
            pass
        elif cc_type == "unix":
            # FIXME: GCC optimizer bug workaround for #330 & #386
            if machine().startswith("aarch64"):
                cc_args.append("--param=early-inlining-insns=9")
        ext.extra_compile_args = cc_args
        ext.extra_link_args = ld_args
        super().build_extension(ext)

ext_modules = [
    Extension(
        name="libtreesitter._platform.tree_sitter",
        sources=[
            "src/libtreesitter/tree-sitter.c/lib/src/lib.c",
            "src/libtreesitter/tree_sitter_py.c",
        ],
        depends=[
            "src/libtreesitter/tree-sitter.c/lib/include/tree_sitter/api.h",
            "src/libtreesitter/tree_sitter.def",
        ],
        include_dirs=[
            "src/libtreesitter/tree-sitter.c/lib/include",
            "src/libtreesitter/tree-sitter.c/lib/src",
        ],
        define_macros=[
            ("_POSIX_C_SOURCE", "200112L"),
            ("_DEFAULT_SOURCE", None),
            ("PY_SSIZE_T_CLEAN", None),
            ("TREE_SITTER_HIDE_SYMBOLS", None),
        ],
    ),
]

setup(
    ext_modules = ext_modules,
    cmdclass = dict(build_ext=BuildExt),
)
