# -*- coding: utf-8 -*-

name = "pybind11"

version = "2.10.4"



build_requires = [
    "boost-1.82",
    "python-3.11",
]

private_build_requires = [
    #'ilmbase-2.4.1',
    #'boost-1.82',
]

requires = [
    # 'boost-1.61',
    #'numpy'
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
    env.REZ_PYBIND_ROOT = "{root}"

    if building:
        env.CMAKE_MODULE_PATH.append("{root}/share/cmake/pybind11")
        env.PKG_CONFIG_PATH.append("{root}/lib/pkgconfig")