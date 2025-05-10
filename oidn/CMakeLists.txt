cmake_minimum_required(VERSION 3.11)

project(oidn)

include(ExternalProject)

ExternalProject_Add(imath
    URL https://github.com/OpenImageDenoise/oidn/releases/download/v1.4.3/oidn-1.4.3.src.tar.gz
    SOURCE_DIR ${CMAKE_CURRENT_BINARY_DIR}/src
    CMAKE_ARGS -DCMAKE_INSTALL_PREFIX=<INSTALL_DIR> 
    INSTALL_DIR ${CMAKE_CURRENT_BINARY_DIR}/install
)

install(DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}/install/ DESTINATION .)