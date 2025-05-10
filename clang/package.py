name = "clang"

version = "16.0.2"

authors = [
    "clang"
]


variants = [
    ["platform-osx"]
]


def commands():
    env.CLANG_INSTALL_DIR = "{root}"
    env.LLVM_INSTALL_DIR = "{root}"
    env.PATH.prepend('{root}/bin')
    if system.platform == "osx":
        env.DYLD_LIBRARY_PATH.append('{root}/lib')
    else:
        env.LD_LIBRARY_PATH.append('{root}/lib')
    env.PYTHONPATH.append('{root}/lib/python3.11/site-packages')

    if building:
        env.CMAKE_MODULE_PATH.prepend("{root}/lib/cmake/clang")
        env.CMAKE_MODULE_PATH.prepend("{root}/lib/cmake/llvm")
