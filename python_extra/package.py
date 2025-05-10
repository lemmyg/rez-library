# -*- coding: utf-8 -*-

name = "python_extra"

version = "0.0.1"



requires = [
    "python-3.11",
    "qt-6.5.3",
]




variants = [["platform-osx"]]

build_system = "cmake"

with scope("config") as config:
    config.build_thread_count = "logical_cores"

def commands():
    env.PYTHONPATH.append("{root}/lib/python3.11/site-packages")
    env.SHIBOKEN6_MODULE_PATH.append("{root}/lib/python3.11/site-packages/shiboken6")
    env.SHIBOKEN6_GENERATOR_PATH.append("{root}/lib/python3.11/site-packages/shiboken6_generator")
    env.PYSIDE6_PATH.append("{root}/lib/python3.11/site-packages/pyside6")
    
