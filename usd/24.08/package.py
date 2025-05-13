# -*- coding: utf-8 -*-
from rez.utils.lint_helper import env
import os
name = "usd"

version = "24.08"

authors = ["lemmyg"]

requires = [
    "boost-1.82",
    "cmake",
    "tbb-2020.3",
    "python-3.11",
    "openSubdiv-3.6.0",
    "glew-2.1.0",
    "glfw-3.3.8",
    "embree-3.10.0",
]

variants = [
    ["platform-osx"],
]

tools = [
    "sdfdump",
    "sdffilter",
    "testusdview",
    "usdcat",
    "usdchecker",
    "usddiff",
    "usddumpcrate",
    "usdedit",
    "usdGenSchema",
    "usdrecord",
    "usdresolve",
    "usdstitch",
    "usdstitchclips",
    "usdtree",
    "usdview",
    "usdzip",
]

build_system = "cmake"


with scope("config") as config:
    config.build_thread_count = "logical_cores"


def commands():
    # Add root path first
    env.CMAKE_PREFIX_PATH.prepend("{root}")
    env.PATH.prepend("{root}/bin")
    env.PYTHONPATH.prepend("{root}/lib/python")
    if system.platform == "osx":
        env.DYLD_LIBRARY_PATH.prepend("{root}/lib")
    else:
        env.LD_LIBRARY_PATH.prepend("{root}/lib")
