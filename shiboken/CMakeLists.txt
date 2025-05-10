cmake_minimum_required(VERSION 3.11)
project(shiboken)

# Find required packages
find_package(Python 3.11 EXACT REQUIRED COMPONENTS Interpreter)


# Include ExternalProject module
include(ExternalProject)


# Add PySide as an external project
ExternalProject_Add(shiboken
    GIT_REPOSITORY https://code.qt.io/pyside/pyside-setup.git
    GIT_TAG 6.5.3
    GIT_SHALLOW 1
    GIT_SUBMODULES_RECURSE 1
    CONFIGURE_COMMAND ""
    BUILD_COMMAND ""
    COMMAND ${Python_EXECUTABLE} setup.py install --qtpaths=${QTPATHS_EXECUTABLE} --verbose-build --internal-build-type=shiboken6
    COMMAND ${Python_EXECUTABLE} setup.py install --qtpaths=${QTPATHS_EXECUTABLE} --verbose-build --internal-build-type=shiboken6-generator
    BUILD_IN_SOURCE 1
)




# Add an empty install target to satisfy rez build system
install(CODE "message(STATUS \"Shiboken installed from source\")") 