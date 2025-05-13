# -*- coding: utf-8 -*-
from rez.utils.lint_helper import env, building

name = 'embree'
version = '3.10.0'
authors = ['lemmyg']
requires = [
            'tbb-2020.3',
            ]
variants = [["platform-osx"]]

build_system = "cmake"

with scope("config") as config:
    config.build_thread_count = "logical_cores"



def commands():
    env.PATH.prepend("{root}/bin")
    env.EMBREE_LOCATION = "{root}"
    if system.platform == "osx":
        env.DYLD_LIBRARY_PATH.prepend("{root}/lib")
    else:
        env.LD_LIBRARY_PATH.prepend("{root}/lib")
    if building:
        env.CMAKE_MODULE_PATH.append("{root}/lib/cmake/embree-{version}")