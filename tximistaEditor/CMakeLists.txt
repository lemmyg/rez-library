CMAKE_MINIMUM_REQUIRED(VERSION 3.11)
project(tximistaEditor)
#include(RezBuild)
include(ExternalProject)

ExternalProject_add(
    tximistaEditor
    SOURCE_DIR "${CMAKE_SOURCE_DIR}/../../tximistaeditor"
    CMAKE_ARGS 
    -DCMAKE_INSTALL_PREFIX=${CMAKE_INSTALL_PREFIX}
    -DCMAKE_BUILD_TYPE=Release
    -DIMGUI_ROOT=$ENV{REZ_IMGUI_ROOT}
    -DEMBREE_SOURCE=$ENV{REZ_EMBREE_ROOT}/src
    -DPython_ROOT_DIR=$ENV{REZ_PYTHON_ROOT}
    BUILD_COMMAND make
    INSTALL_COMMAND make install
)

INSTALL(CODE "message(STATUS Running tximistaEditor install)")