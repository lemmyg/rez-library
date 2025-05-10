# -*- coding: utf-8 -*-
from rez.utils.lint_helper import env, building

name = 'imgui'
version = '1.74'
authors = ['lemmyg']
variants = [["platform-osx"]]
build_system = "cmake"

def commands():
    env.PATH.prepend("{root}")
