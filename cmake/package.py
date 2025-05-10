name = "cmake"

version = "3.31.6"

description = "CMake is an open-source, cross-platform family of tools designed to build, test and package software"

build_system = "cmake"

variants = [
    ["platform-osx"]
]

with scope("config") as config:
    config.build_thread_count = "logical_cores"

def commands():
    env.PATH.prepend("{root}/bin")