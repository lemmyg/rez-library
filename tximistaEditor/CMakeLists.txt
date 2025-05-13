CMAKE_MINIMUM_REQUIRED(VERSION 3.11)
project(tximistaEditor)
#include(RezBuild)
include(ExternalProject)

find_package(OpenGL REQUIRED)
message(STATUS "OpenGL_INCLUDE_DIR: ${OPENGL_INCLUDE_DIR}")
message(STATUS "OPENGL_LIBRARIES: ${OPENGL_LIBRARIES}")
#Set deployment target for macOS
if(APPLE)
    set(CMAKE_OSX_DEPLOYMENT_TARGET "15.2" CACHE STRING "Minimum OS X deployment version")
endif()

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