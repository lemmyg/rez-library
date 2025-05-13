# -*- coding: utf-8 -*-
name = "python"

version = "3.11.11"

authors = ["lemmyg"]

requires = [ 
    "cmake",   
    ] 

variants = [
    ["platform-osx"],
]



with scope("config") as config:
    config.build_thread_count = "logical_cores"

def commands():   
    # Set our Python paths
    env.PATH.prepend("{root}/bin")
    if system.platform == "osx":
        env.DYLD_LIBRARY_PATH.prepend("{root}/lib")
    else:
        env.LD_LIBRARY_PATH.prepend("{root}/lib")
    env.PYTHONPATH.prepend("{root}/lib/python3.11/site-packages")
    env.PKG_CONFIG_PATH.prepend("{root}/lib/pkgconfig")
    env.Python3_EXECUTABLE.set("{root}/bin/python3.11")
    env.PIP3_EXECUTABLE.set("{root}/bin/pip3.11")
    env.PYTHON_VERSION.set("3.11")
    env.PYTHON_VERSION_MAJOR.set("3")
    env.PYTHON_VERSION_MINOR.set("11")
    env.PYTHON_VERSION_PATCH.set("11")
    env.PIP_VERSION_STRING.set("pip3.11")
    env.Python_ROOT_DIR.set("{root}")
    # Create aliases that point to our Python
    #alias("python3", "{root}/bin/python3.11")
