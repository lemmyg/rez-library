cmake_minimum_required(VERSION 3.11)

project(imath)

include(ExternalProject)

ExternalProject_Add(imath
    URL https://github.com/AcademySoftwareFoundation/Imath/archive/refs/tags/v3.1.12.zip
    SOURCE_DIR ${CMAKE_CURRENT_BINARY_DIR}/src
    CMAKE_ARGS -DCMAKE_INSTALL_PREFIX=<INSTALL_DIR> 
    INSTALL_DIR ${CMAKE_CURRENT_BINARY_DIR}/install
)

install(DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}/install/ DESTINATION .)