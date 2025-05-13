CMAKE_MINIMUM_REQUIRED(VERSION 2.8)

# Set CMake policies
cmake_policy(SET CMP0177 NEW)
cmake_policy(SET CMP0174 NEW)

include(RezBuild)
include(ExternalProject)
include(ProcessorCount)
ProcessorCount(ncpus)

# Set deployment target for macOS
if(APPLE)
    set(CMAKE_OSX_DEPLOYMENT_TARGET "15.2" CACHE STRING "Minimum OS X deployment version")
endif()

# Build QtBase (includes QtCore, QtGui, and QtWidgets)
ExternalProject_add(
    qtbase
    URL https://download.qt.io/archive/qt/6.5/6.5.3/submodules/qtbase-everywhere-src-6.5.3.tar.xz
    SOURCE_DIR src/qtbase
    CONFIGURE_COMMAND ./configure
    -prefix ${CMAKE_INSTALL_PREFIX}
    -release
    -confirm-license
    -opensource
    -nomake examples
    -nomake tests
    BUILD_COMMAND cmake --build . --parallel
    INSTALL_COMMAND cmake --install .
    BUILD_IN_SOURCE 1
)



INSTALL(CODE "message(STATUS Running qt6 install)")