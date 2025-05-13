# -*- coding: utf-8 -*-

name = 'os'

version = 'osx-13'

requires = [
    'platform-osx',
    'arch-x86_64'
]



def commands():
    env.MACOSX_DEPLOYMENT_TARGET = '{version}'
