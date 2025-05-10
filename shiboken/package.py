name = "shiboken"

version = "6.5.3"

authors = [
    "pyside"
]

description = \
    """
    Python bindings generator that uses API Extractor and outputs CPython code.
    """

requires = [
    "python-3.11",
    "clang-16.0.2",
    "qt-6.5.3"
]

build_requires = [
]

variants = [
    ["platform-osx"]
]


def commands():
    env.CMAKE_MODULE_PATH.append("{root}/cmake")
    if system.platform == "osx":
        env.DYLD_LIBRARY_PATH.append('{root}/lib')
    else:
        env.LD_LIBRARY_PATH.append('{root}/lib')
    env.PYTHONPATH.append('{root}/lib/python3.11/site-packages')

    if building:
        env.SHIBOKEN_INCLUDE_DIR.append('{root}/include')
