# -*- coding: utf-8 -*-

from rez.utils.lint_helper import env, building, scope  # make linter happy


name = "openSubdiv"

version = "3.6.0"

authors = ['lemmyg']

requires = [
    'openexr',
    'tbb-2020.3',
    'glfw',
]

variants = [
    ["platform-osx"],
]




def commands():
    if system.platform == "osx":
        env.DYLD_LIBRARY_PATH.append("{root}/lib")
    else:
        env.LD_LIBRARY_PATH.append("{root}/lib")
    env.PATH.append("{root}/bin")
    env.OPENSUBDIV_ROOT_DIR = "{root}"

    if building:
        env.CMAKE_MODULE_PATH.append("{root}/cmake")