name = "glm"
version = "1.0.1"

authors = ["lemmyg"]

description = """OpenGL Mathematics (GLM) is a header only C++ mathematics library for graphics software based on the OpenGL Shading Language (GLSL) specification."""

requires = [
    "cmake",
]

variants = [
    ["platform-osx"],
]

build_system = "cmake"

def commands():
    env.CMAKE_PREFIX_PATH.prepend("{root}/share/glm")
    env.PATH.prepend("{root}/bin")
    if system.platform == "osx":
        env.DYLD_LIBRARY_PATH.prepend("{root}/lib")
    else:
        env.LD_LIBRARY_PATH.prepend("{root}/lib")
