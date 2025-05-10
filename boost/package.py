name = "boost"

version = "1.82"

description = """
    Boost provides free peer-reviewed portable C++ source libraries.
    """

authors = ["Boost"]

requires = [
    "python-3.11",
]

variants = [
    ["platform-osx"]
]

build_system = "cmake"

with scope("config") as config:
    config.build_thread_count = "logical_cores"

def commands():
    if system.platform == "osx":
        env.DYLD_LIBRARY_PATH.prepend("{root}/lib")
    else:
        env.LD_LIBRARY_PATH.prepend("{root}/lib")
    env.Boost_ROOT.set("{root}")
    env.Boost_INCLUDEDIR.set("{root}/include")
    env.Boost_LIBRARYDIR.set("{root}/lib")
    if building:
        env.CMAKE_MODULE_PATH.append("{root}/lib/cmake")

