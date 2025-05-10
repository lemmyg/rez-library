# -*- coding: utf-8 -*-

name = "openimageio"

version = "2.5.18.0"

authors = ["lemmyg"]





requires = [
    'cmake',
    'boost-1.82',
    'pybind11-2.10.4',
    'openexr-3.3.3',
    'tbb-2020.3',
    'python-3.11',    #'numpy'
]
build_requires = [
    'python-3.11',
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
        env.CMAKE_MODULE_PATH.append("{root}/lib/cmake/OpenImageIO")
        env.PKG_CONFIG_PATH.append("{root}/lib/pkgconfig")
        env.PYTHONPATH.append("{root}/lib/python3.11/site-packages")