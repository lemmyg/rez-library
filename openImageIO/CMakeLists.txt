cmake_minimum_required(VERSION 3.11)

project(openimageio)

set(PYTHON_VERSION 3.11)
find_package(Python3 COMPONENTS Interpreter Development)
include(RezBuild)
include(ExternalProject)

ExternalProject_Add(openimageio
    URL https://github.com/AcademySoftwareFoundation/OpenImageIO/releases/download/v2.5.18.0/OpenImageIO-2.5.18.0.tar.gz
    SOURCE_DIR ${CMAKE_CURRENT_BINARY_DIR}/src
    CMAKE_ARGS 
    -DCMAKE_INSTALL_PREFIX=<INSTALL_DIR> 
    -DBoost_ROOT=$ENV{REZ_BOOST_ROOT}
    -Dpybind11_ROOT=$ENV{REZ_PYBIND_ROOT}
    -DENABLE_Qt5=0
    -DENABLE_Qt6=0
    -DENABLE_Nuke=0
    -DENABLE_Ptex=0
    -DENABLE_OpenVDB=0
    -DENABLE_OpenCV=0
    -DENABLE_DCMTK=0
    INSTALL_DIR ${CMAKE_CURRENT_BINARY_DIR}/install
)

install(DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}/install/ DESTINATION .)


#rez_install_files(
#    cmake/FindOpenImageIO.cmake
#    DESTINATION .
#)
