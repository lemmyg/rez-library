# -*- coding: utf-8 -*-

name = "alembic"

version = "1.8.5"

authors = ["lemmyg"]





requires = [
    'boost-1.82',
    'python-3.11',
    'imath-3.1.12',
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
    env.REZ_ALEMBIC_ROOT.prepend("{root}")

    if building:
        env.CMAKE_MODULE_PATH.append("{root}/lib/cmake/Alembic")
        env.PKG_CONFIG_PATH.append("{root}/lib/pkgconfig")