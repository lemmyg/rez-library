# -*- coding: utf-8 -*-

name = "openexr"

version = "3.3.3"



requires = [
    'pybind11-2.10.4',
    'boost-1.82',
    'imath-3.1.12'
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
        env.CMAKE_MODULE_PATH.append("{root}/lib/cmake/OpenEXR")
        env.PKG_CONFIG_PATH.append("{root}/lib/pkgconfig")