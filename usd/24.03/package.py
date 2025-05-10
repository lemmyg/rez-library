# -*- coding: utf-8 -*-
from rez.utils.lint_helper import env
import os
name = "usd"

version = "24.03"

authors = ["lemmyg"]

requires = [
    "boost-1.82",
    "cmake",
    "tbb-2020.3",
    "python-3.11",
    "opensubdiv-3.1.1",

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
    env.CMAKE_PREFIX_PATH.prepend("{root}")
    env.PATH.prepend("{root}/bin")
    env.LD_LIBRARY_PATH.prepend("{root}/lib")
