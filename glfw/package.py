# -*- coding: utf-8 -*-
from rez.utils.lint_helper import env, building

name = 'glfw'
version = '3.3.8'
authors = ['lemmyg']
variants = [["platform-osx"]]


def commands():
    if system.platform == "osx":
        env.DYLD_LIBRARY_PATH.prepend("{root}/lib")
    else:
        env.LD_LIBRARY_PATH.prepend("{root}/lib")
    if building:
        env.PKG_CONFIG_PATH.append("{root}/lib/pkgconfig")
    env.CMAKE_MODULE_PATH.prepend("{root}/lib/cmake/glfw3/")