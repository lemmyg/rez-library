# -*- coding: utf-8 -*-

name = "oidn"

version = "1.4.3"

authors = ["lemmyg"]





requires = [
    'tbb-2020.3',
    'ispc-1.15.0',
]

variants = [["platform-osx"]]

build_system = "cmake"

with scope("config") as config:
    config.build_thread_count = "logical_cores"

def commands():
    env.PATH.prepend("{root}/bin")
    if system.platform == "osx":
        env.DYLD_LIBRARY_PATH.prepend("{root}/lib")
    else:
        env.LD_LIBRARY_PATH.prepend("{root}/lib")

    if building:
        env.CMAKE_MODULE_PATH.append("{root}/lib/cmake/OpenImageDenoise-{version}")