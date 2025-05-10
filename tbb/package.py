name = "tbb"

version = "2020.3"

description = "Intel Threading Building Blocks (Intel TBB) lets you easily write parallel C++ programs that take full advantage of multicore performance"

build_system = "cmake"

variants = [
    ["platform-osx"]
]

def commands():
    env = globals()["env"]
    if system.platform == "osx":
        env.DYLD_LIBRARY_PATH.append("{root}/lib")
    else:
        env.LD_LIBRARY_PATH.append("{root}/lib")
    env.PATH.append("{root}/bin")
    env.TBB_ROOT_DIR = "{root}"
    env.TBB_INCLUDE_DIR = "{root}/include"
    env.TBB_LIBRARIES = "{root}/lib"
    env.REZ_TBB_ROOT = "{root}"
    if building:
        env.CMAKE_MODULE_PATH.append("{root}/cmake")
