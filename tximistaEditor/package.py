
name = "tximistaEditor"
version = "0.30.0"

authors = ["lemmyg"]

description = """tximistaEditor is a full featured template engine for Python."""

requires = [
    "cmake",
    "python-3.11",
    "glfw-3.3.8",
    "glm-1.0.1",
    "tbb-2020.3",
    "clang-16.0.2",
    "boost-1.82",
    "pybind11-2.10.4",
    "alembic-1.8.5",
    "imgui-1.74",
    "openexr-3.3.3",
    "openimageio-2.5.18.0",
    "embree-3.10.0",
    "oidn-1.4.3",
    "usd-24.08",
    "qt-6.5.3",
    #"PySide6-6.5.2",
]

variants = [
    ["platform-osx"],
]

build_system = "cmake"

tools = [
    "tximistaEditor",
    "tximistaEditorQTCPP",
    "tximistaGL",
]

with scope("config") as config:
    config.build_thread_count = "logical_cores"


def commands():
    env.PATH.prepend("{root}/bin")
    if system.platform == "osx":
        env.DYLD_LIBRARY_PATH.prepend("{root}/lib")
    else:
        env.LD_LIBRARY_PATH.prepend("{root}/lib")
