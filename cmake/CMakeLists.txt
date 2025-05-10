cmake_minimum_required(VERSION 3.12)
project(cmake)

include(ExternalProject)

ExternalProject_Add(cmake
    URL https://github.com/Kitware/CMake/releases/download/v3.31.6/cmake-3.31.6.tar.gz
    CONFIGURE_COMMAND <SOURCE_DIR>/configure --prefix=<INSTALL_DIR>
    SOURCE_DIR ${CMAKE_CURRENT_BINARY_DIR}/src
    BUILD_IN_SOURCE 1
    INSTALL_DIR ${CMAKE_CURRENT_BINARY_DIR}/install
)

install(DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}/install/ DESTINATION .)
