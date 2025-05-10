# -*- coding: utf-8 -*-
from rez.utils.lint_helper import env

name = 'glew'
version = '2.1.0'
authors = ['lemmyg']
variants = [["platform-osx"]]


def commands():
    if system.platform == "osx":
        env.DYLD_LIBRARY_PATH.prepend("{root}/lib")
    else:
        env.LD_LIBRARY_PATH.prepend("{root}/lib")