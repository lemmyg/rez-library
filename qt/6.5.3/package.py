# -*- coding: utf-8 -*-

name = "qt"

version = "6.5.3"

description = """
The Qt framework contains a comprehensive set of highly intuitive and modularized C++ library classes and is loaded with APIs to simplify your application development.
"""

variants = [
    ["platform-osx"],
]

requires = [
    "clang-16.0.2",
    "python-3.11",
]

private_build_requires = [
    "python-3.11",
]


tools = [
    "designer",
    "assistant",
    "qml",
    "qmake",
    "qpaths"
]


def commands():
    env.PATH.append("{root}/bin")
    env.QT_PLUGIN_PATH.append("{root}/plugins")
    env.QT_QPA_PLATFORM_PLUGIN_PATH = "{root}/plugins/platforms"
    env.QML2_IMPORT_PATH.append("{root}/qml")
    env.QTPATHS_EXECUTABLE = "{root}/bin/qtpaths6"

    if system.platform == "osx":
        env.DYLD_LIBRARY_PATH.append("{root}/lib")
    else:
        env.LD_LIBRARY_PATH.append("{root}/lib")
    
    if building:
        env.QMAKESPEC = "{root}/mkspecs/macx-clang"

        env.DYLD_FRAMEWORK_PATH.append("{root}/lib")
        if building:
            env.QMAKESPEC = "{root}/mkspecs/macx-clang"

    if building:
        env.CMAKE_PREFIX_PATH.append("{root}/lib/cmake")
        env.PKG_CONFIG_PATH.append("{root}/lib/pkgconfig")
        env.Qt6_DIR = "{root}/lib/cmake/Qt6"
