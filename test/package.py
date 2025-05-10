# -*- coding: utf-8 -*-

from rez.utils.lint_helper import env, building, scope  # make linter happy


name = "test"

version = "1.0.0"

authors = ['galder']

requires = [
    'openimageio-2.5.18',
    'usd-24.08',
    'tbb-2020.3',
    'qt-6.5.3',
]


variants = [
    ["platform-osx"],
]

build_system = "cmake"

tools = [
    "test",
]


def commands():
    env.PATH.append("{root}/bin")